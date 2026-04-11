# Math Flash — Game Logic & Design Reference
*Living reference for all game logic, data gathering, and decision-making rationale.*
*Authority: design decisions made here take precedence over code comments. Code implements this; this explains why.*
*Created: 2026-04-10 — Session AG (Spark)*
*Last updated: 2026-04-10 — Session AG*

---

## Purpose of This File

This is the design authority document for Math Flash. It captures:
- What the game tracks, and why
- How the constellation tier system works
- How the Star Scan instruments work, and what they output
- How facts are prioritized in different game modes
- The orientation design principle
- All principled design decisions with their rationale

This file is not a code reference. It does not describe implementation. It describes what the game is supposed to do and why — so that future builds, design sessions, and agent conversations start from a shared foundation rather than reconstructing decisions from scratch.

**For Wright:** When code decisions conflict with this document, flag it. The design authority lives here; implementation is your domain.

**For Spark:** Update this file when design decisions are made in session. Do not let decisions live only in the handoff.

---

## Table of Contents

1. The Two-Level Fluency Model
2. The Tier System — Color Palette and Meaning
3. Mastery Definition and Criteria
4. Response Time Variance as a Mastery Signal
5. The Constellation — How It Works
6. Inactivity, Freshness Flags, and Durability
7. Star Scan Instruments — Three Moments, Three Data Routes
8. Beginning Star Scan — Two-Tier Architecture
9. Multi-Session Full Star Scan
10. Orientation Design Principle
11. Smart Fact Prioritization
12. Smart Practice Mode
13. Practice Quest — The Core Differentiator
14. Data Model Principles
15. Open Design Questions

---

## 1. The Two-Level Fluency Model

Math Flash distinguishes two distinct uses of timing data:

**Level 1 — Per-attempt grade (in-game feedback)**
Describes a single answer. Shown during Per-Question Timer mode.

| Grade | Threshold | Meaning |
|---|---|---|
| ⚡ Fluent | Correct, ≤ threshold (default 3s) | Fast enough to suggest auto-retrieval |
| 🔄 Almost! | Correct, 4–6s | Knows it, not yet automatic |
| 📚 Needs Practice | Wrong or no answer by 7s | Not yet known |

These grades describe a single attempt. They are not mastery. They are not written to the constellation as tier changes — they are input data.

**Level 2 — Longitudinal tier (constellation)**
Describes a pattern across many sessions. What a fact's dot looks like on the constellation. Requires sufficient data before it stabilizes.

The tier system operates on Level 2. A student who answers correctly once in 2.1s does not become "Fluent" — the constellation reflects the pattern of their attempts over time.

**Terminology rule (established Session X, Y):**
- Use "fluency" in-game and in all student-facing copy.
- Use "automaticity" in FAQ and methodology copy only.
- Rationale: fluency is observable (accuracy + speed). Automaticity is a cognitive state (effortless retrieval). Fluency is how you measure your way toward automaticity. The app measures fluency; automaticity is what that fluency is building toward. Do not conflate them in UI copy.

---

## 2. The Tier System — Color Palette and Meaning

**Canonical tier colors (established Session AB — do not deviate without design justification):**

| Tier | Color | Hex | Visual |
|---|---|---|---|
| Mastered | Gold | #ffd93d | Pulsing glow. Pip ★ badge. |
| Fluent | Amber | #ff9f43 | Glow intensity scales with how established the fact is. |
| Almost | Blue | #4d96ff | — |
| Needs Practice | Purple | #c77dff | — |
| Unpracticed | Dim | ~4% white opacity | "Unlit ember." Always present. |

**Consistency rule:** All tier-showing UI elements use this palette — constellation dots, countdown/timer bar, per-question tier flash, legend, tier pills. No element shows a subset of the tier vocabulary without explicit design justification.

**What each tier means:**
- **Mastered (Gold):** Durable, stable automaticity confirmed across multiple sessions. See mastery criteria below.
- **Fluent (Amber):** Consistently answered within the fluency threshold. Not yet confirmed as mastered — needs more sessions and low variance.
- **Almost (Blue):** Answered correctly, but outside the fluency threshold. Knows the fact; not yet automatic.
- **Needs Practice (Purple):** Wrong answers or timed out. Needs targeted practice.
- **Unpracticed (Dim):** No practice data. Default state for all facts at account creation.

---

## 3. Mastery Definition and Criteria

