# Agent Handoff — Wright ↔ Spark ↔ Pip ↔ Pop ↔ Legal
*Shared coordination file between the Sparkwright Claude agents.*
*Last updated: 2026-04-18 — Session AP (Pip)*

**Wright** — Coding & Project Management *(the craft, the build, the how)*
**Spark** — Research, Development & Pedagogy *(the ideas, the why, the research)*
**Pip** — Brand & Visual Design *(the look, the feel, the logo)*
**Pop** — Digital Printable Products *(the companion products, the offline layer)*
**Legal** — Intellectual Property & Compliance *(trademarks, terms, privacy, pre-launch checklist)*

---

## What This File Is

This is the communication layer between Wright (Coding & Project Management) and Spark (Research, Development & Pedagogy). Neither agent can message the other directly — the developer relays by saying "go read the handoff" or "Wright/Spark left you something."

**How to use it:**
- When Wright needs a research or pedagogy decision before he can build, he flags it here under **Wright → Spark**
- When Spark has a design idea or research finding that affects the code, she flags it here under **Spark → Wright**
- When Pip has brand or visual decisions that affect the site code (color tokens, fonts, assets), she flags it here under **Pip → Wright**
- After reading, the receiving agent replies in-line and marks it resolved
- Keep entries dated and brief — this is a coordination tool, not a discussion forum
- The developer should not need to explain context; each entry should be self-contained enough for the other agent to act on

**Archival practice (agreed Session S):**
When an entry is fully actioned — built, committed, and acknowledged by both agents — delete it from the active section entirely. Do not move it to Resolved; just remove it. Git history preserves everything if it's ever needed. The goal is a handoff file that stays short enough to be read in full without token overhead. Neither agent should let resolved entries accumulate. Clean up your own entries when they're done.

**Important — this is not a gate:**
Kimberly can make design decisions in either window and build in either direction without routing through the other agent first. Creative decisions can and should arise organically. The handoff exists to keep both agents informed, not to create a required sequence. If Wright builds something based on an in-session design decision, he notes it here so Spark stays current. If Spark develops a design idea, she flags it here so Wright can pick it up. Neither agent should tell Kimberly she has to go talk to the other one before moving forward — just flag what the other needs to know and keep building.

---

## Wright → Spark — 2026-04-18 — Session AQ close (v83w–v83x)

**Shipped:**
1. ✅ Font audit (v83w) — Comfortaa 700 on `.bmc-screen-title`, `.overlay-title`, `.setup-logo`, `.results-title`, `.assess-results-title`, `.starscan-info-card h2`
2. ✅ Title screen punch-up (v83w) — new B4 star lockup (108px, breathing), "Galaxy" in #ffd280, ambient brand-color starfield, 35 JS twinkling stars, 5 shooting sparks, 3 radial pulse rings
3. ✅ Extended timer dual-zone (v83x) — amber progress bar with pulsing halo (0s → threshold), flat purple→blue extended zone (threshold → autokick), threshold tick. Autokick now unified to `autokickMs` in all modes; grading at `fluencyMs` unchanged.

**Design decision to flag — Star Quest mode card:**
Kimberly made an executive call this session: the Relaxed/Challenge mode selector is **a BMC setup setting**, not an overlay that fires on the first SQ trigger. It appears conditionally in the BMC setup card when Star Quest is enabled. Questions (1) pre-highlight, (2) teacher lock, (3) per-trigger or per-round are resolved: no pre-highlight, no teacher lock for now, choice applies for the full round (set at round start, not per trigger). Flag if you have a pedagogical concern with moving it to setup.

**Not yet pushed to Netlify.**

— Wright, 2026-04-18

---

## Pip → Wright — 2026-04-18 — Galaxy View star state correction

**galaxy_view_mockup.html updated.** Star states corrected from THREE to TWO.

**What changed:**
- Removed amber in-progress state entirely — no amber stars at any stage
- Stars are unlit (dim dot) or gold-with-halo (ALL facts in table mastered) only
- Added `.star-halo` ring (gold stroke, 3.2s breathe animation) to gold stars
- JS `applyStarState()` now dynamically inserts/removes halo circle per star
- Demo states updated: all `'a'` entries converted to `'u'`
- Removed `glow-amber` SVG filter, amber CSS block, `star-pulse-amber` keyframe
- `updateLineOpacity()` now keys on mastered-only ratio (was mastered+amber)

**Build spec for Wright:** Implement exactly as shown. No amber state in production code. Binary: unlit until the full table is mastered, then gold with halo ring.

— Pip, 2026-04-18

---

## Pip → Wright — 2026-04-18 — Star Quest mode card + Extended timer dual-zone

**Extended timer: ✅ BUILT v83x (2026-04-18)**

**Star Quest mode card: design changed — see Wright → Spark below.**

Visual spec for SQ mode card (Relaxed 🌙 / Challenge ⚡) still valid per mockup.
Build location changed: now a BMC setup setting, not a per-trigger overlay.

— Pip, 2026-04-18

---

## Spark → Wright — 2026-04-18 — Session AP (Star Quest mode card + extended timer + scan lifecycle + Star Forge updates)

**Design decisions from Session AP. Read before building the affected areas.**

---

### 1. Star Quest — mode card (per-session, not a settings item)

Remove the Star Quest timer toggle from any settings consideration. Instead: when Star Quest triggers (second wrong answer on a fact), immediately before the first quest content loads, show a brief overlay card:

**Two modes:**
- **Relaxed** 🌙 — no time pressure during the quest
- **Challenge** ⚡ — time pressure during the quest

Student taps one choice; quest begins. The card is not a gate — it's a quick, in-context choice. Emoji does the visual work; minimal copy.

**Data note:** Log which mode was used in session metadata. Neither mode changes tier grading. Mode is a session experience flag only.

**Pip brief:** See Spark → Pip entry for visual direction.

---

### 2. Extended timer — amber glow visual spec

Timer bar in BMC now has two visual zones. Do not stop the bar at the fluency threshold — run it to the autokick window (up to 6s):

- **0s → fluency threshold (e.g., 0–3s):** Amber glow — warm, visually impactful, special. Looks like an achievement state.
- **Threshold → autokick (e.g., 3–6s):** Flat color — purple transitioning to blue. Matches the tier colors. No glow.

**Grading is unchanged:** fluency threshold is still the grading cutoff. The dual-zone bar honestly shows the student which zone their response landed in without changing the standard.

**Why this matters:** A student who can't hit 3s on hard facts but doesn't want to lower their threshold now has a visual path — they see exactly where they landed, get credit for the answer, and understand the signal without the standard changing.

---

### 3. Monthly Star Scan — 30-day date lock

When a student completes a Monthly Star Scan, the next Monthly Scan becomes available 30 days from that date (date only, no timestamp precision). The scan does not auto-expire while locked — it simply isn't available until day 30.

---

### 4. Beginning Scan — window closes based on activity

The Beginning Star Scan window closes when the student has:
- 3+ completed practice sessions, **OR**
- Practiced facts across 4+ tables

When the window closes, the first Monthly Scan opens immediately — no additional wait. From that point the 30-day Monthly Scan cadence applies.

A student who skips the Beginning Scan and hits the threshold goes directly to the Monthly Scan track with no seeded inferred data (constellation builds from practice only — valid path, slower visual start).

---

### 5. Star Forge — architecture updates

**Top-level choice:** Entry into Star Forge now presents a Round Practice vs. Scan choice before any session settings appear. Both modes on the same page; settings branch from the selection.

**Scan mode in Star Forge** (does NOT write to constellation):
- Runs a structured diagnostic scan
- All data recorded: response times, per-fact results, session summary
- Stored in Star Forge session records only — no constellation writes
- Teacher use case: run a diagnostic on a student's account without affecting their constellation; or run as your own account to test without contaminating your own data

**Session naming field:**
- Each Star Forge session has a name/ID field
- Default auto-fill: date + time (e.g., "April 18, 2026 · 3:42 PM")
- User can override with any custom text (student username, initials, session label)
- **Profanity filter required** — basic blocklist on the name field; check on submit (not live). Teachers know what students will type.

---

### 6. Settings — persistence principle

All user-selected settings persist until the user changes them. No silent resets on session start. Whatever was set last is what appears next time. Applies to: fluency threshold, mini-game speed, round length defaults, Star Quest on/off preference, Challenge Level, and all future settings.

— Spark, 2026-04-18

---

## Spark → Pip — 2026-04-18 — Session AP (Star Quest mode card + extended timer + recently played toggle)

**✓ ACTIONED 2026-04-18 by Pip** — all three items built. See `dev/star_quest_and_timer_mockup.html` and `dev/constellation_session_compare_mockup.html`.

Three visual design items from Session AP decisions.

---

### 1. Star Quest mode card

Appears as an overlay card immediately when Star Quest triggers, before the first quest content loads. Student makes one tap; quest begins.

**Two modes:**
- Relaxed — no time pressure
- Challenge — time pressure

**Direction:** Emoji does the visual work — one strong emoji per mode. Copy is 1–2 words max. The card should feel light and in-game, not like a settings screen. Not alarming. Suggest emoji pairings (🌙 / ⚡ or similar) — Pip's call on final icons and copy. Card disappears immediately after selection.

Deliverable: card design, emoji/copy pairing suggestions, and overall feel.

---

### 2. Extended timer — amber glow vs. flat zone

The BMC timer bar has two visual zones:

**Fluency zone (0s → threshold, e.g., 0–3s):** Amber glow — desirable, warm, alive. Reference the amber/gold aesthetic used for Fluent tier and mastered stars throughout the product. Answering here should feel like the ideal. Should be visually impactful — not just a different hue, but a different presence. Consider: does the bar get thicker in the amber zone? Does it pulse slightly? Does it have a warm halo?

**Extended zone (threshold → autokick, e.g., 3–6s):** Flat, plain. Purple transitioning to blue matching the tier colors. No glow, no urgency. Neutral — the student answered, just outside the fluency window. Not alarming, not red.

The contrast between the glowing amber zone and the flat extended zone is the key design challenge. The goal is that answering in the amber zone looks like an achievement without the extended zone looking like failure.

Deliverable: timer bar visual spec for both zones.

---

### 3. Recently played toggle

On the My Constellation screen: a user-controlled button or toggle that lets the student compare their constellation before and after the most recent session.

**What it does:** Student taps → overlay shows constellation as it was before the last session (pre-session state). Current constellation (post-session) is always the default view. Student toggles back and forth to see what changed — which facts moved tiers, what's new.

**Direction:** Should feel celebratory — a "look how far I came" moment, not a diagnostic. The before-state is dimmer/older than the current bright live state. Student controls when they see the comparison. Consider: how is the before-state visually distinguished? How is the toggle/button labeled? How does the student dismiss the comparison view?

Deliverable: toggle/button design, before-state visual treatment, and dismissal behavior.

— Spark, 2026-04-18

---

## Spark → Wright — 2026-04-17 — Session AN (Star Lab + Galaxy View — build-ready)

---

### Star Lab — mini-game overlay from My Constellation

**Name confirmed: Star Lab.**

This is the targeted practice overlay accessed from inside My Constellation. It is student-initiated (not triggered automatically like Star Quest). No name appears in external copy — it is the experience behind the "Practice" button on the fact stats card.

**Full flow:**

1. Student is in My Constellation, clicks any fact cell (e.g., 7×8)
2. Stats card opens — shows response time history, current tier, trend
3. Student clicks **"Practice"** button
4. Star Lab overlay opens — shows three mini-game options (Falling Facts / Find It / Prove It) with brief icon + one-line description each
5. Student picks one
6. Quick round launches: **that fact only, both orientations, ~6 attempts total** (3 reps of 7×8, 3 reps of 8×7, interleaved — not sequential)
7. **No Star Quest within Star Lab** — student is already in a targeted remediation context; repeated misses are noted in results but do not trigger a nested quest
8. Brief results screen showing performance on this fact in this session
9. Returns to My Constellation — constellation updated, that fact's cell reflects new attempts

**Data:**
- Writes to constellation (legitimate practice data)
- Tag source as "targeted-practice" for separability in future analysis
- Round-level tracking var needed: has each orientation been shown in this Star Lab session? Do not repeat an orientation until both have been used.

**What Star Lab is not:**
- Not a full round — scoped to one fact only
- Not Star Quest — Star Quest is automatic and triggered by the game; Star Lab is student-initiated
- Not a replacement for BMC — it is targeted remediation between full rounds

---

### Galaxy View — constellation visual, build-ready for beta

**Beta approach — Option A (table-level stars):**
Shapes are inspired by real constellations but adapted to match fact table count. They carry the visual spirit of the real shape without claiming astronomical accuracy. Star Bloom (V2, see below) is where full IRL accuracy lands.

**Data mapping — each star = one fact table:**
- Multiplication: 12 stars (×1–×12) — Orion-inspired, adapted to 12 stars
- Division: 12 stars (÷1–÷12) — Libra-inspired, adapted to 12 stars
- Addition: 10 stars (addend groups 1–10) — Cassiopeia-inspired, adapted to 10 stars
- Subtraction: 10 stars (derived from paired addition groups) — Gemini-inspired, adapted to 10 stars

**Star visual states — TWO STATES ONLY (corrected 2026-04-18):**
- **Unlit** — tiny dim white dot, very low opacity (an ember not yet burning)
- **Fully lit** — bright gold star with halo ring + glow, full size; star only lights when ALL facts in that table are mastered. No amber in-progress state — a table is either unlit or fully earned.

*Note: original spec included an amber in-progress state. This was removed. See Spark_Agent_Prompt.md line ~206 for correction rationale.*

**Connecting lines:**
Thin white lines between stars, very low opacity — show the constellation shape even when stars are unlit. Always present.

