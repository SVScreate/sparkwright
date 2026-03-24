# Math Flash — Master Project File (MPF)
*Last updated: March 24, 2026 — Session K (no code written: Code Rationale file created, session-start guidance updated to include it)*
*Current Math Flash version: v55 — `2026-03-19_1530_v55.html`*
*Current Sparkwright landing page: `sparkwright/index.html` (updated session F)*
*Replace this file and the HTML at the start of each new session with the latest versions.*

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

*These are the developer's raw ideas from session H — to be developed further into marketing copy and product positioning.*

### The Core Stance
Sparkwright uses **localStorage** — data lives on the student's device, not on a server. This is a deliberate philosophical choice, not a technical limitation.

### Why Local Storage Is the Right Model for This Product

**The user is in control.**
The student (and teacher/parent) owns their data. It doesn't get harvested, analyzed by a third party, or locked inside a subscription. If they stop using the product, their history doesn't disappear into someone else's database.

**In-the-moment practice and feedback.**
Most server-based platforms (e.g. TTRS) cycle through problems, mark wrong answers as wrong, and move on — with no in-the-moment remediation. The data goes to the backend and surfaces later as charts. Math Flash gives immediate Practice Quest remediation and per-session printable results. The learning happens *now*, not in a monthly report.

**The teacher can see what actually happened.**
With TTRS and similar platforms, the teacher has to wait for a reporting cycle (e.g. monthly "gig" summary) to see progress. There's no per-session view of what a student worked on. Math Flash's print output gives the teacher immediate, session-level visibility — what was practiced, what was fluent, what needs more work.

**Wrong answers don't just disappear.**
In TTRS, a missed fact may reappear eventually — but there's no structured in-the-moment remediation, no fact family practice, no "Prove It" gate. The lack of fluency persists because the platform doesn't stop and teach. Math Flash treats a miss as a learning moment, not just a data point.

**Simpler, faster, more honest.**
No account creation friction, no password resets, no server latency, no data breach risk. The game works offline. The student's progress is theirs.

### The Honest Tradeoffs
- Data doesn't follow the student across devices (yet — this is solvable with export/import)
- No cross-classroom aggregate data for schools (a feature for server-based models, but also a surveillance tradeoff)
- If a student clears their browser storage, data is lost (mitigatable with export/backup feature)

### What This Means for the Business Model
The value proposition isn't "we hold your data and show you dashboards." It's "we give you a better learning experience and you keep your data." This is worth paying for — especially for homeschool families and independent teachers who are skeptical of ed-tech data collection.

**⚠️ To develop further:**
- Flesh out this philosophy into About page / marketing copy (share resume in a Claude chat session)
- Compare explicitly to spellingtraining.com (localStorage model) vs. TTRS (server model)
- Articulate what a paid tier looks like in a local-first model (premium features, not data access)
- Consider export/import as a feature that bridges local and portable

---

## Science & Pedagogy

*Full research, pedagogy, competitive landscape, and developer reflections live in the companion file: `Sparkwright_Research_and_Pedagogy.md` (RP). This section contains working summaries only. Always update both files when new research is added.*

### Fluency Automaticity — The 3-Second Threshold
The 3-second threshold for fact fluency is well-established in cognitive load and automaticity research. Retrieval under ~3 seconds suggests the fact is stored as a direct memory trace (declarative recall) rather than being computed procedurally. This threshold is used by major fluency programs including Reflex Math and XtraMath, and is grounded in math fluency research including work by Erin Olson and others.

### Math Flash Fluency Grading (Per-Question Timer mode only)
| Grade | Threshold | Meaning |
|-------|-----------|---------|
| ⚡ Fluent | Correct, ≤3s | Automatic retrieval — fact is memorized |
| 🔄 Almost! | Correct, 4–6s | Knows it, not yet automatic — still computing |
| 📚 Needs Practice | Wrong answer, or no answer by 7s | Not yet known — needs practice |

