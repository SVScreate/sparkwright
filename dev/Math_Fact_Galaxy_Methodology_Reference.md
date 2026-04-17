# Math Fact Galaxy — Methodology Reference
*How the game makes decisions and why*
*For use during beta testing, teacher onboarding, and FAQ drafting*
*Created: Session AN — April 16, 2026*
*Maintained by Spark — update after each session that changes design decisions*

---

## How to Use This Document

This is a living reference. It answers two questions:
1. **Why does the game do that?** — for Kimberly during testing, and for teachers/parents/ed therapists evaluating the product
2. **What am I looking at?** — when something happens during a session and you want to know whether it's working as designed, working as a bug, or still being tuned

It is organized in sections you can jump to independently. Start anywhere.

---

## Part 1 — Core Philosophy

### What is Math Fact Galaxy built on?

Three research-grounded commitments that shape every design decision:

**1. Error is instructional — handled correctly.**
Every major math fact platform responds to a wrong answer the same way: show the correct answer, log the miss, move on. Math Fact Galaxy responds to a wrong answer in the moment, before moving on. This is Star Quest. It is not punishment — it is structured in-moment remediation. The research standard for typically-developing learners is error correction, not errorless learning. The game is designed around what happens when the student fails, not just when they succeed.

**2. Fluency is a measurable standard, not a feeling.**
A fact is fluent when the student produces it automatically — without counting, reconstructing, or deriving — within a specific response time. The 3-second default threshold comes from the research literature (Kling & Bay-Williams, 2015, *Teaching Children Mathematics*, 21(9) — verified). Fluency is not binary: the game tracks the full range of performance (too slow, approaching, fluent, mastered) because that range contains real instructional information.

**3. Cognitive load matters.**
A round that overwhelms the student with too many struggling facts produces less learning, not more. The game limits challenge fact density per round (the "Challenge Level" setting) because effective practice includes interleaving known facts among challenging ones. This is not coddling — it is how retention works. A student who finishes a round feeling capable will return. A student who finishes defeated may not.

### What this game is NOT

- It is not a curriculum. It is a fluency tool. It does not teach operations from scratch.
- It is not a passive drill. It responds to what the student is doing in real time.
- It is not a reward machine. Stars and constellations reflect real performance data, not effort or time spent.
- It is not XtraMath. The comparison is worth having directly: XtraMath shows a correct answer, logs the miss, and moves on. Math Fact Galaxy stays with the student at the moment of struggle. That is a fundamentally different pedagogical stance.

---

## Part 2 — The Timer

### What is the timer measuring?

The timer measures **response time** — how long it takes the student to produce an answer from the moment the fact appears on screen.

Response times are recorded in milliseconds to the database for every attempt. This raw data is never discarded when settings change.

### What is the fluency threshold?

The **fluency threshold** is the response time standard against which practice performance is graded. Default: **3 seconds.**

- Respond within 3s → grades as **Fluent** (the response met the automaticity standard)
- Respond correctly but slower than 3s → grades as **Almost** (correct retrieval, not yet automatic)
- Respond incorrectly → grades as **Needs Practice**

The threshold is adjustable in Settings. Common accommodations:
- Students with ADHD or processing speed differences: 4–5s is a reasonable starting point
- Students with learning disabilities affecting processing: 5–6s or higher
- Advanced students working on extended facts: threshold can be tightened

**Important:** When the threshold changes, all prior response time data is recalculated against the new standard. A student who was "Almost" at 3s may become "Fluent" at 5s — their practice times haven't changed, just the lens. The game shows a notice before applying the change.

### What does the timer bar show?

The timer bar in **Build My Constellation** counts down from the **fluency threshold** — so the bar runs exactly as long as the student has to respond before the fact is auto-kicked. If threshold is 3s, the bar runs 3s.

This was a deliberate design decision: the visible countdown should represent the standard being measured. A bar that runs 7 seconds when the student is graded at 3 seconds sends a mixed signal.

