# Math Fact Galaxy — Screen Reference
*What's on each screen, where it leads, and why every decision was made*
*For use during beta testing, design reviews, and teacher/parent onboarding*
*Created: Session AN — April 17, 2026*
*Maintained by Spark — update when Wright builds new screens or changes navigation*

**Cross-reference key:**
- 📚 **Research** — decision grounded in peer-reviewed literature (citation given)
- 🏫 **Professional judgment** — grounded in Kimberly's experience as an educational therapist / classroom teacher
- 🎨 **Design principle** — product-level decision (brand, philosophy, UX)
- ⚙️ **Technical** — driven by architecture or implementation constraint
- 🔄 **Still being tuned** — decision made but numbers/details pending beta data

---

## Navigation Map — How the Screens Connect

```
[Title Screen — 2×2 grid]
    ├── Top-left  → Build My Constellation (BMC)
    │                   └── Setup Card → Active Round → [Star Quest] → Results
    ├── Top-right → My Constellation
    │                   ├── Constellation Grid
    │                   ├── Facts to Watch
    │                   ├── Galaxy View (all 4 operations)
    │                   └── Records & Print → fact click → stats card → mini-game overlay
    ├── Bottom-left → Star Scan
    │                   ├── Setup → Active Scan → Results → Records
    │                   └── Records (all past scans, print, delete)
    └── Bottom-right → Star Forge
                        └── Session builder → session report (no constellation write)

[Profile Chip — accessible from any screen]
    └── User Menu: Switch User / Add New User / (future: settings, backup)

[Settings — accessible via "Change" links on multiple screens]
    └── Fluency threshold, mini-game speed, other persisted settings
```

---

## Title Screen

### What's here
- Game logo and title: **Math Fact Galaxy**
- 2×2 navigation grid: Build My Constellation (top-left, primary), My Constellation (top-right), Star Scan (bottom-left), Star Forge (bottom-right)
- Profile chip (top area) — shows current user
- Subtitle: Sparkwright brand mark

### Why this layout

**2×2 grid with primary emphasis on top-left:**
🏫 The most important thing a student does is practice. Build My Constellation is the daily action. Everything else — checking progress, running scans, building custom sessions — is secondary to actually building fluency. The layout communicates this hierarchy visually without explaining it.

**Four areas, not a tab bar or menu:**
🎨 Each area has a distinct identity and purpose. A grid gives each area equal visual weight in the layout while the position and visual treatment communicate the hierarchy. A menu or tab bar would flatten the distinction between primary and secondary areas.

**No dashboard or home screen separate from navigation:**
🎨 The title screen IS the navigation. The student arrives and immediately sees their choices. No dead-end home screen, no required sign-in flow, no upsell before action.

### Beta testing: what to check
- Correct user showing in profile chip
- All four grid areas navigating to their correct screens
- Profile chip opens user menu (not mid-game navigation overlay)

---

## Build My Constellation (BMC)

### What this area is for
Daily practice. The student builds their constellation by completing timed rounds. Every correct response within the fluency threshold contributes toward lighting up stars. Star Quest handles misses.

### Setup Card — what's on it

**Operation selector (×, ÷, +, −)**
The student chooses which constellation they are building today.

*Why:* Each operation is its own constellation. The student's galaxy fills in as all four operations are learned — this is the structural logic of the product, not just aesthetic. Choosing an operation is choosing which stars to light up today.

**Fact range: Standard / Advanced**
- Multiplication: Standard = ×1–×12 / Advanced = ×13–×20
- Division: Standard = ÷1–÷12 / Advanced = ÷13–÷20
- Addition: Standard = addends 1–10 (sums ≤20) / Advanced = addends 11–20
- Subtraction: Derived from paired addition ranges

*Why:* 📚 The ×1–×12 range covers the facts students need for multi-digit multiplication and long division (grade 4–5 standard). ×13–×20 represents extended fluency that some curricula and families target. 🏫 Addition with addends 11–20 involves regrouping strategies — labeled "Advanced" (not "Extended") because it signals a qualitatively different challenge, not just more of the same.

**Mode: All Facts / Smart Play**
- All Facts: full fact pool for the selected operation and range, with Challenge Level governing the ratio
- Smart Play: constellation-informed — game reads the student's data and prioritizes the most instructionally valuable facts automatically *(Smart Play filtering logic: designed, not yet built — currently All Facts with Challenge Level is the proxy)*