**Current mastery definition (v2 — proposed Session AB, not yet fully built):**

A fact is **Mastered** when:
- Correct within fluency threshold on **6 of the last 8 attempts**
- Spanning **at least 3 separate sessions**
- Spanning **at least 2 distinct calendar days**
- With **IIV (intraindividual variance) below empirical threshold** (TBD — to be tuned)
- With **at least 1 fluent response within the last N days** (recency gate — N TBD)

**De-certification:** A mastered fact is flagged for review if:
- 3 consecutive attempts exceed the fluency threshold, OR
- Variance spikes above the mastery threshold

De-certification does not remove the gold star visually. It sets an internal flag. See Section 6.

**Rationale for each criterion:**

| Criterion | Why |
|---|---|
| 6 of 8 (not 4 of 5) | More attempts = more robust signal. Reduces false positives from lucky streaks. |
| 3 sessions minimum | Distributed practice across sessions. Spacing effect applies. |
| Calendar day spread | Sessions on the same day are massed practice. Spacing effect requires genuine time gaps. |
| Variance gate | A student who sometimes answers in 1.2s and sometimes 5.8s is not automatic, even if the average looks fine. Variance reveals fragility. |
| Recency gate | Mastery is a current state, not a past achievement. A student who mastered in October and hasn't practiced since December may no longer have reliable retrieval. |

**What can be built now vs. tuned later:**
Structural criteria (session count, day spread, recency gate, de-certification flag) — build now.
Specific variance threshold and recency window (N days) — tune with real use data. Architecture must support this as configurable parameters, not hardcoded values.

---

## 4. Response Time Variance as a Mastery Signal

High intraindividual variance (IIV) in response time is a diagnostic signal of effortful processing — counting or calculating rather than automatic retrieval.

**The simple version:** A student who answers 3×4 in 2.1s, 2.3s, 2.0s, 2.2s demonstrates stable retrieval. A student who answers 3×4 in 2.1s, 5.8s, 1.9s, 6.2s is not automatic, even if the average looks acceptable. The variance reveals that the fact is fragile.

**Research basis:** Stickney, Sharp & Kenyon (2012) — response time variance as a mastery signal. Broader cognitive science literature consistently associates high IIV with effortful/reconstructive processing. Reflex Math uses "response pattern stability" as a mastery condition (Cholmsky, 2011 white paper — commercial, not peer-reviewed).

**Edge cases:**

*Untimed practice:* All attempts are recorded. Mode is tagged in the data. Untimed attempts count as practice exposure; they generate tier ratings only if the actual response time meets the threshold (a 2.4s untimed response still counts; a 7s untimed response correctly does not register as fluent). A student practicing exclusively untimed may produce systematically different response time patterns — this is real information, not a flaw.

*Warm-up data:* First responses of a session are typically slower. The variance model absorbs these without demoting the tier, as long as subsequent responses return to form. Consistently slow warm-up across many sessions is useful information in itself.

*Sparse data:* Variance is not reliable with 2–3 data points. Tier status should require a minimum number of attempts before stabilizing. Early constellation data should be treated as provisional. Exact minimum TBD.

*Bad day / temporary backslide:* A handful of slow responses in one session raise variance slightly but do not tank the tier if there is a long history of tight, fast attempts. Persistent slow responses across multiple sessions raise variance over time and the tier honestly reflects that.

---

## 5. The Constellation — How It Works

The constellation is the student's living record of their fact knowledge. Each dot represents one math fact. Dot color = tier (see Section 2).

**What the constellation is not:**
- Not a score. Not a grade. Not a judgment.
- Not a single-session snapshot — it reflects patterns across all sessions.
- Not a program with its own agenda. The teacher and student are in control of what gets practiced. The constellation responds to what they do.

**Glow intensity:** For Fluent and Mastered dots, glow intensity scales with how established the fact is. Recently fluent = softer glow. Long and consistently mastered = brighter, steadier glow. This is a visual indicator of data depth, not a separate tier.

**Threshold is a rendering parameter, not a grade:**
The fluency threshold (default 3s) is a lens on the raw data, not a stamp on it. All response times are stored in milliseconds. Changing the threshold recalculates tier rendering across the entire constellation without deleting or altering any raw data. This is essential — it means threshold adjustments (for accommodations, for example) are honest and reversible.