### What is the autokick?

The **autokick** is the maximum wait time before the game moves on from a fact the student has not answered. In practice mode contexts this can be longer than the fluency threshold — it gives the student a moment to attempt retrieval even after the fluency window has passed. In BMC, the autokick matches the fluency threshold: no answer within threshold = the timer expires and the game moves on.

### Beta testing: what to watch

| Observation | What it might mean |
|---|---|
| Timer bar feels slow | Check threshold setting — it may be set higher than expected |
| Timer bar and grading feel out of sync | Bug — timer should match threshold exactly |
| Student clearly knew the answer but the timer kicked | Threshold may be set too tight for this student |
| Student taking much longer than the bar but still getting credit | Timer and grading logic may be disconnected — flag as bug |

---

## Part 3 — The Tier System

### What are the tiers?

Every fact in a student's constellation lives in one of five states:

| Tier | Visual | Meaning |
|---|---|---|
| **Unpracticed** | Dim ember (barely visible) | No attempts recorded yet |
| **Needs Practice** | Purple glow | Incorrect responses, or not yet meeting threshold consistently |
| **Almost** | Blue glow | Responding correctly but not yet within the fluency threshold |
| **Fluent** | Amber glow | Meeting the threshold consistently — not yet mastered |
| **Mastered** | Gold star (Sparkwright ★) | Meets full mastery criteria across multiple sessions |

### How does a fact move between tiers?

Tiers are calculated from raw response time data. The game looks at a rolling window of recent attempts and calculates:
- **Accuracy** (correct/incorrect)
- **Speed** (within threshold or not)
- **Variance** (consistency — a fact answered sometimes fast, sometimes slow is less stable than one answered reliably fast)

A fact moves up when performance meets the tier threshold. A fact can move down if performance degrades. The visual star stays — earned tiers are shown honestly. Internal freshness flags (not visible to the student) gate forward progress if a fact hasn't been practiced recently.

### What counts toward the constellation?

All timed practice attempts in BMC count toward the constellation, regardless of mode or Challenge Intensity setting. Star Scan results (Ongoing, Final) do NOT affect the constellation — they are diagnostic snapshots only. The Beginning Star Scan seeds initial tier estimates during onboarding.

### Beta testing: what to watch

| Observation | What it might mean |
|---|---|
| A fact the student clearly knows is showing as Needs Practice | May not have enough attempts yet, or early attempts were slow while learning the interface |
| A fact is not moving up despite correct answers | Check if the student is meeting the speed threshold — correct but slow stays at Almost |
| Fact tiers look wrong after a threshold change | Expected — recalculation on threshold change is by design; show the notice |
| Constellation shows data from the wrong user | User context bug — critical, flag immediately |

---

## Part 4 — Mastery

### When does a fact earn its star?

Mastery (the gold star) requires meeting all of these criteria:

- **3 qualifying sessions minimum** — the student has practiced the fact in at least 3 separate sessions
- **3 different calendar dates** — sessions must be spread across at least 3 different days
- **≥3 timed attempts per session** to count as a qualifying session
- **Fluent in recent practice** — the fact must have produced a fluent response within a recent window (N days — currently being tuned during beta)

### Why spread across days?

Single-session performance is an unreliable mastery signal. A student can drill a fact to fluency in one sitting and lose it within 48 hours. Requiring multiple calendar dates builds in a rudimentary spacing requirement — the student has to retrieve the fact successfully on separate occasions, which is a much stronger retention signal than same-day performance.

This is grounded in the spacing effect research (Cepeda et al., 2006 — flagged for verification before use in copy; the principle is solid).

### Why 3 sessions and not more (or fewer)?

3 is the current beta testing baseline. It will be tuned. The goal is a threshold that:
- Is achievable for a motivated student within a week of regular practice
- Is high enough that a lucky one-session run doesn't grant mastery prematurely
- Is low enough that students see stars lighting up at a pace that feels rewarding

