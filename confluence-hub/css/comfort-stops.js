/* ============================================================================
   COMFORT STOPS — controller
   ----------------------------------------------------------------------------
   Vendored from the gate-green companion (TSP@09b76d8). Two responsibilities:

   1. PRE-PAINT: honor the phone/OS dark preference as the starting stop, set
      BEFORE first paint so there is no flash. Inline the pre-paint block at the
      very top of <body> (a deferred module is too late — the flash is the bug).

   2. The corner control: Day / Softer / Night, with aria-pressed kept in sync.

   Requires comfort-stops.css and, in <head>:
     <meta name="color-scheme" content="light dark">
   ========================================================================== */

/* ---- 1. PRE-PAINT (inline this at the top of <body>, not here) ----
   <script>
     if (window.matchMedia &&
         matchMedia('(prefers-color-scheme: dark)').matches) {
       document.body.classList.add('dark');
     }
   </script>
*/

/* ---- 2. Corner control ---- */
export function setStop(stop, btn) {
  const body = document.body;
  body.classList.remove('softer', 'dark');
  if (stop === 'softer') body.classList.add('softer');
  if (stop === 'dark' || stop === 'night') body.classList.add('dark');
  // keep the three buttons' pressed state truthful
  const group = btn ? btn.closest('.comfort') : document.querySelector('.comfort');
  if (group) group.querySelectorAll('button').forEach((b) =>
    b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'));
}

/* On load, reflect the pre-paint choice onto the buttons. */
export function syncComfortButtons() {
  const dark = document.body.classList.contains('dark');
  const softer = document.body.classList.contains('softer');
  const want = dark ? 'dark' : softer ? 'softer' : 'day';
  document.querySelectorAll('.comfort button').forEach((b) => {
    const isWant = (b.textContent || '').trim().toLowerCase().startsWith(want[0]);
    b.setAttribute('aria-pressed', isWant ? 'true' : 'false');
  });
}
