# Wright — Session R Build Prompt
*From Spark session R, March 28, 2026. Paste this into Wright's window when ready to build.*

---

We had a full Spark research and copy session today. Two new files are in `dev/` — read them before building anything:

- `dev/Sparkwright_Website_Copy_Draft_v1.md` — all website copy (landing page, About page, Math Flash title screen)
- `dev/Sparkwright_Legal_Draft_v1.md` — Terms of Use, Privacy Policy, footer copy, contact form spec

Here's everything that needs to be built. Work through it in the order listed — there are dependencies.

---

## 1. New Pages (create these first — footer links depend on them)

### `about.html`
Full About page. Copy is in `Sparkwright_Website_Copy_Draft_v1.md` under **Tier 2**.
- Same site aesthetic as `index.html` (nav, footer, dark background, same fonts)
- First-person text content, no special interactivity needed
- Nav on this page: same as landing page, but "About" link points back to this page (not an anchor)

### `terms.html`
Terms of Use. Copy is in `Sparkwright_Legal_Draft_v1.md` under **Terms of Use**.
- Same site aesthetic, static text page
- Readable body text — not a wall of undifferentiated copy. Use the section headings from the doc.
- **Do not publish live yet** — developer needs to add the effective date before this goes live. Build it, but hold the deploy or note that it needs the date.

### `privacy.html`
Privacy Policy + Cookie Policy (one page). Copy is in `Sparkwright_Legal_Draft_v1.md` under **Privacy Policy** and **Cookie Policy (Brief)**.
- Same aesthetic, static text
- Cookie Policy is a short section — append it to the bottom of the Privacy Policy page, don't make it a separate page
- Same hold note: effective date needed before publishing

### `contact.html`
Contact form. Uses Netlify Forms — no backend or JavaScript needed.
- **Before building:** In the Netlify dashboard → Forms → Enable form detection
- Form markup and full implementation spec is in `Agent_Handoff.md` under the "Netlify Forms implementation details" entry (March 28)
- Fields: Name, Email, Message, Submit button
- Match site aesthetic — styled form, not a bare HTML form
- **Do not configure the email notification destination yet** — developer is setting up `contact@sparkwright.org` and will confirm when it's live. Build the form; she'll configure the notification in the Netlify dashboard herself once the address is ready.

---

## 2. Footer Updates (both `index.html` and `games/mathflash/index.html`)

Replace the current footer content with:
- Left: `Sparkwright · © 2026`
- Center: `Privacy Policy` (links to `/privacy.html`) · `Terms of Use` (links to `/terms.html`) · `Contact` (links to `/contact.html`)
- Right: `An independent learning project.`

Suggested HTML and a `.footer-link` style spec are in `Sparkwright_Legal_Draft_v1.md` under **Footer Copy**. Links should be muted text, underline on hover, no underline at rest — matching the existing footer text style.

---

## 3. Nav Updates (`index.html`)

- Change the "About" nav link from `href="#about"` (anchor) to `href="/about.html"` (page)
- Add a "Contact" nav link pointing to `/contact.html`
- Nav should now read: `Games · About · Contact`

The about strip (`id="about"`) can stay on the landing page as-is — it's a summary teaser. The nav link just now points to the full About page instead.

---

## 4. Landing Page Copy Updates (`index.html`)

All replacement copy is in `Sparkwright_Website_Copy_Draft_v1.md` under **Tier 1**. These are copy-swap only — no structural changes needed.

- **Hero eyebrow:** Replace `Independent learning tools` with `For homeschool families, tutors, and independent educators` — *this is a positioning choice the developer confirmed is fine, but flag it for her to review before deploying*
- **Math Flash card description:** Replace current card copy with the Tier 1 draft
- **About strip body copy:** Replace both paragraphs with the Tier 1 draft
- **About strip value bullets:** Replace all four bullets with the Tier 1 draft
- **Coming-soon card descriptions:** Replace all three card descriptions with the Tier 1 draft (names — Spelling Sprint, Number Sense Lab, Timed Challenge — stay as-is for now)

---

## 5. Math Flash Title Screen — About Panel

Copy is in `Sparkwright_Website_Copy_Draft_v1.md` under **Tier 3**.

Add an "About Math Flash" or "How this works" button to the game's title/setup screen. Tapping it opens a panel or modal with the Tier 3 copy. This is a **design discussion before coding** — the copy is ready, but the button placement, panel style, and whether it's a modal or slide-in needs a quick conversation with the developer first. Flag this item and don't build it without that discussion.

---

## Summary of Files to Touch

| File | Action |
|---|---|
| `index.html` | Copy updates (Tier 1), nav update, footer update |
| `games/mathflash/index.html` | Footer update only (title screen About panel is separate discussion) |
| `about.html` | Create new |
| `terms.html` | Create new (hold effective date) |
| `privacy.html` | Create new (hold effective date) |
| `contact.html` | Create new (hold notification config) |

---

## What to Ask the Developer Before Starting

One thing to confirm: the hero eyebrow change is a positioning call — she approved it in Spark session but it's worth a quick "does this look right to you?" when you show her the landing page update.

Everything else is clear to build.