If beta testing shows students are mastering facts too quickly or stars feel unearned, raise to 4 or 5. If stars feel impossibly out of reach and students disengage, lower to 2. The data model supports any value — it is a tunable parameter.

### Does a mastered fact ever get taken away?

The visual star does not disappear. Earned mastery is kept. What changes internally: if a mastered fact goes unpracticed for an extended period, it receives an internal **freshness flag** that gates forward progress (badges, certificates, etc.) until fresh data is recorded. The flag is not visible to the student — the star stays. Smart Practice mode includes a small maintenance sprinkle of mastered facts in every round to keep timestamps fresh and clear flags organically.

### Beta testing: what to watch

| Observation | What it might mean |
|---|---|
| Stars lighting up after only one session | Mastery criteria may not be enforcing the calendar-date spread — flag as bug |
| Student has many fluent facts but no stars yet | Normal if the student hasn't reached the session count threshold yet — not a bug |
| Star lights up and student says "I don't know that one" | Star Quest override during Star Quest may have recorded fluent response under unusual conditions; monitor |

---

## Part 5 — Star Quest

### What is Star Quest?

Star Quest is the game's response to a student struggling with a specific fact. It is triggered when the student answers the **same fact incorrectly twice** in a single round.

When it triggers:
- The round pauses
- The timer pauses
- The student exits the main round and enters a structured 3-step sequence: **Find It → mini-game (Falling Facts or similar) → Prove It**
- After completing all three steps, the student returns to the main round exactly where they left off
- The fact that triggered Star Quest is removed from the remaining round pool

### Why Star Quest instead of just showing the answer?

Every other platform shows the correct answer and moves on. Research on error correction for typically-developing learners (not ASD/IDD populations, where errorless learning is appropriate) supports structured in-moment remediation over passive correction. Drilling past a missed fact and seeing it at the end of a round summary does not produce the same retention as actively retrieving it in a structured sequence at the moment of error.

Star Quest is the product's core differentiator. It is not a mini-game feature. It is the entire pedagogical stance of the product made interactive.

### Does Star Quest record to the constellation?

Star Quest attempts are recorded. However, performance under Star Quest conditions is tagged and weighted differently from standard round performance — a correct answer during Prove It is not the same signal as fluent retrieval under normal round pressure. The system tracks source context.

### Can Star Quest be turned off?

Yes. There is a checkbox on the BMC setup card: **"Include Star Quest (recommended)"** — checked by default. The student (or teacher) can uncheck it for any given session.

**When turning Star Quest off makes sense:**
- A fatigued student who knows they'll hit Star Quest multiple times and may not start the round at all
- A warm-up or exploratory session
- A student who just completed a full Star Quest session and needs a change of pace

**What does not change when Star Quest is off:** constellation data is recorded normally. The only thing that changes is whether Star Quest triggers on the second wrong answer.

**What a teacher should watch:** if a student is turning Star Quest off every session, that is useful data. It may mean Star Quest is too frequent (the student has too many struggling facts and is hitting it constantly), or it may mean the student is avoiding the challenge. Either is worth a conversation.

### Once Star Quest starts, can the student leave?

No. Once Star Quest triggers mid-round, the student completes it before returning. The toggle at session start is the only point of control. This is by design — partial Star Quest creates ambiguous data and teaches the student that they can escape at the hard part.

### Beta testing: what to watch

| Observation | What it might mean |
|---|---|
| Star Quest triggering on every other fact | Student has many Needs Practice facts; consider Gentle mode to reduce challenge density |
| Student completing Star Quest correctly but same fact missing again immediately | Normal — one Star Quest pass doesn't guarantee retention; fact will return in future rounds |
| Star Quest not triggering after 2 wrong answers | Bug — flag |
| Timer running during Star Quest | Bug — timer should be fully paused during Star Quest |
| Student clearly disengaging when Star Quest starts | Watch for patterns — is it always the same mini-game? same type of fact? fatigue? |

