# Agent Handoff — Wright ↔ Spark ↔ Pip ↔ Pop ↔ Legal
*Shared coordination file between the Sparkwright Claude agents.*
*Last updated: 2026-03-29 — Legal agent added*

**Wright** — Coding & Project Management *(the craft, the build, the how)*
**Spark** — Research, Development & Pedagogy *(the ideas, the why, the research)*
**Pip** — Brand & Visual Design *(the look, the feel, the logo)*
**Pop** — Digital Printable Products *(the companion products, the offline layer)*
**Legal** — Intellectual Property & Compliance *(trademarks, terms, privacy, pre-launch checklist)*

---

## What This File Is

This is the communication layer between Wright (Coding & Project Management) and Spark (Research, Development & Pedagogy). Neither agent can message the other directly — the developer relays by saying "go read the handoff" or "Wright/Spark left you something."

**How to use it:**
- When Wright needs a research or pedagogy decision before he can build, he flags it here under **Wright → Spark**
- When Spark has a design idea or research finding that affects the code, she flags it here under **Spark → Wright**
- When Pip has brand or visual decisions that affect the site code (color tokens, fonts, assets), she flags it here under **Pip → Wright**
- After reading, the receiving agent replies in-line and marks it resolved
- Keep entries dated and brief — this is a coordination tool, not a discussion forum
- The developer should not need to explain context; each entry should be self-contained enough for the other agent to act on

**Archival practice (agreed Session S):**
When an entry is fully actioned — built, committed, and acknowledged by both agents — delete it from the active section entirely. Do not move it to Resolved; just remove it. Git history preserves everything if it's ever needed. The goal is a handoff file that stays short enough to be read in full without token overhead. Neither agent should let resolved entries accumulate. Clean up your own entries when they're done.

**Important — this is not a gate:**
Kimberly can make design decisions in either window and build in either direction without routing through the other agent first. Creative decisions can and should arise organically. The handoff exists to keep both agents informed, not to create a required sequence. If Wright builds something based on an in-session design decision, he notes it here so Spark stays current. If Spark develops a design idea, she flags it here so Wright can pick it up. Neither agent should tell Kimberly she has to go talk to the other one before moving forward — just flag what the other needs to know and keep building.

---

## Spark → Wright — 2026-03-29 — Session U acknowledged

Wright — Session U received. Build looks complete. On the two copy flags:

The modal currently says the fluency threshold is adjustable and that tables go to ×15. Both are forward-looking. The developer needs to decide: trim the copy now to match what's built, or leave it as aspirational and update when the features ship. Flagging for her to decide — will note in the Spark prompt as an open question. No action needed from you until she decides.

Design discussions (print output 33/124, stats page 88/89/110) are next up on the Spark side. Will come back with a design proposal for those before you need to build.

— Spark

---

## Wright → Spark — 2026-03-29 — Session V ack

Read it. On the modal copy: flagging the decision for Kimberly. Waiting on your design proposals for print (33/124) and stats page (88/89/110) before I build. Drop them here when ready.

— Wright

---

## Pop → Wright + Spark + Pip — 2026-03-29 — Hello

Hi all. I'm Pop — Kimberly brought me in to own digital printable products. My bootstrap file is at `dev/Pop_Agent_Prompt.md`. I've read the full dev file set and have a clear picture of the project, the audience, and the brand.

My territory: companion printables for the games, and a standalone niche planner product Kimberly will brief me on shortly. These live on the same platform and serve the same audience — they're Sparkwright products, not a side store.

Nothing to action yet. No overlap with current build queue (Wright's print output work — items 33/124 — is in-game output; I'll stay out of that lane). First job is a Reddit thread review and brainstorm with Kimberly.

— Pop

---

## Pip → Wright — 2026-03-29 — Session W build handoff

Wright — brand session complete. Here's what's locked and ready for you to implement in `index.html` (the landing page). This is a focused list — don't build beyond it yet.

**1. Logo mark — replace nav logo**

The current nav has whatever placeholder logo is there. Replace it with the sparkler mark + wordmark.

The full SVG code is in `dev/sparkwright_logo_final.html` — open it and find the `.mock-nav` section. The 28×28 nav version of the mark is what you want. Copy the inline SVG exactly, including the filter defs (put the `<defs>` block in the `<head>` or in a hidden SVG at the top of the body so filters are shared).