**Background:**
- Deep space: near-black with subtle blue undertone
- Sparse CSS-generated star field (small random dots, low opacity — atmosphere only, not interactive)
- Four constellations in foreground, larger and more defined than background field

**Layout:**
- Full-screen view triggered by "View My Galaxy" button inside My Constellation
- 2×2 fixed grid matching title screen:
  - × top-left, ÷ top-right, + bottom-left, − bottom-right
- Each constellation centered in its quadrant with breathing room
- Each tile tappable — navigates to My Constellation for that operation
- Close / Back returns to My Constellation for the operation the student was viewing

**No copy on the tiles — visual data only.**
The scene reads as art. No labels, no progress text, no numbers. A mostly-lit shape next to a dim one tells the story without words.

Only orientation marker: a small operation symbol (×, ÷, +, −) at the outer corner of each quadrant — subtle, like a map glyph. From a distance: pure art. Up close: findable.

---

**V2 concept — Star Bloom (design session needed with Pip, do not build yet):**

When the core Galaxy View is stable, Pip to design and Wright to build a zoom layer:
- **Zoomed out:** True IRL constellation shape and star count (Orion's 7, Cassiopeia's 5, etc.) — astronomically accurate, glowing as a whole shape
- **Tap to zoom:** Constellation expands; each star "blooms" open to reveal individual facts clustered around it; the math fact (e.g., 7×8) or operation symbol lives at the heart of each star
- Resolves the IRL star count vs. 144 facts tension: macro view = accurate art; micro view = granular data
- **Flag for Pip:** Needs a full design brief — two rendering states, zoom transition feel, how facts arrange around each star node, whether operation symbol or fact label lives at the center

---

### Build sequence for this session (Star Lab + Galaxy View)

1. **Star Lab overlay** — overlay shell, mini-game picker, 6-attempt single-fact round, brief results, return to My Constellation with updated cell
2. **Galaxy View** — four constellation SVG shapes (table-level stars), three star states, connecting lines, background star field, 2×2 layout, tile navigation, operation symbol glyph per quadrant

---

### Smart Practice — spec for next session

`buildBMCMixPool()` is the foundation. Smart Practice feeds it a constellation-informed priority stack instead of a random shuffle.

**Fact selection order (priority stack):**
1. **Fluent (amber)** — fill first; highest leverage (meets threshold, needs more sessions for mastery)
2. **Almost (blue)** — fill second; correct but not yet fast enough
3. **Needs Practice (purple)** — these are the challenge facts; count governed by Challenge Level
4. **Unpracticed (dim)** — also challenge facts; always inject 2–3 per round regardless of Challenge Level (new facts need introduction)
5. **Mastered (gold)** — sprinkle only: 1–2 per round, rotating by oldest `lastSeen`, to keep timestamps fresh

**Challenge Level interaction:** unchanged — still controls challenge fact count (Needs Practice + Unpracticed). Smart Practice just ensures fill slots come from the top of the priority stack, not a random draw.

**Fallback when constellation data is thin (< 10 practiced facts):** Grey out the Smart Play button on the setup card. Note: "Play a few rounds first to unlock Smart Practice." Do not silently fall back to All Facts — the student should understand why it's unavailable.

**Pre-build check for Wright:** Does `buildBMCMixPool()` currently read per-fact tier data, or does it only know the Challenge Level ratio and draw randomly? If the latter, Smart Practice needs it to accept a pre-sorted fact array as input. Check before touching it.

— Spark, 2026-04-17

---

## Wright → Spark — 2026-04-17 — Session AN close (v83s–v83u, pushed)

**All four of your 2026-04-16 build items are shipped.**

1. ✅ Bug #7 (confirm() kick-out) — replaced with leave-game modal (v83q). Full kick-out audit also done in v83t–v83u: `sw-game-label` header, Enter key handler overlay guard, `pauseEndRound()`, link intercept — zero native confirm() dialogs remain.
2. ✅ BMC timer — kicks at `fluencyMs`, honors user's tier setting.
3. ✅ Challenge Level (Kimberly renamed from "Today's Mix") — Gentle/Balanced/Intensive on BMC setup card; `buildBMCMixPool()` built.
4. ✅ Star Quest toggle — checkbox on BMC setup card, checked by default.
5. ⏸ Thin pool two-orientation behavior — deferred, noted in Wright prompt.

**Star Lab + Galaxy View spec received and read.** Both are queued for the next session. Kimberly is beta testing v83u today — will report results before the next build session.

— Wright, 2026-04-17

---

## Spark → Wright — 2026-04-16 — Session AN (Beta testing decisions — build-ready)

**All four of Wright's questions answered below. New design items follow. Read everything before building BMC settings.**

---

### 1. BMC timer — ANSWER

**Kick at the fluency threshold (`fluencyMs`), not the autokick window.**

Rationale: BMC is a fluency-building context. The visible countdown bar should represent the standard being measured — if fluency is graded at 3s, the bar should run 3s. A 7s bar that grades at 3s sends a mixed signal: the student thinks they have more time than they're actually being evaluated on. The autokick window (7s) was appropriate in practice contexts where you want to allow retrieval attempts. In BMC, the purpose is automaticity — the bar running to the threshold is the honest experience.

**Honor the user's fluency threshold setting** for both grading AND kicking in BMC. If the teacher has set 5s for an accommodation, the bar runs 5s. This is correct — the accommodation applies to both the grade and the time pressure.

---

### 2. BMC print report — confirmed, log and batch

Confirmed: add to BMC print output — total round time (including time in Star Quest), and per-fact breakdown of time in main round vs. time in each Star Quest entry (which fact, how long). Not blocking. Batch with other print work.

---

### 3. Crash bug — CRITICAL #1 priority

Wright's confirm() theory is the leading candidate. Fix: replace midgameNav confirm() with a styled modal (consistent with user delete pattern already shipped). Also add error handling around endGame()/nextQ() near pool exhaustion. This is #1 before any new builds.

---

### 4. Smart Practice / cognitive load — ANSWER + new settings spec

**3–5 challenge facts per round is pedagogically correct.** The principle is interspersal — interleaving known facts among challenge facts produces better retention of the challenge facts and maintains engagement. This is supported by the research framework (specific math-facts interspersal citations to be verified by Spark before use in copy). A round that is overwhelmingly weighted toward unknown facts exceeds cognitive load thresholds and is less effective than a mixed round, even for the challenge facts themselves.

**This unlocks a new BMC setting — build this:**

---

#### Challenge Intensity selector — "Challenge Level"

Add to BMC setup card. Student-facing daily choice. Default: Balanced.

| Option | Challenge facts per round | Fill behavior | Round length behavior |
|---|---|---|---|
| **Gentle** | 2–3 (Needs Practice + Unpracticed) | Fill with Fluent (amber) → Almost (blue) → Mastered sprinkle | Shortens round if fill content is thin — do not pad with extra challenge facts |
| **Balanced** | 4–6 | Fill with Fluent → Almost → Mastered sprinkle | Minor shortening if needed |
| **Intensive** | Up to 8–10 | Still ~30% Fluent/Almost interleaved — interspersal holds even here | Holds to round length setting |

**Label:** "Challenge Level" — not "Difficulty." Difficulty implies the math problems are harder. This controls the ratio of challenging-for-this-student facts. That's a different thing and should be communicated as such.

**Applies to:** Both All Facts mode and Smart Practice mode. Smart Practice still handles fact prioritization automatically — Challenge Intensity governs the ratio within that prioritization.

**Priority fill order within the fill slots:**
1. Fluent (amber) — highest leverage: already meets speed threshold, needs more sessions for mastery
2. Almost (blue) — needs speed improvement, still rewarding
3. Mastered (gold) — small maintenance sprinkle (keeps timestamps fresh, maintains fluency)

---

#### Star Quest toggle — add to BMC setup card

Checkbox on setup card, **checked by default.**
Label: "Include Star Quest (recommended)"

Rationale: A fatigued or resistant student forced into Star Quest produces worse data and less learning than a student who opts out for a session. The constellation data is identical either way. A teacher can see chronic opt-out as its own signal worth a conversation. "Quiet respect baked in."

Note: Once Star Quest kicks in mid-round, it still completes — the toggle only applies at session start.

---

#### New user / thin fact pool behavior

When a student's available fact pool is smaller than the requested round length:

1. **Use both orientations first.** 3×4 and 4×3 are distinct retrieval demands — not padding. Exhaust one orientation across all available facts, then offer the reverse orientation. This is pedagogically valid new practice.
2. **After both orientations are covered, shorten the round.** Do not cycle the same fact a third time. A 6-question round for a student with 3 facts (both orientations) is the correct outcome.
3. **If the round runs out of unique content:** show a brief end note — *"You've practiced all your current facts. Nice work!"* — and close the round cleanly with results showing.

Implementation note: Round-level tracking var needed — for each fact, has each orientation been shown this round? Separate from constellation data.

---

### Build sequence for this session

1. **Critical bug #7 first** — crash/data loss fix (midgameNav confirm() → modal + endGame error handling)
2. **Timer fix** — BMC kicks at `fluencyMs`, honors user threshold setting
3. **"Challenge Level" selector** on BMC setup card — Gentle / Balanced / Intensive
4. **Star Quest toggle** on BMC setup card — checked by default
5. **Thin fact pool behavior** — both orientations before shortening
6. **Print report timing** — log and batch, not blocking

— Spark, 2026-04-16

---

## Wright → Spark — 2026-04-16 — Session AN (Beta testing feedback — Spark input needed)

**Context:** Kimberly ran beta testing on v83p. These notes were shared with both agents. Spark input needed on pedagogy/design questions before Wright builds. Wright's technical read is in the notes below each item.

---

**1. BMC timer — calibration question**

The current BMC timer runs the full autokick window (7s for standard tier) as the visible countdown bar. Kimberly's note: one beta tester found it "too slow." She also notes there may be students who want urgency vs. students who do better with more time, and that there's usable time regardless of what it's measuring.

Wright's technical read: BMC hardcodes `S.format = 'pertimer'`, which uses `S.fluencyTier.autokickMs` (7s for standard). The fluency GRADE threshold is still 3s — so grading is correct, but the visible timer runs 7 seconds. The "too slow" complaint makes sense — the bar drains for 7 seconds when students know fluency is graded at 3s. Options:
- Kick at the fluency threshold (3s for standard) — creates urgency, enforces automaticity, but harsh for struggling students
- Keep 7s autokick, no change
- Add a BMC-specific timer speed setting
- Use `fluencyMs` (3s) as autokick in BMC but honor the user's fluency tier setting

**Spark: Is there a pedagogical reason to kick at the fluency threshold rather than the autokick in a building-fluency context? Should BMC honor the user's threshold setting for both grading AND kicking? Should this be a student-selectable option?**

---

**2. BMC print report — round time breakdown**

New feature request: BMC print report should show (a) total round time including PQ, and (b) time spent in each PQ for which facts vs. main round time.

Wright: this is buildable. The data is all available — `G.startTime`, PQ entry/exit timestamps. Currently the results screen shows total elapsed but doesn't break out PQ time per fact. Will need to add per-PQ timing to the game state object. Logging as a new build item, not blocking.

---

**3. BMC mid-round kick-out bug — CRITICAL**

Beta tester was at the end of a 20-question BMC round (near fact 20/20), was answering a fact, and got kicked back to the title screen with no results shown.

Wright: This is a data-loss / trust bug — highest priority to fix. My leading theory: the `midgameNav()` function uses a native browser `confirm()` dialog. If the user accidentally tapped the profile chip while typing an answer, the confirm dialog fires. Pressing Enter to submit the answer would also dismiss the confirm dialog as "OK" — navigating to title with no results. Second theory: a JS error in `endGame()` or `nextQ()` near the end of a full pool that silently prevents reaching `showScreen('results-screen')`. Need to add error handling and also replace the confirm() in midgameNav with a styled modal. Logging as CRITICAL Bug #7.

---

**4. Smart Practice / cognitive load — pedagogical question**

Beta tester felt too many challenging facts appeared repeatedly, causing high cognitive load and making rounds feel too long. Kimberly asks: should there be 3–5 challenge facts to focus on per round? And we need to flesh out Smart Practice and available BMC settings.

Wright: this is directly the Smart Practice design problem. Currently BMC uses All Facts, which shuffles all facts randomly. The fix is the Smart Practice filtering logic Spark flagged as "design before build." Without Smart Practice, the only lever is limiting re-queuing of wrong facts.

**Spark: Is 3–5 challenge facts per round the right target? What's the pedagogical basis for that number? This is the core Smart Practice spec question that was deferred.**

---

— Wright, 2026-04-16

---

## Wright → Spark — 2026-04-14 — Session AM (v83e–v83f)

**Shipped this session:**
- Starlight Math + Star Quest rename complete
- Mastery criteria: 3 qualifying sessions / 3 calendar dates / ≥3 timed attempts per session
- Ghost catch bug fixed in Falling Facts

**Questions answered by Spark — building now:**
- Star Forge confirmed (was Custom Cluster Creator)
- Build My Constellation confirmed (top-left nav area)
- All Facts now, Smart Play later
- "Practice" button label, Falling Facts / Find It / Prove It mini-game picker

**Still holding:**
- Constellation scatter view (design conversation only, not a build item)

— Wright, 2026-04-14

---

## Spark → Wright — 2026-04-15 — Session AM (Full restructure — read everything)

**This replaces and supersedes all prior Spark → Wright entries. Read in full before building anything.**

---

### Naming — update all display text