---

## Part 6 — Round Composition and Challenge Intensity

### How does the game choose which facts appear in a round?

In **All Facts mode**, facts are drawn from the full pool of facts within the selected operation and range. Without Challenge Intensity applied, this is a shuffle — the student could hit all their hardest facts in a row.

Challenge Intensity governs how many challenging facts (Needs Practice + Unpracticed) appear per round, and fills the rest with facts the student is closer to mastering.

### What is the "Challenge Level" setting?

**Challenge Level** (Challenge Intensity) is a student-facing daily choice on the BMC setup card. It controls the ratio of challenging facts to fill facts in a round — not the difficulty of the math problems themselves.

| Setting | Challenge facts per round | Fill content | Round length |
|---|---|---|---|
| **Gentle** | 2–3 | Fluent → Almost → Mastered sprinkle | Shortens round if fill content is thin |
| **Balanced** | 4–6 (default) | Fluent → Almost → Mastered sprinkle | Minor shortening if needed |
| **Intensive** | Up to 8–10 | Still ~30% Fluent/Almost interleaved | Holds to round length setting |

**The fill priority order matters:**
1. Fluent (amber) — highest-leverage fill: already meets threshold, needs more sessions for mastery
2. Almost (blue) — responding correctly, needs speed work
3. Mastered (gold) — small maintenance sprinkle to keep timestamps fresh

### Why not just drill only the hard facts?

The research on interspersal — embedding challenging items among known items — shows that this produces better retention of the challenging items, not worse. A student who works through a round that is 100% struggle facts is experiencing a different cognitive state than a student who encounters challenges in a context of success. The former is more likely to produce frustration, avoidance, and poorer encoding. The latter is more likely to produce effortful retrieval in a stable emotional context — which is the condition for consolidation.

Intensive mode still keeps ~30% known facts interleaved for this reason. Even a student who wants to push hard benefits from the pacing structure.

### What happens when a new student has only a few facts?

When the student's available fact pool is smaller than the requested round length:

1. **The game uses both orientations of each fact first.** 3×4 and 4×3 are distinct retrieval demands — not the same fact. Both are presented before any repeat is considered.
2. **After both orientations are exhausted, the round shortens.** A 6-question round for a student with 3 facts (both orientations each) is the correct and intended outcome. The game does not pad the round by repeating the same fact a third time.
3. **If the pool runs out entirely**, the game ends the round cleanly with a results screen.

This is especially important for new students: their first rounds may be short. That is a feature, not a bug.

### Does Challenge Intensity apply to Smart Practice mode?

Yes. Smart Practice still handles fact prioritization automatically (reading the constellation and building the round intelligently). Challenge Intensity governs the ratio within that prioritization. A student in Smart Practice + Gentle gets a constellation-informed round with a gentle challenge density. Smart Practice + Intensive gets a constellation-informed round weighted toward challenge.

### Beta testing: what to watch

| Observation | What it might mean |
|---|---|
| Student hitting the same hard fact over and over | Challenge Intensity too high for this student's constellation state; try Gentle |
| Round feels easy and not challenging enough | Student may have a lot of Fluent/Almost facts; Intensive may be appropriate |
| Round ends early unexpectedly | Thin fact pool behavior — correct if student is new; check round settings if not |
| Same fact appearing 3 times in one round | Orientation logic may not be preventing third repeat — flag as bug |

---

## Part 7 — Orientation

### What does orientation mean?

For every math operation, a fact has two orientations that represent distinct retrieval demands:

- Multiplication: **3 × 4 = ?** and **4 × 3 = ?**
- Division: **28 ÷ 4 = ?** and **28 ÷ 7 = ?**
- Addition: **3 + 4 = ?** and **4 + 3 = ?**
- Subtraction: **12 − 4 = ?** and **12 − 8 = ?**