*Why All Facts as the default:*
🏫 A new student has no constellation data yet — Smart Play cannot function without a baseline. All Facts with Challenge Level gives every student a usable starting point immediately, with the daily ratio choice in their hands.

*Why Smart Play at all:*
📚 Deliberate, data-informed fact selection is more efficient than random selection. A student who has 10 mastered facts, 20 fluent, 15 almost, and 30 needs-practice benefits from a round that prioritizes the almost-fluent cluster (highest leverage for advancement) over a random shuffle that might hit mastered facts 10 times. This is the application of deliberate practice principles to fact fluency.

**Challenge Level: Gentle / Balanced / Intensive**
Controls how many challenging facts (Needs Practice + Unpracticed) appear per round, and how the rest of the round is filled.

| Setting | Challenge facts | Fill content | Round length behavior |
|---|---|---|---|
| **Gentle** | 2–3 | Fluent → Almost → Mastered sprinkle | Shortens if fill content is thin |
| **Balanced** (default) | 4–6 | Fluent → Almost → Mastered sprinkle | Minor shortening if needed |
| **Intensive** | Up to 8–10 | ~30% Fluent/Almost still interleaved | Holds to round length setting |

Fill priority order: Fluent (amber) first → Almost (blue) → Mastered maintenance sprinkle.

*Why this setting exists:*
📚 Interspersal effect — embedding challenging items among known items produces better retention of the challenging items than massed challenge practice. A round that is 100% struggle facts creates excessive cognitive load (Sweller, 1988, *Cognitive Science*, 12 — verified) and is less effective at encoding the hard facts than a mixed round. Intensive still keeps ~30% known facts interleaved because the interspersal principle holds even at the highest challenge density.

*Why student-facing and daily:*
🏫 A student coming off a hard day, tired, or in a warm-up session has genuinely different capacity than a student who is fresh and motivated. Respecting that reality is not lowering expectations — it is designing for actual human variability. A student who chooses Gentle and completes a round is building fluency. A student forced into Intensive who doesn't start the round builds nothing. This is the "quiet respect baked in" design principle.

*Why "Challenge Level" not "Difficulty":*
🎨 Difficulty implies the math problems themselves are harder. Challenge Level controls the ratio of facts that are challenging *for this student* — the math is the same. The label should be accurate about what is being controlled.

**Include Star Quest (checkbox — checked by default)**
Whether Star Quest activates during this session.

*Why optional:*
🏫 A fatigued or resistant student who knows they'll hit Star Quest multiple times may not start the round at all. A student who just completed a long Star Quest session may need a change of pace. The constellation data records correctly either way — what changes is whether in-moment remediation triggers on the second wrong answer. Giving the student this choice respects their self-knowledge about their current state without removing the default design.

*Important:* Once Star Quest triggers mid-round, the student completes it. The checkbox controls session-level behavior only. A teacher who sees a student chronically turning Star Quest off has data worth discussing — it may indicate too-high challenge density (too many hard facts triggering too many quests) rather than dislike of Star Quest itself.

**Round length (number of questions)**
How many facts appear in the round. Subject to shortening if the student's fact pool is smaller than requested (see Thin Fact Pool below).

**Fluency threshold (read-only contextual note + Change link)**
Shows current threshold (e.g., "Fluency graded at 3s · Change"). The Change link opens Settings directly.

*Why visible here:*
🎨 The student (or teacher) sets up a round and should know the standard being measured without navigating away. The contextual note is read-only — it's information, not a control. The link goes to Settings where it can be changed.

---

### Active Round — what happens

**Fact display**
One fact at a time. Type answer, press Enter. The fact is cleared and the next appears.

**Timer bar**
Counts down from the fluency threshold (e.g., 3 seconds). Bar runs out = fact auto-kicks (game moves on, fact re-queues for later in round or logged as miss).

*Why the bar runs to the fluency threshold, not a longer window:*
📚 The visible countdown should represent the standard being measured. A bar that runs 7 seconds while grading at 3 seconds sends a mixed signal — the student thinks they have more time than they're actually being evaluated on. Honesty in feedback is a core design principle. The threshold is the measurement; the bar should reflect the measurement. (Session AN design decision.)

