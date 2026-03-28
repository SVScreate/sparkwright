# Sparkwright — Website Copy Draft
*Created: 2026-03-28 — Session R*
*Author: Spark (Research & Pedagogy agent)*
*Status: Rough draft — awaiting developer review and edit pass*

---

## Notes for Wright

This file contains rough draft copy for three tiers of the site. Nothing here is final — the developer will edit for voice and accuracy before anything goes live. Your job is structure; this file gives you the content to work with.

**What's here:**
- **Tier 1** — Drop-in improvements to the existing `index.html` landing page (hero eyebrow, Math Flash card description, about strip)
- **Tier 2** — Full About page draft (currently no dedicated About page exists — nav "About" link scrolls to a strip on the landing page)
- **Tier 3** — Math Flash "About" copy, intended for a panel/modal on the game's title screen (not a separate HTML page — see Tier 3 section for Wright's build note)
- **Coming-soon cards** — improved card descriptions (names unchanged; see open question at bottom)

**Open question flagged at the bottom of this file** — one thing Spark needs the developer to answer before the landing page copy is final.

---

## Tier 1 — Landing Page Copy

*Drop-in replacements for existing `index.html` sections. Keep all existing structure and styling.*

---

### Hero Eyebrow

**Current:** `Independent learning tools`

**Draft:** `For homeschool families, tutors, and independent educators`

*Note: This is a positioning choice — it signals the audience rather than the product category. If she'd prefer to keep it as a category label, "Independent learning tools" is fine. Worth discussing.*

---

### Hero Tagline

**Current:** `Handcrafted learning, built to spark.`

**Recommendation:** Keep. It's working.

---

### CTA Button

**Current:** `See what's here`

**Recommendation:** Keep.

---

### Math Flash Game Card

**Current:**
> A smart flashcard game for building real math fact fluency — not just drilling, but actually learning.

**Draft:**
> Math fact practice built around what happens when a student misses an answer. Most tools mark the miss and move on. Math Flash stops and teaches it right then.

*One sentence for why it exists, one sentence for what makes it different. No hype.*

---

### About Strip — Heading

**Current:** `Built by a teacher, for real students.`

**Recommendation:** Keep.

---

### About Strip — Body Copy

**Current:**
> Sparkwright is an independent project — one educator building tools that actually work in the classroom, not tools that just look like they do.
>
> Everything here is designed around how learning actually happens: with friction, with feedback, and with a student who deserves more than a multiple-choice quiz.

**Draft:**
> Sparkwright comes from a teacher with a Master's in Educational Therapy and 15+ years in classrooms — public schools, private schools, homeschool settings. These tools exist because the right ones didn't.
>
> Every design decision starts with the moment a student struggles. Not how to log it, not how to report it upward — what should actually happen right then.

---

### About Strip — Value Bullets

**Current:**
1. Practice with purpose — Every question, every response, every moment matters. No filler.
2. Mastery, not completion — The goal isn't to finish the worksheet. It's to actually know it.
3. Design that respects students — Dark mode, clean type, real feedback. Not clipart.
4. Made by hand, one spark at a time — No venture backing, no growth team. Just careful work.

**Draft (same structure, tightened):**
1. **Practice with purpose** — No filler, no busywork. Every question has a reason to be there.
2. **Mastery, not completion** — The goal isn't to finish the round. It's to actually know it.
3. **Design that respects students** — Clean, readable, built for middle schoolers as much as second graders. Not clipart.
4. **Made by hand** — No venture backing, no growth team. One educator doing careful work.

*Note: "Not clipart" in bullet 3 is strong — kept. "One spark at a time" in the original header is good as a tagline element but slightly precious as a body bullet. Shortened here.*

---

### Coming-Soon Cards

**See open question at bottom before finalizing these.**

**Spelling Sprint**
*Current:* Pattern-based spelling practice that builds confidence through repetition and rhythm.
*Draft:* Spelling practice built around pattern recognition and word structure — the kind that makes the rules stick, not just the words.

**Number Sense Lab**
*Current:* Visual tools for building number intuition — fractions, place value, and mental math.
*Draft:* Visual tools for understanding how numbers actually work — fractions, place value, and mental math with something to look at, not just something to memorize.

**Timed Challenge**
*Current:* Formal timed tests with fluency grading — a clean measure of where you really stand.
*Draft:* A clean, timed assessment of what a student genuinely knows. Results are graded by fluency level, not just right or wrong.

---

---

## Tier 2 — About Page (Full Draft)

*This does not currently exist as a standalone page. The nav "About" link scrolls to the about strip on the landing page. This draft is for a full `/about.html` page, linked from the nav. Wright: add "About" to the nav as a page link (not anchor) when this is built.*

