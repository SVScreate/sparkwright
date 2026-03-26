# Agent Handoff — Wright ↔ Spark
*Shared coordination file between the two Sparkwright Claude agents.*
*Last updated: 2026-03-26 — Session O*

---

## What This File Is

This is the communication layer between Wright (Coding & Project Management) and Spark (Research, Development & Pedagogy). Neither agent can message the other directly — the developer relays by saying "go read the handoff" or "Wright/Spark left you something."

**How to use it:**
- When Wright needs a research or pedagogy decision before he can build, he flags it here under **Wright → Spark**
- When Spark has a design idea or research finding that affects the code, she flags it here under **Spark → Wright**
- After reading, the receiving agent replies in-line and marks it resolved
- Keep entries dated and brief — this is a coordination tool, not a discussion forum
- The developer should not need to explain context; each entry should be self-contained enough for the other agent to act on

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

*(Spark will reply here)*

---

## Resolved

*(Completed handoffs get moved here with a resolution note)*