*Why the threshold is adjustable:*
📚 Processing speed differences significantly affect timed math fact performance. Lee (2024, *Journal of Attention Disorders* — verified) documented ~0.76 SD effect size for processing speed on math fluency in ADHD populations. A student with a processing speed accommodation should have the same game experience as any other student — the threshold absorbs the accommodation, not the game design.

**Answer input**
Type-in only in BMC. Reveal mode (flip card) is available in Star Forge for different practice contexts.

*Why type-in as default:*
🏫 Type-in requires full retrieval — the student must produce the answer, not recognize it from a shown card. Recognition and retrieval are different cognitive demands. Fluency is a retrieval standard. Reveal mode has a place in certain practice contexts (Star Forge, early exploration) but is not the fluency-building mode.

**Wrong answer handling**
- First wrong answer on a fact in a round: fact is re-queued for later in the round
- Second wrong answer on the same fact in a round: Star Quest activates

*Why two chances before Star Quest:*
🏫 One wrong answer can be a typo, a momentary lapse, a misread. Two wrong answers on the same fact in the same round is a signal that the student does not have reliable retrieval of that fact right now. Two chances is the threshold that distinguishes "slip" from "gap."

**Progress display**
Dots or counter showing position in round (e.g., question 8 of 20).

**Thin fact pool behavior**
When the student's available fact pool is smaller than the requested round length:
1. Both orientations of each fact are used first (3×4 and 4×3 are distinct retrieval demands — not the same fact, not padding)
2. After both orientations are exhausted, the round ends cleanly with results shown
3. No third repetition of the same fact orientation

*Why:*
📚 Orientation transfer is not automatic. Students do not reliably transfer fluency from 3×4 to 4×3 — both represent distinct retrieval pathways (established through clinical practice and supported by the orientation design principle documented in the research framework). 🎨 A short round that is honest is better than a padded round that repeats content to hit an arbitrary number.

---

### Star Quest — what happens

**Trigger:** Second wrong answer on the same fact in the same round.

**What happens:**
1. Round pauses. Timer pauses. Current fact disappears.
2. Student enters the Star Quest sequence for that specific fact: **Find It → mini-game (Falling Facts / Find It / Prove It) → Prove It**
3. After completing all three steps, student returns to the main round
4. The fact that triggered Star Quest is removed from the remaining round pool

**Star Quest badge and step pips**
Visual indicator showing which step the student is on within the quest.

*Why Star Quest exists:*
📚 Error correction outperforms errorless learning for typically-developing students (Terrace, 1963 — the errorless learning paper; the clinical application is legitimate for ASD/IDD populations, but applying it as a universal default is the error). In-moment structured remediation at the point of failure produces better retention than end-of-round review or drilling past misses. This is the product's core differentiator — no other math fact platform handles the moment of failure this way.

*Why the timer pauses during Star Quest:*
🏫 Star Quest is remediation, not a race. The timer existing during a remediation sequence would contaminate what we're measuring — the student is in a different cognitive mode. The pause is both fair and data-honest.

*Why the student can't leave mid-quest:*
🏫 Partial remediation is ambiguous data and teaches the wrong lesson — that the hard part can be escaped. Once the quest starts, the student completes it. The opt-out is at session setup, before the round begins.

**Mini-games in Star Quest**
Currently: Falling Facts. Future pool will grow to 10+ mini-games, 3 chosen randomly per quest. The mini-games are not named individually in UI copy — "a few quick games" or equivalent generic language is used everywhere. Naming specific mini-games in copy would require updating copy every time the pool expands.

---

### Results Screen — what's shown

After the round ends:
- Per-fact results: which facts were answered correctly, which were missed, response times
- Which facts are now in which tier (updated after round)
- Time breakdown: total round time, time in Star Quest per fact (planned — not yet built)
- Navigation: return to BMC setup, go to My Constellation

*Why show per-fact results:*
🏫 The student (and teacher) should be able to see exactly what happened. Opacity about performance is not respectful — it removes the student's ability to understand their own progress. Per-fact results are the most direct feedback the game can provide.

*Why include Star Quest time in the report:*
🏫 A teacher looking at a 25-minute "round" that was actually 8 minutes of practice and 17 minutes of Star Quest on two facts has very different clinical information than a teacher who sees 25 minutes of practice. Time transparency is part of how this product earns trust with professional users.

