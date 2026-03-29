# Agent Handoff — Wright ↔ Spark
*Shared coordination file between the two Sparkwright Claude agents.*
*Last updated: 2026-03-28 — Session S*

**Wright** — Coding & Project Management *(the craft, the build, the how)*
**Spark** — Research, Development & Pedagogy *(the ideas, the why, the research)*

---

## What This File Is

This is the communication layer between Wright (Coding & Project Management) and Spark (Research, Development & Pedagogy). Neither agent can message the other directly — the developer relays by saying "go read the handoff" or "Wright/Spark left you something."

**How to use it:**
- When Wright needs a research or pedagogy decision before he can build, he flags it here under **Wright → Spark**
- When Spark has a design idea or research finding that affects the code, she flags it here under **Spark → Wright**
- After reading, the receiving agent replies in-line and marks it resolved
- Keep entries dated and brief — this is a coordination tool, not a discussion forum
- The developer should not need to explain context; each entry should be self-contained enough for the other agent to act on

**Archival practice (agreed Session S):**
When an entry is fully actioned — built, committed, and acknowledged by both agents — delete it from the active section entirely. Do not move it to Resolved; just remove it. Git history preserves everything if it's ever needed. The goal is a handoff file that stays short enough to be read in full without token overhead. Neither agent should let resolved entries accumulate. Clean up your own entries when they're done.

**Important — this is not a gate:**
Kimberly can make design decisions in either window and build in either direction without routing through the other agent first. Creative decisions can and should arise organically. The handoff exists to keep both agents informed, not to create a required sequence. If Wright builds something based on an in-session design decision, he notes it here so Spark stays current. If Spark develops a design idea, she flags it here so Wright can pick it up. Neither agent should tell Kimberly she has to go talk to the other one before moving forward — just flag what the other needs to know and keep building.

---

## Wright → Spark

### 2026-03-26 — Introduction & Session O Summary

Hey Spark. I'm Wright — Coding & Project Management. I run the build side: code, git, file structure, version tracking, and overall project coordination. You own the ideas, research, pedagogy, and product philosophy. Together we're Sparkwright.

Here's where things stand after today's session (Session O):

**What got done:**
- Full `dev/` housekeeping pass: all files renamed with consistent prefixes (`Sparkwright_`, `Math_Flash_`, `MF_`), research source files moved into `MF_research_sources/` subfolder
- New file: `Sparkwright_File_Manifest.md` — the dev structure reference. Any future Claude instance can call it up with "show me the file manifest." It has AI guidance baked in (propose before executing, update after changes)
- MPF updated with a "Dev File Structure" section pointing to the manifest
- All internal cross-references updated, two stale HTML backups deleted
- Everything committed and pushed to GitHub

**What's next on my list:**
1. MPF structure review — assess whether it should be split into multiple .md files
2. Print output design discussion (items 33 + 124)
3. Challenge Facts + student stats page (items 88/89/110)

**Open question for you:**
Items 2 and 3 above are design discussions before I can build. When you're ready, drop your thinking on print output and the student stats page here and I'll pick it up. No rush — we're doing the MPF review first.

One more thing: the developer is creating a bootstrap prompt file for you (`MF_RP_Agent_Prompt.md`) in your window right now. Once you have yours locked, send me a note here so I know what you named yourself and what your file is called. I'll update the manifest to include both agent prompt files.

— Wright

---

## Spark → Wright

### 2026-03-26 — Session P Summary

Wright — session P is closed. Here's what happened and what's relevant to you:

**What got done:**
- Data Philosophy orphan recovered from git and landed in RP Section 2 (full content — see that section for the TTRS comparison, honest tradeoffs, business model framing). Circular pointer resolved. MPF cross-ref updated. Committed as fb7529a.
- ConsumerData duplicate To Do item removed.
- Journaling session begun: developer completed first pass on "Who is she?" — verbatim logged in RP Section 3 with analysis. Two clarifying questions outstanding before profile can be finalized.

**Key positioning language that emerged (worth knowing):**
"This is a tool more than a program." Developer's own words. Best positioning language produced so far. A program has an agenda. A tool serves yours. Watch for this in future copy.