Students do not automatically transfer fluency between orientations. A student who knows 3 × 4 instantly may hesitate on 4 × 3. This is not always the case — commutativity is often understood at a conceptual level — but fluency research and clinical practice both show that orientation-specific retrieval is a real phenomenon, especially for division and subtraction.

### How does the game handle orientation?

- Both orientations of a fact are tracked separately in the constellation
- Full Star Scan tests both orientations by design (exhaustive = exhaustive)
- Quick Start Scan tests one orientation per fact (table-level picture, not per-fact)
- In rounds, both orientations are eligible to appear independently
- For thin-pool students: both orientations are exhausted before any repeat

### What about the multiplication grid?

The 12×12 multiplication grid in My Constellation shows cells for every fact in the standard range. Because of commutativity, 3×4 and 4×3 share a visual position on the grid — but the underlying data tracks them separately. The visual cell reflects the lower of the two orientation tiers to avoid overstating mastery.

### Beta testing: what to watch

| Observation | What it might mean |
|---|---|
| Student knows "7×8" instantly but hesitates on "8×7" | Orientation-specific retrieval — normal and expected; both need practice |
| Grid shows a fact as Fluent but student is slow on one orientation | The grid may be averaging or taking the higher tier — check display logic |

---

## Part 8 — Star Scan

### What is Star Scan?

Star Scan is the game's assessment instrument. It tests facts systematically — one attempt per fact, no retry, no Star Quest — and records response times. Results classify each fact as **Mastered** or **Needs Practice** (two-bucket system; no in-between during assessment).

Star Scan data is stored separately from practice data. Assessment performance does NOT affect the practice constellation — a student cannot test their way to mastery. These are parallel, non-contaminating data streams.

### Quick Start Scan vs. Full Star Scan

| | Quick Start Scan | Full Star Scan |
|---|---|---|
| **Questions** | 36 questions | All facts in scope |
| **Scope** | 3 facts per table (low / mid / upper range) | Every fact, both orientations |
| **Output** | Table-level picture — "which tables to target" | Per-fact picture |
| **Access** | Free — onboarding | Paid tier |
| **Sessions** | Single session | Multi-session (3 for multiplication) |
| **Constellation effect** | Seeds ghost constellation (onboarding only) | Stored as record only |

### Quick Start Fact Selection — Multiplication Standard Range (×1–×12)

36 facts, 3 per table. For **pattern tables** (×1, ×2, ×5, ×10), the three picks are range-coverage only — these tables have no genuinely harder facts. Easy/medium/hard labels reflect within-table difficulty gradient for non-anchor tables; for anchor tables they reflect low/mid/upper range.

| Table | Easy / Low | Medium / Mid | Hard / Upper | Notes |
|-------|-----------|--------------|--------------|-------|
| ×1 | 1×3 (=3) | 1×7 (=7) | 1×12 (=12) | Range coverage — identity property; all are equally easy |
| ×2 | 2×3 (=6) | 2×5 (=10) | 2×11 (=22) | Doubles range check — upper is not genuinely hard |
| ×3 | 3×5 (=15) | 3×7 (=21) | 3×9 (=27) | 3×7 and 3×9 are genuinely commonly delayed |
| ×4 | 4×3 (=12) | 4×9 (=36) | 4×8 (=32) | 4×8=32 is one of the most frequently missed ×4 facts |
| ×5 | 5×4 (=20) | 5×8 (=40) | 5×12 (=60) | Pattern table; range coverage — all are easy with ×5 rule |
| ×6 | 6×2 (=12) | 6×4 (=24) | 6×7 (=42) | 6×7=42 is one of the most commonly missed facts overall |
| ×7 | 7×2 (=14) | 7×4 (=28) | 7×8 (=56) | Hardest table; 7×8=56 is widely the hardest single fact |
| ×8 | 8×2 (=16) | 8×6 (=48) | 8×9 (=72) | All three are genuinely hard — ×8 has no easy facts after ×2 |
| ×9 | 9×2 (=18) | 9×6 (=54) | 9×7 (=63) | Tests whether ×9 rule is automatic; 9×7=63 without it is hard |
| ×10 | 10×3 (=30) | 10×6 (=60) | 10×9 (=90) | Pattern table; range coverage — all are easy with ×10 rule |
| ×11 | 11×4 (=44) | 11×11 (=121) | 11×12 (=132) | Pattern through ×10; only ×11 and ×12 break the digit-repeat rule |
| ×12 | 12×2 (=24) | 12×6 (=72) | 12×8 (=96) | Upper facts commonly missed; 12×8=96 frequently delayed |