---

## My Constellation

### What this area is for
The student's visual record of progress. Every fact they have practiced is represented here. The constellation shows, at a glance, where the student is across the full fact range.

### What's on this screen

**Operation switcher (×, ÷, +, −)**
Switch between the four constellations. Each operation has its own constellation; all four together form the galaxy.

*Why four separate constellations:*
🎨 Each operation is a distinct fluency domain. Multiplication mastery does not imply division mastery. Addition fluency in one range does not transfer automatically to subtraction in a related range. Keeping them separate reflects the structure of the learning, not just the structure of the game.

**Constellation grid**
12×12 grid (multiplication standard). Each cell represents a fact. Color reflects current tier:

| Color | Tier | Meaning |
|---|---|---|
| Dim ember | Unpracticed | No attempts yet |
| Purple glow | Needs Practice | Incorrect or very slow |
| Blue glow | Almost | Correct but slower than threshold |
| Amber glow | Fluent | Within threshold consistently |
| Gold star (★) | Mastered | Full mastery criteria met |

*Why color-coded:*
📚 Immediate, at-a-glance feedback on the full fact range is more instructionally useful than a list. A teacher can look at the grid and see in seconds that the ×7 and ×8 columns are still purple while the ×2 and ×5 columns are gold — and plan instruction accordingly. 🏫 The color system was designed to be meaningful at every point: purple is "needs work now," blue is "getting there," amber is "close," gold is "earned." No tier color is arbitrary.

*Why unpracticed facts are visible (dim, not absent):*
🏫 Showing the full grid with unpracticed facts as dim embers lets the student (and teacher) see what remains — the shape of what is still ahead. An empty grid that fills in over time communicates a different story than a full grid that lights up. The latter shows the whole territory at once, which is more motivating and more honest.

**Fluency threshold contextual note**
"Fluency graded at Xs · Change" — read-only, with link to Settings.

*Why here:*
🎨 The constellation is a graded display. The viewer should know the grading standard without navigating away. It is contextual information, not a setting control.

**Facts to Watch**
Priority list of facts worth the student's attention right now. Priority order:
1. Needs Practice (most urgent)
2. Almost (high leverage — close to fluency)
3. Unpracticed (still unseen)

Capped at 5. Single row, color-coded border by tier.

*Why this exists:*
🏫 The full 12×12 grid can be overwhelming. A student who sees 40 purple cells doesn't know where to start. Facts to Watch surfaces the most actionable subset — the highest-priority facts for the next practice session. It translates the grid into an instruction.

*Why Almost facts are prioritized above Unpracticed:*
📚 A fact that is Almost fluent (correct, but slower than threshold) is closer to a tier advancement than an unpracticed fact that may still be at Needs Practice after first exposure. High-leverage facts first. 🏫 This mirrors what an experienced tutor does when planning a session — they work the facts that are closest to the next level, not just the ones that are missing.

**Galaxy View button**
Opens a full-screen view: four real constellation shapes in a night sky, one per operation. Stars within each constellation represent fact tables — they light up as tables are mastered.

| Operation | Constellation shape |
|---|---|
| × Multiplication | Orion |
| ÷ Division | Libra |
| + Addition | Cassiopeia |
| − Subtraction | Gemini |

Each star = one fact table. **Two star states only:**
- **Dim ember** — table not yet fully mastered (any amount of progress, or none)
- **Gold with halo** — every fact in the table has reached Mastered tier

There is no amber in-progress state in Galaxy View. The star is either unlit or earned. Partial progress (amber/blue/purple facts within a table) is visible in My Constellation's grid — Galaxy View is the achievement layer, not the progress layer. A star that lights for anything less than full mastery would undermine what the star means.

Connecting lines show the constellation shape even when stars are unlit. Background: deep space with sparse CSS star field.

Layout: 2×2 fixed grid (× top-left, ÷ top-right, + bottom-left, − bottom-right — matches title screen). Each tile tappable, navigates to My Constellation for that operation.

**No copy on the tiles — visual data only.** The scene reads as art. A mostly-lit Orion next to a dim Libra tells the story without words. Only orientation marker: a small operation symbol (×, ÷, +, −) at the outer corner of each quadrant — small enough to not interrupt the scene, findable when needed.

Pip will refine the visual layer later; this design is the permanent structure.