*Voice note: drafted in first person — the developer's voice, not a brand voice. She should edit this to sound like herself. This is a starting point, not a script.*

---

### Page Title

**About Sparkwright**

---

### Opening

I couldn't find what I needed, so I built it.

That's the honest version. The longer version takes a minute.

---

### Who Built This

I'm a teacher. Master's in Educational Therapy, 15+ years working with students across public schools, private schools, and homeschool settings — many of them struggling, most of them capable, all of them deserving better than what the mainstream tools were offering.

I'm not a software company. I'm not venture-backed. I built these tools because I kept running into the same gap: there was nothing that handled the moment a student got an answer wrong the way that moment deserved to be handled.

---

### Why These Tools Exist

Most math practice software does the same thing when a student misses an answer: it shows the correct answer, logs the miss, and moves on. The algorithm will show that fact again sometime. Maybe today, maybe in three days.

That's not remediation. That's deferral.

I wanted a tool that stopped at the moment of failure and actually did something about it — right then, before the student moved on. That tracked which facts a student had genuinely internalized versus which ones they were reconstructing on the fly each time. That let the teacher stay in control of what was practiced, at what pace, with what accommodations.

I also didn't want to hand over a child's practice data to a server somewhere so it could surface in a monthly report the teacher reads six weeks later.

I looked for that tool for a long time. I couldn't find it. So I built it.

---

### A Tool, Not a Program

There's a real difference between the two. A program has its own agenda: it decides what the student does next, in what order, at what pace. The teacher manages the program. The student complies.

A tool does what you tell it. The teacher decides what to practice. The student and teacher stay in the driver's seat. The tool tracks what happens and gives you something useful at the end.

Every design decision in Sparkwright tools comes back to that distinction. The settings exist because you know your student better than any algorithm does. The data is readable because you should be able to understand it without a dashboard. The accommodations are there because one size hasn't fit all the students I've worked with, and it won't fit yours either.

---

### Your Data Stays With You

Sparkwright tools store data in your browser's local storage. No account required to play. No server, no subscription keeping your history hostage, no data harvested or analyzed by a third party.

If you stop using a Sparkwright tool, your session history stays in your browser until you clear it — and eventually, there will be an export option so you can keep it on your own terms.

This is a choice, not a limitation. The value isn't "we hold your data and show you charts." It's a better learning experience, and the data is yours.

---

### On the Research

The design decisions here aren't guesses.

The 3-second fluency threshold comes from research on what distinguishes automatic retrieval from effortful calculation — a fact answered in under 3 seconds is almost certainly pulled from memory, not reconstructed. The in-moment remediation approach is grounded in work on error correction: for most learners, structured feedback at the moment of failure produces better retention than errorless practice. The accommodation options reflect what's known about processing speed differences in students with ADHD, dyslexia, and dyscalculia.

The citations are in the documentation — not paraphrased from a white paper, but read and verified. Where the research is unclear or a claim can't be sourced, it's marked that way. I'd rather leave an honest gap than fill it with a confident-sounding guess.

None of this means Sparkwright tools have been clinically validated. They haven't. What it means is that the principles they're built on are real, cited honestly, and applied with the same care I'd want from a tool being used with my own students.

---

### Who This Is For

Homeschool families working one-on-one with their kids. Independent tutors and educational therapists who need session-level data they can actually hand to parents. Small classroom teachers who want something that works without an IT ticket.

Specifically: people who've tried the mainstream platforms and found them cold, or overwhelming, or just not built for the moment when a student actually needs help.

If you've ever watched a child get anxious at a ticking timer, or wondered what a monthly report was actually telling you, or wished you could just skip the operation your student already knows and go straight to what they're working on — this is built for you.

---

### A Last Note

Sparkwright is one person building tools she believes in. There's no team, no roadmap deck, no growth metrics. There's a teacher who spent years in the room with students and finally has the means to build what she always wanted to use.

The work is careful. The standards are high. The goal is simple: a student who walks away knowing something they didn't know when they sat down.

---

---

## Tier 3 — Math Flash "About" (Title Screen)

*Per developer direction (Session R): this copy lives as a dedicated About section accessible from the Math Flash title screen — not a standalone webpage. Wright: build this as a panel or modal reachable from a button on the game's title/setup screen (e.g., "About Math Flash" or "How this works"). Not a separate HTML page.*

*Audience: the parent or teacher looking at the game for the first time and trying to understand what it is and why it works the way it does. Not the student mid-session.*

---

### Page Heading

**Math Flash**

*Math fact fluency practice built around the moment a student gets an answer wrong.*

---

### The Problem With Most Math Drill Tools

Most of them handle a missed answer the same way: show the right answer, log the miss, keep going. The algorithm decides when to show that fact again. The student moves on.