**All 36 cross-products are unique** — no commutative duplicates (verified). Factor distribution: factors 3, 4, 6, 7, 8, 9 each appear in exactly 7 facts; factor 2 appears in 8 (unavoidable — anchor for hard table "easy" picks); factors 1 and 10 appear in 3 each.

**3-tier seeding from Quick Start results:**

| Score on 3 facts for a table | Tier seeded for all untested facts in that table |
|---|---|
| 3/3 within threshold | Amber — fluent |
| 2/3 within threshold | Blue — almost |
| 1/3 or 0/3 | Purple — needs practice |

Tested facts receive their actual response time data. Untested facts in the same table receive the seeded tier with a `source: quick-start-inferred` flag. Real practice data replaces the inferred tier fact by fact as the student builds. Inferred data is never used to calculate mastery — only measured data qualifies.

### When should Star Scan be run?

**Beginning Star Scan (at account creation):**
The onboarding assessment. Seeds the student's initial constellation tier estimates. Quick Start is the free path — gives a table-level picture and lights up anchor facts in the constellation. Full Star Scan (paid) gives a per-fact baseline.

**Ongoing Star Scan (teacher-initiated):**
Run anytime the teacher wants a current snapshot — before a tutoring session begins, after a break, to check progress on a specific table. Results go to Star Scan Records only; do not affect the constellation.

**Final Star Scan:**
Appears automatically when all facts for an operation reach mastered. Same instrument. Functions as the certification basis — the result that prints as the completion certificate.

### What does the timer do during Star Scan?

Star Scan timer:
- Counts down from the fluency threshold (same standard as practice)
- Hard stop at threshold — no extra time
- **Neutral color only** (white/silver bar) — no tier colors during the scan; tier colors carry meaning in this product and should not appear until results are shown
- No gold flash on unanswered facts — gold means mastery; a skipped fact has not earned that signal

### Can a student pause during Star Scan?

Yes — between facts only, never mid-fact. A mid-fact pause gives extra thinking time and contaminates the response time data. Between-fact pauses are legitimate anxiety management and produce cleaner data (the student completes the fact in a composed state rather than under distress).

### Beta testing: what to watch

| Observation | What it might mean |
|---|---|
| Star Scan results don't match practice performance | Expected — Star Scan is a probe, not a practice session; some divergence is normal |
| Student performing much better on Star Scan than practice | Practice Star Quest may be inflating confidence; check Star Quest data |
| Timer bar showing tier colors during scan | Bug — bar should be neutral |
| Star Scan data appearing in constellation | Bug — critical; Star Scan (except Beginning) must not write to constellation |
| Student skipped a fact and it showed a gold flash | Bug — unanswered facts should not flash gold |

---

## Part 9 — Data and Privacy

### Where does student data live?

All data is stored in the browser's **localStorage** on the device where the game is played. Nothing is transmitted to a server. No account is required for the core game experience.

**Correct positioning language:** *"Your data stays on your device by default."*
Do not use "you own your data" — technically accurate now but creates exposure if server accounts are ever added.

### What data is stored?