*Why this exists:*
🎨 The galaxy is the product concept. Four operations = four constellations = one galaxy. The Galaxy View makes the complete picture visible — it is the "look at everything you've built" moment. Real constellation shapes ground the visual metaphor in something authentic and beautiful rather than abstract UI elements. A student who looks up Orion in the actual night sky and recognizes it from the game — that is the kind of authentic connection this brand is built on.

**Fact click → stats card → Practice button → Star Lab**
Clicking any fact in the grid opens a stats card for that specific fact: response time history, current tier, trend. The Practice button opens **Star Lab** — an overlay showing the three mini-game options (Falling Facts / Find It / Prove It). The student picks one and plays a short focused session on that specific fact: both orientations, ~6 attempts, no Star Quest within Star Lab. Brief results, then returns to My Constellation with the fact cell updated.

*Why:*
🏫 A student or teacher who wants to drill a specific fact should be able to do so without building a full round. Star Lab provides targeted, student-initiated remediation from within the constellation view — the student sees the fact, sees it's purple, and can act on it immediately. The ~6-attempt scope (both orientations, 3 reps each) is short enough to be useful without being exhausting — a remediation tool, not a drill session.

**Records & Print**
Practice session history, Star Scan records, print options.

---

## Star Scan

### What this area is for
Assessment — systematic testing of facts to get a snapshot of where the student is. Star Scan data is stored separately from practice data and does NOT affect the practice constellation (except the Beginning Star Scan at onboarding, which seeds initial tier estimates).

*Why separate data streams:*
📚 A probe attempt and a practice attempt are not the same signal. During practice, the student has had warm-up, Star Quest support, and round context. During a scan, the student is cold — one attempt per fact, no retry, no support. Mixing these into the same data pool would corrupt the practice-based tier calculations and make the mastery signal unreliable. The streams must stay parallel.

### Quick Start Scan vs. Full Star Scan

| | Quick Start Scan | Full Star Scan |
|---|---|---|
| Questions | 36 | All facts in scope |
| Scope | 3 per table (low / mid / upper range) | Every fact, both orientations |
| Output | Table-level picture | Per-fact picture |
| Access | Free — onboarding | Paid tier |
| Sessions | Single | Multi-session (3 for multiplication) |
| Constellation effect | Seeds ghost constellation (onboarding only) | Records only |

*Why a Quick Start exists:*
🎨 A 78–144 question assessment as the very first thing a new user does will cause drop-off before they ever experience the game. The Quick Start gives a meaningful starting picture (~5 minutes) that seeds the constellation visually — the student sees something light up — without requiring a full assessment commitment at the door. The Full Star Scan is available for users who want the complete per-fact baseline.

*Why the Full Star Scan is multi-session:*
🏫 A tutor with a 45-minute weekly session cannot complete a 144-question assessment in one sitting alongside actual instruction. A student with anxiety or short attention span may not have the stamina. Multi-session structure respects real practice contexts without reducing the rigor of the assessment — the student can complete it in one sitting if they want, or across up to 3 sessions over 4 weeks.

### Setup — what's on it

**Operation selector**
Which constellation this scan is assessing.

**Scope selector: Full / Per-Table / Family Groups**
- Full: all facts in the selected range
- Per-Table: select specific tables (e.g., ×6, ×7, ×8 only)
- Family Groups: Doubling Facts (×2,4,8), Anchor Facts (×5,10), Triple Family (×3,6,9)

*Why family groups:*
🏫 Facts cluster by strategy family — a student who knows ×5 often has a scaffold for ×10; a student who struggles with ×6 may also struggle with ×3 and ×9 (triple family). Running a scan on a family group rather than random tables can surface pattern-level gaps more efficiently than table-by-table. This reflects educational therapy practice.

**Dynamic question count**
"You'll answer X questions" — updates live as scope is adjusted.

*Why:*
🏫 Informed consent about the length of an assessment. A student who knows they're answering 24 questions can mentally prepare differently than one who thinks it might be 100. Knowing the scope also lets the teacher plan time accordingly.

**Fluency threshold note**
Same threshold used in practice is used in the scan — no separate assessment threshold.

*Why same threshold:*
🏫 The scan is measuring against the same standard the student practices against. A separate threshold would create data that's not comparable to practice data — and the comparison is the whole point.

### Active Scan — what happens

