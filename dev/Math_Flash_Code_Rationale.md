# Math Flash — Code Rationale
*A running log of non-obvious code decisions: what was chosen, why, and what alternatives were considered.*
*Updated at the end of any session where a significant architectural or design-in-code decision is made.*

---

## How to Use This File

This file answers: "Why does the code look like this?" and "What exactly is stored where?"

**What belongs here:**
- Code architecture choices where the reason isn't obvious from reading the code
- localStorage schemas and key reference (see localStorage Schema Reference section)

**What lives elsewhere:**
- Pedagogy, product philosophy, research rationale → `Math_Flash_Research_and_Pedagogy.md` (RP)
- To-do list, session notes, version history, operational context → `Sparkwright_MPF_March_22_2026_v55.md`
- Dev folder structure → `Sparkwright_File_Manifest.md`

**Rule of thumb:** If you made a choice between two or more reasonable approaches and the reason isn't obvious from reading the code, log it here.

---

## Architecture

### Single HTML File
**Decision:** The entire Math Flash game lives in one `.html` file (HTML + CSS + JS all inline).

**Why:** The developer is not a professional developer and doesn't use a build system (npm, webpack, etc.). A single file can be opened directly in a browser, shared easily, and edited without tooling. No server required to run locally (though one is needed for `localStorage` cross-page features). This is the right tradeoff for this project's scale and authorship context.

**Tradeoff:** As the file grows, it becomes harder to navigate. Mitigation: clear section headers with `// ══ SECTION NAME ═══` comment dividers.

---

### No Build Process, No Frameworks
**Decision:** Vanilla HTML/CSS/JS. No React, Vue, jQuery, etc.

**Why:** Same as above — zero tooling dependency, zero build step, works offline. The game's interactivity doesn't require a framework.

---

### Safari as Primary Test Browser
**Decision:** All testing is done in Safari. Chrome is not used for local testing.

**Why:** Chrome on Mac was causing repeated crashes (v36–v50) related to DOM mutations on live elements. The issue was complex and partially worked around, but the crashes were unpredictable. Switching to Safari eliminated the crashes entirely. Safari is also the primary browser for the target user (homeschool/family Mac users). See Crash Log in MPF for full history.

---

## localStorage Design

### Nested Structure: `{ username: { factKey: record } }`
**Decision:** `mathflash_facts` is stored as a nested object keyed first by username, then by fact key.

**Why:** Flat storage (just `{ factKey: record }`) would work for a single-user app, but Math Flash supports multiple profiles. Nesting by username means all profiles share one localStorage key and can be read/written in one `JSON.parse` / `JSON.stringify` call. The alternative — one localStorage key per user (e.g., `mathflash_facts_CosmicOtter`) — would work but requires knowing the username to construct the key, and makes it harder to enumerate all users.

---

### Fact Key Format: `"mul_6x7"`, `"div_42d7"`, `"add_3p4"`, `"sub_9m3"`
**Decision:** Keys use a short operation prefix + the two operands joined by a separator (`x`, `d`, `p`, `m`).

**Why:** Keys need to be stable (the same fact always maps to the same key), human-readable for debugging, and safe for use as object property names. The separators are chosen to be unambiguous: `6x7` can only mean 6 × 7; `42d7` can only mean 42 ÷ 7. A format like `"6*7"` or `"6×7"` would work but special characters can cause issues as object keys.

**Note on multiplication deduplication:** `6x7` and `7x6` are the same fact. The `factKey()` function always stores multiplication facts with the smaller number first (e.g., `mul_6x7`, never `mul_7x6`) to prevent duplicate records.

---

### One localStorage Key for All Fact Data (`mathflash_facts`)
**Decision:** All per-fact records for all users live under a single key.

**Why:** Keeps the data model simple — one read to load everything, one write to save. The tradeoff is that the object can grow large over time (many users × many facts). For a student-scale app on a personal device, this is fine. If the app ever scales to classroom-level use, a migration strategy would be needed (see Item 106 in MPF).

---

## localStorage Schema Reference

*This section is the authoritative reference for what lives in localStorage — key names, schemas, and behavior. For the decisions behind these choices, see the localStorage Design section above. For the product philosophy behind local-first storage, see `Math_Flash_Research_and_Pedagogy.md` (Data Philosophy section).*

