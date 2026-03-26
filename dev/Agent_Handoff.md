# Agent Handoff — Wright ↔ Spark
*Shared coordination file between the two Sparkwright Claude agents.*
*Last updated: 2026-03-26 — Session O (both agents online)*

---

## What This File Is

This is the communication layer between Wright (Coding & Project Management) and Spark (Research, Development & Pedagogy). Neither agent can message the other directly — the developer relays by saying "go read the handoff" or "Wright/Spark left you something."

**How to use it:**
- When Wright needs a research or pedagogy decision before he can build, he flags it here under **Wright → Spark**
- When Spark has a design idea or research finding that affects the code, she flags it here under **Spark → Wright**
- After reading, the receiving agent replies in-line and marks it resolved
- Keep entries dated and brief — this is a coordination tool, not a discussion forum
- The developer should not need to explain context; each entry should be self-contained enough for the other agent to act on

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

## Resolved

*(Completed handoffs get moved here with a resolution note)*

- **2026-03-26 — Data Philosophy orphan** — Spark recovered full content from git, expanded RP Section 2, updated MPF cross-reference. Both documents self-consistent. ✅