**One attempt per fact**
No retry, no Star Quest, no second chance.

*Why:*
📚 Assessment validity requires controlled conditions. A retry opportunity changes what's being measured — it's no longer a cold retrieval probe, it's a practice trial. The scan is a snapshot, not a practice session. Mixing them would invalidate the data.

**Timer bar — neutral color only**
White/silver countdown bar. No tier colors.

*Why no tier colors during the scan:*
🎨 Tier colors carry meaning throughout the product. A purple bar during a scan doesn't mean the student is in the Needs Practice tier — it means the timer is running. Showing tier colors mid-scan assigns meaning that isn't yet earned. Results with tier color appear after the scan, not during it.

**Hard stop at threshold**
When the bar runs out: fact is auto-kicked, recorded as unanswered (not incorrect), and the next fact loads.

*Why hard stop (no extra time):*
📚 Data integrity. The scan is measuring fluency against the threshold. Allowing extra time after the bar expires means the recorded response is not a fluency measure — it's a retrieval-with-extra-time measure. The two are different things and should not be in the same dataset. (This is the same principle as the BMC timer design.)

**No gold flash on unanswered facts**
An unanswered fact is shown neutrally when the answer is revealed. No gold visual.

*Why:*
🎨 Gold = mastery throughout the product. An unanswered fact has not earned a gold signal — giving it one would send a false message about the student's performance and erode trust in the tier system.

**Pause between facts**
The student can pause between facts — not mid-fact.

*Why between facts only, not mid-fact:*
📚 Mid-fact pause gives extra thinking time and contaminates the response time data — the student's recorded time would no longer reflect cold retrieval. Between-fact pauses are legitimate anxiety management and produce cleaner data (the student completes each fact in a composed state). The distinction is not pedantic — it is what makes the data usable.

### Results — what's shown

**Two-bucket results: Mastered / Needs Practice**
Each fact lands in one of two buckets. No in-between tier during assessment.

*Why binary:*
📚 Assessment data is a snapshot, not a trend. The rich tier gradations (Almost, Fluent, etc.) require a history of practice data with variance calculations. A single-session probe cannot support those gradations reliably — one fast correct answer does not establish fluency; one slow incorrect answer does not establish persistent struggle. The scan gives a coarser but more honest signal: "knows it" or "needs work."

**Print Targeted Deck button**
Prints a flashcard deck of only the Needs Practice facts from this scan. Same format as Star Forge print output.

*Why at the results screen:*
🏫 The teacher has just run a scan and has a list of the student's gap facts. The most natural next action is a targeted deck for homework or focused practice. Routing through Star Forge to print the same facts would add friction to an obvious workflow.

### Records — what's stored

- Each scan saved with: date, operation, scope, threshold used, results per fact
- Print button on each record
- Delete button on each record (with confirmation modal)

*Why save scan records:*
🏫 Diagnostic value is in the comparison over time. A single scan is a snapshot. Assessment 1 vs. Assessment 3 is a growth story — one that teachers, ed therapists, and homeschool parents can use to document progress. The records layer is what makes the tool useful for professional practice.

*Why include the threshold in each saved record:*
🏫 If the teacher changes the fluency threshold between scans, the comparison is only valid if you know what threshold each scan used. A scan run at 3s and a scan run at 5s are not directly comparable. Stamping each record with its threshold preserves interpretability.

---

## Star Forge

### What this area is for
Custom session builder. The teacher or student builds a fully configurable practice session: any operation, any range, any settings, any question format. Results go to a session report only — Star Forge sessions do NOT write to the student's constellation.

*Why no constellation writes from Star Forge:*
🏫 Star Forge is a controlled practice context — a teacher might run a Star Forge session to practice specific facts before an assessment, to warm up, or to drill a targeted set. That session performance is not the same signal as a student's independent BMC practice. Mixing the two data streams would contaminate the constellation with non-standard practice data.

### What's on this screen (planned — not yet fully built)

**Session builder**
- Operation and range selector
- Timer settings
- Question format: type-in or reveal
- Star Scan-style question formats (assessment-style presentation within a practice session)
- Round length

**Print: Custom Deck Print**
Teacher builds settings → clicks Print → printable flashcard sheet.

