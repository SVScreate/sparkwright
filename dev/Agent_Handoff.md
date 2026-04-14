# Agent Handoff — Wright ↔ Spark ↔ Pip ↔ Pop ↔ Legal
*Shared coordination file between the Sparkwright Claude agents.*
*Last updated: 2026-04-14 — Session AL (Wright)*

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

## Wright → Spark — 2026-04-14 — Session AL (v83a)

**"Falling Facts" — renamed from "Fact Catcher".** Display text updated throughout. Internal function/class names stay as `factCatcher`/`fc-*` for stability.

**Beta testing session today — items flagged for Spark:**

**Practice session definition question.** Constellation stat cards currently show "2/2 practice sessions ✓" based on 2 unique calendar dates in `recentAttempts`. Kimberly noticed this and asked: should we require MORE sessions before mastery? And what exactly counts as a "practice session"? Right now it's any day with at least one timed attempt recorded. Spark: is the 2-session minimum pedagogically sound, or should it be higher (3? 4?)? Does a session need a minimum number of attempts to count? This affects mastery criteria design — the current 2-session gate was a placeholder.

**Constellation reimagining — log for future design exploration.** Kimberly wants a conversation about whether there could be a second view: click a button and the grid "scatters" into a real constellation shape (a sky field), where fact dots retain their tier colors and form a shape — maybe the user's avatar. Grid remains the primary view; this would be a toggle/alternate view. Not a build item — just a design conversation worth having.

**Mini-game area spec — urgent.** Kimberly confirmed the concept today: in My Constellation, clicking a fact shows a button to open a mini-game menu. Student picks from 3 Practice Quest mini-games → plays a quick PQ round for just that fact. Needs: a name (better than "mini-game madness"), a spec (how does the mini-game menu card look? what 3 games are available?), and confirmation that this lives inside My Constellation (not a separate screen). This was flagged in AK and now has more detail — Spark should spec it.

**PQ engagement concern — Spark's territory.** Beta tester (Kimberly's nephew) noted that kids might intentionally get facts wrong to play mini-games, and that the PQ timer pause encourages kids to "check out." Is intentional wrong-to-PQ a real risk that needs a design fix, or is the pedagogy working as intended (PQ IS supposed to be the learning moment)? Spark's read on whether we need to add friction to PQ entry.

**Settings page redesign — needs design thinking.** Constellation is only fed by Per-Question Timer mode. Currently all modes share one settings screen. Kimberly suggested separating "Constellation Builder mode" (Per-Question Timer) from practice/exploration modes. Or maybe two areas: "Build your constellation" vs. "Practice tool." Design discussion needed before any code — Spark should think about the mode hierarchy first.

— Wright, 2026-04-14

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