### Key Map

| Key | Scope | Purpose |
|---|---|---|
| `sparkwright_profiles` | Site-level | JSON array of all profile objects |
| `sparkwright_active` | Site-level | Username string of active profile |
| `mathflash_settings` | Game | Last-used setup screen values |
| `mathflash_facts` | Game | Per-fact tracking, nested by username |
| `mathflash_practice_time` | Game | Cumulative practice time *(planned, item 90)* |

---

### `sparkwright_profiles` — Profile Array (session F)
Stored at the site level in `sparkwright/index.html`. Any future Sparkwright game reads these same keys.

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

---

### `mathflash_settings` — Settings Memory (session F)
Saved on every `startGame()` call after all `S` values are finalized. Restored silently on setup screen open.

**Saved fields:** `ops, tablesX, tablesDiv, easyX, easyDiv, maxAdd, maxSub, allowNeg, format, qCount, timeLimit, mode, remed, repeat`

---

### `mathflash_facts` — Per-Fact Tracking (session G — v55) ⚠️ UNTESTED
Stored as nested object: `{ [username]: { [factKey]: factRecord } }`

**Fact record schema:**
```json
{
  "key": "mul_6x7",
  "label": "6 × 7",
  "correct": 14,
  "incorrect": 3,
  "questTriggered": 2,
  "responseTimes": [2100, 4800, 1900, 3200],
  "recentAttempts": [{ "ms": 2100, "correct": true, "date": "2026-03-22" }],
  "fluencyCounts": { "fluent": 9, "almost": 4, "needs": 1 },
  "mastered": false,
  "masteredDate": null,
  "firstSeen": "2026-03-22",
  "lastSeen": "2026-03-22"
}
```

**Recording hooks:**
- `handleCorrect()` → outcome `'correct'`, elapsed ms from `G.qStartTime`
- `handleMiss()` → outcome `'miss'` (quest triggered) or `'incorrect'` (no quest)
- `autoKick()` → outcome `'autokick'`, elapsed 7000ms — `handleMiss` skips to prevent double-count
- Guests skipped silently (no `sparkwright_active` in localStorage)

**Rolling windows:**
- `responseTimes` — last 20 correct-answer response times (`MAX_TIMES = 20`)
- `recentAttempts` — last 10 attempts, all outcomes (`RECENT_ATTEMPTS_MAX = 10`)

**Fluency thresholds:** ≤3000ms → fluent, ≤6000ms → almost, else → needs (`FLUENCY_MS_F`, `WORKING_MS_F`)

**Test checklist (pending):**
- A. Correct answer → `correct` increments, `responseTimes` gains entry, `fluencyCounts` increments correctly
- B. Wrong answer (2nd attempt, mul/div with remed on) → `incorrect` + `questTriggered` increment
- C. Wrong answer (add/sub or remed off) → `incorrect` increments, `questTriggered` does NOT
- D. Auto-kick (wait 7s) → `incorrect` increments, `responseTimes` gains 7000, no double-count
- E. Guest (no profile) → no `mathflash_facts` entry written at all
- F. 21+ answers for same fact → `responseTimes` stays capped at 20 entries

---

### Math Flash Header Bar (session F)
Fixed 48px header at top of every Math Flash screen.
- Left: ← Sparkwright (link to `../../`) | Math Flash label
- Right: profile chip (emoji + username, or 👤 Guest)
- Reads `sparkwright_profiles` + `sparkwright_active` from localStorage
- `body { padding-top: 48px }` pushes game content below header

---

## Per-Fact Tracking

### Rolling Window of 20 Response Times
**Decision:** `responseTimes` stores only the last 20 correct-answer response times. Oldest entries drop off when the array exceeds 20.

**Why:** An all-time record would skew variance calculations toward old data. A student who struggled with a fact two months ago but has been answering in 1.2s consistently for the past two weeks should look stable — not penalized by old high-variance entries. 20 is enough to compute meaningful variance while staying recent.

**Constant:** `MAX_TIMES = 20` (defined at the top of the per-fact tracking section).

---

### Auto-Kick Recorded as 7000ms, Not Excluded
**Decision:** When a student times out (7 seconds, no answer), the attempt is recorded in `responseTimes` as `7000` — not skipped.