Card format:
- Front: problem (7 × 8 = ?)
- Back: full equation (7 × 8 = 56)
- Tier color border + text label (e.g. "Needs Practice") — B&W compatible
- Ordered by table; Sparkwright mark in corner
- 8-per-page (2×4) or 10-per-page (2×5) layout option

*Why print from Star Forge:*
🏫 A teacher who wants to send home a specific deck — "practice your ×6 and ×7 facts" — needs a physical product they can hand to a family. Digital practice is good; physical flashcards are still a durable, accessible tool, especially for students who do better offline or whose families don't have reliable device access during homework time.

**Free vs. paid: still open**
Star Forge free/paid tier has not been decided. Do not gate yet.

---

## Settings

### What's here
Accessible via "Change" links throughout the product (My Constellation, Star Scan setup, BMC setup card). Not a standalone settings screen in the traditional sense — a modal or panel that can be reached from multiple points of access.

**Fluency threshold**
The response time standard for grading practice (default: 3 seconds). Adjustable.

*Why adjustable:*
📚 Research on processing speed differences (Lee, 2024, *Journal of Attention Disorders* — verified: ~0.76 SD effect on math fluency in ADHD) establishes that a single fixed threshold is not appropriate for all learners. Extended time accommodations are documented in IEPs and 504 plans precisely because processing speed is a real variable. The threshold setting is the product's accommodation mechanism. 🏫 An ed therapist or tutor who has a student with a documented 5-second processing time accommodation should be able to set the game to that standard without workarounds.

*What happens when threshold changes:*
🎨 All prior practice data is recalculated against the new threshold. A visible notice appears before the change is applied: *"Changing the threshold will recalculate your practice tiers using the new standard. Your response time data is never deleted."* The constellation may look different after a change — this is correct and expected. The notice makes the behavior legible rather than alarming.

**Mini-game speed (Slow / Medium / Fast)**
Controls the speed of elements in Star Quest mini-games (e.g., how fast blocks fall in Falling Facts).

*Why:*
🏫 Different students have different motor processing speeds and different levels of gaming experience. A student who is new to the game or has fine motor challenges may need Slow. A student who finds the mini-games too easy on Medium may want Fast. This is not difficulty — it is pacing.

---

## User Management

### Profile chip
Visible on all screens. Shows current user's name/avatar. Clicking opens the user menu.

**User menu contains:**
- Switch User (list of profiles on this device)
- Add New User
- (Future: data backup, settings)

*Why chip everywhere:*
🎨 The student should always be able to see whose session this is and switch if needed — especially important in household or tutoring contexts where multiple users share a device. The chip is ambient presence, not a navigation element.

*Why chip opens user menu (not mid-game navigation):*
🎨 Prior to this design, the chip opened a navigation overlay mid-game, which created confusion — the student would accidentally navigate away from a round. The chip's job is user management, not round navigation. These are different things that should not share the same entry point.

**User profiles**
- Username (generated or custom) — no real name required, no email, no password
- Avatar (emoji + color)
- All data scoped to the username on this device

*Why no email/account:*
🎨 The product's philosophy is local-first. No account required = no barrier to entry, no privacy concern, no sign-in friction. A 9-year-old can create a profile in 10 seconds and start practicing. ⚙️ localStorage is the data layer — no server, no transmission, no COPPA exposure in current architecture.

**Delete user**
- Requires checkbox confirmation before delete
- Destructive — all data for that user is removed
- 🔄 Full reset vs. per-operation reset (design before building)

*Why confirmation modal:*
🎨 Destructive actions require friction. A student who accidentally taps Delete should not lose months of constellation data without a confirmation step. The checkbox pattern (not just "Are you sure?") requires an intentional action.

---

## Data Architecture — How the Game Measures and What It Does Next

### The full chain for every practice attempt