The problem isn't the algorithm. It's the timing. The moment a student misses a fact is the exact moment they're primed to learn it — attention is up, the error is fresh, the brain is looking for the correction. That window closes fast. By the time the fact recycles, it's just another card.

Math Flash was designed to work in that window.

---

### What Happens When a Student Misses an Answer

The round stops. No score penalty, no alarm. The student enters a Practice Quest: a short, structured sequence built around that one fact.

**Find It** — The student locates the correct answer. Low pressure, no timer.

**Practice** — A brief mini-game reinforces the fact in a different mode. The goal is to separate it from the pressure context where it just failed.

**Prove It** — The student answers the fact correctly before returning to the round.

The round timer pauses for the entire sequence. When Practice Quest is complete, the round resumes where it left off.

This isn't a punishment mechanic. Research on error correction consistently shows that structured feedback at the moment of failure produces better long-term retention than errorless approaches — where errors are minimized and the student just keeps moving. Practice Quest is the direct design response to that research.

---

### How Fluency Is Measured

Math Flash tracks not just whether an answer was correct, but how fast it came.

**Fluent (⚡)** — Correct in 3 seconds or under. At this speed, the fact is being retrieved from memory, not recalculated.

**Almost (🔄)** — Correct in 4–6 seconds. The student knows it; it isn't automatic yet.

**Needs Practice (📚)** — Wrong answer, or no answer within the time limit.

The 3-second threshold comes from research on math fact automaticity — specifically, the point at which response time suggests direct memory retrieval rather than effortful calculation. Students working at 4–6 seconds may know the fact but haven't yet internalized it to the point where it's freeing up working memory for harder math.

**Accommodation options.** For students with documented processing speed differences, the fluency threshold is adjustable. A 5-second threshold aligns with a 1.5× extended-time accommodation; 6 seconds aligns with 2×. These correspond to conventions used in IEP and 504 practice. The labels on the results screen update to reflect whatever threshold is in use.

---

### Mastery Tracking

A single fast answer isn't mastery. Math Flash defines a fact as mastered when a student has answered correctly in under the fluency threshold on 4 of their last 5 attempts, across at least 2 separate sessions, with consistent response times.

The two-session requirement is there because one good day isn't mastery. The consistency check is there because a student who answers in 1 second sometimes and 6 seconds other times isn't automatic on that fact — they're alternating between retrieval and calculation.

---

### After the Round

The results screen shows what happened: which facts were fluent, which are developing, which triggered Practice Quest. Print it or keep it on screen. The data is readable without a manual — a teacher who's never used Math Flash before can look at the results and understand what they mean.

There is no login, no monthly report, no dashboard. What happened in this session is visible right now, in plain language. That's the design intent.

---

### Who Math Flash Is Designed For

Students in grades 2–8 working on multiplication and division fluency. It works well in 1:1 and small-group settings where a teacher or parent can watch what's happening and adjust settings mid-session if needed.

Particularly useful for:
- Students who've had anxiety with timed tools — the round timer pauses during Practice Quest, and there's a no-timer mode for students who need it
- Students working past ×12 (Math Flash supports tables up to ×15, a range most tools don't cover)
- Teachers who use mastery-based curricula and need a tool that matches that philosophy rather than pushing students forward before facts are solid

---

### Your Data

Math Flash stores session data in your browser's local storage. No account required. No data sent to any server. If you share a device, multiple student profiles are supported — each with their own history, stored separately.

---

### [Play Math Flash →]

---

---

## Open Questions

### 1. Coming-soon card names — are these locked?

The landing page currently shows three coming-soon cards: **Spelling Sprint**, **Number Sense Lab**, and **Timed Challenge**. These were added by Wright and may be placeholders. Before finalizing the card copy:

- Are these real planned products with names you're committing to?
- Is "Timed Challenge" a separate product, or a mode within Math Flash (MPF item 64 mentions a timed test mode)?
- Is "Spelling Sprint" a game in the vein of Math Flash, or something different?

*Hold the coming-soon card copy until these are confirmed. The draft above can be updated once names and descriptions are locked.*

### 2. Math Flash "About" — resolved

Developer confirmed (Session R): this copy lives as a section/modal on the Math Flash title screen. Wright to build as a panel reachable from the title/setup screen. Not a standalone page.

### 3. About page — first or third person?

The About page is drafted in first person (developer's voice). This is the right call for an indie product, but it only works if the developer edits it to sound like herself. If she'd rather keep it in third person for now, that's easy to convert.

---

*This file is a working draft. Do not use any copy here in the live site without developer review and edit. Prices, feature descriptions, and any claims about what is or isn't built should be verified against the current game before publishing.*