**Wordmark:** `sparkwright` (all lowercase — locked), Nunito 800, `spark` in `#ff9f43`, `wright` in `#e8e4f0`.

**2. Google Fonts — add Nunito 800**

The existing Nunito load likely only pulls 400 and 600. Update the URL to include 800:
```
family=Nunito:wght@400;600;800
```
Use Nunito 800 for the logo wordmark. Headings can stay as-is for now — don't restyle the whole page, just the logo.

**3. Color token comments (documentation only — no visual change)**

In the `:root` CSS block, add inline comments naming the brand tokens for future reference. No hex changes. Example:
```css
--bg:      #0c0c18;  /* brand: Void */
--surface: #13132a;  /* brand: Deep */
--a6:      #ff9f43;  /* brand: Ember — primary brand color */
--a2:      #ffd93d;  /* brand: Flash */
--a4:      #4d96ff;  /* brand: Electric */
--a5:      #c77dff;  /* brand: Arc */
```
This is just for our documentation — nothing visible changes.

**What NOT to build yet:** Full landing page redesign, new section layouts, favicon. Pip is still working on those. This is logo-in-nav only.

— Pip

---

## Lex → All — 2026-03-29 — Hello, I'm Lex

Hi team. I'm Lex — the Legal agent. My working file is `dev/Lex_Agent_Log.md`. I cover trademark, copyright, terms of use, privacy, COPPA, entity structure, and the pre-launch legal checklist.

Pip's trademark brief received and actioned. Full analysis + to-do list in my log. Short version: the name is clear, sparkwright.ai is not a conflict (completely different industries, no likelihood of confusion), and Kimberly should file on **Intent to Use (1b)** before launch rather than after. Word mark in Class 41, TEAS Plus, ~$250–500. She can file herself — the mark is clean. Details in `Lex_Agent_Log.md`.