```
Student sees fact
    → Student types answer + presses Enter
    → Response time recorded (milliseconds from fact appearance to Enter)
    → Answer checked: correct or incorrect?

If CORRECT:
    → Response time compared to fluency threshold
    → If ≤ threshold: recorded as FLUENT response
    → If > threshold: recorded as ALMOST response
    → Fact pool: fact is retired from remaining round pool
    → Constellation: tier recalculated from updated data (rolling window)

If INCORRECT (first time this fact in this round):
    → Recorded as NEEDS PRACTICE response
    → Fact re-queued for later in the round

If INCORRECT (second time this fact in this round):
    → Recorded as NEEDS PRACTICE response
    → STAR QUEST ACTIVATES
        → Round pauses, timer pauses
        → Student completes: Find It → mini-game → Prove It
        → Star Quest attempts recorded (separately tagged)
        → Student returns to round
        → Fact removed from remaining round pool

If TIMER EXPIRES (no answer within threshold):
    → Recorded as no-response / miss
    → Fact re-queued for later in the round (or removed, depending on pool logic)

END OF ROUND:
    → Results screen shows per-fact performance
    → Constellation tiers recalculated
    → New mastered facts flagged if criteria met
    → Session recorded (date, operation, round length, elapsed time, PQ time per fact)
```

### How tiers are calculated

Tier assignment reads from the rolling window of recent practice data for each fact:
- **Mastered (gold):** Full mastery criteria — 3+ qualifying sessions / 3+ calendar dates / ≥3 attempts per qualifying session / fluent in recent window (🔄 N-day recency gate — being tuned in beta)
- **Fluent (amber):** Meets fluency threshold consistently in recent practice; variance is low
- **Almost (blue):** Correct in recent practice but not consistently within threshold; or correct with higher variance
- **Needs Practice (purple):** Incorrect responses dominate recent attempts; or no consistent correct pattern
- **Unpracticed (dim):** No attempts recorded

*Why variance matters:*
📚 Stickney, Sharp & Kenyon (2012, *Assessment for Effective Intervention*, 37 — verified with caveat) showed that response time variance is a mastery signal — a fact answered sometimes in 1 second and sometimes in 4 seconds represents less stable retrieval than a fact answered consistently in 2 seconds. The tier system uses both average response time and variance, not just average. A "lucky fast answer" does not move a fact to Fluent if the variance is high.

### How Star Scan data flows differently

```
Student sees fact (Star Scan)
    → Student types answer + presses Enter (one attempt only — no retry)
    → Response time recorded
    → Compared to fluency threshold
    → Classified as: MASTERED (within threshold, correct) or NEEDS PRACTICE (incorrect or over threshold)
    → Saved to Star Scan Records (separate data store from practice data)
    → Constellation: NOT updated (except Beginning Star Scan at onboarding)
```

*Why these two streams never mix:*
📚 Practice data and probe data have different reliability profiles. Practice data is high-volume, multi-session, and supports variance calculations. Probe data is single-attempt, cold-retrieval, and is designed as a snapshot. A tier calculation based on a mix of both would be neither a reliable practice signal nor a reliable assessment signal — it would be noise. The data stores are strictly separated.

---

## Open Items Affecting Screen Design

These decisions are made but not yet built, or are still being tuned:

| Item | Status | Note |
|---|---|---|
| Smart Play filtering logic | Designed, not built | All Facts + Challenge Level is current proxy |
| Galaxy View visual polish | Simple display for beta; full design later | Pip to design when prioritized |
| Star Forge free vs. paid | Open — do not gate yet | Design session needed |
| Mini-game overlay (fact click → practice) | Spec confirmed; build when prioritized | No name for the overlay |
| New user onboarding/setup series | Design before build | Full session needed |
| Payment/licensing flow | Design before build | Processor TBD — Lemon Squeezy account denied (site not polished enough at time of application); re-apply when copy/product are ready, or choose alternative |
| Beginning Star Scan data routing | Design before wiring | Quick Start seeds table-level tiers (3-tier seeding); Full Star Scan seeds per-fact tiers. Quick Start spec in Methodology Reference Part 8. |
| Mastery session count | 🔄 Currently 3/3 calendar dates | Will adjust based on beta data |
| Challenge Level ratios | 🔄 Exact numbers being validated | Adjust if beta shows too hard/easy |
| Star Scan session count (÷, +, −) | TBD | After beta on those operations |
| Freshness flag N-day window | TBD | After beta on inactivity patterns |
| Per-operation reset | Design before build | Full vs. per-operation reset; destructive |
| Empty state graduation check | Needs simpler signal | >80% mastery proximity before "Nice work!" |

---

*This document reflects build state and design decisions through Session AO (April 17, 2026).*
*Update when Wright builds new screens, navigation changes, or design decisions are revised.*
*Cross-reference with Math_Fact_Galaxy_Methodology_Reference.md for deep-dive on research citations.*