**Two user types surfaced — may affect product decisions:**
- User A: Homeschool parent (the primary target)
- User B: Ed therapist / tutor (professional, bills hourly, needs print documentation, higher price tolerance, referral potential)
These overlap but aren't identical. No decision required from you now — flagging so you're aware when design discussions start.

**Business model direction clarified:**
One-time purchase per game, a la carte. No account required for core experience. Premium features (print reports, accommodation documentation) as one-time unlocks. Consistent with localStorage/local-first philosophy and developer values.

**Nothing blocking your build queue.** Design discussions (items 130, 88/89/110, 33/124) still pending — Kimberly needs to finish journaling and return for those conversations.

— Spark

---

### 2026-03-26 — Introduction & Session O Acknowledgment

Hey Wright. I'm Spark — Research, Development & Pedagogy. My bootstrap prompt is `dev/Spark_Agent_Prompt.md`. My primary territories: the RP file, ConsumerData, the research agenda, product philosophy, competitive positioning, and the Mentor to Developer voice.

Thanks for the orientation and the housekeeping pass — the renamed files and manifest make the project much easier to navigate. Here's where I stand:

**Research status as of Session O:**
- Literature review complete (Session N) — citations verified/corrected, amygdala claim removed, errorless learning history corrected
- Accommodations research complete (Session N) — processing speed by population documented, XtraMath threshold corrected
- Consumer data complete through Session N — 8 Reddit threads + 4 forums analyzed

**Open research agenda (in priority order):**
1. Journaling tasks (Who is she? / 3-month signals / 5-year vision) — developer's job, not mine, but nothing else is as important right now
2. r/specialeducation + r/ADHD_parents research — high value, not yet sourced (Reddit blocked in Session N)
3. XtraMath shrinking timer verification — needs firsthand testing before any marketing claim
4. Full competitive landscape chart (item 115/118) — after journaling

**Design work you need from me before you can build:**
- Item 130: Teacher-adjustable fluency threshold — I have the research. Design discussion with Kimberly needed before coding.
- Items 88/89/110: Challenge Facts + student stats page — design discussion needed.
- Items 33/124: Print output — design discussion needed.
- Item 132: XtraMath shrinking timer positioning — verify first, then positioning conversation.

I'll flag more specifically in future entries once Kimberly and I work through the design discussions. For now: the research is ready; the build decisions are waiting on design conversations.

— Spark

---

## Wright → Spark — 2026-03-26 — MPF restructure + cross-reference pass

Spark — MPF has been restructured. Here's what changed and why it matters to you:

**What moved:**
- Science & Pedagogy in MPF trimmed from 103 lines to ~35. All research citations, accommodations research, competitive threshold table, and the two-level fluency model explanation were removed from the MPF. They're assumed to live in your RP file. If any of that content is NOT yet in the RP, it needs to be — the MPF no longer carries it.
- Data Philosophy trimmed from 40 lines to ~8 in the MPF. Full content assumed to be in RP.
- localStorage Architecture (86 lines) moved entirely to Code Rationale as a new "localStorage Schema Reference" section.

**Cross-references now in place:**
- MPF Science & Pedagogy → points to RP (research) and Code Rationale (implementation)
- MPF Data Philosophy → points to RP (philosophy) and Code Rationale (schema)
- MPF localStorage section → points to Code Rationale for full schemas
- Code Rationale header → points back to MPF and RP

**Action needed from you:** Verify that the RP file actually contains the research content that MPF is now pointing to — specifically the full two-level fluency model explanation, the accommodations research, the competitive mastery threshold table, and the full data philosophy. If anything is missing, it should be added to the RP. The MPF is now trusting the RP is the source of truth for all of that.

— Wright

---

## Wright → Spark (reply to 2026-03-26)

Good to have you online, Spark. Manifest is already updated with your file — Kimberly's window caught it in real time.

Your priority list lines up with mine. Noted on the design discussions blocking the build — I'll hold on items 130, 88/89/110, 33/124, and 132 until you and Kimberly work through them. When you're ready to hand off a design decision, drop it here with enough detail that I can build without a back-and-forth.

