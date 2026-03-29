# Agent Handoff — Wright ↔ Spark
*Shared coordination file between the two Sparkwright Claude agents.*
*Last updated: 2026-03-29 — Session V (Spark design proposals incoming)*

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

**One thing to confirm with Kimberly before building:** Should Quest count (how many Practice Quest sessions triggered) appear in the summary? It's tracked. Could be useful for a teacher file. Low-urgency — add if she says yes, skip if not.

— Spark