| Old name | New name | Notes |
|---|---|---|
| Math Flash | **Math Fact Galaxy** | Game title everywhere — third rename this session, this one is final |
| Practice Quest | **Star Quest** | All display text; internal function/class names stay as-is |
| Custom Cluster Creator / Starlight Math area | **Star Forge** | Confirmed |
| Play | **Build My Constellation** | Nav area name — confirmed |

---

### The Product Concept — read this first

**Math Fact Galaxy** is built on a four-operation architecture:
- Each operation (×, ÷, +, −) is its own **constellation**
- All four constellations together form the student's **galaxy**
- As facts are mastered, stars light up in each constellation
- The galaxy fills in as all four operations are learned

This is not just a name — it is the product's visual and structural logic. Build toward it from the start.

---

### Four-area navigation — confirmed structure

Title page: 2×2 grid.

| Position | Area |
|---|---|
| Top-left (primary) | **Build My Constellation** |
| Top-right | **My Constellation** |
| Bottom-left | **Star Scan** |
| Bottom-right | **Star Forge** |

---

**BUILD MY CONSTELLATION**
- Per-Question Timer only — no mode selection screen
- Two quick-select options on setup card: **All Facts** / **Smart Play** (constellation-informed; build Smart Play filtering logic separately — do not block on it)
- Operation selector on setup card — student chooses which constellation to build (×, ÷, +, −)
- Feeds the selected operation's constellation automatically
- **Build All Facts mode now and ship it**

**MY CONSTELLATION**
- Operation-aware — shows one constellation at a time; student can switch between all four (×, ÷, +, −) via selector/tabs
- Multiplication: 12×12 grid (already built) — no change
- Addition/Subtraction/Division: same grid-style layout; visual design pass later; empty state until student has data
- **Galaxy View** — button inside My Constellation: "View My Galaxy." Opens full-screen aggregate view showing all four constellations together. For beta: simple progress display per operation (% mastered or stars lit). Visual polish later.
- Fact click flow: stats card opens → **"Practice"** button → overlay with 3 Star Quest mini-games (Falling Facts / Find It / Prove It) → user picks one → quick round for that fact → returns. No name needed for overlay.
- Records & Print archive: practice session history + Star Scan records + print from here

**STAR SCAN**
- No structural change to existing build
- Add: **"Print Targeted Deck"** button in Star Scan results — prints gap deck of needs-practice facts only (see print spec). Direct output, does not route through Star Forge.
- Full Star Scan: **both orientations by design** (exhaustive = exhaustive)
- Star Scan accessed from Star Forge = report only, no constellation writes
- Star Scan should work across all four operations

**STAR FORGE**
- Full session builder: all settings (operation, range, timer, mode) + Star Scan-style question formats
- Supports all four operations and both ranges (standard + advanced)
- Results go to session report only — no constellation writes
- Lightweight session-level records; may be used without a user account
- Free vs. paid: **still open — do not gate yet**

---

### Four-operation fact ranges — confirmed

| Operation | Standard | Advanced |
|---|---|---|
| Multiplication | ×1–×12 | ×13–×20 |
| Division | ÷1–÷12 | ÷13–÷20 |
| Addition | addends 1–10 (sums ≤ 20) | addends 11–20 |
| Subtraction | derived from addition standard | derived from addition advanced |

**Note on Advanced Addition:** Addends 11–20 involve regrouping strategies, not pure recall. Label this tier **"Advanced"** (not "Extended") in the UI to signal a different kind of challenge. Copy note for later.

**Grid design for addition/subtraction advanced range** (11–20 addends = large grid): data structure and range selector first; visual grid design pass later. Do not block beta on this.

Division and subtraction derive from their paired operations — same constellation grid, inverse presentation.

---

### Print system — confirmed, two paths

**Path 1: Custom Deck Print** (from Star Forge)
- Teacher builds settings → runs digital session OR clicks Print
- Printable flashcard sheet matching exact specs
- Offer 8-per-page (2×4) and 10-per-page (2×5) as a print setting
- Card front: problem (7 × 8 = ?), back: full equation (7 × 8 = 56)
- Tier color border + text label (e.g. "Needs Practice") for B&W compatibility
- Ordered by table; Sparkwright mark in corner

**Path 2: Gap Deck Print** (from Star Scan results)
- "Print Targeted Deck" button in Star Scan results
- Needs-practice facts only; same format as Path 1
- Direct output from results — does not route through Star Forge

Print available contextually at point of action everywhere. Full archive in My Constellation → Records. Star Forge has its own session-level records.

---

### Pedagogy answers — confirmed

**Full Star Scan orientations:** Both by design. Exhaustive = exhaustive.

**Practice session definition:** 3 sessions minimum, 3 different calendar dates, ~3 timed attempts per session to qualify. Tune during beta.

**Star Quest engagement concern:** No design fix needed. Monitor in beta.

---

### Build sequence

1. **Rename throughout: Math Fact Galaxy, Star Quest, Star Forge, Build My Constellation** — do this first
2. **Title page 2×2 grid** — shell: Build My Constellation, My Constellation, Star Scan, Star Forge
3. **Build My Constellation** — All Facts mode, operation selector, feeds correct operation's constellation
4. **My Constellation** — operation switcher (×, ÷, +, −); Galaxy View button (simple progress display for beta)
5. **Four-operation data model** — ensure fact data stored per-operation across all four; multiplication already done
6. **Star Forge, Records, mini-practice** — each as separate builds when prioritized

---

### Still open

- [ ] Smart Play filtering logic — design before build; ships after All Facts
- [ ] Galaxy View visual polish — simple progress display for beta; full visual design later
- [ ] Addition/Subtraction grid visual for advanced range — data structure first, grid design later
- [ ] Empty state graduation check — needs >80% mastery proximity signal
- [ ] Star Forge free vs. paid — open, do not gate yet
- [ ] Mini-game overlay — spec confirmed above; build when prioritized

— Spark, 2026-04-15

---

## Wright → Spark — 2026-04-13 — Session AK close (v82a–v82k)

**Fact Catcher mini-game — shipped and in Fact Catcher.** Full build across this session and the prior one. Summary:
- 5-star win condition, inactivity timer (not countdown), 3 lanes, controlled distractor-heavy spawn ratio, lane enforcement (no same-lane correct cards consecutively), cooldown after correct catch
- Progress display: CSS dots (yellow filled, white outline empty) — no emoji
- Wrong catch: lose 1 dot, freeze + ghost flash; 0-star guard (no effect if no progress yet)
- Kid exploit fix: MAX_WRONG=8 total wrong catches forces advance to next PQ step
- Mini-Game Speed setting in Setup → Practice Features (Slow/Medium/Fast, persisted)
- PQ step pips now stack below the "⚡ Practice Quest" badge

**Mini-game madness area — flagging for Spark.** Kimberly's concept: a place (likely in My Constellation) where a student clicks a fact and gets a card with mini-games they can play to practice it. Clicking a mini-game launches it directly for that fact. Needs a better on-brand name than "mini-game madness" — Spark should name it and sketch the spec. Not built, not in the MPF yet.

**Empty state graduation check — flagging for Spark (open from v82).** "Nothing to see here. Nice work!" currently shows whenever Facts to Watch is empty and the user has data. Should only show when the student is close to mastery (>80% of facts mastered). The check requires iterating constellation cells. Spark flag: is there a simpler mastery-proximity signal we can use before building the full cell-count approach?

**6 critical bugs from v82j remain open** — see Wright prompt bug queue for full descriptions.

---

## Spark → Wright — 2026-04-11 — Session AI (revenue model absorbed + Beginning Star Scan confirmed)

**Flint's revenue model correction — absorbed. Beginning Star Scan architecture confirmed. Multi-session Full Star Scan spec holds — build-ready for beta once testing clears.**

**Revenue model — what changed and what it means for the build:**
- Paid tier = records/tracking layer. Not a user-type gate.
- Homeschool parents and tutors/ed therapists both want records. No copy, prompt, or UI should distinguish them by tier.
- IEP documentation language is dropped entirely. Do not reference it anywhere.

**Beginning Star Scan architecture — CONFIRMED under new model:**
- **Quick Start Scan** = free, once, at onboarding. Seeds ghost constellation. Table-level output (~20 questions). No change to spec.
- **Full Star Scan** = paid tier. Per-fact, exhaustive, multi-session. All specs from Session AH hold exactly.

**Multi-session Full Star Scan spec (Session AH) — confirmed build-ready for beta.**
No changes. Proceed as written once testing clears.

**Welcome overlay — recommendation for `completeMFWelcome('scan')` routing:**
Route the Beginning Star Scan button to Quick Start Scan. Do not route to Full Star Scan. Add a brief note near the button: *"Full Star Scan available with upgrade — unlocks per-fact tracking and printable records."* Don't open with a paywall — let Quick Start seed the ghost constellation, upgrade prompt comes naturally at session-10 freeze.

**Copy framing — applies everywhere tier language appears:**
Drop any language that implies "professional = paid, homeschool = free." The distinction is experience vs. records.

The following tier chart is approved by Kimberly for use in product copy (About page, FAQ, upgrade prompt, onboarding):

| | Free | Paid |
|---|---|---|
| Full game, Practice Quest, all settings | ✓ | ✓ |
| Quick Start Scan (onboarding, once) | ✓ | ✓ |
| 10 calendar-day constellation tracking | ✓ (ghost) | — |
| Live constellation (unlimited) | — | ✓ |
| Full Star Scan (Beginning, Ongoing, Final) | — | ✓ |
| All Star Scan records, printable | — | ✓ |
| Print reports | — | ✓ |

— Spark, 2026-04-11

---

## Wright → Spark — 2026-04-11 — Session AJ close (v79–v81)

**Spark AI notes absorbed.** Revenue model, Beginning Star Scan architecture, and Full Star Scan spec all confirmed. Quick Start = free onboarding. Full Star Scan = paid. Welcome overlay routing: "Yes, start with a Star Scan" → Quick Start Scan, with "Full Star Scan available with upgrade" note alongside button. Will build once nav consistency issues (below) are resolved.

**v79–v81 build summary — all committed:**
- Star Scan results: "Mastered" → "Fluent" throughout scan context. Summary stat row removed. Print from live results now functional. Navigate overlay bug fixed.
- Star Scan setup: Threshold "Change" link removed. Settings now persist across opens. Default changed to ×3, ×4, ×5 Per-Table scope.
- Facts to Watch: Rebuilt. Priority order: needs-practice → almost → unpracticed. Cap 5, single row, no tier labels, color-coded top border (blue/purple/dim). Smart empty state. Em dash removed. Tooltip updated.
- My Constellation: "Go to Star Scan Area" button removed.
- Profile chip: Chip from stats-screen and assess-area-screen now opens user menu (not mid-game nav overlay).
- User management (Math Flash): Delete button added to Switch User overlay with checkbox confirmation modal. Card widened to 400px.
- User management (Sparkwright homepage): Custom delete confirmation modal replacing confirm(). Trash icon display bug fixed.
- Delete modals both places: "data" hyperlink placeholder added (wire to backup page when built).

**Critical bugs found during testing — NOT YET FIXED — priority for next session:**

1. **User context does not reset on switch/create/delete.** When a user is switched, created, or deleted from any screen other than the title screen, the active screen (e.g. My Constellation) keeps showing the previous user's data. New user activity can bleed into the wrong account. Fix: any user switch/create/delete from any location must (a) update active user in localStorage, (b) force reload of all data-dependent UI, (c) navigate to title screen. This is the highest-priority bug before beta.

2. **Welcome flow triggers on existing users after switch.** Switching to an existing onboarded user is re-triggering the welcome overlay. Root cause likely: `mathflash_onboarded_[username]` flag check is running on the wrong timing or the wrong username. Investigate `checkMFOnboarding`.

3. **Profile chip inside assessment-screen (mid-scan) still shows "Navigate" overlay.** The v79 fix only covers `assess-area-screen`. The `assessment-screen` (active during the scan) is correctly in the mid-game nav path — BUT the scan timer doesn't pause when the chip is clicked. The nav overlay should either pause the timer or be replaced with the user menu for mid-scan (since you can't switch users mid-scan anyway — that would be destructive). Design decision needed: what does chip-click do while a scan is actively running?

4. **Nav consistency redesign.** Profile chip behavior across all screens needs a single coherent model rather than piecemeal fixes. Suggested design for next session: chip click always opens user menu. Mid-game navigation (leave round / go to constellation) lives on a separate button or the round header. This avoids the chip/nav confusion entirely.

5. **Star Scan record delete.** Need a delete button on each Star Scan record (Star Scan Area + My Constellation) with the same checkbox-gate modal pattern as user delete.

6. **"Nothing to see here. Nice work!" empty state** — currently triggers whenever there are no needs-practice/almost/unpracticed facts, even for users who are fluent but not close to mastery. Needs a graduation proximity check (suggest: >80% of facts mastered) before showing this message. Flag: the graduation check requires iterating all constellation cells, not just userFacts keys.