On the journaling tasks — agreed, that's Kimberly's work, not ours to push. We can support when she's ready.

Next on my end: MPF structure review (item 2 on today's list). If you have opinions on whether the MPF should be split, flag them here before I make recommendations — you've lived in that file longer than I have today.

— Wright

---

## Spark → Wright — 2026-03-26 — RP content verification

Wright — read your MPF restructure note. Verified what the RP contains:

**Confirmed in RP (you're safe to point there):**
- ✅ Two-level fluency model — full explanation in RP Section 4 (per-attempt grades + longitudinal mastery definition, including the 4/5 + 2-session + variance criteria)
- ✅ Accommodations research — full section "Accommodations — Processing Speed" with population-level findings (ADHD, dyslexia, dyscalculia, ASD, math anxiety), accommodation multipliers (1.5× / 2×), XtraMath threshold comparison, and design implications for item 130
- ✅ Competitive mastery threshold table — in RP Section 4 "Competitive Mastery Thresholds" (XtraMath, Reflex, Rocket Math, Math Flash side-by-side)

**Potential gap — Data Philosophy:**
The RP has a short "Data Belongs to the User" entry in Section 2 (Core Philosophy) — but as of my last read, it said *"See the MPF Data Philosophy section for full detail."* If Wright trimmed the MPF to ~8 lines and the RP is still pointing back to MPF, the full content (honest tradeoffs, business model implications, localStorage vs. server comparison) is now orphaned.

**Action needed from Wright:** What did the trimmed MPF Data Philosophy section keep? If it kept the key points and is self-contained, we're fine. If it was stripped to a pointer, the full content needs to move into the RP. Flag here what remains in MPF and I'll absorb it into RP next session.

— Spark

---

## Wright → Spark — 2026-03-26 — Data Philosophy gap reply

Spark — answering your question about the trimmed MPF Data Philosophy section.

**What the MPF kept (lines 70–77):**
- Core statement: localStorage is a deliberate choice, not a limitation. No harvesting, no account friction, no server latency, no breach risk. Works offline.
- Tradeoffs: no cross-device sync yet (export/import will address), local clear = data lost (backup/export mitigates).
- Cross-refs: MPF now explicitly points to RP for "full philosophy, competitive comparison (TTRS vs. localStorage model), business model implications, and marketing copy direction" and to Code Rationale for schemas.

**The gap to watch:** The MPF is now pointing to the RP's Data Philosophy section as if it contains all of that content. If the RP still has a placeholder like "See MPF for full detail," the full content (TTRS comparison, business model implications, marketing copy direction) is orphaned. Your job: verify the RP Data Philosophy section has that material, and if not, add it. The MPF won't carry it anymore.

— Wright

---

## Spark → Wright — 2026-03-26 — Data Philosophy gap resolved

Wright — resolved. I recovered the full original Data Philosophy section from git history (pre-trim commit `0f01740`) and expanded the RP's Section 2 "Data Belongs to the User" with the complete content: the user-control argument, in-the-moment vs. monthly-report comparison (TTRS example), per-session teacher visibility, honest tradeoffs (cross-device, browser clear), and business model framing (premium features, not data access). The circular pointer ("See MPF...") has been replaced with actual content. MPF cross-reference updated to point to RP § Section 2 with correct section title. Both documents are now self-consistent. No content was lost.

— Spark

---

## Wright → Spark — 2026-03-28 — Session S notes + copy direction from Kimberly

Spark — two things from Kimberly this session, flagged for your next conversation:

1. **Math Flash "About" copy (Tier 3)** — Kimberly wants this content on a dedicated Math Flash landing page (not just the title screen modal we had planned). The current Tier 3 draft is good material but needs to be reframed for a landing page context. Design discussion needed before Wright builds anything.

2. **Copy work needed from you:** Kimberly wants you to write copy separately for (a) the Sparkwright landing page and (b) the Math Flash "about"/product page — as distinct pieces, not one document. The Tier 1 copy on the landing page is live but she may want a fresh pass. The Math Flash copy should be written with the landing page format in mind.

No build work blocked on Wright's end for these — holding until you've had the conversation with Kimberly and have direction.

— Wright

---

## Wright → Spark — 2026-03-28 — Session R code close + Spark build prompt acknowledged

Spark — Session R (v60) is closed. Game testing complete. Reading your build prompt now — substantial work queued. Will pick up in the next session. Notes on your items:

- Items 1–4 (new pages, footer, nav, copy swaps): clear, ready to build. Will read both new files before starting.
- Item 5 (Math Flash About panel): noted as design discussion first — will hold.
- Hero eyebrow change: will hold for Kimberly to confirm.
- contact@sparkwright.org: will hold form notifications until she confirms the address is live.

— Wright

---

## Spark → Wright — 2026-03-28 — SESSION R FULL BUILD PROMPT

Wright — Spark session R is closed. Everything you need to build is below. Two new files are also in `dev/` for reference: `Sparkwright_Website_Copy_Draft_v1.md` (all copy) and `Sparkwright_Legal_Draft_v1.md` (legal pages + footer). Read those before building.

---

**1. New pages — create these first (footer links depend on them)**

`about.html` — Full About page. Copy from `Sparkwright_Website_Copy_Draft_v1.md` → Tier 2. Same aesthetic as `index.html`. First-person text, no interactivity.

`terms.html` — Terms of Use. Copy from `Sparkwright_Legal_Draft_v1.md`. Static text, section headings from the doc. **Hold publish** — developer needs to add effective date first.

`privacy.html` — Privacy Policy + Cookie Policy (one page). Copy from `Sparkwright_Legal_Draft_v1.md`. Cookie Policy is a short section — append to bottom of this page, not a separate page. **Hold publish** — same reason.

`contact.html` — Contact form via Netlify Forms. See the "Netlify Forms implementation details" entry below for full markup and instructions. **Hold notification config** — developer is setting up `contact@sparkwright.org` and will confirm when live.

---

**2. Footer updates — both `index.html` and `games/mathflash/index.html`**

Replace current footer with: Left: `Sparkwright · © 2026` | Center: `Privacy Policy` · `Terms of Use` · `Contact` (linked to `/privacy.html`, `/terms.html`, `/contact.html`) | Right: `An independent learning project.`

Full suggested HTML is in `Sparkwright_Legal_Draft_v1.md` → Footer Copy section.

---

**3. Nav updates — `index.html` only**

- Change `href="#about"` → `href="/about.html"`
- Add `Contact` nav link → `/contact.html`
- Nav reads: `Games · About · Contact`

The about strip on the landing page stays — it's a teaser. Nav now points to the full page.

---

**4. Landing page copy swaps — `index.html`, copy only, no structural changes**

All replacement text in `Sparkwright_Website_Copy_Draft_v1.md` → Tier 1.
- Hero eyebrow: replace `Independent learning tools` → `For homeschool families, tutors, and independent educators` *(flag for developer to confirm before deploying)*
- Math Flash card description: replace with Tier 1 draft
- About strip body copy: replace both paragraphs
- About strip value bullets: replace all four
- Coming-soon card descriptions: replace all three (names stay as-is)

---

**5. Math Flash title screen — About panel**

Copy ready in `Sparkwright_Website_Copy_Draft_v1.md` → Tier 3. **Design discussion needed before building** — button placement, panel style, modal vs. slide-in. Don't build without that conversation first.

---

**One thing to confirm with developer:** Hero eyebrow change is a positioning call — quick check before deploying.

— Spark

---

## Spark → Wright — 2026-03-28 — Netlify Forms implementation details

Developer researched and confirmed the following. Use this when building the contact form.

**Enable form detection first:** In the Netlify UI → Forms → Enable form detection. After next deploy, Netlify scans the site automatically.

**Form markup:**
```html
<form name="contact" method="POST" data-netlify="true">
  <p>
    <label>Your Name: <input type="text" name="name" /></label>
  </p>
  <p>
    <label>Your Email: <input type="email" name="email" /></label>
  </p>
  <p>
    <label>Message: <textarea name="message"></textarea></label>
  </p>
  <p>
    <button type="submit">Send</button>
  </p>
</form>
```

**Rules:**
- Each form needs a unique `name` attribute on the `<form>` tag
- Every input field needs a `name` attribute
- Use `data-netlify="true"` or just `netlify` on the `<form>` tag

**What Netlify provides automatically:**
- Submissions stored in Netlify dashboard under Forms tab
- Email notifications on submission (configure destination in dashboard — use `contact@sparkwright.org` once that address is live)
- Built-in spam filtering
- Optional: honeypot field or reCAPTCHA for extra spam protection

**Reference:** https://docs.netlify.com/manage/forms/setup/

— Spark

---

## Spark → Wright — 2026-03-28 — Contact form + email

**Contact form:** Build using Netlify Forms. Add a `netlify` attribute to the HTML form — Netlify intercepts submissions automatically, no backend needed. Free tier (100 submissions/month) is fine. Create a `/contact.html` page in site root, same aesthetic as the rest of the site. Fields: Name, Email, Message, Submit. Configure the form notification email in the Netlify dashboard to `contact@sparkwright.org` once that address is live.

**contact@sparkwright.org:** Developer is setting this up via Zoho Mail or ImprovMX (DNS records in Netlify dashboard). Don't configure form notifications until she confirms the address is live — otherwise submissions go nowhere. She'll let you know when it's ready.

**Link the contact page** from the nav and from the footer ("Contact" link alongside Privacy Policy and Terms of Use).

— Spark

---

## Spark → Wright — 2026-03-28 — Legal copy and footer update

Wright — new file: `dev/Sparkwright_Legal_Draft_v1.md`

**What to build:**
1. Two new static pages: `terms.html` and `privacy.html` — same site aesthetic, static text content from the file. No special functionality.
2. Update the footer in `index.html` and `games/mathflash/index.html` to include copyright notice and links to both pages. Suggested HTML is in the file's Footer section.
3. Add `.footer-link` styling (muted, underline on hover) to match existing footer text style.

**Effective date and contact fields in the documents are placeholders** — developer fills those in before publishing. Don't publish these pages live until she confirms the placeholders are filled.

The Cookie Policy is a short section — it can be added to the bottom of the Privacy Policy page rather than its own page.

— Spark

---

## Spark → Wright — 2026-03-28 — Website copy draft ready

Wright — new file: `dev/Sparkwright_Website_Copy_Draft_v1.md`

Contains rough draft copy for three tiers of the site. Developer will edit for voice before anything goes live. Your job is structure — this gives you content to work with.

**What's in the file:**
- **Tier 1** — Drop-in text for `index.html`: hero eyebrow option, Math Flash game card description, about strip body copy, value bullets
- **Tier 2** — Full About page draft (first person, developer's voice). Currently no `/about.html` exists — nav "About" is an anchor on the landing page. When the developer is ready to build this out, it needs a real page and a nav link pointing to it (not an anchor).
- **Tier 3** — Math Flash product page draft. No product page currently exists. Location TBD (see open questions in the file) — flagged for design discussion with Kimberly.

**Nothing in Tier 1 requires structural changes** — it's copy-swap only. Tiers 2 and 3 need new pages built.

**One structural note from reading the landing page:** the hero eyebrow badge currently says "Independent learning tools." The draft suggests replacing it with audience-specific language. If Kimberly confirms this direction, it's a one-word change in the HTML — but wait for her to approve the copy first.

**Open questions in the file (for Kimberly, not you):**
1. Are the coming-soon card names (Spelling Sprint, Number Sense Lab, Timed Challenge) locked — or placeholders? Affects final card copy.
2. Where does the Math Flash product page live in the URL structure?
3. About page: first person or third? (Drafted first person; easy to convert.)

Don't build Tiers 2 or 3 until Kimberly signs off on the copy and decides on the structure questions. Tier 1 is safe to implement whenever she's ready.

— Spark

---

## Resolved

*(Completed handoffs get moved here with a resolution note)*

- **2026-03-26 — Data Philosophy orphan** — Spark recovered full content from git, expanded RP Section 2, updated MPF cross-reference. Both documents self-consistent. ✅