Per student (identified by username, not real name):
- Practice history: every attempt, response time in milliseconds, fact, orientation, mode, session ID, timestamp
- Star Scan records: each scan, date, threshold used at time of scan, results per fact
- Constellation tiers: current tier per fact, based on calculated summary of practice history
- Settings: fluency threshold, operation preferences, round defaults
- Session count and calendar dates (for mastery tracking)

### What happens if the student clears their browser or switches devices?

All data is lost unless a backup was downloaded first. The game prompts a quiet backup reminder every 10 sessions. The backup is a JSON file named per student that can be restored later. This is a known limitation of the local-first architecture — it is a deliberate values choice (no server, no account required) with a real trade-off (data portability requires manual backup).

### What about COPPA?

Because the game uses localStorage exclusively — no server, no data transmission — COPPA is not triggered by the current architecture. If server accounts are ever added, COPPA assessment with Lex is a required step before build. Flagged in the pre-launch legal checklist.

---

## Part 10 — Common Questions (FAQ Source Material)

These are the questions teachers, parents, and ed therapists are most likely to ask. Answers here are draft source material for the FAQ page — not final copy.

---

**Q: Is this timed? My child gets anxious about timed tests.**

A: Yes, the game uses a timer — and that is intentional and research-grounded. The difference is what the timer *does*. In Math Fact Galaxy, the timer measures fluency for the constellation. It does not generate a score, appear on a report card, or create public pressure. The student sees a countdown bar; they do not see a clock face, a number counting down, or a comparison to other students. If the student needs more time, the fluency threshold in Settings can be adjusted — a student practicing at 5 seconds is still building toward automaticity, just at an appropriate pace for their processing speed.

**Q: What happens when my child gets a problem wrong?**

A: The first wrong answer: the problem returns later in the round. The second wrong answer on the same fact in the same round: Star Quest activates. The round pauses, and the student does a short structured practice sequence on exactly that fact — Find It, a mini-game, Prove It — before returning to the round. This is the game's core design. No other math fact platform handles the moment of failure this way.

**Q: How does the game know what facts to practice?**

A: The game reads the student's constellation — their personal record of which facts are mastered, which are fluent, which are approaching fluency, and which still need work. It builds each round using this information, mixing challenging facts with facts the student is close to mastering. The ratio depends on the "Challenge Level" setting the student chooses at the start of each session.

**Q: My child blew through it the first time and got everything right. Does the constellation reflect that?**

A: Partially. One session of correct answers moves facts from Unpracticed toward the Needs Practice / Almost / Fluent range depending on speed. But no fact earns a star (Mastered) after a single session — mastery requires at least 3 sessions across 3 different calendar days. This is by design: single-session performance is an unreliable mastery signal. The constellation reflects durable learning, not a good day.

**Q: Can I adjust the game for a student with an IEP accommodation for extended time?**

A: Yes. The fluency threshold in Settings controls both the grading standard and the timer display. Set it to the student's accommodation — 5 seconds, 6 seconds, whatever is documented. The constellation will reflect the student's performance against their threshold, not against the default 3s standard. The game does not require a specific threshold.

**Q: How is this different from XtraMath?**

A: XtraMath shows a correct answer when the student misses and moves on. Math Fact Galaxy stops the round and practices the missed fact immediately in a structured sequence. XtraMath's fluency threshold is set by a teacher across five static options; Math Fact Galaxy's threshold is continuously adjustable. XtraMath's data lives on a server; Math Fact Galaxy's data stays on your device. Both use timed practice. The fundamental difference is what happens at the moment of failure.

**Q: What does "Almost" mean on the constellation?**

A: Almost (blue) means the student is responding correctly — they know the fact — but not yet within the fluency threshold. They're retrieving it, not recalling it automatically. Almost is not a problem; it's a stage. With more practice, Almost facts move toward Fluent.

**Q: My student is getting a lot of the same hard facts over and over. Is something wrong?**

