# THE BENCH — Supabase setup
**15 minutes, once. Then the studio has real playtesters in a real table.**
**Only Matt can do this. Claude cannot provision a Supabase project.**

---

## THE SECURITY MODEL — read this first, it is the whole thing

The `anon` key ships **in the page source.** Anyone can read it. **That is by design and it
is safe — but only if you get one setting right.**

> **RLS ON. INSERT allowed to anon. SELECT allowed to NOBODY.**

**Anyone can drop a card in the box. Nobody can open the box but you.**

If `SELECT` is open to anon, **the key in your page leaks your entire signup list** — every
name and email, to anyone who views source. The SQL below sets this correctly. **Do not
"fix" it later by enabling read access.**

---

## STEP 1 — make the project (5 min)

1. **supabase.com** → **Start your project** → sign in with GitHub
2. **New project**
   - **Name:** `tight-spiral`
   - **Database password:** let it generate one, then **save it in your password manager**.
     You will not be shown it again and you cannot recover it.
   - **Region:** `East US (North Virginia)` — closest to Boston
   - **Plan:** **Free**. It covers 50,000 monthly active users. You have zero. It will be
     free for years.
3. **Create new project.** It takes ~2 minutes to provision. Wait for it.

---

## STEP 2 — make the table (3 min)

In the left sidebar: **SQL Editor** (the icon that looks like a terminal prompt, about
halfway down). Then **New query**.

**Paste all of this and hit Run** (bottom right, or ⌘↵):

```sql
-- THE BENCH. Playtester signups from the studio face.

create table playtesters (
  id         bigint generated always as identity primary key,
  created_at timestamptz default now(),
  name       text,
  email      text not null,
  wants      text,          -- games | class | client | any
  reads      text,          -- typical | lowvis | screenrd | kb
  note       text,
  source     text           -- which page they came from
);

-- ROW LEVEL SECURITY. This is the load-bearing part.
alter table playtesters enable row level security;

-- Anyone may INSERT. This is what the public page does.
create policy "anyone can sit the bench"
  on playtesters for insert
  to anon
  with check (true);

-- NOBODY may SELECT with the anon key. No policy = no access.
-- You read this table from the Supabase dashboard, authenticated as yourself.
-- If you ever add a SELECT policy for anon, you leak every signup. Don't.
```

You should see **"Success. No rows returned."**

---

## STEP 3 — get the two strings (2 min)

Left sidebar, at the very bottom: **Project Settings** (gear icon) → **API**.

Copy **two things**:

1. **Project URL** — looks like `https://abcdefghijk.supabase.co`
2. **anon / public** key — a long string starting `eyJ...`
   ⚠ **NOT the `service_role` key.** That one is a master key and must never leave your
   machine. It is on the same page, one row down, usually hidden behind a "Reveal" button.
   **If you paste service_role into a public page, anyone can read, edit, and delete your
   whole database.**

---

## STEP 4 — paste them to Claude

Send both strings. Claude wires them into `index.html`, byte-verifies, and pushes.

**Until that happens, the form does not lie.** With no keys configured it says *"Signup is not
wired up yet"* and opens your mail app instead. **It never shows a fake confirmation** — a
person walking away believing they are on a list that does not exist is worse than an error.

---

## STEP 5 — read your signups

**Table Editor** (left sidebar, top) → **playtesters**.

Every signup, with a timestamp. Export to CSV from the top right when you want it.

---

## WHAT THIS BUYS YOU — and the honest tradeoff

**Buys:** a real table you can query, cohort, and export. The `reads` column means you can
find every low-vision and screen-reader tester in one click — **that is a research asset no
other game studio has, and it is the exact thing you would show an HR department or a grant
reviewer.**

**Costs:** it is the first thing in the studio that is not single-file-offline. The page still
loads with zero network calls; the fetch fires only when someone taps the button. **But the
studio now has a dependency on a vendor.** If Supabase disappears, the signups need exporting
and the form needs rewiring.

**Mitigation, and do it once a term:** Table Editor → **Export CSV** → drop it in Drive. Then
the data is yours regardless of what Supabase does. **The vendor holds a copy, not the copy.**