**Why:** A timeout is real data. It means the student had no answer after 7 full seconds. Recording it as 7000ms correctly inflates variance for struggling facts and lowers the chance those facts will be flagged as mastered. Excluding it would make the record incomplete and artificially tidy.

---

### `_autoKicking` Flag to Prevent Double-Recording
**Decision:** A boolean `G._autoKicking` is set to `true` inside `autoKick()` and checked inside `handleMiss()`.

**Why:** `autoKick()` records the attempt *before* calling `handleMiss()`. Without the flag, `handleMiss()` would record a second attempt for the same question. The flag tells `handleMiss()` to skip its own recording step when it was called by an auto-kick. It resets to `false` at the end of `handleMiss()`.

---

### Two Miss Outcomes: `'miss'` vs `'incorrect'`
**Decision:** Wrong answers are stored as either `'miss'` (quest triggered) or `'incorrect'` (no quest).

**Why:** These are pedagogically different. A `'miss'` means the student got a full Practice Quest remediation sequence. An `'incorrect'` means they got a shake + clear and tried again, or the game mode didn't support quests (add/sub without remed). Keeping them distinct preserves the ability to later ask "how many times did this fact actually trigger a full quest?" vs "how many times was it answered wrong?"

---

### `qStartTime` Set in All Modes
**Decision:** `G.qStartTime` is set to `Date.now()` when a question is displayed, in all game modes — not just Per-Question Timer mode.

**Why:** Per-fact response time tracking was added after the timer modes were designed. The cleanest way to record elapsed time for any correct answer is to always capture when the question appeared. In non-timer modes, the student is not under a countdown, but their actual response time is still worth recording for future variance/mastery use. This was a bug in v55 that was caught and fixed in Session H.

---

## Timing & Fluency

### 50ms Interval for Per-Question Timer Bar
**Decision:** The per-question countdown bar updates every 50ms.

**Why:** A 1000ms (1s) interval would produce a jerky bar. 50ms gives 20 updates per second — smooth enough to look animated without meaningfully taxing performance. The bar is purely visual; the actual elapsed time is always computed from `Date.now() - G.qStartTime`, not accumulated from the interval ticks.

---

### Timer Resume Calculation
**Decision:** When the game resumes from pause, `qStartTime` is recalculated as `Date.now() - ((7 - G.perQSecsLeft) * 1000)`.

**Why:** Storing a raw `Date.now()` start time and pausing doesn't work — if the student pauses for 30 seconds, the elapsed time calculation would show 30+ seconds when they resume. The fix is to reconstruct `qStartTime` as if the question had been shown exactly `(7 - secsLeft)` seconds ago from *now* — so the remaining time is exactly what it was when they paused.

---

### Fluency Thresholds as Named Constants
**Decision:** `FLUENCY_MS_F = 3000` and `WORKING_MS_F = 6000` are named constants at the top of the tracking section.

**Why:** These thresholds appear in multiple places (recording, grading, future variance logic). Hardcoding `3000` inline would make them invisible and easy to accidentally change in one place but not another. Constants make it easy to adjust both thresholds in one place if the pedagogy decisions change.

---

## Pedagogy-Driven Code Decisions

### Guests Silently Skipped (No Error, No Prompt)
**Decision:** If no `sparkwright_active` value exists in localStorage, `recordFactAttempt()` returns immediately without writing anything.

**Why:** Guests should be able to play freely without friction. A prompt or alert would interrupt the game. The tradeoff is that guest play produces no data — this is intentional and consistent with the product's data-belongs-to-the-user philosophy. The UX question of whether to nudge guests toward creating a profile is a design discussion (Item 105), not a tracking decision.

---

### Variance Calculated as Standard Deviation, Not Raw Variance
**Decision:** `calcResponseSD(times)` returns the population standard deviation in ms, not variance (ms²) or coefficient of variation (CV).

**Why:** Standard deviation is in the same unit as the response times themselves (milliseconds), making the threshold constant `VARIANCE_STABLE_MS` intuitive — "1000" means "responses that swing by more than about a second." Raw variance (ms²) would produce large opaque numbers. CV (SD/mean) normalizes for student speed, but introduces complexity and requires guarding against division by zero. SD in ms is the simplest interpretable form for a threshold that will need tuning.

