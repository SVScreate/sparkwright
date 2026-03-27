# Sparkwright — Dev File Manifest
*Last updated: 2026-03-26 — Session O (housekeeping pass, file renames, subfolder)*

---

## Guidance for Future AI Instances

This file is the **single source of truth for what lives in `dev/`** — file names, purposes, and structure. Use it at the start of any session involving file housekeeping, renaming, or cleanup.

**Rules:**
- Read this file before touching any file names, locations, or structure in `dev/`
- You may propose changes in chat using the chart format below
- **Always present changes to the developer for approval before executing** — never rename, move, or delete without explicit confirmation
- After any approved changes are executed, update this file and commit it in the same git pass
- When in doubt about whether a file is still needed, ask — don't assume

---

## Folder Hierarchy

```
sparkwright/
├── index.html                          ← Sparkwright landing page (live)
├── games/
│   └── mathflash/
│       └── index.html                  ← Math Flash game (live, current version)
└── dev/                                ← All development files
    ├── Sparkwright_File_Manifest.md        ← THIS FILE — dev structure reference
    ├── Sparkwright_MPF_March_22_2026_v55.md ← Master Project File (operational hub)
    ├── Sparkwright_WORKSPACE_SETUP.md       ← Dev environment setup notes
    ├── Wright_Agent_Prompt.md               ← Bootstrap prompt for Wright (Coding & PM)
    ├── Spark_Agent_Prompt.md                ← Bootstrap prompt for Spark (Research & Pedagogy)
    ├── Agent_Handoff.md                     ← Wright ↔ Spark coordination file
    ├── Math_Flash_Research_and_Pedagogy.md  ← Research, pedagogy, philosophy (the "why")
    ├── Math_Flash_ConsumerData.md           ← Consumer research, competitive audit
    ├── Math_Flash_Code_Rationale.md         ← Running log of code decisions
    ├── 2026-03-19_1530_Math_Flash_v55_milestone-baseline.html
    ├── 2026-03-25_1635_Math_Flash_v57_pool-cycling-easy-toggle.html
    ├── 2026-03-26_1200_Math_Flash_v59_gold-flash-bug8-bug2-house.html
    ├── 2026-03-25_1700_Math_Flash_v58_pool-notices-2attempt-pool-guard.html
    └── MF_research_sources/                 ← Raw source material (feeds ConsumerData)
        ├── Math_Flash_reddit_scrape.py
        ├── MF_reddit_rTeachers_math-facts-controversial.md
        ├── MF_reddit_rHomeschool_fun-math-facts-game.md
        ├── MF_reddit_rHomeschool_math-game-stipulations.md
        ├── MF_reddit_rTeaching_iready-xtramath-experience.md
        ├── MF_reddit_rHomeschooling_created-math-facts-site.md
        ├── MF_reddit_rHomeschool_memorizing-math-facts.md
        ├── MF_reddit_rMathTeachers_whats-good-about-reflex.md
        ├── MF_reddit_rGenZ_anyone-remember-reflex.md
        ├── MF_forum_ComplaintsBoard_xtramath.md
        ├── MF_forum_LDOnline_timed-math-dyslexia.md
        ├── MF_forum_SmartCustomer_xtramath-reviews.md
        └── MF_forum_changorg_stop-xtramath.md
```

---

## File Reference Chart

| File | Type | Description |
|---|---|---|
| `Sparkwright_File_Manifest.md` | Dev reference | This file. Structure, names, purposes. Update after any housekeeping. |
| `Sparkwright_MPF_March_22_2026_v55.md` | Master plan | Operational hub: to-do lists, session notes, file structure, terminal instructions, version history. The "what." |
| `Sparkwright_WORKSPACE_SETUP.md` | Dev environment | Terminal profiles, window setup, Safari tabs, key commands, local server notes. |
| `Wright_Agent_Prompt.md` | Agent bootstrap | Bootstrap prompt for Wright (Coding & PM agent, Claude Code window). Includes session start instructions and paste-in prompt. |
| `Spark_Agent_Prompt.md` | Agent bootstrap | Bootstrap prompt for Spark (Research & Pedagogy agent, Claude.ai chat window). Full reconstitution key — paste into any chat session to restore Spark's knowledge, voice, and research agenda. |
| `Agent_Handoff.md` | Agent coordination | Wright ↔ Spark async communication. Wright flags code-blockers needing research; Spark flags design decisions needing build input. |
| `Math_Flash_Research_and_Pedagogy.md` | Research | The "why" — pedagogy, philosophy, academic backing, developer story. Feeds About page, FAQ, marketing copy. Math Flash specific but broadly applicable. |
| `Math_Flash_ConsumerData.md` | Market research | Consumer research, competitive audit, Reddit/forum analysis summary. Draws on `MF_research_sources/`. |
| `Math_Flash_Code_Rationale.md` | Dev log | Running log of why code is structured the way it is. Read before making structural changes to the game. |
| `2026-03-19_1530_Math_Flash_v55_milestone-baseline.html` | HTML backup | Milestone baseline — version at time of MPF creation. Keep. |
| `2026-03-25_1635_Math_Flash_v57_pool-cycling-easy-toggle.html` | HTML backup | Most recent prior version before current. Keep. |
| `2026-03-26_1200_Math_Flash_v59_gold-flash-bug8-bug2-house.html` | HTML backup | **Current version.** Keep. This is what `games/mathflash/index.html` reflects. |
| `2026-03-25_1700_Math_Flash_v58_pool-notices-2attempt-pool-guard.html` | HTML backup | Prior version. Keep as recent fallback. |
| `MF_research_sources/Math_Flash_reddit_scrape.py` | Script | Python script used to scrape Reddit threads for consumer research. |
| `MF_research_sources/MF_reddit_*.md` (8 files) | Source data | Raw Reddit thread exports. Reference material for ConsumerData. |
| `MF_research_sources/MF_forum_*.md` (4 files) | Source data | Raw forum thread exports (XtraMath complaints, LD Online, Change.org). Reference material for ConsumerData. |

---

## HTML Version Archive Policy

Keep the **current version**, the **most recent prior version**, and **one milestone backup**. Delete intermediate versions. When a new version is saved to `dev/`, delete the oldest non-milestone backup.

**Naming convention:** `YYYY-MM-DD_HHMM_[Project]_v[N]_[short-description].html`

---

## Notes on File Scope

- **MPF** is Sparkwright-level (houses the overall brand and build momentum). Once Math Flash is considered complete, it may migrate to its own space. For now, the MPF covers all active work.
- **RP file** (Research_and_Pedagogy) is Math Flash-specific but contains principles broadly applicable to future games. Leave it Math Flash-scoped for now.
- **ConsumerData** and research sources are Math Flash-specific.
- **Code_Rationale** is Math Flash-specific.
