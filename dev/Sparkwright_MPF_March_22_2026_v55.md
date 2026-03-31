# Math Flash — Master Project File (MPF)
*Last updated: March 31, 2026 — Session Z close (v66)*
*Current Math Flash version: v66 — live at `games/mathflash/index.html` (no backup file this session — all changes committed directly)*
*Current Sparkwright landing page: `index.html` (updated Session X — new logo, hero treatment, sparks)*
*Replace this file and the HTML at the start of each new session with the latest versions.*

---

## Dev File Structure

The `dev/` folder is managed by a dedicated reference file: **`Sparkwright_File_Manifest.md`**.

It contains the full folder hierarchy, a file-by-file reference chart, naming conventions, and the HTML archive policy. Read it before any housekeeping, renaming, or cleanup work. Always present proposed changes to the developer before executing — never rename or delete without explicit approval.

To pull it up: *"Show me the file manifest."*

---

## Who Is Building This

The developer is a teacher with a Master's in Educational Therapy and 15+ years working with students across public, private, and homeschool settings. Not a professional developer — learning tools gradually, building through collaboration with Claude. Has a 2019 MacBook Air (1.6GHz dual-core Intel i5, Intel UHD Graphics 617, 8GB RAM), a Claude Pro subscription, and a genuine vision for the product. Cares deeply about quality and integrity — it should feel purposeful and well-designed, not like a generic AI-generated app.

**Note on credential language:** Do not use "Educational Therapist" as a title — it implies active licensed practice. The correct framing is: *"a teacher with a Master's in Educational Therapy and 15+ years working with students across public, private, and homeschool settings."* See the RP file for full context.

**Primary testing browser: Safari** (switched from Chrome in v50 session — see Crash Log for why).

**Local development setup:** To test the Sparkwright site with working links, use a local server. See the Terminal Instructions section below.

**Claude Code:** Set up in session G. Claude Code works directly in the project folder — no upload/download cycle needed. See the Claude Code Workflow section below.

---

## The Game — What It Is

**Math Flash** is a math fact flashcard game for students focused on building fluency through smart, responsive, student-centered practice. A student is shown a math fact, types or reveals the answer, and the game adapts to what they know and don't know.

It is not a passive drill. The game is designed to:
- **Maximize unique exposure** — no wasted repetition of facts already known
- **Respond intelligently to misses** — wrong answers trigger a structured Practice Quest
- **Feel alive and responsive** — the game pays attention to the student
- **Eventually know the student** — track progress per fact, surface challenge facts, recognize mastery

Target audience: elementary and middle school students working on multiplication and division fluency. Also supports addition and subtraction.

---

## What Makes It Different

- **Practice Quest** — remediation sequence triggered immediately on wrong answer. Most flashcard apps just show the answer and move on. This turns a miss into a learning moment.
- **Fluency grading system** — Per-Question Timer mode grades each answer as Fluent (≤3s), Almost! (4–6s), or Needs Practice (wrong or no answer by 7s). Most apps use a binary pass/fail.
- **Tables beyond ×12** — planned. Almost no consumer math game goes past ×12. Deliberate differentiator.
- **Pet Fact system** — planned. Students choose a "pet fact" they're working to master.
- **Student-centered data** — planned. Simple stats page the student can read and understand.
- **Teacher/competitive mode** — planned toggle so a teacher can control pace manually for classroom use.
- **Smart round design** — pre-built unique fact pool, missed facts re-queued intelligently, done pile recycled only when pool is exhausted.

---

## The Ethos

- Practice should be **rich, not rote** — every question should feel purposeful
- **Mastery is the goal**, not completion
- **Student agency matters** — empowering, not punishing
- **Design quality matters** — dark mode, clean typography, smooth animations, no generic clipart
- **Pedagogically grounded** — TTRS, skip counting strategies, fact families, spaced repetition concepts, fluency automaticity research
- **Data belongs to the user** — see Data Philosophy section below

---

## Data Philosophy — Local vs. Server Storage

Sparkwright uses **localStorage** — data lives on the student's device, not a server. This is a deliberate philosophical choice, not a technical limitation. The student owns their data: no harvesting, no account friction, no server latency, no breach risk. The game works offline.

**Tradeoffs:** Data doesn't follow the student across devices yet (export/import will address this). Local storage cleared = data lost (mitigatable with backup/export feature).

*Full philosophy, competitive comparison (localStorage vs. TTRS/server model), business model implications, and marketing copy direction → `Math_Flash_Research_and_Pedagogy.md` § "Data Belongs to the User" (Section 2).*
*Technical schema and key structure → `Math_Flash_Code_Rationale.md` (localStorage Schema Reference section).*

---

## Science & Pedagogy

*Full research, citations, accommodations design, competitive landscape, and pedagogy rationale → `Math_Flash_Research_and_Pedagogy.md` (RP). This section contains only the working definitions that directly drive code behavior.*
*Implementation decisions behind these definitions → `Math_Flash_Code_Rationale.md` (Timing & Fluency, Per-Fact Tracking, Pedagogy-Driven Code Decisions sections).*

### Fluency Grading (Per-Question Timer mode only)
| Grade | Threshold | Meaning |
|-------|-----------|---------|
| ⚡ Fluent | Correct, ≤3s | Automatic retrieval — fact is memorized |
| 🔄 Almost! | Correct, 4–6s | Knows it, not yet automatic — still computing |
| 📚 Needs Practice | Wrong answer, or no answer by 7s | Not yet known — needs practice |

Fluency grading is **displayed** in Per-Question Timer mode only. Silently tracked in all modes for future use. The "Almost!" middle tier is the developer's own pedagogical addition — not in the research standard. The **7-second auto-kick** is practical, not research-derived.

### Mastery Definition
A fact is **Mastered** when:
> Correct in ≤3s on **4 out of the last 5 attempts**, spanning **at least 2 separate sessions**, with **low response time variance** (SD < `VARIANCE_STABLE_MS`).

- 2-session gate prevents "one good day" mastery
- Variance gate: high SD = still computing, not automatic — a key differentiator vs. XtraMath
- Mastery is de-certifiable — flag resets if performance degrades
- Exact `VARIANCE_STABLE_MS` threshold is TBD, tuned with real use

### Two-Attempt System (v39+)
Students get a silent second chance before Practice Quest triggers. First wrong answer: shake + clear, clock keeps running. Second wrong answer: Practice Quest triggers. Score bonus: `4 - attempts`.

### Timed Round + Practice Quest
Global countdown and stopwatch timers pause during Practice Quest — students are not punished for learning.

---

## 🌟 Positive Feedback & Learning Evidence Log

### 🧠 Pedagogy / Learning Evidence
- Student reported that high consequences for missed facts + immediate Practice Quest creates more urgency and requires more attention — validates the core remediation design. *(Session B)*

### ⚡ Engagement / Motivation
- *(none logged yet)*

### 🔬 Science Validation
- *(none logged yet)*

### 🎨 Design / UX
- Student wants to see fluency labels visible during the timer as it progresses so they know what threshold they're passing through. *(Session B)*
- Student reported 4 correct cards stacked in first column on Find All — fixed in v54. *(Session F)*

### 💬 Other / Raw
- *(none logged yet)*

---

## Near-Term Vision (next few months)

1. **Solidify core game mechanics** — Practice Quest pathways, mini-games, print output, Prove It logic, input polish
2. Perfect the multiplication and division pathways — most relevant to current students
3. Add extended tables (×13, ×14, ×15+)
4. Add localStorage progress tracking and the Challenge Facts workspace
5. Add the student-facing stats page
6. Add the Pet Fact system (after mechanics are solid)
7. Timed test / practice test area in app — separate from the main game

---

## Long-Term Vision

- Math Flash is the first product under the **Sparkwright** brand
- Sparkwright becomes a website hosting multiple learning games and tools built by the developer
- Future products live in the same aesthetic world (alchemy, cosmos, rainbow, maker energy)
- Site reflects developer's identity as educator and creator — blog, insights, other work
- Eventually includes payments/subscriptions for premium features; Google AdSense compatible with static hosting
- **Platform:** Custom site built on Netlify (full control, zero monthly fees, same host as game) — NOT Wix or Squarespace
- **Hosting:** `sparkwright.org` registered March 18, 2026 via Netlify
- **GitHub repo:** `https://github.com/SVScreate/Math-Flash.git` — not yet connected, Git setup deferred