**Tradeoff:** SD doesn't normalize for a student's average speed — a student who answers in ~1s has less "room" for variance than one who answers in ~3s. This is acceptable for now; the threshold is explicitly TBD and will be tuned with real data. If normalization becomes important, switching to CV is a one-function change.

**Constants:** `VARIANCE_MIN_TIMES = 5` (minimum entries before variance is meaningful), `VARIANCE_STABLE_MS = 1000` (initial SD threshold in ms — tune with use). Both are named constants at the top of the per-fact tracking section.

---

### `isStableVariance` Returns `false` for Insufficient Data
**Decision:** When `responseTimes` has fewer than `VARIANCE_MIN_TIMES` entries, `isStableVariance()` returns `false` (not `null`, not `true`).

**Why:** The mastery criterion requires low variance. If there isn't enough data to compute variance, we cannot confirm stability — so the conservative answer is "not yet stable." Returning `null` would require every caller to handle a third state. Returning `true` would incorrectly allow mastery on facts with very little data. `false` keeps the mastery gate conservative by default.

---

### `recentAttempts` Is Separate from `responseTimes`
**Decision:** The mastery check uses a separate `recentAttempts` rolling window (last 10 attempts, each `{ms, correct, date}`), not `responseTimes`.

**Why:** `responseTimes` only stores correct answers and autokicks — wrong answers (`'miss'`, `'incorrect'`) are never pushed to it. If the mastery check used `responseTimes`, recent misses would be invisible, and a student with a recent wrong answer could still pass the 4/5 gate. `recentAttempts` records every outcome, so misses count as failures in the mastery window. The two arrays serve different purposes: `responseTimes` feeds variance (needs only times from actual answers), `recentAttempts` feeds mastery (needs full outcome history including misses).

---

### `recentAttempts` Window Is 10, Mastery Gate Uses Last 5
**Decision:** `RECENT_ATTEMPTS_MAX = 10` (window size), `MASTERY_WINDOW = 5` (gate looks at last 5).

**Why:** The mastery criterion needs the last 5 attempts. Storing 10 gives headroom — the stats page, print report, and challenge facts system (Items 88, 89, 109) will likely want to display recent attempt history beyond just the last 5. 10 is enough history without meaningfully growing localStorage size.

---

### Mastery Is De-Certifiable
**Decision:** `checkMastery(rec)` runs after every attempt. If it returns `false` for a previously mastered fact, `mastered` resets to `false` and `masteredDate` clears.

**Why:** A student who was mastered but then starts struggling should lose the flag. This is consistent with how Reflex Math treats mastery (they explicitly de-certify facts if performance degrades). A mastery flag that can never be revoked would gradually lose meaning. At the same time, de-certification is currently internal-only — no UI shows `mastered` yet — so students won't feel punished by a visible change. When the stats page is built (Item 89), the UX question of how to display a "fading" or "at risk" mastery state can be designed then.

---

### Mastery Check Uses the 2-Distinct-Dates Rule on `recentAttempts`, Not `firstSeen`/`lastSeen`
**Decision:** The "2 separate sessions" criterion checks for 2 distinct date values within the last 5 `recentAttempts` entries, not by comparing `firstSeen` to `lastSeen`.

**Why:** `firstSeen` ≠ `lastSeen` only proves the fact was practiced on 2 different days ever — not that the most recent performance spans 2 sessions. A student could have 20 attempts all from today, plus one attempt months ago (setting `firstSeen`), and the weak check would pass even though all recent attempts are from one session. The 2-session requirement exists specifically to prevent "one good day" mastery — using per-attempt dates in `recentAttempts` is the only way to enforce it correctly.

---

### Fluency Tracking Runs Silently in All Modes
**Decision:** Fluency data (`fluencyCounts`) is recorded in all game modes, even though it's only *displayed* in Per-Question Timer mode.

**Why:** The per-question timer is the only mode that shows real-time fluency feedback. But the underlying data — whether a correct answer was fast or slow — is meaningful in any mode. Capturing it silently preserves the option to surface it later (stats page, print report, mastery calculation) without requiring a code change.

---
