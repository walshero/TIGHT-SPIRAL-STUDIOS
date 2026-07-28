/* TIGHT SPIRAL PRODUCTIONS - model proxy
   ---------------------------------------------------------------------------
   Why this exists: a page served from walshero.github.io or any real URL can
   never call a model without a key in the file, and a key in the file is the
   PAT law broken in a new coat (SESSION-2026-07-28 R1). This function holds the
   key server-side. The page calls the function; the function calls the model.

   THE KEY NEVER APPEARS IN THIS FILE OR IN ANY REPO.
   It is set once in the Netlify UI as the environment variable
   ANTHROPIC_API_KEY and is read here from process.env.

   Hardening, deliberate:
     - POST only.
     - Model is PINNED here. A caller cannot ask for a different one.
     - max_tokens is capped here. A caller cannot ask for more.
     - Origin allowlist. Anything not on it gets 403 and never reaches the model.
     - Body size ceiling, so the endpoint cannot be used as a firehose.
   Add a new surface by adding its origin to ALLOWED, nothing else.
--------------------------------------------------------------------------- */

const MODEL       = 'claude-sonnet-4-6';
const MAX_TOKENS  = 1500;
const MAX_BODY    = 40000;          // characters of prompt, generous for a slip
const API         = 'https://api.anthropic.com/v1/messages';

const ALLOWED = [
  'https://walshero.github.io',
  'http://localhost:8888',
  'http://localhost:3000'
];

/* Same-origin calls from this Netlify site send no Origin header on POST in
   some browsers, and send this site's own origin in others. Both are fine. */
function allow(origin, host) {
  if (!origin) return true;
  if (ALLOWED.includes(origin)) return true;
  try { return new URL(origin).host === host; } catch { return false; }
}

function json(body, status, origin) {
  const h = { 'Content-Type': 'application/json' };
  if (origin) {
    h['Access-Control-Allow-Origin']  = origin;
    h['Access-Control-Allow-Headers'] = 'Content-Type';
    h['Access-Control-Allow-Methods'] = 'POST, OPTIONS';
    h['Vary']                         = 'Origin';
  }
  return new Response(JSON.stringify(body), { status, headers: h });
}

export default async (req) => {
  const origin = req.headers.get('origin') || '';
  const host   = new URL(req.url).host;

  if (!allow(origin, host)) {
    return json({ error: 'origin not allowed' }, 403, null);
  }
  if (req.method === 'OPTIONS') {
    return json({ ok: true }, 204, origin);
  }
  if (req.method !== 'POST') {
    return json({ error: 'POST only' }, 405, origin);
  }

  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) {
    /* Named plainly so the failure is never mistaken for a model outage. */
    return json({ error: 'proxy has no key configured' }, 500, origin);
  }

  let inbound;
  try { inbound = await req.json(); }
  catch { return json({ error: 'body was not JSON' }, 400, origin); }

  const messages = Array.isArray(inbound.messages) ? inbound.messages : null;
  if (!messages || !messages.length) {
    return json({ error: 'messages missing' }, 400, origin);
  }
  const weight = JSON.stringify(messages).length;
  if (weight > MAX_BODY) {
    return json({ error: 'request too large (' + weight + ' > ' + MAX_BODY + ')' }, 413, origin);
  }

  try {
    const upstream = await fetch(API, {
      method: 'POST',
      headers: {
        'Content-Type'      : 'application/json',
        'x-api-key'         : key,
        'anthropic-version' : '2023-06-01'
      },
      body: JSON.stringify({
        model      : MODEL,
        max_tokens : Math.min(Number(inbound.max_tokens) || MAX_TOKENS, MAX_TOKENS),
        messages
      })
    });

    const text = await upstream.text();
    /* Pass the model's own body straight through so the page's parser is
       unchanged whether it is talking to the runtime or to this function. */
    return new Response(text, {
      status  : upstream.status,
      headers : {
        'Content-Type'               : 'application/json',
        'Access-Control-Allow-Origin': origin || '*',
        'Vary'                       : 'Origin'
      }
    });
  } catch (e) {
    return json({ error: 'upstream unreachable: ' + e.message }, 502, origin);
  }
};

export const config = { path: '/.netlify/functions/claude' };