### Future Games — Concept Backlog
*(Logged Session R — March 28, 2026. These are concepts, not commitments. Landing page coming-soon cards are currently filler; this backlog is where real candidates live.)*

**Word Flash** *(most developed concept — Session R)*
The natural next game after Math Flash. Same core mechanic (fluency timing, Practice Quest equivalent, mastery tracking) applied to spelling and/or sight word recognition. A teacher shows a word — student spells it or reads it — response time tracked. Fluency tiers apply. The homeschool and ed therapy market uses spelling/sight word drill constantly and has the same gap: tools that are either boring or fluffy, with no structured in-moment help.
- Same tech stack as Math Flash — mechanic is half-built
- Target: grades K–5 primarily, remediation through middle school
- Word lists: Dolch, Fry, or teacher-custom
- Could include a "word families" mode (phonics patterns) as a variant
- Most likely next build after Math Flash reaches v1 release

**Other concepts logged for future consideration:**
See Spark session R brainstorm. Full list of 10 ideas available for review. Strongest candidates after Word Flash: Clock Flash (telling time / elapsed time — genuine market gap), Fraction Flash (fractions/decimals, same audience as Math Flash), Decode (phonics decoding patterns, aligned with ed therapy work), Sight Word Sprint (high-frequency word fluency, younger students).

---

## ✨ Sparkwright — Business & Brand

### Brand Name
**Sparkwright** — chosen name for the developer's educational platform.

- "Wright" = maker by trade (wheelwright, playwright, shipwright) — Sparkwright = one who crafts sparks
- Implies learning, ignition, alchemy, and making without stating any of them explicitly
- Completely distinctive — no known ed-tech company uses this name
- One word, easy to say, easy to spell, memorable
- Carries the full brand identity: alchemy + quantum/energy + magic + maker culture

**Tagline:** *Handcrafted learning, built to spark.* *(working tagline, not fully locked)*

**The word "sparkwright" — coining and IP:**
Google surfaces a loose definition for "sparkwright" but it is not an established dictionary word. Developer wants to lean into what exists and "own" it as part of the brand — both in feel and potentially in a legal/IP sense. Questions to explore in a future chat session:
- What does Google currently define it as? (Developer to share)
- Can a coined/near-coined word be claimed as a trademark?
- What's the difference between common law trademark (using it in commerce) vs. registered trademark?
- How does this interact with the brand identity and About page copy?