A: Not necessarily a bug — it may be a settings mismatch. If the student has many Needs Practice facts and the "Challenge Level" is set to Balanced or Intensive, the game will pull 4–10 challenge facts per round. Try Gentle, which limits challenge facts to 2–3 per round and fills the rest with facts the student is closer to mastering. Rounds should feel mostly achievable with a few hard ones, not mostly hard.

**Q: Can I run this without a student account?**

A: The core game works without creating a user profile — you can practice without saving data. Creating a user profile (a username, no password, no email) turns on constellation tracking and saves history. It takes 10 seconds and requires no personal information. No account in the school/corporate sense is ever required.

**Q: Does the game work offline?**

A: Yes. The game runs entirely in the browser from a local file or web address. No internet connection is needed after the initial load. Data is stored on the device.

**Q: How do I know if a student has actually mastered a fact vs. just performed well once?**

A: The star (Mastered tier) requires at least 3 qualifying sessions across 3 different calendar dates with fluent performance in recent practice. A single good session will not light a star. If a star is lit, the student has demonstrated fluent recall on multiple occasions across multiple days — that is a meaningful threshold, not a vanity metric.

**Q: Should I run Star Scan before or after practice sessions?**

A: Ongoing Star Scans are typically most useful as a snapshot before a new phase of instruction, after a break, or to confirm progress before a Final Star Scan. Running it immediately after a practice session (when facts are warm) will overstate baseline performance — the student's results will reflect recency, not retention. A small gap (hours, or the following day) gives cleaner data.

---

## Part 11 — Beta Testing Quick Reference

### What to log during every session

- **Student name / profile** (to check correct user context is loading)
- **Operation and range being practiced**
- **Challenge Level setting** (Gentle / Balanced / Intensive)
- **Star Quest on or off?**
- **Round length chosen**
- **Anything unexpected** — crashes, wrong data, behavior that doesn't match the spec

### Green flags (things working as designed)

- Timer bar matches the student's threshold setting
- Star Quest triggers on second wrong answer of the same fact in a round
- Star Quest pauses the timer and round
- After Star Quest: student returns to round, fact removed from remaining pool
- Challenge facts appear 2–10 times per round depending on Challenge Level
- New student sees short rounds until fact pool grows
- Both orientations of a fact appear before any repeat
- Stars (Mastered) only light up after multiple sessions across multiple days

### Red flags (log and flag immediately)

- **Any data loss** — crash, unexpected navigation, results not showing after a round
- **User context mismatch** — data from User A showing under User B
- **Star Quest not triggering** — second wrong answer on same fact passes without Star Quest
- **Timer running during Star Quest** — should be fully paused
- **Gold flash on skipped Star Scan facts** — should be neutral
- **Star Scan data appearing in practice constellation** — data streams must stay separate
- **Star earned after single session** — mastery criteria not enforcing day spread

### Yellow flags (tune, don't panic)

- Rounds feeling too hard or too easy → adjust Challenge Level
- Star Quest triggering so often it dominates the round → student may have too many Needs Practice facts; reduce challenge density or shorten round
- Student turning Star Quest off every session → worth observing; may indicate Star Quest density, not dislike of the format
- Facts repeating more than expected → check pool size, orientation logic
- Timer feeling off-speed → verify threshold setting matches expectation

### Open items still being tuned (as of April 16, 2026)

These are known design decisions that are not yet final. Do not interpret them as bugs:
- **Mastery session count** (currently 3 sessions / 3 calendar dates) — will be adjusted based on beta data
- **Challenge Intensity ratios** — exact numbers being validated in beta
- **Freshness flag N-day window** — how many days of inactivity before a flag is set; TBD
- **Session count for ÷, +, − Star Scan** — multiplication confirmed at 3 sessions; others TBD after beta on those operations
- **Smart Practice filtering logic** — architecture designed, not yet built; All Facts with Challenge Level is the current proxy

---

*This document reflects design decisions through Session AO (April 17, 2026). Update after any session that changes a spec, adds a feature, or resolves an open item.*