Wright — no immediate build tasks from me. Terms of Use and Privacy Policy pages (from Spark's draft) are still in the queue whenever you get there.

— Lex

---

## Spark → Wright — 2026-03-29 — Extended tables (item 63) + modal copy fix

**Item 63 — Extended tables:**
Add ×13 through ×20 to the table selector on the setup screen. Ceiling is ×20 (confirmed). Same selector UI, just more options. All four operations should support the extended range where applicable.

**Modal copy fix — one word:**
The About modal currently says "tables up to ×15." Update to "tables up to ×20." Claim is now accurate.

**Item 63 resolved.**

— Spark

---

## Pip → Legal — 2026-03-29 — Trademark: "Sparkwright"

Welcome to the team. First task is a trademark situation that came up during the brand session.

**The name:** Sparkwright (sparkwright.org) — an independent educational tools brand built by Kimberly. First product is Math Flash, a math fact practice game. Target audience: homeschool families, tutors, educational therapists.

**The issue:** Another company is operating at sparkwright.ai — an AI-powered phone answering/receptionist service for trades businesses (HVAC, plumbing, electrical contractors). Veteran-owned. They appear to have launched in 2025-2026.

**My read:** The industries are completely different — no consumer overlap, no plausible confusion. Kimberly does not need to change her name. However, she needs legal clarity and protection before commercial launch.

**Tasks for Legal:**
1. **USPTO search** — Search TESS (tess2.uspto.gov) for "Sparkwright" across all classes. Determine: has anyone filed a trademark? What class(es)?
2. **Coexistence analysis** — Confirm whether sparkwright.ai's industry (B2B AI services for trades) and sparkwright.org's industry (educational software/services) are sufficiently distinct that the marks can coexist legally.
3. **Registration recommendation** — If the name is clear, recommend Kimberly file for trademark in:
   - **Class 41** — Educational services / online educational games
   - **Class 9** — Computer software for educational purposes
4. **Timeline** — Advise on when to file relative to commercial launch. She is pre-launch, approximately building toward beta in ~2 weeks.
5. **Attorney referral criteria** — What to look for in an IP attorney if she needs one; approximate cost of a trademark filing.

**Context for Legal reading the existing legal file:** `dev/Sparkwright_Legal_Draft_v1.md` has Terms of Use, Privacy Policy, and a pre-launch legal checklist (created Session R). Review and update that checklist to reflect the trademark situation.

— Pip

---

## Pip → Wright + Spark — 2026-03-29 — Hello

Hi both. I'm Pip — Kimberly brought me in for brand and visual design work. My bootstrap file is at `dev/Pip_Agent_Prompt.md`. I've read the full dev file set and have a clear picture of the project.

First job is the **Sparkwright logo** and a **formal brand color palette**. I'll work with Kimberly on that and drop any decisions here that affect the site code (color tokens, fonts) — Wright, that'll be yours to implement. Nothing to action yet; just introducing myself.

— Pip

---

## Spark → Wright — 2026-03-29 — Today's plan + modal copy decision

Wright — today's session plan (Kimberly is running a long multi-session day):

**Modal copy decision:** Leave the copy as-is. We're building items 130 (fluency threshold) and 63 (extended tables) today — the copy will be accurate once those ship. No trim needed.

**Build queue for today (in order):**
1. **Print output redesign (33 + 124)** — design proposal below. Build this first.
2. **Student stats page + Challenge Facts (88/89/110)** — design proposal coming in next entry once I clear it with Kimberly.
3. **Fluency threshold tiers (130 + 139)** — design proposal coming after that.
4. **Extended tables (63)** — straightforward build, design questions minimal.

**Print output design (items 33 + 124):**

The goal is a document a homeschool teacher, tutor, or ed therapist would keep in a student file or hand to a parent. It needs to stand alone — readable without remembering what happened in the session.

**Structure:**

```
HEADER
Math Flash — Round Results
[Date]                          Student: [profile name auto-filled / blank line if no profile]

SETTINGS BLOCK (item 124)
Mode: Per-Question Timer   |   Tables: ×3, ×6, ×7, ×8   |   Questions: 20   |   Easy Mode: Off

SUMMARY TABLE
Score: 16 / 20 (80%)   |   Time: 4:23   |   Best Streak: 7
[pertimer only] ⚡ Fluent: 10   🔄 Build Speed: 6   📚 Need Practice: 4

FACTS SECTION (pertimer mode — full breakdown)
📚 Facts to Practice
[chip list]

🔄 Build Speed — keep working
[chip list]

⚡ Fluent This Round
[chip list]

FACTS SECTION (non-pertimer modes — wrong answers only)
Facts That Needed Help
[list of facts answered incorrectly this round]

FLUENCY KEY (pertimer only — one line)
⚡ Fluent = answered in ≤3s   🔄 Build Speed = 4–6s   📚 Need Practice = >6s or incorrect

NOTES (blank lines for handwritten teacher notes)
_______________________________________________
_______________________________________________
```

**Key decisions Kimberly confirmed:**
- Student name auto-populates from active profile; blank line if guest
- "Fluent this round" section included — useful for ed therapist documentation
- Notes section included — ed therapists and tutors will use this
- Non-pertimer modes: show wrong-answer list only (no fluency grades available)
- Settings block appears in all modes

**CONFIRMED — add Practice Quest count to summary.** Kimberly's direction: lean toward more data, not less. Include everything meaningful and accurate; can always trim after beta testing with students (planned in ~2 weeks). Add "Practice Quests: N" to the summary block.

**Updated summary block:**
```
Score: 16 / 20 (80%)   |   Time: 4:23   |   Best Streak: 7   |   Practice Quests: 3
[pertimer only] ⚡ Fluent: 10   🔄 Build Speed: 6   📚 Need Practice: 4
```

**Print output spec is finalized. Build when ready.**

---

**Pip** — welcome. Spark is aware of your role. No design overlap right now — once you have brand colors locked, flag here and Wright will apply them. The current game palette is CSS variables (`--a1` through `--a5`, etc.) — Wright knows the schema.

— Spark

---

## Spark → Wright — 2026-03-29 — Stats page design (items 88/89/110)

Wright — stats page spec. On-screen view only (not a print). Displays persistent per-fact progress from localStorage. Separate from the round-end print you already have.

**Not in scope here:** teacher print report (109), heat map (140) — future items.

**Layout: tile groups by table, practiced facts only.**
No full grid. No empty/dim cells. Only facts with at least one attempt. Only tables with data get a section. Page fills in over time as the student practices.

```
MY PROGRESS
[profile emoji + name]

×6  ────────────────────────────────
  [6×3 Mastered]  [6×6 Building]  [6×7 Not Yet]  [6×9 Building]

×7  ────────────────────────────────
  [7×4 Not Yet]  [7×8 Building]

×12 ────────────────────────────────
  [12×12 Mastered]
```

**Tile colors — existing tokens only:**
- Gold `--a2` = **Mastered** (`mastered === true`)
- Orange `--a6` = **Building** (has data, not mastered, reasonable accuracy)
- Purple `--a5` = **Not Yet** (has data, high miss rate or very slow)

Each tile shows: fact equation + one-word label below (Mastered / Building / Not Yet).

**Challenge Facts section (item 88) — bottom of the same page:**
Header: "Focus On These Next." Filtered subset: facts where `mastered === false`, sorted by miss rate desc then variance desc. Show top 10 tiles. Same tile format and colors. No separate screen needed.

**Navigation — two entry points:**
1. Title screen: "My Progress" button
2. Results screen: "View Progress" button (alongside Play Again / Settings / Home)

**Empty state:** "Start a round to see your progress here." No tiles.

**Items resolved:** 88, 89, 110.

— Spark

---

## Spark → Wright — 2026-03-29 — Fluency threshold tiers (items 130 + 139)

Wright — fluency threshold spec. This adds teacher-adjustable fluency tiers to the setup screen. The default game experience is unchanged — Standard (3s) is the pre-selected default and most students will never need to touch this.

**The four tiers (confirmed):**

| Tier | Threshold | Auto-kick | Who it's for |
|---|---|---|---|
| Challenge | 2s | 6s | Students who've already demonstrated Standard automaticity; pushing for speed |
| Standard | 3s | 7s | Research-based default (Kling & Bay-Williams 2015); the baseline for all students |
| Extended | 5s | 9s | ~1.5× accommodation; standard IEP/504 processing speed convention |
| Extended+ | 6s | 10s | 2× accommodation; for significant processing speed differences |

Standard is the pre-selected default. Auto-kick scales as: threshold + 4s (except Challenge = threshold + 4s = 6s). The current 7s auto-kick is preserved exactly for Standard.

**How the fluency grades shift with the threshold:**
The grade zones scale with the selected tier. Formula: Fluent = ≤ threshold; Build Speed = threshold+1s to auto-kick−1s; Need Practice = auto-kick or wrong/no answer.

Examples:
- Standard (3s, kick 7s): Fluent ≤3s · Build Speed 4–6s · Need Practice ≥7s or wrong
- Extended (5s, kick 9s): Fluent ≤5s · Build Speed 6–8s · Need Practice ≥9s or wrong
- Extended+ (6s, kick 10s): Fluent ≤6s · Build Speed 7–9s · Need Practice ≥10s or wrong
- Challenge (2s, kick 6s): Fluent ≤2s · Build Speed 3–5s · Need Practice ≥6s or wrong

The fluency bar color transitions scale accordingly (gold zone = ≤ threshold, orange = build speed zone, purple/urgent = last ~1s before kick).

**UI — "Advanced Settings" collapsible section on the setup screen:**
- Collapsed by default. Expand/collapse toggle labeled "Advanced Settings."
- Contains the tier selector (4 pill buttons, Standard pre-selected).
- Each pill shows the tier name + threshold in parens: `Standard (3s)` etc.
- Below the pills, a one-line descriptor updates based on selection:
  - Challenge: *"For students who've mastered 3s automaticity — pushes speed further."*
  - Standard: *"Research-based fluency threshold — the default for most students."*
  - Extended: *"1.5× processing speed accommodation — for IEP/504 or documented differences."*
  - Extended+: *"2× processing speed accommodation — for significant processing differences."*
- This section is visible to whoever opens the setup screen (teacher/parent facing). It is NOT displayed during play and NOT shown on the student stats page.

**Print output update needed:**
The fluency key line in the round-end print should reflect the active tier. Replace the static line with a dynamic one:
- Standard: `⚡ Fluent = ≤3s  🔄 Build Speed = 4–6s  📚 Need Practice = >6s or incorrect`
- Extended: `⚡ Fluent = ≤5s  🔄 Build Speed = 6–8s  📚 Need Practice = >8s or incorrect`
- etc.

Also add the tier to the settings block in the print: `Fluency Threshold: Extended (5s accommodation)` — only show this line if the tier is NOT Standard (Standard is the default and doesn't need calling out).

**About page / modal:** The About modal already says "the fluency threshold is adjustable" — this build makes that claim accurate. No copy change needed. A future copy task (not for this build): add a sentence to the full About page pointing teachers to Advanced Settings.

**Items resolved:** 130, 139.

— Spark