**Fluency grading is only shown in Per-Question Timer mode.** Other modes (Set #, Timed, Stopwatch) do not display fluency data — Set # of Questions is intentionally urgency-free. Fluency is silently tracked in all modes internally for potential future use.

**Note:** The three-tier grading is a custom category system. The binary fluent/not-yet-fluent distinction is research-standard; the "Almost!" middle category is the developer's own pedagogical addition.

**The 7-second auto-kick** is practical rather than research-derived — long enough that if they haven't answered, they don't know it.

### Accommodations — Processing Speed & Timer Flexibility *(Session I — research needed)*

**The core issue:** The 3-second fluency threshold and 7-second auto-kick are calibrated for typical processing speeds. Students with slower processing speed (common in learning disabilities, ADHD, anxiety, dyslexia, and other profiles) may be penalized by these thresholds even when they genuinely know a fact.

**Questions to research and design around:**
- What does the research say about processing speed variability across neurotypes? Is there a published accommodation standard for timed math fact assessments?
- Should teachers be able to set a custom fluency threshold (e.g. 5s instead of 3s) for specific students?
- Should teachers be able to adjust the per-question timer length (currently 7s auto-kick) per student or per session?
- Should there be a named "Accommodations" toggle in settings, or just adjustable sliders?
- How do we document this in the FAQ so teachers understand both the default (research-based) and the accommodation options?

**Preliminary design instinct:** Teacher-adjustable fluency threshold and auto-kick timer, set in the game setup screen or a teacher settings panel. The defaults remain research-based (3s / 7s). Accommodated settings would be clearly labeled so print reports reflect the threshold used.

**Why it matters for Sparkwright's identity:** This product is built by an Educational Therapist. Accommodation support is not an afterthought — it is core to the product's integrity and its appeal to the homeschool and learning-support market.

⚠️ *Research pass needed before designing. Add to FAQ once designed.*

### Two-Level Fluency Model (Session I — design decision)

Math Flash uses two distinct concepts that must not be confused:

**Level 1 — Per-attempt grade** (in-game, shown during Per-Question Timer mode):
| Grade | Threshold | Meaning |
|---|---|---|
| ⚡ Fluent | Correct, ≤3s | Fast enough to suggest automatic retrieval |
| 🔄 Almost! | Correct, 4–6s | Knows it, not yet automatic |
| 📚 Needs Practice | Wrong or no answer by 7s | Not yet known |

These grades describe a single answer. They are not mastery.

**Level 2 — Longitudinal mastery** (tracked over time, across sessions):
A fact is **Mastered** when a student demonstrates durable, stable automaticity — not just one good answer.

**Math Flash Mastery Definition:**
> Correct in ≤3s on **4 out of the last 5 attempts**, spanning **at least 2 separate sessions**, with **low response time variance**.

- The 2-session requirement prevents "one good day" mastery
- The variance condition is a differentiator backed by research (see below)
- The exact variance threshold (what counts as "low") is TBD — will be tuned with real use

**Why this matters:** A student who sometimes answers in 1.2s and sometimes in 5.8s is NOT automatic on that fact, even if their average looks good. High intraindividual variance in response time is a diagnostic signal of effortful processing (counting/calculating), not automatic retrieval.

### Response Time Consistency — The Research Case

Research on variance as a mastery signal:
- **Stickney, Sharp & Kenyon (2012)** — "Technology-Enhanced Assessment of Math Fact Automaticity" — found that response time *variability* distinguishes lower-achieving from typically-achieving students even when average speeds are similar. High variance = not yet automatic.
- **Reflex Math** explicitly uses "response pattern stability" language in their white paper as a condition for fact certification. They can de-certify a fact if variance returns. (Algorithm proprietary but the principle is published.)
- **Broader cognitive science:** High intraindividual variability (IIV) in RT is consistently associated with effortful processing vs. automatic retrieval. Low IIV = more automatic.

**Design implication:** Variance is tracked internally (via `responseTimes` array in `mathflash_facts`) and will:
1. Factor into the Mastered threshold
2. Influence which facts stay in the Challenge Facts pool (item 88)
3. Appear in teacher print report with a human-readable consistency label

### Competitive Research — Mastery Thresholds

| Program | Time threshold | Repetition criterion | Variance check |
|---|---|---|---|
| **XtraMath** | ≤3s (adjustable) | 2 correct out of last 3, across sessions | No |
| **Reflex Math** | ~1–2s (proprietary) | Proprietary — uses "stability" language | Yes (implied) |
| **Rocket Math** | Timed (program-set) | 12 consecutive correct | No |
| **Math Flash** | ≤3s | 4 out of last 5, across 2+ sessions | Yes |

XtraMath's 2/3 criterion is simple and defensible. Math Flash's 4/5 + variance model is stricter and more diagnostically valid — backed by Stickney et al. and Reflex's own published language.

**Academic consensus:** No single peer-reviewed magic number exists. The field treats automaticity as a performance criterion (speed + accuracy + consistency sustained over time), not a raw repetition count. Woodward (2006), Kling & Bay-Williams (2015), and Baker & Cuevas (2018) all emphasize distributed practice across sessions over massed repetition.

**Sources:**
- Stickney, Sharp & Kenyon (2012) — ResearchGate
- Cholmsky (2011) — Reflex White Paper
- Woodward (2006) — Developing Automaticity in Multiplication Facts
- Baker & Cuevas (2018) — ERIC EJ1194585
- XtraMath support documentation
- SuperMemo SM-2 algorithm (Wozniak, 1990)

### Timed Round + Practice Quest
Timers (global countdown, stopwatch) pause during Practice Quest so students are not punished for learning.

### Two-Attempt System (v39+)
Students get a silent second chance on wrong answers before Practice Quest triggers. First wrong answer: shake + clear input, clock keeps running. Second wrong answer: Practice Quest. Score bonus (`4 - attempts`) applies.

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

---

## 👤 Profile & localStorage Architecture

### Sparkwright Profile System (landing page — session F)
Profiles are stored at the **site level** (in `sparkwright/index.html`), not inside Math Flash. Any future game reads the same keys.

**localStorage keys:**
- `sparkwright_profiles` — JSON array of all profile objects
- `sparkwright_active` — username string of active profile

**Profile object schema:**
```json
{
  "username": "CosmicOtter",
  "avatar": "🦊",
  "createdAt": "2026-03-19",
  "hasVisited": true
}
```

**Behavior:**
- First visit after profile creation → "Welcome, [name]!"
- Return visits → "Welcome back, [name]!"
- Multiple profiles supported — switcher modal lists all, active badge shown
- Switch user keeps all data, switches active profile
- Delete profile — per-profile trash icon in switcher, confirmation dialog required
- No profile → "Create profile" button in nav; chip shows "👤 Guest" in Math Flash header

### Math Flash Settings Memory (session F)
**localStorage key:** `mathflash_settings`

Saved on every `startGame()` call (after all S values are finalized). Restored silently on setup screen open.

**Saved fields:** ops, tablesX, tablesDiv, easyX, easyDiv, maxAdd, maxSub, allowNeg, format, qCount, timeLimit, mode, remed, repeat

### Math Flash Per-Fact Tracking (session G — v55) ⚠️ UNTESTED
**localStorage key:** `mathflash_facts`

Stored as nested object: `{ [username]: { [factKey]: factRecord } }`

**Fact key format:** `"mul_6x7"`, `"div_42d7"`, `"add_3p4"`, `"sub_9m3"`

**Fact record schema:**
```json
{
  "key": "mul_6x7",
  "label": "6 × 7",
  "correct": 14,
  "incorrect": 3,
  "questTriggered": 2,
  "responseTimes": [2100, 4800, 1900, 3200],
  "fluencyCounts": { "fluent": 9, "almost": 4, "needs": 1 },
  "firstSeen": "2026-03-22",
  "lastSeen": "2026-03-22"
}
```

**Recording hooks:**
- `handleCorrect()` → outcome `'correct'`, elapsed ms from `G.qStartTime`
- `handleMiss()` → outcome `'miss'` (quest triggered) or `'incorrect'` (no quest), elapsed 0
- `autoKick()` → outcome `'autokick'`, elapsed 7000ms — `handleMiss` skips recording to prevent double-count
- Guests skipped silently (no `sparkwright_active` in localStorage)

**Rolling window:** last 20 response times per fact (oldest drop off)

**Fluency thresholds:** ≤3000ms → fluent, ≤6000ms → almost, else → needs

**Test checklist (pending):**
- A. Correct answer → `correct` increments, `responseTimes` gains entry, `fluencyCounts` increments correctly
- B. Wrong answer (2nd attempt, mul/div with remed on) → `incorrect` + `questTriggered` increment
- C. Wrong answer (add/sub or remed off) → `incorrect` increments, `questTriggered` does NOT increment
- D. Auto-kick (wait 7s) → `incorrect` increments, `responseTimes` gains 7000, no double-count
- E. Guest (no profile) → no `mathflash_facts` entry written at all
- F. 21+ answers for same fact → `responseTimes` stays capped at 20 entries

### Math Flash Header Bar (session F)
Fixed 48px header at top of every Math Flash screen. Contains:
- Left: ← Sparkwright (link to `../../`) | Math Flash label
- Right: profile chip (emoji + username, or 👤 Guest)
- Reads `sparkwright_profiles` + `sparkwright_active` from localStorage
- `body { padding-top: 48px }` pushes game content below header

### Future localStorage Keys (planned)
- `mathflash_practice_time` — cumulative practice time (item 90)

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

### 🔧 UI / COPY
6–31. *(all completed — see COMPLETED log)*
32. Auto-advance / "Student Speed Mode" toggle *(discussed, not yet designed)*
33. **Print output** — functional via popup. Needs real-world testing and refinement.
34. ✅ "Format" → "Mode" — renamed (v52)
35. ✅ "— no time pressure." copy — removed (v52)
36. ✅ Typing field character limit — 4 characters max (v52)
37–49. *(all completed — see COMPLETED log)*
50. Results screen — revisit design and information hierarchy
51. Animations — title screen bokeh + setup flair *(deferred — after core mechanics)*
52. **Device screen fit / viewport clipping** — Chromebooks cut off cards. *(Design discussion)*
53. **Timer option for Practice Quest** *(see item 84)*
100. **Math Flash title screen overhaul** — change tagline (sounds AI-generated), rethink layout, replace four example facts with four operation symbols, add button placeholder for future areas, review "How to Play" content. *(Session F — design discussion needed)*
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
87. **Response time variance** — calculate internally from `responseTimes` array. Flag facts with high intraindividual variance as "not yet stable." Feeds mastery threshold, challenge facts, and print report. Variance threshold (what counts as "low") TBD — tune with real use. *(Design decided session I — ready to code)*
88. **Challenge Facts workspace** — facts that have high attempt counts, high variance, or are close to Mastered threshold surface here for targeted practice. Design discussion needed.
89. **Student-facing stats page** — simplified, encouraging, no raw numbers. Fact tiles with tier colors, plain-language labels. Design discussion needed.
90. **Practice time tracking** (`mathflash_practice_time`) — cumulative practice time per user
108. **Mastery flag** — add `mastered: boolean` and `masteredDate` to fact record schema once mastery threshold is finalized. Criterion: correct in ≤3s on 4 of last 5 attempts, spanning 2+ sessions, with low variance. *(Ready to code after variance threshold is tuned)*
109. **Teacher print report** — separate from round-end print. Shows per-fact data across time windows (round / day / week / month / year / all-time). Columns: avg response time, consistency label, attempt count, quest triggered count, last practiced. Heat map equivalent using Sparkwright fluency tier colors. Design discussion needed.
110. **Student stats page — consistency labels** — human-readable labels derived from variance for fact tiles. Current candidates: Automatic / Developing / Not Yet. Word choice TBD. Design discussion needed.
111. **FAQ / methodology page** — explains what fluency means, how Mastered is determined, why facts get flagged as challenge facts, what the tiers mean. Written for teachers and parents. Protects IP by explaining the *what* without exposing exact thresholds. Build after stats/print report are designed.
112. **Competitive research pass** — extensive comparison of IXL, iReady, XtraMath, TTRS, Reflex Math, Rocket Math, Khan Academy, Prodigy, and others. Document: mastery model, remediation approach, timer/accommodation options, pricing, data model, UX feel, differentiators vs. Math Flash. Feeds FAQ, About page, and product positioning.
114. **Student & teacher agency — core design principle** — Math Flash is explicitly designed so that the student and their teacher/helper feel in control of how practice feels. Settings, timer options, and accommodations exist to serve the learner — not to enforce a one-size-fits-all drill. Most competing programs (XtraMath, TTRS, IXL, iReady, etc.) have a sterile, punishing vibe: the program drills the student, marks them wrong, and moves on. Math Flash's differentiator is that it meets students where they are, respects their pace, and gives both student and teacher meaningful guidance on how to use it well. This philosophy should be explicit in the FAQ, onboarding, and About page copy.

113. **Accommodations — processing speed** — research adjustable fluency thresholds and timer lengths for students with slower processing speed (learning disabilities, ADHD, anxiety, dyslexia). Design teacher-adjustable settings for: fluency threshold (default 3s) and auto-kick timer (default 7s). Document accommodation options in FAQ. Core to Sparkwright's identity as an Educational Therapy-grounded product. *(Research pass needed first)*
114. **Student & teacher agency — core design principle** — Math Flash is explicitly designed so that the student and their teacher/helper feel in control of how practice feels. Settings, timer options, and accommodations exist to serve the learner — not to enforce a one-size-fits-all drill. Most competing programs have a sterile, punishing vibe: the program drills the student, marks them wrong, and moves on. Math Flash's differentiator is that it meets students where they are, respects their pace, and gives both student and teacher meaningful guidance on how to use it well. This philosophy should be explicit in the FAQ, onboarding, and About page copy.
115. **Practice Quest engagement mechanic** — Design discussion needed. Timer pauses during Practice Quest (pedagogically correct). Risk: students may use wrong answers as an intentional escape ("escape-motivated errors") or mentally check out when the overlay appears. Need a mechanic that requires genuine presence without punitive pressure. Possible directions: response-required steps that can't be passively clicked through; subtle non-scoring ambient indicator; Prove It gate already partially addresses this. Do not touch code until design is settled.
116. **Literature review pass** — Dedicated research session to gather and document primary sources on: errorless learning vs. error correction, math anxiety and timed assessments, neurodivergence and cognitive load, fluency automaticity thresholds, in-the-moment vs. delayed feedback. Builds into RP Science & Pedagogy section. Backbone of FAQ and differentiates Sparkwright's claims from generic "science-backed" marketing language.
117. **Competitive landscape chart** — Structured cross-comparison of all current math fluency programs: XtraMath, Reflex, Rocket Math, TTRS, IXL, iReady, Zearn, Khan Academy, 99Math, Boddle, Monster Math, MathFactLab, spellingtraining.com, and small flashcard apps. Chart axes: wrong-answer response, remediation type, timer model, neurodivergent accommodation, age range, price model, data model, tables covered, school vs. family market. Do in a dedicated chat session. Do after journaling about target user — the questions will be sharper.
106. **localStorage schema migration** — as the game evolves, localStorage schemas will change (new fields added, old ones renamed). Design discussion needed: how do we avoid wiping or breaking a student's saved progress when updates ship? Needs a versioning/migration strategy before real student data accumulates. *(Session H)*

### 👤 USERNAMES & PROFILE
95. ✅ Profile system — generated usernames + emoji avatar, multi-profile support, switcher modal, site-level localStorage (session F, landing page)
96. ✅ Generated names — adjective+noun combos, no profanity possible (session F)
97. ✅ Math Flash header bar showing active profile (session F)
105. **Guest play UX** — currently guests can play freely but tracking is silently skipped and there is no logout button (only "Switch Profile"). Design discussion needed: should the game prompt "Create a profile to save your progress" before starting, or allow frictionless guest play? Also consider: should a logout/guest option be added to the profile switcher? *(Session H)*

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

---

## WHERE TO PICK UP

*Session K ended March 24, 2026 — no code written.*

**Session K covered:**
- Created `dev/Math_Flash_Code_Rationale.md` — 16 decisions documented across 5 categories (Architecture, localStorage Design, Per-Fact Tracking, Timing & Fluency, Pedagogy-Driven Code Decisions)
- Updated HOW TO START A NEW SESSION to include reading the Code Rationale file
- Session-end checklist updated: update Code Rationale when non-obvious code decisions are made
- Memory index updated with pointer to Code Rationale file

**Next session — ready to code:**
1. Item 87 — variance calculation (internal only, no UI) — ready to code
2. Item 108 — mastery flag (`mastered: boolean`, `masteredDate`) — ready after variance threshold decided

**Next — design discussion needed first:**
3. Item 88 — Challenge Facts workspace
4. Item 89 / 110 — student stats page + consistency label wording

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
Read this file in full (`dev/Math_Flash_MPF_March_22_2026_v55.md`), then read the RP file (`dev/Sparkwright_Research_and_Pedagogy.md`), then skim the Code Rationale file (`dev/Math_Flash_Code_Rationale.md`). Do not rely on the memory files in `.claude/projects/` — they may be stale. The dev files are the source of truth. Reading all three takes ~4 reads due to size limits but is always worth it.

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
- Session K (housekeeping — no code): Code Rationale file created (`dev/Math_Flash_Code_Rationale.md`), 16 decisions documented, HOW TO START A NEW SESSION updated to include it
- Session J (housekeeping — no code): MPF/RP updated, completed log patched, items 93/99 marked ✅, session-start guidance added for future Claude instances
- Session G (v55): per-fact tracking built (item 86 — untested), assessment area added to to-do (item 66), Claude Code set up