**Flag for Spark — Star Scan reversals:** Should Full Star Scan include both orientations by design (per Spark's orientation principle), or should it be a user toggle? Wright's read: Full Star Scan includes both orientations by design (exhaustive = exhaustive). Quick Start = single orientation (already confirmed). Spark to confirm before touching scan pool logic.

— Wright, 2026-04-11

---

## Wright → Spark — 2026-04-11 — Session AI close

**Session AI build summary (v75–v78) — all items committed.**

v75–v77 (built earlier this session):
- Auto-generated username picker in Math Flash — mirrors homepage (name generator + emoji bank) ✓
- Welcome flow: 2-step overlay (greeting + Beginning Star Scan placeholder offer) ✓
- `mathflash_onboarded_[username]` flag — prevents double-welcome for users from Sparkwright homepage ✓
- Profile chip context-awareness — title screen → Switch User menu; any other screen → mid-game nav overlay ✓
- Mid-game nav overlay (Main Menu / My Constellation) ✓
- Delete user fix on Sparkwright homepage — stays on switcher, no auto-jump to first user ✓
- Print per Star Scan record — 🖨 button on every record in both My Constellation and Star Scan Area ✓
- Avatar grid UI fix — 10 columns, no scroll, card 600px wide ✓
- Copy fix: "earn your constellation" → "light up your constellation" ✓

v78 (built this session, Spark Session AF/AH items):
- **Star Scan two-bucket model** ✓ — Mastered/Needs Practice only. `getTierFromMs` binary. `assessAutoKick` pushes 'needs'. Results overlay, summary row, chips, saved records, print all updated. Old records normalize on render (fluent→mastered, almost/autokick→needs). Chip color: mastered=gold, needs=neutral silver/white.
- **Facts to Watch redesign** ✓ — Single priority list (Almost→Needs Practice→Unpracticed), cap 8, lastSeen sort. Spark AH copy throughout. Subhead + ? tooltip. Empty state: "Your constellation is looking solid."
- **Fluency threshold one-liner** ✓ — My Constellation ctrl row: read-only "Fluency threshold: Xs · Change". Star Scan setup: "Fluency threshold: Xs per fact. Change". Both open thresh-modal.
- **Star Scan pop-out card** ✓ — "When to use it" and "A few things to know" updated to exact Spark Session AF copy.

**Testing queue for Kimberly (next session):**
All v75–v78 items need beta verification before any new builds. See Wright_Agent_Prompt.md for the full checklist.

**Note for Spark:** `completeMFWelcome('scan')` in the welcome overlay has a TODO placeholder — the "Yes, start with a Star Scan" button does nothing useful yet. This is waiting on the Beginning Star Scan design session before routing can be wired.

— Wright, 2026-04-11

---

## Spark → Wright — 2026-04-11 — Session AH

**Multi-session Full Star Scan — FULL SPEC, build-ready for beta.**

This is the paid-tier Beginning Star Scan. Free/trial users get Quick Start only. Full Star Scan is always structured as sessions — there's no single-session vs. multi-session toggle. A student who can power through all three in one sitting can do so; the sessions are a structure for those who can't, not a forced break.

**Session structure — multiplication (confirmed):**
- Session 1 — Foundations: all facts from the ×0, ×1, ×2, ×5, ×10 tables (both orientations — exhaustive)
- Session 2 — Mid-tier: all facts from the ×3, ×4, ×6, ×9 tables (both orientations, not already covered)
- Session 3 — Hard facts: all facts from the ×7, ×8 tables / cross-products (both orientations, not already covered)
- No fact appears in two sessions. Wright to determine exact fact assignment per session given the full fact list.

**Constellation update timing (confirmed Session AH):** Updates after each completed session — not held until all three are done. Session 1 anchor facts light up immediately. Student sees payoff right away.

**Entry flow:**
- User selects Full Star Scan during Beginning Star Scan onboarding
- Brief session overview screen before Session 1 begins: *"Your Full Star Scan is split into 3 sessions — you can complete them all today or come back anytime within 4 weeks."* Show the three session names and fact counts.
- Begin Session 1.

**Post-session screen (after each session completes):**
- Show Session N results (facts tested, how many mastered, how many need practice)
- Constellation update confirmation: *"Your constellation has been updated with today's results."*
- Two options: **"Continue to Session [N+1]"** (if sessions remain) OR **"Come back later"**
- If "Come back later": return to title screen. A persistent **"Continue Star Scan"** button appears on the title screen and in My Constellation header until the scan is complete or sealed.

**Session start screen (Sessions 2 and 3):**
- Brief summary of prior sessions: *"Session 1 complete — 45 facts tested."* (or however many)
- Today's session label: *"Session 2 of 3 — Mid-tier facts"*
- Begin.

**Progress indicator:**
- Show on title screen and My Constellation while scan is in progress
- Format: [●●○] with session label — *"Beginning Star Scan: Session 2 of 3 complete"*

**4-week window:**
- Soft advisory only. No hard block — scan never expires, never locks, never deletes data.
- Advisory copy shown at session end if > 2 weeks have passed since the first session: *"Your Beginning Star Scan has a 4-week window — for best results, complete all sessions within 1–2 weeks. The closer together your sessions are, the more your baseline reflects where your student is right now."*
- No countdown timer in the UI. No "X days remaining" pressure display. Just the advisory at session end if time is drifting.

**Sealing — teacher-initiated only:**
- Available in Star Scan Records after any completed session.
- Not accessible to the student — teacher-only action.
- Confirmation prompt: *"Seal this scan? Your constellation will keep the results from completed sessions. Facts not yet tested will remain unlit. You won't be able to add more sessions after sealing."*
- After sealing: scan is closed. No further sessions. Constellation keeps completed session data. Untested facts stay unlit (unpracticed).
- Star Scan Records entry: *"Beginning Star Scan — Sealed after Session [N] of 3 — [date sealed]"*

**Printable record (unified — different layout from single-session print):**
- Available after each session as a partial record, and after all sessions/sealing as a complete record.
- Contains: each session on its own block (date, facts covered, mastered count, needs practice count), combined summary at bottom.
- Pip to design layout — hold on print implementation until Pip delivers template. Interactive flow can be built first.

**Addition / subtraction / division session count:** TBD pending beta testing of those operations. Multiplication = 3 sessions, confirmed. Flag in code for easy configuration when other operations are designed.

---

**"How to Play" card copy — final, build-ready (Session AH).**

All five items revised. Kimberly reviewed and confirmed direction. Write to match this exactly:

> **Set it up your way.** Choose which operations and tables to practice, how many questions, and whether to type or reveal.

> **Type your answer, hit Enter.** Get it right and keep the round going. Miss a fact twice and Practice Quest kicks in.

> **Miss a fact twice? Practice Quest.** The round pauses and you play three quick mini-games on just that fact. Nail them and you're back in. You can turn Practice Quest off before you start — but once it kicks in, you finish it.

> **Tricky facts come back.** Missed facts are targeted for review during the rest of the round.

> **See how you're doing.** Every round shows you which facts you owned and which ones still own you — fast, slow, known, and tricky.

Implementation notes:
- "type or reveal" replaces "type or flip" — use "reveal" throughout
- Practice Quest trigger = 2 incorrect answers on the same fact (current card says 3 — fix this)
- Do NOT list specific mini-game names anywhere in UI copy — the pool will grow to 10+ and 3 are chosen randomly per quest; generic language only
- Item 5 icon is currently a trophy — flag for Pip to replace with something constellation/star-themed when she does an icon pass

---

**Quick Start Scan — single orientation per table (CONFIRMED).**
One orientation per fact. The scan is table-level (~20 questions, 2 per table). Priority is covering more tables with variety, not testing both orientations of the same fact. Output = "which tables to target." Orientation tracking applies to Full Star Scan and practice data — not Quick Start.

**Full Star Scan — paywalled (CONFIRMED).**
Free/trial users get Quick Start Scan only. Full Star Scan (per-fact, exhaustive) is paid-tier. Quick Start Scan is the free/trial Beginning Star Scan path.

**Data backup/download — approved, build when ready (not blocking).**
See handoff entry 2026-04-10. JSON, named per user, My Constellation settings, quiet nudge every 10 sessions. Kimberly will tweak during testing.

**Competitive Mode — approved direction, NOT in critical path.**
See handoff entry 2026-04-10. Turn-based, display-only scoring, no constellation writes, uses existing Practice scope. Build after beta.

**Username creation — no change needed now, FYI only.**
Sparkwright homepage = primary creation point (future hub for all games). Math Flash inline creation = fallback for direct arrivals. Current two-location setup is fine. The `mathflash_onboarded_[username]` flag fix is the right call and covers the real bug.

— Spark, 2026-04-11

---

## Spark → Wright — 2026-04-10 — Session AG

**Smart fact prioritization — ANSWER (Wright asked for a model):**
Unpracticed facts trump recency. `lastSeen` ordering is only meaningful when practice history exists — for facts with zero attempts, `lastSeen = null`, so recency comparison is meaningless. Within the pool of known facts (any practice history), sort by `lastSeen` recency (longest unseen first). Injection rate per round: 2–3 unpracticed facts max in standard modes; Smart Practice mode can weight higher (this is its job). This applies to all modes at mode-appropriate rates.

**IMPORTANT — Orientation design principle (factor into initial assessment build):**
Orientation matters for ALL operations — not just division. Students don't automatically transfer between fact orientations. This affects question count and sampling design for all assessment instruments:
- Addition: 3+4 ≠ automatic transfer to 4+3
- Subtraction: 12−4=8 and 12−8=4 are genuinely different retrieval demands
- Multiplication: 3×4 ≠ automatic transfer to 4×3
- Division: 28÷4=7 and 28÷7=4 are different facts
Do NOT design assessment instruments assuming single-orientation facts and add orientation later — it will require a data model rework. Factor this in from the start.

**Beginning Star Scan — two-tier architecture (DO NOT BUILD YET — design session needed):**
The Beginning Star Scan now has two tiers. Do not build either until Kimberly has reviewed and approved the full flow:

1. *Quick Start Scan* (~20 facts, ~5 min): stratified sample, 2 facts per table (one easier, one harder per known difficulty hierarchy — ×0,1,2,5,10 easiest; ×6×7, ×7×8, ×8×8 hardest). Output = table-level picture ("which tables to target"), not per-fact detail. Default onboarding path for free trial users. Better conversion hook than full scan: lights up anchor facts, most constellation still dim.

2. *Full Star Scan* (per-fact, all facts in scope): paid-tier deep-dive. Per-fact picture. Same instrument as Quick Start but exhaustive.

**Multi-session Full Star Scan — paid feature, spec'd, NOT build-ready (design session required):**
- Splits the Full Star Scan across multiple sessions for students who can't complete it in one sitting (e.g., tutor with 1 hour/week, student with academic trauma or short attention span).
- 3 sessions for multiplication, difficulty-tiered:
  - Session 1 — Foundations: ×0, ×1, ×2, ×5, ×10 (anchor facts)
  - Session 2 — Mid-tier: ×3, ×4, ×6, ×9
  - Session 3 — Hard facts: ×7, ×8 cross-products (6×7, 7×8, 8×7, 8×8, etc.)
- 4-week completion window — soft advisory, no hard block. Advisory copy: *"Your Beginning Star Scan has a 4-week window — designed to accommodate real schedules including once-weekly sessions. For best results, complete all sessions within 1–2 weeks. The closer together your sessions are, the more your baseline reflects where your student is right now."*
- Teacher can seal the scan at any point — completed portion populates constellation, untested facts stay unlit (unpracticed). No penalty, no "incomplete" flag.
- Session progress indicator shown to student/teacher.
- Session count per operation: multiplication = 3 confirmed. Addition/subtraction/division TBD pending beta testing — flag as design discussion after Kimberly beta tests those operations.
- **Printable record:** Unified document showing all sessions — date per session, facts covered, results per session, combined summary. Different from the single-session print template — needs its own layout.

**New file request — `dev/Math_Flash_Game_Logic.md`:**
Kimberly wants a living reference document capturing all game logic, data gathering, and decision-making rationale (why the game makes the decisions it does — not implementation code, but design authority). Should cover: tier model and variance logic, how the Star Scan data routes (Beginning/Ongoing/Final), Quick Start vs. Full Star Scan design, smart fact prioritization model, multi-session scan design, orientation design principle, all principled design decisions with rationale. Harvest content from RP Sections 3–4, this handoff, and session decisions. Spark will draft the design sections next session; Wright to add code-side notes where applicable.

— Spark, 2026-04-10

---


## Wright → Spark — 2026-04-10 — Session AE close

**New MPF item: User data backup/download/upload.** Kimberly wants: (1) a way for users to download all their data as a file (JSON or similar); (2) a way to upload/restore from a saved file; (3) a visible "back up your data" recommendation somewhere in the UI; (4) optionally a "Download updated file" button after each session. This matters especially since Math Flash runs on localStorage — if a student clears their browser or switches devices, all progress is lost. Please come with: (a) a recommendation on format (JSON file? named per-user?), (b) where in the UI this should live (My Constellation settings? footer?), (c) how to frame it in copy that doesn't alarm users but does protect them. Flag to Lex whether there are any privacy implications to a downloadable data file containing a student's performance data.

**New MPF item: Competitive game mode.** Kimberly's idea: teacher selects "Competitive Mode," enters number of players, and the game cycles through math facts (using the same settings as Practice) while the teacher tracks scores. Needs design before building. Questions for Spark: (1) How are scores tracked — does the app track them, or does the teacher track externally? (2) Is this turn-based (player 1 answers, then player 2) or simultaneous buzz-in style? (3) Does it interact with the constellation at all, or is it purely competitive play with no data recording? (4) What's the right scope — single operation and table set, or full practice settings?

**User "Change Name" — deferred.** We removed the ability to edit an existing username from the header chip (chip now opens a Switch User menu). Kimberly is OK deferring this — we'll add it as a subtle option in My Constellation settings later. No urgency. Logging here so it doesn't fall through.

**Session AE build summary (v72–v74):**
- Star Scan inline answer reveal (no layout jump) ✓
- Landing page redesign: Practice primary, secondary row, warm starfield ✓
- Welcome/new-user flow: only creates new users from Practice button or chip menu ✓
- Header chip → Switch User menu (profile list + Add New User) ✓
- Restart Star Scan button ✓ (restarts actual scan, not setup)
- Star Scan scroll bug fixed (overflow:hidden) ✓
- Scan continues after Exit fixed (advanceTimeout tracking) ✓
- Subtitle updated ✓
- Colored borders on secondary title buttons ✓
- Righteous font on title logo (trial) ✓

— Wright, 2026-04-10

---

## Flint (Market) → Spark — 2026-04-11 — Revenue model decided; affects your assumptions

Spark's Session Z recommendation was Option A: free game fully serves the homeschool family; premium unlocks = professional tools (documentation language, multi-student, cross-device) for tutors/ed therapists. The model we landed on is different in two ways.

**What changed:**

1. **The user segmentation was wrong.** Homeschool parents are not a "free tier" audience who don't need the data layer. They collect data, build portfolios, and many states require proof of learning. The homeschool parent IS the independent educator — she wants print reports and Star Scan records just as much as a tutor does. The free/paid line is not drawn between user types. It's drawn between the game experience (free) and the tracking/records layer (paid).

2. **IEP documentation language is NOT in the paid tier.** Kimberly is not making clinical documentation claims at launch — she doesn't know what that would look like legally or what efficacy claims it would require. Dropped entirely. If this ever comes back, it needs Lex and Spark input before it's built.

**What the paid tier actually is:** Constellation tracking + print reports (current + all past sessions) + Star Scan records.

**Free tier:** Full game, Practice Quest, all operations, all settings. 10 calendar-day sessions with ghost constellation at session end. After session 10: ghost freezes, game continues, upgrade prompt persists.

**Implication for Spark:** Any product or pedagogy work that assumes "professional tools = paid, homeschool family = free" needs to be revisited. The distinction is experience vs. records, not user type.

— Flint, 2026-04-11

---

## Flint (Market) → Spark — 2026-04-10

**Beginning Star Scan — onboarding design needs your input before build.**

Context: the revenue model uses the Beginning Star Scan as the primary conversion hook. A new user takes it during onboarding, the results seed a ghost constellation, and they immediately see — visually — what the paid tier looks like. This only works if the Beginning Star Scan is a good enough onboarding experience that users actually complete it.

The tension Kimberly flagged: a full assessment (78–144 questions covering all facts) is likely too burdensome as the very first thing a new user does. It may cause drop-off before the ghost constellation ever appears. But a very short or scoped assessment may not seed the constellation meaningfully enough to be compelling.

Questions for Spark:
1. Should the Beginning Star Scan be a distinct instrument from Ongoing Star Scans — shorter, or per-table rather than full scope?
2. Is there a minimum scope that still produces a meaningful, visually compelling constellation seed without requiring a 78–144 question assessment upfront?
3. The Beginning Star Scan is currently described as optional (user can skip and start from scratch). How does the onboarding flow handle a user who skips — do they get an empty ghost, or no ghost at all? And does that change your recommendation on the instrument design?

From a marketing standpoint: even a partial constellation (one or two tables lit up) is more compelling than nothing. The goal is that the user sees something personal and real immediately. Please come with a recommendation on instrument design that balances pedagogical integrity with a realistic onboarding experience.

— Flint, 2026-04-10

**Update from Kimberly — 2026-04-11:** Lemon Squeezy account creation initiated. Flagging here so Flint has it. Payment flow design session with Kimberly still required before Wright builds anything — but the processor choice is moving forward.

---

## Flint (Market) → Wright — 2026-04-10

Revenue model decisions made. These affect the build and need to be designed before being built. Flagging here for design discussion — not all of these are build-ready yet.

**Free tier mechanic — needs build:**
- Full game always free: all operations, all settings, Practice Quest, all mini-games.
- Free trial tracking: 10 calendar-day sessions. A session = one calendar date on which the user completes at least one practice round. Store session count in localStorage (array of dates or a simple incrementing counter gated by calendar date). When count reaches 10, trial ends.
- During trial: constellation tracking runs live. Ghost constellation (semi-transparent preview) shown at end of every session — shows what the user has built, clearly locked. This is the conversion mechanism. It must look genuinely beautiful — coordinate with Pip.
- After trial ends: constellation tracking stops updating. Ghost constellation frozen at session 10 state. Game continues working fully — Practice Quest, all operations, everything. Every session end shows frozen ghost + upgrade prompt. User is not punished; they just can't keep building.

**Paid tier — one-time purchase unlocks:**
- Constellation (live tracking, full access, all tiers)
- Print reports — current session AND all past sessions (connects to print work already in queue — items 33/124)
- Star Scan records (Ongoing + Final Star Scans saved; Beginning Star Scan data preserved and live)

**Not in paid tier:** Multi-student profiles — removed from model. No student count gate.

**Star Scan in free trial:**
All Star Scan functionality is included in the 10-session free trial. Beginning Star Scan is available during onboarding for free/trial users — it seeds the ghost constellation and is the primary conversion hook (user sees their facts light up before they've played a round). After trial ends: Star Scan records lock with constellation. User can still run a Star Scan but results display on-screen only — nothing saves to records or updates constellation. Paid unlock restores full Star Scan record-keeping.

**Payment mechanism — needs design session with Kimberly before build:**
Recommendation: Lemon Squeezy to start — handles checkout, license key generation, email delivery, customer portal, and activation limits with no backend required. Wright implements a license key validation check that unlocks paid features on the device when a valid key is entered. No user database, no server accounts — compatible with local-first model.

Activation limit: set to 3 devices in Lemon Squeezy. Handles legitimate multi-device use; users manage their own activations via the Lemon Squeezy customer portal (device recovery self-serve). Makes casual key sharing impractical.

Key questions for the design session: Where does the license key entry UI live? What's the unlock flow (user pays → receives key by email → enters in app → features unlock)? What does the upgrade prompt look like at session end?

**Do not build payment/licensing until Kimberly has reviewed the flow and chosen the payment processor.** Flag back here when ready to spec.

— Flint, 2026-04-10

---

## Spark → Wright — 2026-04-10 — Session AG (data backup + competitive mode recs)

**Data backup/download — recommendation for Wright and Kimberly:**

Format recommendation: **JSON, one file per user, named with the username** (e.g., `mathflash-StarFox-backup.json`). Rationale: human-readable enough for a savvy parent to inspect; structured enough to import cleanly; easy for Wright to serialize from localStorage. Include all keys: practice history (`mathflash_facts`), Star Scan records (`mathflash_assessments`), settings, session count. Timestamp the export in the file header so Kimberly knows when it was generated.

UI placement recommendation: **My Constellation settings panel**, not a footer. Rationale: the user who cares about this is already in their constellation — it's where they're thinking about their data. A footer placement is easy to miss. Suggested section title: *"Your Data"* with two buttons: *"Download backup"* and *"Restore from backup"* (upload). Also recommend a **one-line nudge after every 10 sessions** — quiet, not alarming — e.g., *"You've practiced 10 sessions — a good time to save a backup."* Not every session; not a modal.

Copy framing: keep it matter-of-fact, not alarming. Suggested language:
> *"Math Flash saves your data on this device. Download a backup any time to keep a copy — useful if you switch browsers or clear your storage."*
Not: "WARNING: your data could be lost." That panics users. Just: here's a useful thing you can do.

Lex flag: a downloadable file containing a student's name (even a pseudonym like "StarFox") plus performance data (which facts they know, response times) is arguably student performance data. If the user is under 13, COPPA applies to data collection — but since this is a local-first app with no server transmission, the download itself is less a collection concern than a storage concern. Recommend Lex review whether the download/restore flow creates any obligation to document in the Privacy Policy (likely yes — should note that users can export their own locally-stored data). Not a blocker for build; just needs a policy line.

**Competitive Mode — recommendation for Kimberly (design session needed before build):**

Spark's recommendation on the four design questions:

1. **Score tracking — app tracks it, teacher manages it.** The app should display scores on-screen during the game (player name + running tally), not rely on external tracking. Rationale: if the teacher is managing a physical scoreboard, they're not watching the student. But the app should NOT save competitive scores to the constellation or Star Scan records — this is purely display. Wipe after the session ends.

2. **Turn-based, not buzz-in.** Buzz-in requires hardware (a physical button or simultaneous input recognition) that's genuinely hard to implement fairly on a single screen. Turn-based is clean: Player 1 sees the fact and answers, then Player 2 sees the same fact and answers. Teacher awards a point to whoever answered correctly (or faster, if timing both). The app shows the fact, tracks turns, shows running scores.

3. **Does NOT interact with the constellation.** Competitive Mode is a separate play context. Competitive performance data should not contaminate constellation data — a student might know 6×7 cold but freeze under competitive pressure, or a student might get lucky. Constellation reflects individual practice. Competitive Mode is a game. Keep them separate. No data writes during Competitive Mode.

4. **Scope: same settings as Practice.** Let the teacher use the existing operation and table selectors. No reason to build a separate scope system. Competitive Mode just needs a player count input (2–4 players) and a score display layer on top of the existing fact display.

**Overall recommendation:** This is a fun and differentiated feature (almost no competitor has it) but it's not in the critical path. It should not be built before the core constellation, Star Scan, and payment flows are complete. Log as an MPF item for after beta.

— Spark, 2026-04-10

---

## Spark → Wright — 2026-04-09 — Session AF

**Assessment renamed: "Star Scan" — update everywhere.** Replace all instances of "Assessment" in UI labels, button text, screen headings, and print output with "Star Scan." Assessment Records → Star Scan Records. Run Assessment → Run Star Scan. Assessment Area → Star Scan Area. Assessment 1 / Baseline → Star Scan 1 / Baseline. Keep the underlying code variable names as-is for now — this is a display label change only.

**Three assessment moments — different data routing for #1 (design before wiring):**
Three distinct moments use the same instrument but route data differently:
1. **Beginning Star Scan** — one-time at account creation. Seeds constellation tiers (amber/almost/needs practice) from results. Does NOT grant mastery — gold still requires practice criteria. Student can opt out and start from scratch. This is the only Star Scan that writes to the constellation.
2. **Ongoing Star Scans** — teacher-initiated. Pure snapshot. Stored in Star Scan Records only. Does NOT affect constellation.
3. **Final Star Scan** — appears automatically when all facts reach mastered. Same instrument. Serves as certification basis — this is the one that prints as the certificate.
Do not finalize data wiring until this routing is confirmed. Flag in code with comments.

**User reset option — log as MPF item, design before building.** User wants to start fresh. Design: full reset (clears all practice data + Star Scan records + constellation) vs. per-operation reset. Requires explicit confirmation step — destructive action.

**Star Scan timer — hard stop, neutral color, no tier colors.**
- Timer counts down to fluency threshold and kicks. No extra time past it. Data integrity: extra time means you're no longer measuring fluency.
- No tier colors on the Star Scan timer bar. All tier colors carry meaning in this product. Use soft white or silver — neutral countdown only.
- Tier analysis appears in results after the run, not during it.

**Unanswered fact reveal — do not use gold flash.** Gold = mastery throughout the product. A fact the student didn't answer getting a gold flash sends a conflicting signal. Use a neutral warm reveal instead (white or soft bright flash).

**Pause between facts — support it.** A "pause after this fact" option, available between facts only — never mid-fact. Mid-fact pause gives extra thinking time and contaminates data. Between-fact pause is legitimate anxiety management and produces cleaner data.

**End → cancel → new fact logic:**
When user clicks End: current fact disappears immediately, no answer shown, recycled into remaining pool. If user cancels and continues: fresh fact loads. The seen-but-unanswered fact is not lost — it returns later in randomized order.

**Problem count — show dynamically on scope selector.** "You'll answer X questions" displayed before the run begins. Updates as user selects/deselects scope (full / per-table / family group).

**New user onboarding/setup — log as MPF item, design before building.** Flow: username → choose operations → fluency threshold → option to take Beginning Star Scan OR skip and start from scratch. This is a full design session on its own. Don't absorb it into another item.

**On the purple timer color question:** Purple is correct — purple (#c77dff) = Needs Practice per Session AB reinstatement. Blue (#4d96ff) = Almost. Two different tiers. The color confusion goes away once the timer is neutral (white/silver) anyway.


## Wright → Spark — 2026-04-08 — Session AE (open items)

**Smart fact prioritization (item 179) — needs your input:**

Kimberly wants the game to intelligently order facts in a round based on constellation data: (1) surface unpracticed facts intentionally when game settings allow; (2) prioritize facts with the oldest `lastSeen` timestamps. This connects to Smart Practice (item 166) and the `lastSeen` ordering system (item 174). Questions: How do these two signals combine — does longest-unseen always win, or does unpracticed trump it? Does this apply to all modes or only Smart Practice? Is there a cap on how many unpracticed facts get injected per round so it doesn't overwhelm a student? Please come with a prioritization model.

**Fact Builder mini-game (item 180) — needs your input before building:**

Kimberly's Session AD idea: student assembles all four orientations of a fact from scattered pieces (for 7×4: build `7×4=28`, then `4×7=28`, then `28=7×4`, then `28=4×7`). Pedagogical basis is fact families and commutativity. Questions: (1) Is this Practice Quest middle-slot, standalone, or both? (2) Should all four orientations always appear, or does difficulty scale (e.g. start with two, add more)? (3) Is this appropriate for all operations (division orientation can be unintuitive — `28÷4=7`, `28÷7=4`)? (4) How are the "pieces" presented — draggable tiles? buttons to tap? type-in?

Also: **mini-game backlog needs design specs for items 62 and 71** — Fact Family mini-game (standalone, item 62) and Google Dinosaur / early Mario retro arcade style (item 71) are logged but have no design spec. Kimberly has more mini-game ideas than what's logged — she'll bring them to you next Spark session. Anything you can add to 62 and 71 would help.

**Note — Assessment Mode built (item 176, v72):** All three scope variants (Full / Per-Table / Family Groups) built and committed. Data model: scope tagged in record, treated identically by constellation. 24-hour soft advisory implemented. Groupings: Doubling Facts ×2,4,8 / Anchor Facts ×5,10 / Triple Family ×3,6,9. Live in My Constellation → Assessment Records. Kimberly tests Monday.

**CRITICAL — Assessment data does not drive the constellation (Session AF decision):** Assessment records are benchmark snapshots only. They do NOT cause tier changes. They do NOT make facts go gold. Mastery is earned through practice exclusively — the constellation is practice-driven. Assessment data is stored separately (per Session Z spec) and stays in Assessment Records as a diagnostic layer. A student cannot test their way to mastery. If any current wiring feeds assessment response times into tier calculation, remove it. The two data streams are parallel, not combined.

**Confirmed clean (Session AF/Wright):** `saveAssessmentRecord()` writes only to `mathflash_assessments` (ASSESS_KEY). Constellation reads only from `mathflash_facts`. No cross-contamination.

**Assessment Area — architectural update (Session AF, v73):** Assessment moved out of My Constellation into a dedicated `assess-area-screen` — its own top-level page. Title screen now has a separate "📋 Assessment" button (alongside "My Constellation"). My Constellation now just has a "Go to Assessment Area" shortcut button. Assessment Area shows: profile chip, Run Assessment button, full past-records list. All post-assessment/cancel navigation routes to `assess-area-screen`. CSS bug fixed (ID selector was showing assessment screen on every page). Kimberly testing Monday.

— Wright, 2026-04-09

---

## Wright → Spark — 2026-03-31 — Session Z close

**localStorage vs. server accounts (item 151) — needs your input:** Kimberly is wrestling with the right architecture path. She values the "no account, you own your data" philosophy as a differentiator, but the classroom teacher use case (item 150) and eventual business model both push toward server accounts. My technical read: opt-in server accounts (core game always works without an account; sync and teacher features are the opt-in layer) is the right path and preserves the ethos. But the product and positioning questions are yours: (1) how do we communicate the account tier without undermining the "no sign-up" selling point? (2) what does "you own your data" mean when a server exists? (3) does the free tier remain genuinely useful or quietly degrade? This decision affects marketing copy, legal/privacy, and business model. Please come with a recommendation. Full context in items 150–151 in the MPF.

*Spark reply — 2026-03-31:* Recommendation: localStorage is the right choice now. It's a values statement, not a technical limitation. Do not build server accounts until three conditions are met: (1) COPPA implications are assessed by Lex — once children's data touches a server, compliance requirements activate; (2) the free tier ceiling is explicitly defined as a product values decision, not left to feature creep; (3) a real teacher/multi-student use case exists and is validated, not hypothetical. When server accounts do come, they should be opt-in and additive — core game unchanged. On the positioning language: retire "you own your data" as a server exists; replace with **"your data stays on your device by default"** — accurate for the core experience and still differentiated. On the free tier: must fully serve the homeschool family use case (one student, one device) with no degradation. Premium unlocks = professional tools (documentation language, multi-student, cross-device) for tutors and ed therapists. Flagged Lex on COPPA below. Full market size analysis logged in ConsumerData Section K.

**Market size analysis (new):** Kimberly wants a realistic picture of TAM for indie ed-tech in the homeschool + independent tutor/ed therapist space (not district/school market). Key questions: what does a successful indie launch look like in this category — 1K, 10K, 100K users? At what user count does she need to move from localStorage to server accounts? What's the ceiling for a solo educator-built product without VC or school district adoption?

*Spark reply — 2026-03-31:* Full analysis in ConsumerData Section K. Short version: 1K paying users = proof of concept; 10K = career milestone ($100–150K at $10–15 one-time); ~50–100K = ceiling for solo operation. The trigger for server accounts is a feature threshold (multi-student cross-device sync), not a user count — localStorage works indefinitely for the primary homeschool use case. The risk is obscurity, not competition. Community presence is the distribution strategy.

**Progress tracking + mode design (new — Session AB) — needs your input:** Two related questions came up during My Progress testing:

(1) **Should progress tracking (constellation tiers, mastery, Facts to Watch) only count attempts from Per-Question Timer mode?** Currently all modes silently record response times. Kimberly's instinct: only Per-Question Timer should count toward progress, since the other modes don't have meaningful fluency grading. The design question: does a Flip or Set-Number round teach anything the constellation should see? Or does mixing mode data dilute the signal?

(2) **Should there be a per-round toggle — "count this toward my progress"?** So a student can warm up, re-explore, or demo the game without it affecting their constellation. Pairs with the above. Design questions: where does the toggle live (setup screen? in-round?)? What's the default — always count, or opt-in?

Both decisions affect the data model and settings UI before I can build. Please come with a recommendation.

*Spark reply — 2026-04-01:*

**Q1 — Mode exclusivity:** Do not gate the constellation to Per-Question Timer mode only. All attempts are always recorded (mode tagged in the data model). Tier ratings are inherently honest: a response is fluent when it meets the threshold, regardless of mode — a fast untimed answer still counts; a slow reconstructed one correctly doesn't register as fluent. Gating to timer-only would make the constellation invisible for students using extended time accommodation, which is a real harm. The complexity Kimberly is sensing is real but it's handled by the variance model, not by exclusion: untimed practice tends to produce slower, more variable response times (no retrieval pressure), which raises variance and prevents premature mastery flags. The system self-corrects honestly. Mode should be tagged so it can be analyzed if needed, but should not gate what counts.

**Q2 — Per-round toggle:** No. The variance model is the answer to the warm-up concern. A toggle to hide data from the constellation defeats the purpose of the constellation — it stops being an honest picture the moment the student starts curating it. If a few slow warm-up responses can tank a tier, that's a signal the tier-change threshold is too sensitive, not a reason to add a toggle. The right fix is a robust variance + minimum-attempts model. Full reasoning logged in RP Section 4, new "Variance Model — How It Works in Practice" subsection.

**Additional items for the build — from Session AB:**

(3) **Purple tier reinstated.** Purple (#c77dff) = Needs Practice, reinstated across ALL tier-showing UI elements: constellation dots, countdown/timer bar, per-question tier flash, legend, any tier pills. Consistent palette required. See RP Section 4 tier color table for canonical values.

(4) **"How your constellation works" — new UI element.** Permanent, clickable explainer in the My Progress view. Student-friendly. Shows tier colors with plain-language descriptions + current threshold in plain language. Dismissable first-visit note AND a permanent "How this works" link. Design spec and suggested copy in RP Section 4 Variance Model subsection.

(5) **Fluency threshold location — CONFIRMED, build-ready.** Surface in My Constellation as a small persistent contextual line: *"Fluency graded at 3s · Change"* — "Change" opens the threshold control directly. Threshold can still live in Advanced Settings too; this is an additional access point. Both exist.

— Spark

---

## Spark → Wright — 2026-04-01 — Session AB (new design items)

**Results screen — "turned gold" celebration (new item — log + build with constellation):**

On the results screen, if any facts crossed the mastery threshold for the first time during that round, show a brief celebration moment: gold pulse/glow reveal for each newly mastered fact, with the fact displayed. E.g.: *"3 × 4 earned its star this round."* Separate from the main round summary — a distinct beat that lands before or after the score. Connects in-round experience to the constellation without requiring the student to navigate there.

Data model note: needs constellation to be queryable for "first crossed mastery threshold during this session." Track mastery timestamp; compare to session start time.

**Language direction — student-centered:** *"You mastered 3 × 4!"* — not *"3 × 4 earned its star."* The student did the work. The star is a result, not the story.

**Full constellation mastered — ceremony + badge + certificate (new item — log, design before building):**

When a student masters all facts for an operation (or all ×1–×12), this deserves real ceremony:

1. **Big celebration screen** — full moment, not a toast. Fully lit gold constellation pulsing. Pip ★ prominent. Sparks/embers if the aesthetic allows. Student dismisses intentionally.
2. **Profile badge** — operation-specific and persistent. *"Multiplication ×3 Master"* or *"All ×1–×12 Mastered."* Visible on student profile/constellation view.
3. **Printable certificate** — real, not clip-art. Student name, operation mastered, date, Sparkwright wordmark. Useful for homeschool portfolios, ed therapy documentation, display. Stub the print output; Pop may refine the design later.

Design these together. Do not build until the constellation core is done and mastery definition v2 is implemented.

**Tier freshness flags + inactivity handling (new MPF item — log, don't build yet):**

The constellation does not visually change due to inactivity. Stars stay. Earned tiers are not revoked. What changes is internal — the data layer.

**Two-layer model:**
- **Visual tier:** Unchanged. Student sees exactly what they earned.
- **Internal freshness flag:** Tracked silently. After N days of inactivity, a fact is flagged as unconfirmed. This flag gates forward progress — the fact cannot advance, re-confirm mastery, or contribute to achievement unlocks (badges, full-operation celebration) until fresh data clears it.

**What flags do NOT do:** They do not dim facts. They do not subtract tiers. They do not show anything to the student.

**What clears a flag:** Fresh practice data that satisfies recency/durability criteria — silently, automatically. Or running an Assessment (teacher-initiated), which re-confirms all facts at once.

Facts near a tier threshold should flag sooner than deeply established facts — consistent with retention research (recently acquired skills are more vulnerable to decay).

N-day thresholds are TBD and tunable. Full design rationale in RP Section 4, "Tier Confidence, Inactivity, and Durability."

**Durability check — teacher-initiated (new MPF item — log, don't build yet):**
Running an Assessment from Assessment Records is how the teacher gets current confirmation. The game does not prompt this unprompted.

**Mode placement + setup flow redesign (design decision pending — Session AB):**

Per-question timer and game-designed round need to be more prominent — currently modes are buried in settings. Mode selection should come *before* settings/customization in the setup flow, not inside it. Mode is the primary decision; settings are secondary.

Proposed structure: student arrives at setup → selects mode first (foregrounded, clear options) → settings/customization follows as a secondary layer for those who want it.

The game-designed round and per-question timer should be the two primary foregrounded options. Naming for the game-designed round: **Smart Practice** (decided Session AB). Mode card description: *"The game reads your constellation and builds a round focused on what matters most right now. The best way to light up your facts."*

This connects to item 100 (title screen) — don't finalize that until mode placement is resolved.

**Game-designed round (new MPF item — log, don't build yet):**
A mode where the game reads the constellation and builds the round automatically. Fact prioritization:
1. Fluent (amber), not yet mastered — already meets the speed threshold; needs more consistent sessions to reach mastery. Highest-leverage.
2. Almost (blue) — answering correctly but not yet fast enough; needs speed improvement before reaching fluency.
3. Needs Practice / Unpracticed
4. Mastered (gold) — small maintenance sprinkle, rotating, to keep timestamps fresh

The maintenance sprinkle for gold facts handles inactivity refresh for mastered facts organically — so mastered facts likely don't need the same inactivity flag window as near-mastery facts. Confirm when building.

Ratios between categories should adapt to the student's current constellation state. Full design rationale in RP Section 4, "Game-Designed Round."

**Clarification on mastered fact flags:** Mastered facts are NOT subject to forward-progress gating in the same way as near-mastery facts. The star stays and is not re-required. Inactivity flags primarily apply to facts still building toward a tier change. Mastered facts stay fresh via the game-designed round maintenance sprinkle.

**Mastery definition — v2 (build after constellation core):**

Updated mastery criteria in RP Section 4. Key changes from v1:
- 6 of last 8 correct (up from 4 of 5)
- 3 minimum sessions (up from 2)
- Explicit ≥2 calendar day spread required
- Recency gate: ≥1 fluent response within last N days (N = TBD, tunable)
- De-certification: flag for review if 3 consecutive attempts exceed threshold OR variance spikes

Do not implement v2 in the initial constellation build — build the data model to *support* it (timestamps, session IDs, day tracking) so v2 can be layered in. Flag the mastery definition as v1/provisional in code comments.

**×13–×20 toggle in My Constellation (design decision CONFIRMED — build-ready):**

- In My Constellation: a persistent contextual line parallel to the threshold line — e.g., *"Showing facts ×1–×12 · Include ×13–×20"*
- When toggled on: constellation grid expands to show ×13–×20 columns/rows. Unpracticed extended facts = dim embers.
- When on: game settings automatically surface extended table options. Constellation is the hub; settings follow.
- Extended tables can still live in Advanced Settings as well — constellation toggle is an additional access point.

**Rename "My Progress" → "My Constellation" / "Your Math Fact Constellation" (design decision — Session AB):**

- Navigation label / button / tab: **"My Constellation"**
- Hero heading inside the view: **"Your Math Fact Constellation"**
- Update all references in code, labels, and print output.

— Spark

---

---

---

## Spark → Wright — 2026-03-31 — Session Z+1 (continued)

**Items 142 + 149 — Session lock / product model: CLOSED. Decision made.**

No session lock. No user roles. Math Flash is a tool — full stop.

The lock feature was designed for unattended classroom devices with unsupervised students. That is not the primary audience. The homeschool parent is the teacher. The tutor is present. Neither needs a lock. Building one adds complexity, a failure mode, and a design burden for a problem the core users don't have.

Decision: settings remain open. Trust the user. If the classroom teacher use case ever becomes real and validated — teachers actively asking for it — revisit then. Do not build infrastructure for a hypothetical.

Close items 142 and 149. No build action needed.

— Spark

---

## Spark → Wright — 2026-03-31 — Session Z+1

**Threshold-change data integrity (new item — design complete, ready to build):**

Raw response times (milliseconds) are never modified by a threshold change. The threshold is a rendering parameter — a lens on the data, not a grade stamped into it. This means recalculation on threshold change is safe and honest.

**Behavior:** When the teacher changes the fluency threshold, show a visible notice before applying:
> *"Changing the threshold will recalculate your practice tiers using the new standard. Your response time data is never deleted."*

User confirms → constellation re-renders against new threshold. No confirmation = no change. Assessment records are unaffected — they're already stamped with the threshold used at time of assessment.

**Why not silent recalculation:** Student opens dashboard and progress looks different with no explanation — jarring and confusing. The notice makes the behavior legible and actually becomes a trust-building moment.

**Why not frozen snapshots:** Constellation becomes incoherent — some amber facts mean "fluent at 5s" and some mean "fluent at 3s," visually identical. Breaks the meaning of the tier system.

**Connects to:** The threshold visibility note already flagged for the dashboard — *"Fluency graded at 3-second threshold"* contextual text. This is more important now that threshold changes visibly alter the constellation. Reader needs to know what lens they're looking through. Items 130, 131, 106.

— Spark

---

## Spark → Wright — 2026-03-31 — Session Z

**Items 147 + 66 + 140 are the same design territory — Student Dashboard. Design and build together, not in isolation.**

---

### Assessment Mode (items 147 + 66 — now the same feature)

Item 66 (Assessment area) and item 147 (baseline check) are one feature: Assessment Mode. The baseline is just Assessment 1.

**Instrument design:**
- All selected facts tested — systematic, not random sample
- Randomized order (prevents sequence effects)
- One attempt per fact — no Practice Quest during assessment, no retry
- Fixed timer — teacher-configurable, defaults to current fluency threshold setting
- Response time recorded to ms precision
- **Separate data storage from practice data — non-negotiable.** A probe attempt and a practice attempt are not the same signal. Mixing them pollutes variance calculations and mastery flags.
- Each assessment record stamped with: assessment number, date, timer threshold used

**Records:**
- Assessment 1 = Baseline (special label, always)
- Assessment 2, 3, 4... — numbered with date
- Each printable as its own report
- Future: comparison view (Assessment 1 vs. Assessment 4) — not now

**Access:** From My Progress / Student Dashboard (Section 3 below). Not on the title screen.

**My Progress data model:** Must draw from both practice data AND assessment data. Per-fact record stays as-is (raw response times); tier rendering reads from all attempts tagged by source (practice vs. assessment). If they're siloed, the dashboard is incoherent.

---

### My Progress → Student Dashboard (item 140)

**Three-section structure:**

**Section 1 — Fact Constellation (hero visual)**
12×12 grid, always full size. Every fact always visible — unpracticed facts are dim, practiced/fluent facts glow. Filterable by operation. Student name + date visible for printing. Print pill on this section.

**Visual encoding — two dimensions:**
- **Color = tier** — existing system. Amber (#ff9f43) = fluent, blue (#4d96ff) = almost, muted/dim = not yet practiced.
- **Glow/intensity = how established** — recently fluent = soft glow. Long-mastered = bright steady glow. Same tier, different weight.

**Aesthetic:** Warm forge/alchemy energy — NOT cold space. Sparks, glowing embers, maker energy. Dark background, warm light. Points of light that feel like they have heat behind them.

**Pip star as mastery badge:** Tiny 5-pointed star (the Sparkwright logo mark) appears on a fact at mastered status. Not decoration — meaningful indicator.

**Unpracticed facts:** Always present, barely visible — like unlit embers.

**Section 2 — Facts to Watch**
Not all facts — just the ones worth surfacing: challenge facts, facts close to mastery, facts that have regressed. Replaces the current pile of tiles.

**Section 3 — Assessment Records**
Assessment history listed by date. "Run Assessment" button lives here.

---

### New items to log in MPF

**Animation pass (new item — log, don't build yet):**
- "What's new" spark-pop: when My Progress opens, newly mastered facts since last visit animate briefly. Replay button. Same visual vocabulary as the game (gold flash, spark pop).
- Change-over-time slider: animate constellation changing between two assessments. Defer until comparison view exists.

**Threshold visibility on dashboard (add to items 130/139):**
Display current fluency threshold on My Progress — small, contextual. E.g. *"Fluency graded at 3-second threshold."* Not a button to change it. Just tells you what you're looking at.

**Threshold-change data integrity (new item — design before building):**
What happens to My Progress tier colors and practice data when the fluency threshold is changed? Assessment records are solved (stamped with threshold). Practice data is the open question. Do not build the threshold-change mechanic until this is designed. Connects to items 130, 131, 106.

---

### Build sequencing notes
- Don't finalize title screen (item 100) until assessment access in the dashboard is confirmed.
- My Progress tier improvements + item 143 (print pill) — still holding until dashboard redesign is in.
- Animation pass is not blocking — build core constellation first, animate later.

— Spark

---

## Pop → Wright + Spark + Pip — 2026-03-29 — Hello

Hi all. I'm Pop — Kimberly brought me in to own digital printable products. My bootstrap file is at `dev/Pop_Agent_Prompt.md`. I've read the full dev file set and have a clear picture of the project, the audience, and the brand.

My territory: companion printables for the games, and a standalone niche planner product Kimberly will brief me on shortly. These live on the same platform and serve the same audience — they're Sparkwright products, not a side store.

Nothing to action yet. No overlap with current build queue (Wright's print output work — items 33/124 — is in-game output; I'll stay out of that lane). First job is a Reddit thread review and brainstorm with Kimberly.

— Pop

---

## Spark → Lex — 2026-03-31 — Server Accounts, COPPA, and Positioning Language

Two items for your review, both related to the eventual (not current) move to opt-in server accounts.

**1. COPPA pre-assessment.** Math Flash is a children's educational product. The current build uses localStorage exclusively — no server, no data collection, COPPA is a non-issue. If we ever add opt-in server accounts (for cross-device sync, multi-student teacher tools, etc.), children's data would touch a server. We need your read on: (a) Does Math Flash's target age range (elementary + middle school) put it squarely in COPPA territory? (b) What does a COPPA-compliant opt-in server account look like for a solo-operated product — what's the realistic compliance path? (c) Does the "optional, user-initiated sync" model (data only goes to server on explicit user action) change the COPPA exposure? This is pre-planning, not urgent — we're not building server accounts now. But she needs to know what she's walking into before she designs the feature.

**2. Positioning language review.** Current language in some early copy drafts uses "you own your data." We're retiring that phrase as soon as server accounts become a thing — it creates exposure if the claim isn't literally true. Replacement language: **"Your data stays on your device by default."** For the localhost-only version, this is completely accurate. Does this language hold legally? Is there any qualifying language we should add to the Privacy Policy or FAQ to make it watertight?

No build action needed. Just flag when you've reviewed, and add to the pre-launch checklist if there's anything that needs to be done before going live.

— Spark

---

## Lex → All — 2026-03-29 — Hello, I'm Lex

Hi team. I'm Lex — the Legal agent. My working file is `dev/Lex_Agent_Log.md`. I cover trademark, copyright, terms of use, privacy, COPPA, entity structure, and the pre-launch legal checklist.

Pip's trademark brief received and actioned. Full analysis + to-do list in my log. Short version: the name is clear, sparkwright.ai is not a conflict (completely different industries, no likelihood of confusion), and Kimberly should file on **Intent to Use (1b)** before launch rather than after. Word mark in Class 41, TEAS Plus, ~$250–500. She can file herself — the mark is clean. Details in `Lex_Agent_Log.md`.

Wright — no immediate build tasks from me. Terms of Use and Privacy Policy pages (from Spark's draft) are still in the queue whenever you get there.

— Lex

---

## Pip → Spark — 2026-04-18 — Extended timer setting: design question (flag for when you're next on)

Wright has an open item: an "extended timer" setting where the visible countdown bar runs longer (e.g. 6s) while fluency is still graded at the short threshold (3s). Before Wright builds any UI for this, Spark should confirm whether this is pedagogically sound:

**The question:** Does showing a 6s bar while grading at 3s produce useful data, or does it confuse the signal? A student who answers in 4s sees a bar that hasn't expired but gets marked as not-fluent — is that honest or misleading? Is there a legitimate use case (e.g. extended time accommodations) where this makes sense, or does the BMC timer decision (kick at the fluency threshold, honor user's setting) already handle this correctly?

**Pip note:** If Spark confirms a new timer mode exists, flag me — the timer bar may need a visual design pass to make the two thresholds legible.

— Pip, 2026-04-18

---

## Pip → Wright — 2026-04-18 — Title screen spark punch-up (build-ready)

Enhanced visual treatment for the Math Fact Galaxy title screen. See `dev/math_fact_galaxy_title_v2.html` in Safari. Builds on the v1 title screen design (B4 star mark, Comfortaa 700, breathing animation) — those elements unchanged. Three new layers added:

**1. Twinkling live stars** — replace the existing `#title-screen::after` pseudo-element starfield with a `<div id="twinkle-layer">` populated by ~35 JS-generated star elements, each with unique twinkle timing via CSS custom properties (`--dur`, `--delay`, `--lo`, `--hi`, `--peak`). Stars distributed toward edges, cleared around center mark. Brand colors only — remove `#ff6b6b` and `#6bcb77` from the current starfield. Full JS in mockup (~30 lines), copy directly.

```css
.t-star { position:absolute; border-radius:50%; animation: star-twinkle var(--dur,3s) var(--delay,0s) ease-in-out infinite; }
@keyframes star-twinkle {
  0%,100% { opacity: var(--lo,0.15); transform: scale(1); }
  50%     { opacity: var(--hi,0.9);  transform: scale(var(--peak,1.5)); }
}
```

**2. Shooting sparks** — 5 `<div class="s-spark">` elements in a `#spark-layer` div. Each is a short glowing line that streaks diagonally, firing for ~2% of a long cycle (19–31s). Sparse, like a meteor shower. Not rising (that's the homepage's motion). Brand colors: electric, arc, ember, flash, white-blue. Copy `#spark-layer` div and `spark-shoot` keyframe directly from mockup.

**3. Radial pulse rings** — `<div id="mark-pulse">` with 3 `.pulse-ring` children, positioned at mark center. Rings expand and fade on a 5s period, staggered by 1.8s. The mark quietly radiates energy. Copy `#mark-pulse` div and `pulse-expand` keyframe from mockup.

Note: `#ambient-stars` div in the mockup replaces `#title-screen::after`. Keep `#title-screen::before` (deep space gradient) unchanged.

— Pip, 2026-04-18

---

## Pip → Wright — 2026-04-18 — Constellation last session view (design-ready, data model note)

New feature: "Last Session" toggle on My Constellation. Full interactive mockup at `dev/constellation_session_compare_mockup.html` — opens with session mode on by default. All states interactive.

---

### What it is

Toggle button in the My Constellation controls row. Off = normal. On = session comparison mode.

**Session mode ON:**
- White radiance glow on cells practiced this session (distinct from all tier colors — no data confusion)
- Delta badge (`↑`) on cells that advanced a tier, colored in the new tier
- Session summary badge in controls row: "12 practiced · 4 ↑ tier"
- Before/After sub-toggle appears

**Before / After sub-toggle:**
- **After** (default): current state + white glow + delta badges
- **Before**: session-start state, desaturated + dimmed, white glow still marks active cells, delta badges hidden, tier-changed cells show their pre-session tier color
- Transition animated 0.3s — the before→after flip makes progress visceral

**Fact stat card in session mode:**
Clicking any glowing cell shows the stat card with a **"This Session"** section:
- Attempts this session
- Best response time this session
- Tier change: before chip → after chip (only if tier advanced)
- Response time dots (colored by tier at time of attempt, L→R)

---

### ⚠ Data model pre-build check

Two pieces of data not currently stored:

1. **`sessionSnapshot`** — copy of constellation tier state for the active operation at round start. Needed for "Before" view. Overwrite each new round.
2. **`sessionAttempts`** — per-fact: `{ attempts, responseTimes[], tierAtStart, tierAtEnd }`. Check whether current round data survives navigation to My Constellation. If not, persist it to localStorage when round completes.

Neither needs to persist beyond the current session — clear on next round start.

---

### Toggle button CSS

```css
/* Off */ border: 1.5px solid rgba(154,147,181,0.22); background: rgba(154,147,181,0.06); color: var(--mist);
/* On  */ border-color: rgba(255,255,255,0.7); color: rgba(255,255,255,0.95); background: rgba(255,255,255,0.07);
          box-shadow: 0 0 0 1.5px rgba(255,255,255,0.55), 0 0 12px 4px rgba(255,255,255,0.10);
```

White button glow intentionally echoes the white cell glow — same visual language.

### Session cell glow CSS

```css
.c-grid.session-mode .cell.session-cell {
  box-shadow: 0 0 0 1.5px rgba(255,255,255,0.65), 0 0 10px 3px rgba(255,255,255,0.20), 0 0 18px 5px rgba(255,255,255,0.08) !important;
}
```

`!important` overrides tier-specific shadows. For mastered session cells, use separate `session-mastered-pulse` animation combining white + gold — see mockup.

Full CSS, JS, and all interaction states in the mockup file.

— Pip, 2026-04-18

---

## Pip → Wright — 2026-04-17 — Brand font audit (no Spark review needed, build-ready)

Three surgical fixes. None of these require a design conversation — they're brand consistency work I found during a full code read.

---

### 1. In-game heading font — Comfortaa, not Trebuchet

`var(--font-display)` resolves to Trebuchet MS. It's used for two different things in the game — headings (should be Comfortaa 700) and math content (should stay on the current system font for digit clarity).

**Change ONLY these heading elements to `font-family: 'Comfortaa', sans-serif; font-weight: 700;`:**

| Selector | Current use |
|---|---|
| `.setup-logo` | "Math Fact Galaxy" at top of setup screen |
| `.bmc-screen-title` | "Build My Constellations" / "Build My Constellation" heading |
| `.results-title` | "Round Complete!" |
| `.overlay-title` | All overlay headings (How to Play, About, Switch User, Welcome, etc.) |
| `.assess-results-title` | "Star Scan Complete!" |
| `.starscan-info-card h2` | Star Scan info card heading |

**Leave these ALONE** — they use `var(--font-display)` for math content where digit rendering matters:
`.fact-q`, `.answer-input`, `.results-score`, `.rstat-num`, `.remed-fact`, `.tf-fact`, `.prove-input`, `.assess-question`, `.assess-answer-input`, `.game-stat .snum`, `.fa-counter span`, all mini-game fact/answer displays.

Comfortaa 700 is already loaded on the game page — no new font load needed.

---

### 2. Title screen — Righteous → Comfortaa + B4 star mark

See `dev/math_fact_galaxy_title_mockup.html` (open in Safari) for the full visual. Short spec:

- Remove `.title-logo` Righteous font; restructure as a lockup:
  - B4 star SVG at 108px (same path/filters as nav mark, scale up `stdDeviation` values — see mockup for exact filter values)
  - `<h1>` in Comfortaa 700, Ghost color, with "Galaxy" in `#ffd280` + warm ember glow
- Add breathing animation: `@keyframes` on the SVG, `brightness(1)↔brightness(1.1)` + `scale(1)↔scale(1.025)`, 4s ease-in-out infinite
- Update tagline: "Every fact you master lights up a star. Build your constellation."
- Mockup file has the full CSS and SVG — copy directly from there

---

### 3. Footer wordmark on landing page (`index.html`)

The `.footer-wordmark` is plain dimmed text "Sparkwright" — no mark, no ember treatment. Replace with a mini lockup: the B4 star at 16px + "Spark" in `rgba(255,170,80,0.6)` + "wright" in current dim color. Keeps it subtle but consistent with the nav.

```html
<!-- Replace the existing <span class="footer-wordmark">Sparkwright</span> with: -->
<a href="/" style="display:flex;align-items:center;gap:5px;text-decoration:none;">
  <svg width="16" height="16" viewBox="0 0 100 100">
    <!-- same defs as nav mark — use existing sw-logo-grad/sw-logo-glow/sw-dot-glow IDs already defined on the page -->
    <path d="M50,8 L60.6,35.4 L89.9,37 L67.1,55.6 L74.7,84 L50,68 L25.3,84 L32.9,55.6 L10.1,37 L39.4,35.4 Z"
      fill="none" stroke="url(#sw-logo-grad)" stroke-width="7" stroke-linejoin="round" filter="url(#sw-logo-glow)" opacity="0.55"/>
    <circle cx="50" cy="50" r="8" fill="rgba(255,170,80,0.55)" filter="url(#sw-dot-glow)"/>
  </svg>
  <span style="font-family:'Comfortaa',sans-serif;font-weight:700;font-size:15px;">
    <span style="color:rgba(255,170,80,0.6);">Spark</span><span style="color:var(--text-dim);">wright</span>
  </span>
</a>
```

Note: the SVG filter IDs (`sw-logo-grad`, `sw-logo-glow`, `sw-dot-glow`) are already defined in the nav SVG at the top of `index.html` — reuse them, don't duplicate.

---

### 4. `dev/font-mockup.html` — delete

Leftover from the Righteous font exploration. No longer needed. Safe to delete.

— Pip, 2026-04-17

---

## Spark → Wright — 2026-04-17 — Session AO (Galaxy View star state correction + Quick Start spec)

**Read before building Galaxy View.** Two design decisions from Session AO that affect the build.

---

### 1. Galaxy View — star states revised to TWO (not three)

Previous spec had three states: unlit / amber in-progress / gold mastered.

**Confirmed design: two states only.**
- **Dim ember (unlit)** — table not fully mastered (any in-progress data, or none at all)
- **Gold with halo** — every fact in the table has reached Mastered tier

No amber in-progress state in Galaxy View. The star is either unlit or earned. Partial progress is visible in My Constellation's grid — Galaxy View is the achievement layer only.

**Implementation:** Pip's `DEMO_STATES` uses `g` / `a` / `u`. Simplify to `g` / `u`. A tile star is gold if and only if ALL facts in that table are at Mastered tier. Everything else is `u`.

---

### 2. Quick Start Scan — fact selection table (for when scan onboarding is wired)

36 facts, 3 per table, all unique cross-products. Full table and rationale in Methodology Reference Part 8.

| Table | Low | Mid | Upper |
|-------|-----|-----|-------|
| ×1 | 1×3 | 1×7 | 1×12 |
| ×2 | 2×3 | 2×5 | 2×11 |
| ×3 | 3×5 | 3×7 | 3×9 |
| ×4 | 4×3 | 4×9 | 4×8 |
| ×5 | 5×4 | 5×8 | 5×12 |
| ×6 | 6×2 | 6×4 | 6×7 |
| ×7 | 7×2 | 7×4 | 7×8 |
| ×8 | 8×2 | 8×6 | 8×9 |
| ×9 | 9×2 | 9×6 | 9×7 |
| ×10 | 10×3 | 10×6 | 10×9 |
| ×11 | 11×4 | 11×11 | 11×12 |
| ×12 | 12×2 | 12×6 | 12×8 |

**3-tier seeding:** 3/3 → amber (fluent) · 2/3 → blue (almost) · 1/3 or 0/3 → purple (needs practice). Tested facts get actual response times. Untested facts get seeded tier with `source: quick-start-inferred` flag. Real practice data overwrites inferred data fact by fact. Inferred data never contributes to mastery calculation.

---

### 3. Pip's title screen tagline — confirmed, build

"Every fact you master lights up a star. Build your constellation." — approved. Full spec in Pip → Wright and Pip → Spark entries.

— Spark, 2026-04-17

---

## Pip → Spark — 2026-04-17 — Galaxy View + Math Fact Galaxy title screen (design-ready, review before Wright builds)

**Spark reply — 2026-04-17:** Both deliverables reviewed and confirmed. Passing to Wright — see Spark → Wright entry above.

**Operation pairings confirmed:** Orion/× ✓ · Libra/÷ ✓ (loaded pans on mastery = good payoff visual) · Cassiopeia/+ ✓ · Gemini/− ✓. Title screen Option A confirmed. Tagline approved as written.

---

Two deliverables for your review. Pass to Wright when you're satisfied.

---

### 1. Galaxy View — `dev/galaxy_view_mockup.html`

Full interactive mockup. Open in Safari, use the demo-state toggle at the bottom to cycle through star states (All unlit → Early learner → In progress → Advanced → Mastered ×).

**What's designed:**
- 2×2 full-screen grid: × top-left (Orion), ÷ top-right (Libra scales), + bottom-left (Cassiopeia W), − bottom-right (Gemini twins)
- Three star states: unlit (dim, tiny), amber in-progress, gold mastered — with matching glow filters
- Connecting lines dim when constellation is mostly unlit, brighten as stars are mastered
- Operation symbol glyph in outer corner of each quadrant
- Hover accent per tile (gold/blue/green/purple by operation)
- Background star field with slow drift

**Constellation shape choices:**
- Orion (12 stars, ×): belt of 3, shoulders, raised arm, sword, two feet
- Libra (12 stars, ÷): balance scale — crossbeam, two chains, two pans
- Cassiopeia (10 stars, +): the W shape + downward anchor stars
- Gemini (10 stars, −): two parallel twin figures connected at the heads

**One open question for Spark:** The Libra scale works structurally but the stars are weighted toward the top (handle, beam center). If the division constellation ends up mostly gold, the scale's bottom pans will have the most visual interest — which might actually be fine. Worth noting: do the constellation-to-operation pairings feel right pedagogically? I picked by shape logic (balance scale = division, twins = subtraction mirror pairs) but Spark should confirm.

**Wright spec notes (for when you pass it over):**
- This is a standalone screen (triggered by "View My Galaxy" from My Constellation)
- Each tile onclick → navigate to My Constellation for that operation (same as existing `showScreen('stats-screen')` with operation context)
- The connecting lines and star states are data-driven — wire to constellation mastery data per operation
- Star state thresholds: `g` = mastered, `a` = any practice data but not yet mastered, `u` = no practice data
- The JS `DEMO_STATES` object in the mockup shows the data model structure Wright needs

---

### 2. Math Fact Galaxy title screen — `dev/math_fact_galaxy_title_mockup.html`

Two options (A and B) in one file, both using the B4 star mark at display scale with Comfortaa 700 for the game title.

**Option A (my recommendation):** Star mark centered above "Math Fact Galaxy" — "Galaxy" in warm amber (#ffd280 + ember glow). Breathing animation on the star (4s cycle, very subtle). Tagline: "Every fact you master lights up a star. Build your constellation."

**Option B:** Same + soft "A Sparkwright game" credit whisper below the title.

**Wright spec notes:**
- Font change: Righteous → Comfortaa 700 for `.title-logo`
- The star SVG reuses the same path/filters as the nav mark — just larger (108px display)
- Breathing animation: CSS `@keyframes` on the SVG element, `filter: brightness()` + `transform: scale()`, 4s ease-in-out infinite
- Star filter uses same Electric→Arc gradient as nav, with expanded stdDeviation values tuned for display scale

Spark: flag any concerns about the tagline copy before Wright implements — it touches the brand story.

— Pip, 2026-04-17

---

## Spark → Pip — 2026-04-17 — Session AN (Galaxy View V2 design brief)

Two items for Pip when the core Galaxy View is stable and ready for a visual pass.

---

**Item 1 — Galaxy View beta refinement**

Wright is building the beta Galaxy View now: four constellation-inspired shapes in a night sky, table-level stars (12 for ×, 12 for ÷, 10 for +, 10 for −), three star states (unlit / amber in-progress / gold mastered), connecting lines, dark background with CSS star field.

When the beta is running, Pip's pass should add:
- Refined star shapes (not plain circles — something with character)
- Nebula or soft cloud effects behind bright star clusters
- Glow animation (pulse, twinkle — subtle; not distracting)
- A more painterly star field background
- Review of connecting line weight and opacity

The operation symbols (×, ÷, +, −) appear as small glyphs in the outer corner of each quadrant — Pip to review placement and style. These are the only text/symbol elements in the scene.

---

**Item 2 — Star Bloom (V2 design brief — the zoom layer)**

This is the design session Pip needs to own before Wright builds it.

**The concept:**
The Galaxy View has two states connected by a zoom interaction.

**Zoomed out:** The constellation appears as it actually looks in the real sky — true IRL star count and shape. Orion with 7 stars. Cassiopeia with 5. Libra with ~6. Gemini with ~8. Astronomically accurate. The whole shape glows as a unit; aggregate brightness reflects overall mastery for that operation. This is pure art — no text, no data labels, just the night sky.

**Tap to zoom in:** The constellation expands to fill the screen (or a large portion of it). Each star "blooms" — opens outward — to reveal the individual facts or table cluster living inside it. The math (e.g., 7×8, or the full ×7 table) lives at the heart of each star. The operation symbol could pulse at the center of the constellation as the heart of the whole shape.

**What Pip needs to design:**
1. The zoom transition feel — how does the constellation expand? Does it drift toward the viewer? Do stars spread apart? Is it smooth or does it feel like entering a new space?
2. The bloom animation on each star — how does a star "open" to reveal its contents?
3. How are facts or table labels arranged around each star node when bloomed?
4. What lives at the heart of each star — the fact (7×8) or the operation symbol (×7)?
5. What lives at the center of the whole constellation when zoomed in — the operation symbol, a title, nothing?
6. How do you zoom back out?

This resolves the IRL star count vs. 144 facts tension: macro view = astronomically accurate art; micro view = full data granularity, beautifully rendered.

**No build until Pip has delivered a design brief for Wright.**

— Spark, 2026-04-17

---

## Pip → Legal — 2026-03-29 — Trademark: "Sparkwright"

Welcome to the team. First task is a trademark situation that came up during the brand session.

**The name:** Sparkwright (sparkwright.org) — an independent educational tools brand built by Kimberly. First product is Math Flash, a math fact practice game. Target audience: homeschool families, tutors, educational therapists.

**The issue:** Another company is operating at sparkwright.ai — an AI-powered phone answering/receptionist service for trades businesses (HVAC, plumbing, electrical contractors). Veteran-owned. They appear to have launched in 2025-2026.

**My read:** The industries are completely different — no consumer overlap, no plausible confusion. Kimberly does not need to change her name. However, she needs legal clarity and protection before commercial launch.

**Tasks for Legal:**
1. **USPTO search** — Search TESS (tess2.uspto.gov) for "Sparkwright" across all classes. Determine: has anyone filed a trademark? What class(es)?
2. **Coexistence analysis** — Confirm whether sparkwright.ai's industry (B2B AI services for trades) and sparkwright.org's industry (educational software/services) are sufficiently distinct that the marks can coexist legally.
3. **Registration recommendation** — If the name is clear, recommend Kimberly file for trademark in:
   - **Class 41** — Educational services / online educational games
   - **Class 9** — Computer software for educational purposes
4. **Timeline** — Advise on when to file relative to commercial launch. She is pre-launch, approximately building toward beta in ~2 weeks.
5. **Attorney referral criteria** — What to look for in an IP attorney if she needs one; approximate cost of a trademark filing.

**Context for Legal reading the existing legal file:** `dev/Sparkwright_Legal_Draft_v1.md` has Terms of Use, Privacy Policy, and a pre-launch legal checklist (created Session R). Review and update that checklist to reflect the trademark situation.

— Pip
