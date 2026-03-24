# Math Flash — Code Rationale
*A running log of non-obvious code decisions: what was chosen, why, and what alternatives were considered.*
*Updated at the end of any session where a significant architectural or design-in-code decision is made.*

---

## How to Use This File

This file is for answering the question: "Why does the code look like this?"

It is **not** for documenting pedagogy or product decisions — those live in the MPF and RP files. This file is specifically for code architecture choices that a developer (or future Claude session) might look at and wonder about.

**Rule of thumb for what belongs here:** If you made a choice between two or more reasonable approaches, and the reason isn't obvious from reading the code, log it here.

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

### Fluency Tracking Runs Silently in All Modes
**Decision:** Fluency data (`fluencyCounts`) is recorded in all game modes, even though it's only *displayed* in Per-Question Timer mode.

**Why:** The per-question timer is the only mode that shows real-time fluency feedback. But the underlying data — whether a correct answer was fast or slow — is meaningful in any mode. Capturing it silently preserves the option to surface it later (stats page, print report, mastery calculation) without requiring a code change.

---