**Student-facing language (approved Session AB):**
> *"Your constellation shows how well you know each fact. One rough session won't change it — the game tracks patterns over time, not just today. If a fact keeps being slow, it'll show up that way too. That's useful to know."*

---

## 6. Inactivity, Freshness Flags, and Durability

**Core principle:** Stars are earned, not revoked, and not re-required.

The constellation does not visually change due to inactivity. A mastered fact keeps its star. Earned tiers are not taken back. The student should not have to keep proving facts they have genuinely mastered.

**The two-layer model:**

| Layer | What the student sees | What the system tracks |
|---|---|---|
| Visual tier | Unchanged — stars stay, colors stay | — |
| Internal freshness flag | Nothing — invisible to student | Timestamps, inactivity duration, durability status |

**What freshness flags actually do:**
A stale fact freezes in place. It cannot:
- Advance to the next tier
- Contribute to a "full operation mastered" celebration or badge
- Have mastery re-confirmed or re-stamped

It can still be practiced. When fresh data satisfies the recency/durability criteria, the flag clears silently. No drama, no notification.

**Who this primarily affects:** Near-mastery facts (Fluent, Almost) — still accumulating evidence. For Mastered facts, freshness is handled organically by the game-designed round's maintenance sprinkle (see Section 12).

**Why no visual punishment:** The consequence of staleness is forward-facing only. You can't unlock new achievements on old data — but nothing you already earned disappears. This is pedagogically honest and psychologically sound.

**Durability check — teacher-initiated:**
Running a Star Scan (Ongoing) is the clean way to get current confirmation across all facts. The game does not prompt this unprompted — that would be program behavior, not tool behavior. The teacher decides when a durability check is warranted.

---

## 7. Star Scan Instruments — Three Moments, Three Data Routes

The Star Scan is a single instrument (timed fact assessment) used in three distinct contexts. The context determines how data is routed. **These must not be conflated.**

### Moment 1 — Beginning Star Scan
- Timing: One-time, at account creation / onboarding
- Scope: Two tiers — see Section 8
- Output: Seeds the constellation tiers from results
  - Does NOT grant mastery. Gold still requires practice criteria.
  - Student can opt out and start from scratch (constellation begins all-unpracticed)
- **This is the only Star Scan that writes to the constellation.**
- Data written to: `mathflash_facts` (constellation), and `mathflash_assessments` (record)

### Moment 2 — Ongoing Star Scan
- Timing: Teacher-initiated, any time after onboarding
- Scope: Teacher-selected (Full scope or per-table)
- Output: Pure snapshot. Stored in Star Scan Records only.
  - Does NOT affect the constellation.
  - Exists for teacher visibility and documentation, not for game data.
- Data written to: `mathflash_assessments` only. Never touches `mathflash_facts`.

### Moment 3 — Final Star Scan
- Timing: Appears automatically when all facts in the selected scope reach Mastered
- Scope: Full scope (all facts for the selected operation)
- Output: Certification basis. Printable certificate.
  - Same instrument as Ongoing, same data routing (records only, not constellation)
  - Distinguished by trigger condition and printable output format
- Data written to: `mathflash_assessments` only.

**Implementation note for Wright:** Flag each Star Scan's data routing in code comments. Assessment data (`mathflash_assessments`) and constellation data (`mathflash_facts`) must never be mixed. The clean separation is confirmed and tested (v73).

---

## 8. Beginning Star Scan — Two-Tier Architecture