**Landing page to-do:** Add a small hover bubble or tooltip over the word "Sparkwright" that shows a definition (the developer's own, informed by what exists). *(Item 107 — design discussion needed)*

### Brand Identity
**Keywords:** wonder, discovery, energized, challenged, like stepping into another world

**Aesthetic worlds:**
- Cottage witchy / forest magic
- Cosmic / stars and galaxies
- Alchemist's workshop
- Rainbow / colorful and bright

### Developer Bio
Master's in Educational Therapy, 15+ years across public, private, and homeschool classrooms. This background is core to Sparkwright's identity — not just a credential, but the foundation for every pedagogical decision in the games.

**GitHub repo description (written session H):**
*"Sparkwright is a growing collection of educational games and learning tools handcrafted by a teacher with a Master's in Educational Therapy and 15+ years across public, private, and homeschool classrooms. Home of Math Flash, a responsive math fact fluency game for students."*

**⚠️ To-do: About page copy**
Developer needs to share their resume in a Claude chat session to work on About page copy for the Sparkwright site. This is separate from the game work — do in a chat session, not Claude Code. *(flagged session H)*

### Competitive Landscape
*(documented Session D — see prior MPF versions for full notes)*
Key differentiators vs XtraMath, Reflex Math, Prodigy, Khan Academy: immediate remediation, fluency grading tiers, student-centered feedback, Sparkwright aesthetic identity.

**⚠️ Full competitive research pass needed (item 112) — see to-do list.**

---

## 🗂️ Site File Structure

```
sparkwright/
├── index.html              ← Sparkwright landing page
└── games/
    └── mathflash/
        └── index.html      ← Math Flash game (v55)
```

---

## 🖥️ Session Startup Checklist

Open **3 Terminal windows** at the start of each session:

**Window 1 — Local server**
```
cd /Users/kimberlywelle/Desktop/sparkwright
python3 -m http.server 8000
```
Leave this running. Don't type in it again.

**Window 2 — Claude Code**
```
cd /Users/kimberlywelle/Desktop/sparkwright
claude
```
This is where you work with Claude.

**Window 3 — Git (use at end of session to push changes)**
```
cd /Users/kimberlywelle/Desktop/sparkwright
git add .
git commit -m "Session X — description"
git push
```
Pushing to GitHub auto-deploys to Netlify. No manual upload needed.

**Safari tabs to open:**
- `http://localhost:8000` — landing page
- `http://localhost:8000/games/mathflash/` — live game
- `https://github.com/SVScreate/sparkwright` — to verify push landed
- `https://app.netlify.com` — to verify deploy succeeded

**Do not deploy to Netlify manually** — GitHub push handles it. 300 credits/month, spend wisely.

---

## 🤖 Claude Code Workflow

Claude Code is a terminal tool that lets Claude edit files directly in your project folder. No upload/download cycle. Set up in session G.

### Starting a Claude Code session
1. Open Terminal
2. `cd` into your `sparkwright` folder (or drag it in)
3. Run: `claude`
4. Paste in the MPF at the start of the session so Claude has full context
5. Tell Claude what to work on — it edits files directly

### Key differences from chat sessions
- Claude sees and edits files in place — no need to upload the HTML or download a new version
- Still test in Safari with the local server (`python3 -m http.server 8000`)
- MPF is still the source of truth — update it at the end of each session
- File naming convention still applies for any exported/backup copies

### What Claude Code is good for
- Multi-file edits in one go (game + landing page together)
- Searching the codebase (`grep`, file reads) without you having to paste code
- Iterating quickly without the upload/download friction
- Running terminal commands (local server, file operations)

### What it doesn't change
- You still test in Safari — Claude Code can't see the rendered game
- Design decisions still happen collaboratively
- MPF is still updated at session end

### Testing protocol
When Claude provides a list of things to test, each item will be numbered or lettered (T1, T2, A, B, etc.) so you can refer back to specific items by label when reporting results.

---

## 👤 Profile & localStorage Architecture

*Full schemas, keys, fact record structure, recording hooks, and test checklist → `Math_Flash_Code_Rationale.md` (localStorage Schema Reference section).*
*Decisions behind the architecture (why nested, why this key format, etc.) → `Math_Flash_Code_Rationale.md` (localStorage Design section).*

**Quick reference — key names:**
- `sparkwright_profiles` — site-level profile array
- `sparkwright_active` — active username string
- `mathflash_settings` — last-used setup screen values
- `mathflash_facts` — per-fact tracking, nested `{ username: { factKey: record } }`
- `mathflash_practice_time` — cumulative practice time *(planned, item 90)*

---

## 🐛 CRASH LOG & KNOWN BUG PATTERNS

### Chrome Reflow Crash (RESOLVED — v36–v42)
Any DOM mutation (appendChild loops, innerHTML assignment, toggling visibility) on a *live, visible* element can crash Chrome. Fix: detach → mutate → reattach. Applies to `buildTableGrid()`, `showTableHelper`, pause overlay. **Now testing in Safari — this is less of a concern but the pattern is still worth following.**

### Multiplication Fact Pool Deduplication (RESOLVED — v38)
Facts like 5×12 and 12×5 were stored as duplicate pool entries with swapped `hint.table` values. Fixed: deduplicate at pool-build time using sorted-pair key. Always use `hint.table` for Find It display.

### Round Ending Early (RESOLVED — v53d)
Pre-fill loop used `for` with fixed count — if `drawFact()` returned null (pool exhausted mid-fill), slots were skipped and `G.qs` ended up shorter than `S.qCount`. Fixed: `while` loop that keeps drawing until `G.qs.length === n`, recycling done pile as needed.

### Same Facts on Restart (RESOLVED — v53d)
Related to above — small pools exhausted and recycled in the same order. Fixed by the while-loop pre-fill which forces proper recycling and reshuffling.

### Find All Card Clustering (RESOLVED — v54)
Correct cards could stack 4-in-a-row in one column. Distribution check was using correct column count (3) but too-loose threshold (allowed up to 3 correct per column). Fixed: max 2 correct per column, plus no two adjacent correct cards in the same row. 30-attempt limit before accepting best available.

### Script Error on Page Load — Safari (INVESTIGATED — session F)
"Uncaught Error: Script error" appeared in Safari sidebar view. Caused by missing `function buildTableGrid(op) {` declaration — accidentally consumed by a str_replace that inserted the settings persistence functions. Restored in v53c. Root cause: str_replace used the function declaration line as the unique anchor point, and it got eaten. **Lesson: always diff the output file against the input when a new function block is inserted near another function declaration.**

---

## TO-DO LIST

### 🐛 BUGS
1. ✅ Select All toggle crash — Chrome only, resolved (v42)
2. Addition-only start bug — Start does nothing when only addition is selected *(deferred)*
3. ✅ Re-queue system / round ending early — resolved (v53d)
4. **Prove It input bug (intermittent)** — one student couldn't type in Prove It on first load; refresh fixed it. Monitor.
5. **Chrome crash via Netlify on Mac** — fine on Chromebooks. Test: Mac Chrome locally, Windows desktop. *(Hold)*
6. ✅ **Prove It "Back to Round" button not appearing** — button text changed but browser immediately re-fired click when focus shifted from disabled input to button (Enter-key-focus-shift in Safari). Fixed in v56: button is disabled for 600ms after correct answer. *(Session L)*
7. ✅ **Round Ended Early with small fact pool** — smart cycling fix implemented in v56 Session M. Pool padded with shuffled cycles before pre-fill in both `startGame()` and `restartRound()`. Pool size notice added to setup screen below question count fields. *(Session M)*
8. **Intermittent typing glitch on main answer input** — reported by developer and beta testers. Typing becomes intermittent or stops working mid-round, especially as per-question timer gets low. Occurred on question 13/20, answer was 66. May be related to focus shifting during `perQTimer` tick or DOM interaction. Different from Bug 4 (Prove It input). Monitor and investigate. *(Session M)*
9. **Pool notice not clearing after validation error** — if user submits with empty question count (triggering error message), then types a number, the error warning stays and the pool notice does not replace it. The two message states conflict in the same `num-input-msg` div. *(Session M — fix needed)*

### 🔧 UI / COPY
6–31. *(all completed — see COMPLETED log)*
32. Auto-advance / "Student Speed Mode" toggle *(discussed, not yet designed)*
143. **Print button on My Progress / Stats page** — add a print pill button to the stats screen. Holding until heat map / My Progress redesign is settled — print a finalized layout, not a draft. *(Session X — on hold pending item 140 design)*
144. **Logo update — all pages** — new nav logo (5-pointed star SVG, Comfortaa 700 wordmark, Spark glow) was applied to `index.html` (landing page) in Session X. Needs to be applied to `games/mathflash/index.html` and any other pages. *(Session X)*
145. ✅ **Advanced Settings — body text spacing** — 14px top padding added to content area. *(Session X/Y)*

148. **Session results history** — students (and teachers) should be able to access past round results without relying on the end-of-round print. Currently, if the results screen is closed or the page reloads, the round data is gone. Fix: store a rolling log of round summaries in localStorage (student name, date/time, mode, tables, score, fluency breakdown). Accessible from My Progress or a dedicated "History" tab. Each entry printable individually. Connected to item 109 (teacher print report) and item 143 (My Progress print). Design discussion needed: how many sessions to retain? What's in each entry? Route to Spark for design input. *(Session Z)*

149. **Teacher settings lock / teacher area** — currently any student can change all settings. Teacher use case needs a way to lock settings so students can't alter the configuration mid-session. Connected to item 142 (product model: tool vs. platform), which is the broader design discussion needed first. Key question from item 142: does Math Flash have user roles (student vs. teacher/parent), and is that established at account setup? The settings lock is a downstream feature of that decision — can't build it until the role model is settled. Do not build until item 142 design discussion is resolved with Spark. *(Session Z)*

146. **Download / Save as PDF button** — developer wants a download button on the results screen and wherever there's a print button. For a static site, the only practical path is `window.print()` relabeled "Print / Save as PDF" (browser provides "Save as PDF" destination in print dialog). Adding a PDF library (jsPDF, etc.) not recommended — significant weight for marginal UX gain. Implementation: relabel existing print buttons + add a tooltip or helper text "→ Choose 'Save as PDF' in the dialog." Design discussion needed before coding. *(Session Z)*

147. **Initial assessment / baseline check** — developer wants a way to establish a student's starting point before regular practice begins. Connected to the assessment area (item 66), My Progress page (item 89), and heat map (item 140). Big feature — design discussion with Spark needed before scoping. Key questions: (1) Is this a formal timed test, or a lighter diagnostic pass? (2) Does it seed the `mathflash_facts` localStorage data to pre-populate the stats page? (3) Is it the same mechanic as the assessment area (item 66) or different? Route to Spark. *(Session Z)*
33. ✅ **Print output** — redesigned Session W (v62). Settings block, summary, fluency counts, fact chips, fluency key, notes lines. Developer using in practice; feedback pass pending.
34. ✅ "Format" → "Mode" — renamed (v52)
35. ✅ "— no time pressure." copy — removed (v52)
36. ✅ Typing field character limit — 4 characters max (v52)
37–49. *(all completed — see COMPLETED log)*
50. Results screen — revisit design and information hierarchy
51. Animations — title screen bokeh + setup flair *(deferred — after core mechanics)*
52. **Device screen fit / viewport clipping** — Chromebooks cut off cards. *(Design discussion)*
53. **Timer option for Practice Quest** *(see item 84)*
120. **"Answer Mode" copy misalignment** — label reads "3 tries before reveal" but the actual mechanic is 2 wrong attempts before Practice Quest triggers. Needs language audit for accuracy and consistency with other settings copy. *(Session M)*
121. **Small pool prevention** — if pool size is 1 (or very small, e.g. < 3 unique facts), the round is useless but currently allowed to start. Should block start with a plain-language message: "Only X unique fact(s) selected. Select more tables or turn on Full Table Range." Design discussion: what is the minimum useful pool size? *(Session M)*
122. **Stopwatch mode design** — is "Set number of items" under Stopwatch redundant with "Set # of Questions" mode? One is "how long does it take to do N questions" (Stopwatch), one is "do N questions at your own pace" (Set #). May be genuinely distinct but user-facing language is confusing. Design discussion needed. *(Session M)*
123. **Reverse fact in requeue mechanic** — design question: if a student misses 6×12, should 12×6 also be added to the requeue at least once? Pedagogically, fact families suggest yes — seeing both orientations reinforces the relationship. Design discussion needed before coding. *(Session M)*
124. ✅ **Print output — include round settings** — shipped in v62. Feedback pass pending after real use. *(Session M/W)*
125. ✅ **Find All — correct card visual feedback** — cards flash gold and settle to gold on correct selection (`.fa-card.fa-flash` + updated `.fa-card.fa-good`). Built Session P, v59.
126. **Find All — wrong answer graphic** — after 3 wrong selections, show a graphic or visual illustrating the fact group (e.g. the fact family or multiplication array). *(Session M)*
127. ✅ **Fact Family Chase — house overlap** — house SVG extended (y=468→520, height=490→550). Gives ~54px clearance below last chip. Built Session P, v59.
128. **Settings globalization** — meta discussion: when a fix or feature is built for one mode/operation, ensure it applies consistently across all relevant modes and operations. Avoid whack-a-mole per-branch fixes. Discuss approach before next major feature pass. *(Session M)*
129. **Easy toggle for ×** — default changed from OFF to ON in Session M. Label rewritten to plain language: "Practice every fact in your chosen table(s) — ON: all facts included. OFF: exclude facts where one of the numbers comes from a table you haven't picked (e.g. ×6, ×7, ×8 selected → no 6×2, 7×5, 8×9)." *(Session M — completed, log only)*

100. **Math Flash title screen overhaul** — change tagline (sounds AI-generated), rethink layout, replace four example facts with four operation symbols, add button placeholder for future areas, review "How to Play" content. Button hierarchy: "Let's Go" (primary), "How to Play" + "My Progress" (btn-ghost pills, same row), "About" (text link below). My Progress promoted to pill style in Session X — full hierarchy discussion still open. *(Session F/X — design discussion needed)*
141. **Fluency bar purple zone design decision** — Bar has 3 states: gold (fluent zone), orange (almost zone), purple (last 1s before autokick). Purple doesn't map to a grade — it's a fuse warning. 3 colors, only 2 grade outcomes. Options: keep as-is, remove purple (drain orange to 0), or change to red for urgency. Route to Spark for input. *(Session X)*
101. **Teacher fact-picker** — per-operation panel dropdown/selector allowing teacher to hand-pick specific facts a student will practice. *(Session F — design discussion needed)*

### 🏗️ CORE MECHANICS — PRIORITY
54. **Practice Quest restructure: 3 screens** — Find It → random mini-game → Prove It *(deferred)*
55. **Mini-game randomization** — randomly select for middle slot *(after 2–3 games exist)*
56. **Fact Scramble** — mini-game *(build first)*
57. **Skip Counting Chase** — mini-game *(build second)*
58. **Type It** — mini-game *(build third)*
59. **Find All reverse operations** — e.g. `20 = 4 × 5` as valid card format
60. **Exclude individual facts** — setup panel
61. **Math tools area** — multiplication chart and other reference tools
62. **Fact Family mini-game** — standalone
63. Extended tables — ×13, ×14, ×15+
64. Practice Quest trigger options — immediately / after N seconds
65. Prove It wrong-answer — explore alternatives to Fact Family Chase
66. **Assessment area** — dedicated section to formally test skills and facts (not practice). Design discussion needed. Developer wants a way to assess what a student actually knows vs practices. *(Session G)*
67. **Second-attempt fluency grading** — factor attempt count into grade
68. **Fluency labels visible during per-question timer** — student-requested *(Session B)*
69. ✅ Prove It — 2 attempts before Fact Family Chase, correct → "Back to Round! 🎉" (v52)
70. **Prove It auto-return** — currently manual click. Keep as-is pending discussion.
71. **Google Dinosaur / early Mario style mini-games** — retro arcade-style. Design TBD.
72. **Practice Quest too long?** — students fatiguing. Design discussion needed.
73. **Mini-game absorption + Prove It gate** — students clicking through without learning. *(Session B)*

### 🐾 PET FACT SYSTEM *(deferred — after core mechanics are solid)*
74. Pet egg appears on progress bar as a marker riding along with the fill
75. Pet egg appears in results screen with mastery status indicator
76. Pet Fact Sanctuary — persistent screen showing all hatched/mastered facts
77. Egg crack trigger — star/sparkle when mastery threshold reached
78. Egg idle animation — subtle squish/bounce, CSS scaleX/scaleY keyframes, ~3s loop
79. Egg art integration — local server + `src="egg.png"`
80. Egg in Tamagotchi area — dedicated pet screen with fact woven into design
81. Tamagotchi area access gate — 10 minutes of practice to unlock
82. Mastery threshold decision — TBD
83. Cats and puppies — first pets after egg hatches

### ⏱️ PRACTICE QUEST TIMER
84. **Practice Quest internal timer** — separate from round timer. Settings toggle needed. *(Session B)*

### 📊 DATA / TRACKING *(after core mechanics)*
85. ✅ Settings memory via localStorage (v53)
86. ✅ **Per-fact tracking** — built in v55, tested and confirmed working (session H). Two bugs found and fixed: (1) response time stored raw timestamp instead of elapsed ms, (2) `qStartTime` not set in non-timer modes. Both resolved. Foundation for stats page, challenge facts, pet fact mastery.
87. ✅ **Response time variance** — `calcResponseSD(times)` returns population SD in ms; `isStableVariance(rec)` returns boolean. Constants: `VARIANCE_MIN_TIMES = 5`, `VARIANCE_STABLE_MS = 1000` (tune with real use). Built v56, session L.
88. **Challenge Facts workspace** — facts that have high attempt counts, high variance, or are close to Mastered threshold surface here for targeted practice. Design discussion needed.
89. **Student-facing stats page** — simplified, encouraging, no raw numbers. Fact tiles with tier colors, plain-language labels. Design discussion needed.
90. **Practice time tracking** (`mathflash_practice_time`) — cumulative practice time per user
108. ✅ **Mastery flag** — `mastered: boolean`, `masteredDate: string|null` added to fact record. Also added `recentAttempts: []` rolling window (last 10 attempts, each `{ms, correct, date}`) to enable correct 4/5 and 2-session checks. `checkMastery(rec)` runs after every attempt; de-certification included. Built v56, session L.
109. **Teacher print report** — separate from round-end print. Shows per-fact data across time windows (round / day / week / month / year / all-time). Columns: avg response time, consistency label, attempt count, quest triggered count, last practiced. Design discussion needed. See also item 140.

140. **Fact fluency heat map — standalone printable view** — Full 12×12 grid (or subset by operation) showing every fact colored by fluency tier (gold = Mastered, orange = Building, purple = Not Yet, dim = not yet practiced). Accessible on-demand from the stats page or teacher report — NOT printed automatically with every round. Teacher or parent can generate and print when they want a snapshot of overall progress. Useful for student files, IEP documentation, parent conferences. Design discussion needed: (1) Where is it accessed from — stats page button, teacher report section, or both? (2) Should it be filterable by operation (×, ÷, +, −)? (3) Should it include a date stamp and student name for filing purposes? *(Session V — added at developer request)*
110. **Student stats page — consistency labels** — human-readable labels derived from variance for fact tiles. Current candidates: Automatic / Developing / Not Yet. Word choice TBD. Design discussion needed.
111. **FAQ / methodology page** — explains what fluency means, how Mastered is determined, why facts get flagged as challenge facts, what the tiers mean. Written for teachers and parents. Protects IP by explaining the *what* without exposing exact thresholds. Build after stats/print report are designed.
112. **Competitive research pass** — extensive comparison of IXL, iReady, XtraMath, TTRS, Reflex Math, Rocket Math, Khan Academy, Prodigy, and others. Document: mastery model, remediation approach, timer/accommodation options, pricing, data model, UX feel, differentiators vs. Math Flash. Feeds FAQ, About page, and product positioning.
114. **Student & teacher agency — core design principle** — Math Flash is explicitly designed so that the student and their teacher/helper feel in control of how practice feels. Settings, timer options, and accommodations exist to serve the learner — not to enforce a one-size-fits-all drill. Most competing programs (XtraMath, TTRS, IXL, iReady, etc.) have a sterile, punishing vibe: the program drills the student, marks them wrong, and moves on. Math Flash's differentiator is that it meets students where they are, respects their pace, and gives both student and teacher meaningful guidance on how to use it well. This philosophy should be explicit in the FAQ, onboarding, and About page copy.

113. **Accommodations — processing speed** — ✅ *Research complete (Session N).* Full findings in RP Science & Pedagogy section. Key findings: ADHD ~0.76 SD slower; ASD g=0.35 effect; dyslexia impairs fact retrieval via phonological processing; dyscalculia core deficit is fact automaticity. XtraMath offers 3s/6s/10s/12s — 12s explicitly for students with disabilities. Principled accommodation increments: 4.5s (1.5×) and 6s (2×). Design and implementation: see item 130.

130. **Teacher-adjustable fluency threshold — design + implementation** — Informed by item 113 research. Design discussion needed before coding. Key questions: (1) What values to offer? Recommended: 3s (default), 5s, 6s — or a slider with teacher-set value. (2) How labeled? Not "easier mode" — framed as "accommodation for processing speed differences." (3) How does the threshold affect Fluent/Almost/Needs Practice grading labels? Labels should reflect the threshold used (e.g., "Fluent at 5s"). (4) How documented in print reports? Format: "Fluency assessed at 5s threshold (accommodation); N = [X] trials." (5) Does the auto-kick timer (7s default) scale with the fluency threshold? Probably yes. Design discussion needed. See RP Accommodations section for full research basis. Connected to items 109 (print report), 111 (FAQ), 113 (research). *(Session N — design discussion needed before coding)*

131. **Retrieval vs. reconstruction at 4–6 seconds — open research question** — No study currently validates whether a student answering correctly at 4–6s is auto-retrieving vs. reconstructing. This is a real empirical gap. It affects: (1) how Math Flash documents its accommodation thresholds in FAQ/marketing, (2) whether the mastery criteria should differ for students using an accommodation threshold, (3) the honest limits of what we can claim about a student who "passes" at 5s. Research question worth tracking: is there a way to distinguish retrieval from reconstruction in-game? Possible signal: response time distribution shape and trial-to-trial consistency. A student consistently fast (low variance) at 5s may be retrieving; a student variable at 5s may be reconstructing. The existing variance tracking (item 87) may already be the right tool. Design discussion needed before making any claims in FAQ. *(Session N — research and design discussion needed)*

132. **XtraMath timer model — design discussion + positioning** — Consumer research (Session N) surfaced a student review (Penny M., 5th grade, ADHD): *"you only get 3 SECONDS TO ANSWER! Then its 2.6 then its 1.5! That's too stressful and I have ADHD."* Session S research investigated this claim and found it **unverifiable for current XtraMath**. Current XtraMath uses five static, teacher-set thresholds (12s, 6s default, 3s, 2s, 1.5s) — the timer does not auto-shrink within a session. The 2.6s figure matches no current standard option. Penny M.'s account likely reflects an older version of XtraMath, a teacher who manually tightened the setting over time, or perceived time from visual pressure. **Do not cite the 3s→2.6s→1.5s progression in any marketing copy.** The broader anxiety finding stands — multiple sources confirm XtraMath is experienced as punishing regardless of the specific mechanic. Math Flash uses a fixed threshold per session, which is already meaningfully different from XtraMath's model. Design discussion still needed: (1) Is fixed always right, or is there a thoughtful progressive threshold that could serve advanced students without panic? (2) This is a differentiator worth naming explicitly in FAQ. Connected to item 130 (accommodation threshold) and item 139 (tiered threshold design). *(Session N/S — verify firsthand still recommended before any specific claims)*

139. **Tiered fluency threshold design — principled alternative to XtraMath's model** — XtraMath offers 5 teacher-set thresholds: 1.5s, 2s, 3s (all premium), 6s (default), 12s (disability accommodation). The instinct is right but the framing is arbitrary — nothing tells a teacher *why* they would choose 2s vs. 3s. Math Flash has the opportunity to offer the same range with principled labels grounded in science and ethos. **Proposed tiered model for design discussion:**
- **1.5–2s — Challenge** (students who have demonstrated 3s automaticity and want to push further; advanced/gifted)
- **3s — Standard** (research-based automaticity threshold; Kling & Bay-Williams 2015; the default)
- **5s — Extended** (~1.5× accommodation; standard IEP/504 convention for processing speed differences)
- **6s — Extended+** (2× accommodation; standard IEP/504 convention; notably XtraMath's default — their "default" is our accommodation)
- **Beyond 6s** — outside Math Flash's current scope; XtraMath's 12s is for early learners and severe processing deficits

**The ethos difference:** XtraMath labels by number only. Math Flash labels by purpose — "Standard / Extended / Challenge" — so teachers understand what they're choosing and why. The choice is framed as meeting this student where they are, not making it easier. **Design questions for discussion:** (1) Named tiers only, or custom entry too? (2) Does Challenge mode need a separate mastery definition? (3) How do the labels appear in print reports? *"Fluency assessed at Extended threshold (5s); accommodation for documented processing speed difference."* (4) Should the threshold setting be visible to students or only to teachers/parents? Connected to items 130, 131, 132. *(Session S — design discussion needed before coding)*

114. **Student & teacher agency — core design principle** — Math Flash is explicitly designed so that the student and their teacher/helper feel in control of how practice feels. Settings, timer options, and accommodations exist to serve the learner — not to enforce a one-size-fits-all drill. Most competing programs have a sterile, punishing vibe: the program drills the student, marks them wrong, and moves on. Math Flash's differentiator is that it meets students where they are, respects their pace, and gives both student and teacher meaningful guidance on how to use it well. This philosophy should be explicit in the FAQ, onboarding, and About page copy.
115. **Practice Quest engagement mechanic** — Design discussion needed. Timer pauses during Practice Quest (pedagogically correct). Risk: students may use wrong answers as an intentional escape ("escape-motivated errors") or mentally check out when the overlay appears. Need a mechanic that requires genuine presence without punitive pressure. Possible directions: response-required steps that can't be passively clicked through; subtle non-scoring ambient indicator; Prove It gate already partially addresses this. Do not touch code until design is settled.
116. **Literature review pass** — Dedicated research session to gather and document primary sources on: errorless learning vs. error correction, math anxiety and timed assessments, neurodivergence and cognitive load, fluency automaticity thresholds, in-the-moment vs. delayed feedback. Builds into RP Science & Pedagogy section. Backbone of FAQ and differentiates Sparkwright's claims from generic "science-backed" marketing language.
118. **Pool-too-small guard** — if the fact pool is smaller than `qCount`, the game currently ends early with "Round Ended Early" instead of recycling facts. Fix: detect pool exhaustion at game start and recycle/repeat facts to reach `qCount`. Possible UX addition: auto-enable Easy (or reverse facts) when pool would otherwise be too small, with a gentle note to the user. Wording in the settings area around Easy/tables also needs plain-language improvement. *(Session L — discovered during v56 testing)*
118. **Competitive landscape chart** — Structured cross-comparison of all current math fluency programs: XtraMath, Reflex, Rocket Math, TTRS, IXL, iReady, Zearn, Khan Academy, 99Math, Boddle, Monster Math, MathFactLab, spellingtraining.com, and small flashcard apps. Chart axes: wrong-answer response, remediation type, timer model, neurodivergent accommodation, age range, price model, data model, tables covered, school vs. family market. Do in a dedicated chat session. Do after journaling about target user — the questions will be sharper.
106. **localStorage schema migration** — as the game evolves, localStorage schemas will change (new fields added, old ones renamed). Design discussion needed: how do we avoid wiping or breaking a student's saved progress when updates ship? Needs a versioning/migration strategy before real student data accumulates. *(Session H)*

132. **Re-queue: round length inflation** — With Re-queue ON, a round set to 20 questions silently grows. Miss 5 facts and the round could reach 25–28 questions. No indicator tells the student the round extended. Could feel surprising or endless. Design question: should there be a subtle counter ("3 bonus questions from misses") or just accept the behavior as-is since it's pedagogically sound? *(Session N)*
133. **Re-queue: near-end budget dropoff** — `requeueBudget()` returns 0 when ≤3 questions remain. A fact missed on question 17/20 is silently dropped and never returns. Student doesn't know this happened. May be fine, but should be intentional — worth noting in FAQ or teacher documentation. *(Session N)*
134. **Re-queue: small pool compounding** — Small pool already repeats facts via cycling. Re-queue ON on top of that means the same few facts appear via both cycling AND requeue — very high repetition. The pool notice helps the teacher see a small pool, but the compound effect should be considered in the UX messaging. *(Session N)*
135. **Re-queue: confirm toggle is session-only** — Re-queue can only be toggled at setup, not mid-round. This is intentional and correct. Confirm this is documented in FAQ/teacher guidance so teachers understand the setting applies to the whole session. *(Session N)*
136. **Re-queue: results screen doesn't distinguish requeued questions** — End-of-round summary doesn't show "you answered 23 questions (3 were repeats from misses)." Could be a useful teacher-facing detail in print output (item 109) or results screen (item 50). Low priority — log for when those screens are designed. *(Session N)*

130. **Teacher pre-set shareable links** — A teacher should be able to configure game settings and share a link (or QR code) that opens Math Flash with those settings pre-loaded. Removes the complexity of setup for younger students who may find the options overwhelming. Likely implementation: encode settings as URL query parameters (e.g. `?op=x&tables=3,4,5&easy=1&qCount=20`); on load, parse params and apply them before `loadAndApplySettings()`. Design questions: should the URL fully lock settings (student can't change), or just pre-fill (student can still adjust)? Should there be a "teacher mode" that hides the setup screen entirely? *(Session N — design discussion needed)*

### 👤 USERNAMES & PROFILE
95. ✅ Profile system — generated usernames + emoji avatar, multi-profile support, switcher modal, site-level localStorage (session F, landing page)
96. ✅ Generated names — adjective+noun combos, no profanity possible (session F)
97. ✅ Math Flash header bar showing active profile (session F)
105. **Guest play UX** — currently guests can play freely but tracking is silently skipped and there is no logout button (only "Switch Profile"). Design discussion needed: should the game prompt "Create a profile to save your progress" before starting, or allow frictionless guest play? Also consider: should a logout/guest option be added to the profile switcher? *(Session H)*

142. **Product model: tool vs. platform — design discussion needed (soon)** — Core tension: Math Flash works right now as a free tool anyone can use however they want. But the teacher use case wants something different: teacher configures settings, student plays, teacher reviews progress and controls what the student can see/access. Those are two different product models. Several existing features are already pulling toward the platform model (shareable links #130, assessment area #66, stats page, Advanced Settings, fluency threshold). Before building more infrastructure, a design discussion is needed to decide: (1) Does Math Flash have a concept of user *roles* (student vs. teacher/parent)? (2) Are some settings teacher-only — hidden from the student by default? (3) Does account setup ask "how are you using this?" to configure the experience (family at home, classroom, tutor/therapist, independent student)? (4) How does the assessment area (#66) fit — is it always available, or teacher-gated? This decision will shape the profile system, the setup screen, Advanced Settings visibility, stats access, and the assessment area. Do not build new settings infrastructure until this is resolved. Connected to: #66 (assessment), #101 (teacher fact-picker), #105 (guest play), #109 (teacher print report), #130 (shareable links). *(Session X — design discussion with Spark, soon)*

### 🌐 HOSTING / DEPLOYMENT
91. ✅ Domain registered — `sparkwright.org` via Netlify, March 18, 2026
92. ✅ Sparkwright landing page built — Session E
93. ✅ **v55 live on Netlify** — promoted to `games/mathflash/index.html` via GitHub auto-deploy (Session H)
94. **Cross-device testing** — Mac Chrome locally, Windows desktop Chrome/Edge, iPad.
98. **Rename Netlify project** to sparkwright *(cosmetic)*
99. ✅ **GitHub + Netlify auto-deploy** — repo `SVScreate/sparkwright` created, connected to Netlify, auto-deploy confirmed working. Push to GitHub → live on sparkwright.org automatically (Session H)
102. **Landing page polish** — tagline not fully locked, coming-soon card names are placeholders
107. **"Sparkwright" definition tooltip** — small hover bubble over the word "Sparkwright" on the landing page showing a definition. Developer to share Google's version; then craft the official brand definition. Design discussion needed. *(Session H)*
103. Long term: payments/subscriptions, Google AdSense integration
104. **File naming convention:** always use `YYYY-MM-DD_HHMM_vN.html` format for both HTML and MPF files

### ⚖️ LEGAL / IP
118. **IP ownership — consult an attorney before commercial launch.** US copyright law requires human authorship; AI-assisted work is a gray area still being settled. The ownership argument is reasonably strong here (developer makes all creative/product/pedagogical decisions; Claude executes them), but this should be reviewed by an IP attorney before selling or licensing the product. Not urgent now — needed before commercial launch. *(Session K)*
119. **Trademark — "Sparkwright" brand name.** Can a coined/near-coined word be claimed as trademark? What's the difference between common law trademark (use in commerce) vs. registered trademark? What does Google currently define "sparkwright" as? Explore in a dedicated chat session once the product is closer to launch. *(Session D / Session H)*
137. **Legal copy — Terms of Use and Privacy Policy.** Needed before any commercial activity or public launch. Even with localStorage (no server-side data), a Privacy Policy is standard and sets user expectations. Terms of Use establishes rules for using the site. Both can be drafted by Spark in a chat session using the project's data model and philosophy as inputs; however, the developer should have a real attorney review before publishing. DMCA policy also worth adding once user-submitted content is a possibility. *(Session R — flagged for Spark session)*
138. **Legal discussion — should a Legal agent be added to the Sparkwright system?** Currently handled in Spark sessions. Discussed briefly Session R — see Agent_Handoff for Spark's recommendation. *(Session R)*

---

## WHERE TO PICK UP

*Session Z close — March 31, 2026 — v66 committed.*

**Session Z full build log:**
- ✅ T3 confirmed — landing page logo color split + glow looks good
- ✅ T4 confirmed — Settings screen Per-Question Timer description, tier pills, section description render correctly
- ✅ T4 fix — Per-Question Timer description updated: added "(default: 3 seconds)" to end
- ✅ T4 fix — Fluency Threshold section description: removed "Adjust to match what's realistic and meaningful"
- ✅ T5 confirmed — print output shows "5 Seconds" label correctly
- ✅ T7 confirmed — fact tiles appear on My Progress after a round
- ✅ Items 33 + 124 — print output marked done (looking good; feedback pass after real use)
- ✅ Contact page nav — updated to match about.html/index.html (full logo SVG, split Spark/wright wordmark, active link state CSS)
- ✅ Easy toggle lock — when all tables selected, Easy toggle is forced ON and locked (`.switch-locked` CSS); unlocks when any table is deselected
- ✅ Find All column bug — 3rd column was missing a card for small facts (e.g. 1×1, which only has ~11 unique wrong answers). Fixed: wrong answers are now padded by cycling the pool to always reach 12

**Testing needed this session:**
- T1 — contact page nav: confirm logo + split wordmark renders correctly in Safari
- T2 — Easy toggle: select all 12 tables, confirm Easy toggle locks (greys out, can't turn off). Deselect a table, confirm it unlocks.
- T3 — Find All: trigger Practice Quest on a 1×1 or 2×1 fact, confirm all 3 columns have 6 cards
- T4 — Settings: Per-Question Timer description shows "(default: 3 seconds)" | Fluency Threshold desc no longer has "Adjust what's realistic and meaningful"

**Build queue for next session (priority order):**
1. **My Progress tier improvements** — add response-time–aware tier ("Fluent" sub-tier) + relabel "Not Yet" → "New" (design confirmed Session Y) — hold until heat map design settled
2. **Find All orientation scramble (item 59)** — all 4 formats: `5×8=`, `8×5=`, `?=5×8`, `?=8×5` — greenlight pending
3. **Practice Quest matching celebration** — brief animation on matched pair; pair persists until gold flash — greenlight pending
4. **Item 143** — print pill on My Progress page — holding until My Progress redesign/heat map is settled
5. **Session Mode (item 142)** — big feature, own session when ready
6. **Item 100** — title screen overhaul (design discussion first)

**Design discussions open:**
- My Progress / heat map redesign — item 140, not yet designed; blocks items 143 and tier improvements
- Initial assessment / baseline check — flagged for Spark (see Handoff)
- Find All scramble + Practice Quest celebration — greenlight still pending from developer
- Download/Save as PDF — new item 146; see to-do list

**Notes on held/deferred items:**
- Item 143 (My Progress print): holding because the page layout will likely change when heat map is designed. Print a finalized layout, not a draft.
- Download/PDF (item 146): static site limitation — no server-side PDF generation. Best path is `window.print()` relabeled "Print / Save as PDF"; browser provides "Save as PDF" in the dialog. Adding a PDF library (jsPDF, etc.) not recommended. See item 146.
- Items 33 + 124 (print output): marked done. Developer to use in practice and report feedback.

*Session W (continued) — March 29, 2026 — bug fix pass + UX revision, v63.*

**v63 covered (in-session fixes after testing feedback):**

- **Stats screen persistence bug fixed ✅** — `#stats-screen { display: flex }` was overriding `.screen { display: none }`. Removed `display` from the ID rule; `.screen.active` now fully controls visibility. Stats no longer leaks into Setup or game round.
- **"My Progress" removed from title screen ✅** — Button deleted from `.title-link-row`. Stats accessible from results screen ("View Progress") only.
- **Extended tables moved to Advanced Settings toggle ✅** — ×13–×20 is now off by default. New checkbox "Extended tables (×13–×20)" in Advanced Settings. `buildTableGrid()`, `updateSelAllLabel()`, `updateEasyLabel()`, `buildMults()`, and Select All handlers all respect `S.extendedTables`. Prunes selected tables > 12 when toggled off. Saved/loaded in localStorage.
- **Tier descriptor copy revised ✅** — Removed IEP/504/diagnosis language. "students" → "learners" throughout tier descs. New copy: Challenge: "For learners who've mastered 3s automaticity." / Standard: "Research-based fluency threshold — the default for most learners." / Extended: "For learners who work best with more response time." / Extended+: "For learners who benefit from significantly more response time." Updated in TIER_DESCS map AND in the duplicate copy inside `loadAndApplySettings`.
- **About modal copy updated ✅** — Tables line updated: "up to ×12 (or up to ×20 with extended tables enabled in Advanced Settings)."

**Session W original features (v62):**

- **Extended tables ×13–×20 ✅** — Now behind a toggle (see above). (Item 63)
- **Print output redesign ✅** — Full new layout: header, student name, settings block, summary, fluency counts, fact chips, fluency key, notes lines. (Items 33 + 124)
- **Fluency threshold tiers ✅** — Advanced Settings collapsible, 4 pills, dynamic timer/grading/print. (Items 130 + 139)
- **Stats page ✅** — Tiles by table (gold/orange/purple), Challenge Facts section. (Items 88 + 89 + 110)
- **Sparkwright logo ✅** — Pip's sparkler mark, Nunito 800 wordmark.
- **Favicon ✅**
- **Bug 9 fixed ✅** — Pool notice / validation error conflict.

*Session Q ended March 28, 2026 — Spark only (journaling). No code changes.*

*Session P ended March 26, 2026 — gold flash, Bug 8, Bug 2, Item 127, v59.*

**Session P covered:**

- Item 125 ✅ — Find All correct cards now flash gold and settle to gold (was green). Reuses `match-flash` animation via new `.fa-card.fa-flash` class. `.fa-card.fa-good` updated to gold styling. `card-pop` (green scale) removed from click handler.
- Item 68 — Partially built (zone label below fluency bar) then removed at developer request. Bar color states are sufficient. Item closed.
- Bug 8 (partial) — perQTimer interval reduced from 50ms → 100ms in both `startPerQTimer()` and `resumeTimers()`. Halves DOM write frequency during active questions, expected to reduce typing jank in Safari on low-power hardware. Needs testing to confirm fix.
- Bug 2 (partial) — q-count input fields now pre-populated from `S.qCount` defaults in `buildSetupUI()`, so they're never empty even if `loadAndApplySettings()` UI restore fails. Addresses most likely cause of "Start does nothing." Needs testing to confirm fix.
- Item 127 ✅ — Fact Family Chase house SVG extended: bottom wall moved from y=468 → y=520, SVG height 490 → 550, viewBox updated, hardcoded pathLen updated 1330 → 1434. Gives ~54px clearance between last fact chip and house bottom line.
- Session O Data Philosophy handoff ✅ — Spark resolved: full content recovered from git and added to RP Section 2. MPF cross-reference now points to RP correctly.

**Testing needed next session (all from Session P):**
- T1 — Bug 8: type 2-digit answers in Per-Question Timer mode as timer gets low — confirm no missed keystrokes
- T2 — Bug 2: addition-only start (deselect ×, select +, click Start) — confirm game launches
- T3 — Item 127: Fact Family Chase house — confirm clear space below last chip after house draws

**Immediate next priorities (in order):**
1. Complete T1/T2/T3 testing from Session P
2. Design discussion with Spark: print output (items 33 + 124) — has been deferred longest
3. Design discussion with Spark: Challenge Facts + student stats page (items 88/89/110)
4. After design discussions: those features become the next build

*Session N ended March 25, 2026 — setup screen polish, pool notices, v58.*

**Session N covered:**

- Bug 9 ✅ — pool notice / validation error conflict fixed. Input listeners for all three q-count fields now clear non-info error text before calling `updatePoolNotice()`.
- Item 120 ✅ — "3 tries before reveal" → "2 attempts, then Practice Quest" (or "2 attempts, then answer revealed" when Practice Quest is OFF). Dynamic via `updateAnswerModeDesc()`.
- Answer Mode card ✅ — moved below Practice Features card so the toggle context comes first. Type Answer description updates live when Practice Quest is toggled.
- Practice Features label ✅ — "after 3 wrong answers" → "after 2 wrong answers."
- D121 ✅ — pool guard added to `startGame()`: blocks start if pool < 2, shows error.
- Easy toggle copy ✅ — × and ÷ labels now use identical structure and style. ÷ example added: "÷6, ÷7 selected → no 30÷6, 28÷7."
- Select All ÷ ✅ — toggle added to ÷ card matching × card. `updateSelAllLabel(op)` generalized for both ops.
- No-tables warning ✅ — `tgrid-msg-x` and `tgrid-msg-/` divs added below each grid. Show red "Select at least one table to play." when all tables deselected.
- Pool=1 warning ✅ — yellow "Only 1 unique fact — add more tables or turn on the **Practice Every Fact** toggle below." appears in `tgrid-msg` when 1 table + Easy OFF. Triggered from chip click handlers and easy toggle listeners.
- Repeat notice ✅ — "X unique facts — questions will repeat to fill N items. (Select the **Practice Every Fact** toggle above to include full tables.)" shown near question count field when pool < qCount.
- Items 130, 132–136 logged — teacher shareable links (130), re-queue design tensions (132–136).
- Testing protocol added to MPF Claude Code Workflow section — test items must be numbered/lettered (T1, T2, A, B…).
- `.num-input-msg.warn` CSS class added — yellow (#ffd93d), font-weight 400 with bold toggle names via `<strong>`.

**Testing completed this session:**
- T9 (Answer Mode copy) ✅
- T10 (Practice Features first, Answer Mode second; dynamic description) ✅
- T11 (pool=1 warning in table grid) ✅
- T12 (repeat notice with unique count) ✅
- T13 (bold toggle names, warn font weight) ✅

**Immediate next priorities (in order):**
1. **dev/ housekeeping review** *(requested, Session N)* — review all files in `dev/`, confirm file names are descriptive enough to identify at a glance, produce a table with file name, abbreviation, and one-line summary for developer reference. Do at session start.
2. **MPF structure review** *(requested, Session N)* — MPF is getting long. Review whether it should be split into multiple `.md` files (e.g. separate files for to-do list, science/pedagogy, data philosophy, session log). Do alongside dev/ housekeeping.
3. Print output work (items 33 + 124) — developer has notes; design discussion first
4. Items 88 / 89 / 110 — Challenge Facts workspace + student stats page (design discussion)

---

*Session K ended March 24, 2026 — no code written.*

**Session K covered:**
- Created `dev/Math_Flash_Code_Rationale.md` — 16 decisions documented across 5 categories (Architecture, localStorage Design, Per-Fact Tracking, Timing & Fluency, Pedagogy-Driven Code Decisions)
- Updated HOW TO START A NEW SESSION to include reading the Code Rationale file
- Session-end checklist updated: update Code Rationale when non-obvious code decisions are made
- Memory index updated with pointer to Code Rationale file

---

*Session J ended March 24, 2026 — housekeeping only, no code written.*

**Session J covered:**
- MPF header updated, items 93 and 99 marked ✅
- Completed log patched (Sessions G, H, I, J added)
- Session-start guidance added to HOW TO START A NEW SESSION
- Workflow discussion: Claude Code should read MPF + RP in full at session start, not rely on memory files alone

---

*Session I ended March 23, 2026.*

**Session H covered:**
- Item 86 ✅ — per-fact tracking tested, two bugs fixed, confirmed working
- Item 99 ✅ — GitHub + Netlify auto-deploy connected, v55 live on sparkwright.org
- Item 93 ✅ — v55 live

**Session I covered (design only — no code written):**
- Two-level fluency model defined: per-attempt grades (existing) vs. longitudinal Mastered (new)
- Mastery definition decided: correct in ≤3s on 4 of last 5 attempts, 2+ sessions, low variance
- Variance confirmed as a real diagnostic signal (research-backed)
- Competitive research logged: XtraMath, Reflex, Rocket Math thresholds documented
- New items added: 108 (mastery flag), 109 (teacher print report), 110 (consistency labels), 111 (FAQ page)
- Science & Pedagogy section in MPF significantly expanded

**Recommended next session — chronological order:**
1. Item 87 — variance calculation (internal, no UI yet) — ready to code
2. Item 108 — mastery flag added to fact record — ready to code after variance threshold decided
3. Item 88 — Challenge Facts workspace — design discussion first
4. Item 89 / 110 — student stats page + consistency label word choice — design discussion
5. Item 109 — teacher print report — design discussion
6. Item 111 — FAQ / methodology page — after above are designed

**Items needing design discussion before coding:**
- Item 66 — Assessment area (what does a formal assessment look like in Math Flash?)
- Item 84 — Practice Quest internal timer
- Item 73 — Mini-game absorption + Prove It gate
- Item 72 — Is Practice Quest too long?
- Item 82 — Pet Fact mastery threshold
- Item 100 — Math Flash title screen overhaul
- Item 101 — Teacher fact-picker design
- Item 105 — Guest play UX (prompt to create profile? logout option?)

---

## BATCHING GUIDE

| Batch | Items | Notes |
|-------|-------|-------|
| Per-fact tracking — test first | 86 | Verify A–F checklist before building on it |
| Response time stats | 87 | After 86 confirmed working |
| Student stats page | 89 | After 86+87 |
| Practice time tracking | 90 | Small add-on alongside 86 |
| Assessment area | 66 | Design discussion first |
| Title screen overhaul | 100 | Design discussion first |
| Teacher fact-picker | 101 | Design discussion first |
| Print output | 33 | Test first, then refine |
| Mini-game build | 56, then 57, then 58 | One at a time |
| Mini-game randomization | 55 | After 2–3 mini-games exist |
| PQ timer | 84 | Design discussion first |
| Pet Fact egg integration | 74–79 | After mechanics solid; requires local server |

---

## HOW TO START A NEW SESSION

**For Claude Code instances — do this first, before anything else:**
Read this file in full (`dev/Sparkwright_MPF_March_22_2026_v55.md`), then read the RP file (`dev/Math_Flash_Research_and_Pedagogy.md`), then skim the Code Rationale file (`dev/Math_Flash_Code_Rationale.md`). Current game file: `dev/2026-03-25_1700_Math_Flash_v58_pool-notices-2attempt-pool-guard.html`. Do not rely on the memory files in `.claude/projects/` — they may be stale. The dev files are the source of truth. Reading all three takes ~4 reads due to size limits but is always worth it.

1. Open the `sparkwright` project folder in Terminal
2. Run `claude` to start Claude Code (or upload HTML + MPF to claude.ai chat if preferred)
3. Read MPF, RP, and Code Rationale files in full (see above) before proposing anything
4. Tell Claude which item(s) to work on, or say "suggest a batch"
5. Claude proposes batching, waits for confirmation before coding
6. Lettering resets to A at the start of each new session
7. Always use `YYYY-MM-DD_HHMM_vN.html` naming for HTML files
8. At session end: update MPF + update Code Rationale file if any non-obvious code decisions were made
9. **Test in Safari**, not Chrome
10. **Use local server for testing** — drag sparkwright folder into Terminal, run `python3 -m http.server 8000`, open `http://localhost:8000`
11. **Do not deploy to Netlify just to test** — 300 credits/month, spend wisely
12. **Screenshot/attachment rule:** If developer hints at sharing an attachment and none arrives, pause and ask
13. **Image work is deferred** — do not attempt until core mechanics are done
14. **Always diff output vs input** when inserting new code blocks near existing function declarations — str_replace can accidentally consume a function declaration line

---

## COMPLETED — ALL SESSIONS (cumulative)

- Pool system, re-queue budget, 1-Strike system
- How to Play overlay
- Pause menu (game + remediation)
- Results screen: Play Again / Settings / Home / Print
- Combined Check/Next button
- All Chrome crash fixes through v38
- Fact Family Chase built and polished
- Practice Quest 4-step flow complete and button-restructured
- Deduplication fix for multiplication pool
- v36: stability pass
- v37: full timer system overhaul — 4 formats, fluency grading, pause/resume
- v37b: stopwatch pause crash fix
- v38: remediation button restructure, Find All distribution, Match It fix, mode descriptions, print button, Prove It feedback, Enter key fix
- v39: two attempts before quest, division label fix, addition panel spacing
- v40: op button labels, panel spacing wrapper, error message clear
- v41: removed rAF from showScreen
- v42–v50: comprehensive crash hardening — safeTimeout/G.gen, restartGame separation, openPause timeout cancel, animation-play-state, browser switch to Safari
- v51: shared toolbar across game + quest, timer color states, toolbar color updates, fluency tier rename, results overhaul, Find It gold pulse, Enter key for Fact Family Chase, house chip padding, floating quest badge
- Session B: design exploration — aesthetic documentation, Pet Fact system design, pixel art egg created by developer, MPF expanded
- Session C: strategic reset — mechanics-first direction established, Pet Fact / image work deferred
- Session D: brand & business — Sparkwright name chosen, sparkwright.org registered, hosting/localStorage/username architecture documented, competitive landscape mapped
- Session E: Sparkwright landing page built, site file structure established, local server workflow established
- Session F (v52–v54): profile system (landing page), Math Flash site header, items 34/35/36/69, settings memory (item 85), round-ending-early bug fix, same-facts-on-restart bug fix, Find All card clustering fix
- Session G (v55): per-fact tracking built — `mathflash_facts` localStorage key, fact record schema, recording hooks in `handleCorrect` / `handleMiss` / `autoKick`, guest skip logic, 20-entry rolling window
- Session H: per-fact tracking tested and confirmed (item 86 ✅) — two bugs found and fixed: (1) `responseTimes` stored raw timestamp instead of elapsed ms, (2) `qStartTime` not set in non-timer modes. GitHub repo `SVScreate/sparkwright` created, Netlify auto-deploy connected, v55 live on sparkwright.org (items 93 ✅, 99 ✅)
- Session I (design only — no code): two-level fluency model defined, mastery definition decided (correct in ≤3s on 4/5 attempts, 2+ sessions, low variance), variance research documented (Stickney et al., Reflex white paper), competitive mastery thresholds logged. New items added: 108 (mastery flag), 109 (teacher print report), 110 (consistency labels), 111 (FAQ page), 112–117 (research/design backlog). RP file created and populated.
- Session P (v59): Item 125 ✅ — Find All correct cards flash gold. Item 68 — zone label built and removed (bar colors sufficient). Bug 8 partial — perQTimer reduced 50ms→100ms. Bug 2 partial — q-count fields pre-populated in buildSetupUI(). Item 127 ✅ — house SVG extended, ~54px clearance. Session O housekeeping completed; Spark resolved Data Philosophy orphan. Tests T1/T2/T3 pending next session.
- Session O (housekeeping — no code): full dev/ rename pass, Sparkwright_File_Manifest.md created, MPF trimmed 793→620 lines, localStorage schema moved to Code Rationale, dual-agent system (Wright + Spark) established, all committed and pushed.
- Session K (housekeeping — no code): Code Rationale file created (`dev/Math_Flash_Code_Rationale.md`), 16 decisions documented, HOW TO START A NEW SESSION updated to include it
- Session J (housekeeping — no code): MPF/RP updated, completed log patched, items 93/99 marked ✅, session-start guidance added for future Claude instances
- Session G (v55): per-fact tracking built (item 86 — untested), assessment area added to to-do (item 66), Claude Code set up