*(Spec'd Session AG. Design session with Kimberly required before Wright builds.)*

The Beginning Star Scan is the primary conversion hook. A new user takes it during onboarding, results seed a ghost constellation, and they immediately see — visually — what the paid tier looks like. The instrument must be a good enough onboarding experience that users actually complete it.

### Tier 1 — Quick Start Scan (default onboarding path)
- **Scope:** ~20 facts, ~5 minutes
- **Design:** Stratified sample — 2 facts per table (one easier, one harder, per known difficulty hierarchy)
  - Easiest: ×0, ×1, ×2, ×5, ×10
  - Hardest: ×6×7, ×7×8, ×8×8 cross-products
- **Output:** Table-level picture only — "which tables to target." Not per-fact detail.
- **Constellation seed:** Lights up anchor facts with most still dim. This is actually a stronger conversion hook than a full scan — the user sees real lit facts against a mostly-dark constellation, making the value of continued practice visually clear.
- **Who it's for:** Free trial users. Default path for all new users.

### Tier 2 — Full Star Scan (paid tier)
- **Scope:** All facts in the selected operation (per-fact, exhaustive)
- **Design:** Same instrument as Quick Start but complete
- **Output:** Per-fact picture across all facts
- **Constellation seed:** Dense seed; more facts lit from the start
- **Who it's for:** Paid users. Available to free users? TBD — pending design session.
- **May be split across sessions:** See Section 9.

### Quick Start Scan — orientation policy (decided Session AH):
**One orientation per table only.** With only ~20 total questions and 2 per table, every question must contribute table-level breadth. Testing both orientations of the same fact would sacrifice coverage of other tables. The output is "which tables to target" — not per-fact orientation detail. Per-fact orientation data is the job of the Full Star Scan and ongoing practice tracking.

### Full Star Scan — access (decided Session AH):
**Paid tier only.** Free/trial users access the Quick Start Scan only. Full Star Scan (per-fact, exhaustive) is a paid-tier feature. This applies to the Beginning Star Scan context — the Quick Start is the free beginning assessment path.

### Data routing for Beginning Star Scan tiers:
- Quick Start → seeds table-level tiers (affects all facts in that table uniformly based on sample performance)
- Full Star Scan → seeds per-fact tiers directly

**Design note:** These routing rules must be designed explicitly before wiring. Do not infer from the assessment results alone — the mapping logic is a design decision, not a technical default.

---

## 9. Multi-Session Full Star Scan

*(Designed Session AH — April 11, 2026. Build-ready for beta.)*

The Full Star Scan (paid tier) is always structured as sessions — it is not a toggle between "single-session" and "multi-session." A student who can complete all three sessions in one sitting can do so; the session structure accommodates those who can't.

### Session structure (multiplication — confirmed):

| Session | Facts covered |
|---|---|
| 1 — Foundations | All facts from ×0, ×1, ×2, ×5, ×10 tables (both orientations, exhaustive) |
| 2 — Mid-tier | All facts from ×3, ×4, ×6, ×9 tables (both orientations, not already covered) |
| 3 — Hard facts | All facts from ×7, ×8 tables / cross-products (both orientations, not already covered) |

No fact appears in two sessions. Session count for other operations: TBD pending beta testing.

### Constellation update timing:
**Updates after each completed session** — not held until all three are done. Immediate payoff: Session 1 anchor facts light up right away.

### Entry flow:
Brief session overview screen before Session 1 begins:
> *"Your Full Star Scan is split into 3 sessions — you can complete them all today or come back anytime within 4 weeks."*
Show three session names and fact counts. Then begin Session 1.

### Post-session screen:
- Session N results (facts tested, mastered count, needs practice count)
- Constellation update confirmation: *"Your constellation has been updated with today's results."*
- Two options: **Continue to Session N+1** OR **Come back later**
- If "Come back later": persistent **"Continue Star Scan"** button on title screen and My Constellation header until scan is complete or sealed

### Sessions 2 and 3 start screen:
- Brief prior session summary: *"Session 1 complete — 45 facts tested."*
- Today's label: *"Session 2 of 3 — Mid-tier facts"*
- Begin.

### Progress indicator:
Shown on title screen and My Constellation while scan is in progress.
Format: [●●○] *"Beginning Star Scan: Session 2 of 3 complete"*

### 4-week window:
Soft advisory only. No hard block — scan never expires, never locks, never deletes data.
Advisory shown at session end if > 2 weeks have passed since first session:
> *"Your Beginning Star Scan has a 4-week window — for best results, complete all sessions within 1–2 weeks. The closer together your sessions are, the more your baseline reflects where your student is right now."*
No countdown timer. No "X days remaining" pressure display.

### Sealing — teacher-initiated only:
Available in Star Scan Records after any completed session. Not student-accessible.

Confirmation prompt:
> *"Seal this scan? Your constellation will keep the results from completed sessions. Facts not yet tested will remain unlit. You won't be able to add more sessions after sealing."*

After sealing: scan closed, no further sessions, untested facts stay unlit.
Star Scan Records label: *"Beginning Star Scan — Sealed after Session N of 3 — [date]"*

### Printable record:
Unified document — different layout from single-session print. Available as partial record after each session; complete record after all sessions or sealing.
Contents: each session block (date, facts covered, mastered/needs practice counts) + combined summary.
**Pip to design layout. Hold on print implementation until Pip delivers template — build interactive flow first.**

---

## 10. Orientation Design Principle

**Students do not automatically transfer knowledge between orientations of the same fact.**

This is not a technical edge case — it is a pedagogical reality that affects every assessment instrument and data model in the game. It must be factored into all instrument design from the start, not added later.

### What this means per operation:

| Operation | Orientation A | Orientation B | Same retrieval demand? |
|---|---|---|---|
| Addition | 3 + 4 = ? | 4 + 3 = ? | No — separate retrieval paths |
| Subtraction | 12 − 4 = ? | 12 − 8 = ? | No — genuinely different demands |
| Multiplication | 3 × 4 = ? | 4 × 3 = ? | No — separate facts for many students |
| Division | 28 ÷ 4 = ? | 28 ÷ 7 = ? | No — different facts |

### Design implications:
- **Assessment instruments** must account for both orientations — or explicitly document that they are sampling only one and note the limitation.
- **Question count** for any complete scan is higher than it appears if only one orientation is counted.
- **Sampling design** for the Quick Start Scan must decide: test one orientation per fact or both? If one, which one, and how is the limitation communicated?
- **Data model:** Orientation must be stored per attempt, not assumed. `3×4` and `4×3` are distinct fact records.

**Critical implementation note for Wright:** Do NOT design the assessment data model assuming single-orientation facts and plan to add orientation later. Retrofitting this requires a data model rework. It must be in the schema from the start.

---

## 11. Smart Fact Prioritization

*(Governs all game modes at mode-appropriate injection rates. Resolved Session AG.)*

### The core rule:
**Unpracticed facts trump recency.** `lastSeen` ordering is only meaningful when practice history exists. For facts with zero attempts, `lastSeen = null` — recency comparison is meaningless. Unpracticed facts should not sort to the bottom because their null date appears "oldest."

### Priority order (all modes):

| Priority | Pool | Logic |
|---|---|---|
| 1 — Unpracticed | Any fact with zero practice attempts | Inject first. No recency comparison possible. |
| 2 — Known facts by recency | Any fact with ≥1 attempt | Sort by `lastSeen` ascending (longest unseen first). |
| 3 — Maintenance sprinkle | Mastered facts | Small fixed count per round. Rotating. Not weighted by recency. |

### Injection rate per mode:

| Mode | Unpracticed injection rate |
|---|---|
| Standard modes | 2–3 unpracticed facts per round max |
| Smart Practice | Higher — this is its job. Exact rate TBD during build. |

Rationale for cap in standard modes: overwhelming a student with all unpracticed facts in a single round is pedagogically counterproductive. Gradual introduction allows practice history to develop. Smart Practice mode lifts this cap because it is explicitly designed to work from the constellation — the student opted into that mode knowing it.

---

## 12. Smart Practice Mode

*(Planned game mode. Not yet built. Connected to constellation data model.)*

**Working name: Smart Practice**

**Mode card description (approved Session AB):**
> *The game reads your constellation and builds a round focused on what matters most right now. The best way to light up your facts.*

The game reads the student's constellation and builds the round automatically. No teacher or student selection of facts required. The constellation is the input.

### Fact prioritization in Smart Practice:

| Priority | Tier | Rationale |
|---|---|---|
| 1 | Fluent (amber), not yet mastered | Closest to advancing. Already meets speed threshold; needs more sessions of consistent evidence. Highest-leverage. |
| 2 | Almost (blue) | Correct but not yet fast enough. Needs speed improvement. |
| 3 | Needs Practice (purple) / Unpracticed | Needs exposure. |
| 4 — maintenance sprinkle | Mastered (gold) | Small number per round, rotating. Keeps retrieval timestamps current. Spaced retrieval of mastered material is pedagogically sound, not just data housekeeping. |

The ratio between categories is tunable and should adapt to the student's constellation state:
- Student with many Fluent facts: more Priority 1 and 2
- Student just starting: more Priority 3

The maintenance sprinkle is small and unobtrusive. The student experiences it as a normal mixed round.

**Connection to freshness flags:** The maintenance sprinkle is the primary mechanism keeping mastered facts fresh. Because gold facts appear in every Smart Practice round, their timestamps update regularly. The inactivity flag for mastered facts may have a significantly longer trigger window — or may not be needed for gold facts at all — given this design. Confirm when built.

---

## 13. Practice Quest — The Core Differentiator

**Trigger:** 2 wrong attempts on a single fact within a round.

**Sequence:**
1. Round stops.
2. Student exits the performance environment.
3. Enters structured multi-step sequence: Find It → mini-game → Prove It.
4. Returns to the same round. Timer was paused during quest.

**What no competitor does:**
Every major platform handles a wrong answer the same way — show the correct answer, log the miss, move on. Math Flash handles it *now*, in the moment, before the student moves on.

| Platform | Response to wrong answer |
|---|---|
| XtraMath | Shows correct answer, student types it to confirm, moves on |
| Reflex Math | Correct answer flashes briefly in red, moves on |
| Rocket Math | Fact recycles sooner — no structured sequence |
| Monster Math | Popup, respawn, move on — no in-moment remediation |
| MathFactLab | Visual/strategy models — different philosophy |
| **Math Flash** | Round stops. Find It → mini-game → Prove It. Returns to round. |

**Research basis:** Immediate corrective feedback after an error outperforms errorless learning for retention and transfer in typically-developing students. Practice Quest is not a punishment mechanic — it is the pedagogically correct response to a miss. See RP Section 4 (Errorless Learning vs. Error Correction) for full research basis.

**Timer behavior:** Timer pauses during Practice Quest. No score pressure during the remediation sequence. The student exits the performance environment entirely and enters a lower-stakes sequence focused on just that one fact.

**Accommodation note:** The remediation toggle gives teachers the ability to apply errorless-style flow for students where that is clinically appropriate (significant cognitive disabilities, ASD where error correction triggers behavioral shutdown). This toggle is a teacher-controlled option, not the default, which is the correct nuanced position.

---

## 14. Data Model Principles

**All response times stored in milliseconds.** Not grades, not tier labels — raw numbers. Tier rendering is computed from raw data at display time.

**The threshold is a rendering parameter.** Changing the fluency threshold (from 3s to 5s for an accommodation, for example) recalculates tier rendering across the constellation without altering any raw data. No data is deleted or overwritten. This is non-negotiable — it makes threshold changes honest and reversible.

**Mode tagged per attempt.** Timed / untimed / extended time accommodation. Allows analysis of response time patterns by mode without conflating them.

**Assessment data is separate from practice data.**
- `mathflash_assessments` — Star Scan records only
- `mathflash_facts` — constellation / practice history only
- These two structures must never be mixed. The Beginning Star Scan writes to both (it seeds the constellation AND logs a record). Ongoing and Final Star Scans write to `mathflash_assessments` only.

**localStorage is a deliberate philosophical choice.** Data lives on the student's device. Not harvested, not locked in a server, not held hostage to a subscription. The honest tradeoff: data doesn't follow the student across devices without an export/import feature. That feature is planned.

**Orientation stored per attempt.** `3×4` and `4×3` are distinct records. Do not collapse into a single fact record and do not assume transfer between orientations.

---

## 15. Open Design Questions

These are live questions — do not design around them without flagging first.

| Question | Status | Who decides |
|---|---|---|
| Variance threshold for mastery gate | TBD — tune with real use | Spark + beta testing |
| Recency gate (N days) for mastery | TBD — tune with real use | Spark + beta testing |
| Minimum attempt count before tier stabilizes | TBD | Spark + beta testing |
| Fluency threshold UI location (settings vs. My Progress contextual display) | Proposed: contextual in My Progress. Not finalized. | Design session with Kimberly |
| Quick Start Scan — one orientation per fact or both? | **Decided (Session AH): one orientation per table only.** | — |
| Full Star Scan available to free/trial users? | **Decided (Session AH): No — paid tier only.** Free/trial = Quick Start only. | — |
| Multi-session scan — constellation update timing | **Decided (Session AH): updates after each session.** | — |
| Multi-session scan session count for addition/subtraction/division | TBD — after beta testing those operations | Spark design discussion post-beta |
| Smart Practice injection ratio (exact numbers) | TBD during build | Wright + Spark tuning |
| Data backup/export format and UI placement | Recommendation drafted — awaiting Kimberly review | See handoff |
| Competitive Mode design (turn-based vs buzz-in, score tracking, constellation interaction) | Recommendation drafted — awaiting Kimberly review | See handoff |
| Payment/licensing flow and processor choice (Lemon Squeezy recommended) | Design session required before build | Kimberly |

---

*Update this file at the end of any session that produces a design decision. Replace the Open Design Questions table rather than appending. Add new sections as new systems are designed.*
