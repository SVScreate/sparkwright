# Sparkwright — Website Copy Draft
*Created: 2026-03-28 — Session R*
*Updated: 2026-03-28 — Session T (Tier 2 and Tier 3 revised; developer to fine-tune voice)*
*Author: Spark (Research & Pedagogy agent)*
*Status: Rough draft — developer edit pass needed before anything goes live*

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

*Voice note: drafted in first person — the developer's voice. She will edit this to sound like herself before it goes live. This is a starting point, not a final script.*

---

### Page Title

**About Sparkwright**

---

I'm a teacher with a Master's in Educational Therapy and 15+ years working with students — public schools, private schools, homeschool settings, a lot of one-on-one work with kids who learn differently. Over those years I kept running into the same problem: the tools that existed were built for schools, not for the people actually sitting with a student. Account systems, admin dashboards, monthly reports. Nothing designed for a tutor with one kid and 45 minutes.

Sparkwright is me finally building what I kept looking for.

The plan is a growing collection of games and tools — made one at a time, grounded in real teaching experience and research I've actually read. Math Flash is the first. Each one starts with a specific gap I identified in my own work and ends with something I'd use with my own students.

---

### How these tools work

No accounts, no subscriptions. Session data stays in the student's browser — not on a server, not in a system I control. You decide what to practice, at what pace, with what settings. The software tracks what happens and gives you something readable at the end.

That's the design philosophy in plain terms: you and the student are in charge, not the program.

---

### The research behind the design

My training in Educational Therapy means I've read the research on fluency thresholds, error correction, cognitive load, and processing speed differences in students with ADHD, dyslexia, and dyscalculia. The design decisions here come from those sources, not from gut instinct or convention.

I cite what I use. Where a claim is sourced, I can tell you exactly where it comes from. Where something can't be verified, I say so rather than papering over the gap.

---

### Who this is for

Homeschool families, tutors, educational therapists, and independent teachers who want tools that work in small settings without an IT setup. If you've used one of the major platforms and found it either too anxiety-inducing for your student, too locked-down in how it operates, or just not designed for the way you actually work — that's the gap these tools are meant to fill.

---

Sparkwright is one person. I respond to emails personally and take feedback seriously. If something doesn't work the way you expected, I want to know.

[contact@sparkwright.org]

---

---

## Tier 3 — Math Flash "About" (Title Screen)

*Per developer direction (Sessions R + T): this copy lives as a panel or modal on the Math Flash title screen, accessible from an "About" button. NOT a standalone webpage. Wright: build as a scrollable panel or modal reachable from the title/setup screen. Not a separate HTML page.*

*Audience: the parent or teacher looking at the game for the first time and trying to understand what it is and why it works the way it does. Not the student mid-session.*

---

### Panel Heading

**About Math Flash**

---

Math Flash is a math fact practice game for grades 2–8, designed for 1:1 and small-group use with a teacher or parent in the room.

---

### The idea behind it

Most math fact tools handle a missed answer the same way: show the right answer, log the miss, and keep going. The algorithm will show that fact again sometime. That approach always bothered me — the moment a student misses something is exactly when they're ready to work on it. Math Flash stops at that moment and does something about it.

---

### Practice Quest

When a student misses a fact after two attempts, the round stops and Practice Quest begins:

**Find It** — Locate the correct answer. No timer, no pressure.

**Practice** — A short activity with the fact in a different mode, outside the timed context where it just failed.

**Prove It** — Answer the fact correctly before returning to the round.

The round timer pauses for the full sequence and resumes where it left off. There's no score penalty for a miss — Practice Quest is a learning moment, not a punishment. Research on error correction consistently shows that structured practice at the moment of failure produces better long-term retention than errorless approaches, where mistakes are minimized and the student moves on. No major math fact platform handles a wrong answer this way.

---

### Fluency grading

Math Flash measures response time, not just accuracy.

**⚡ Fluent** — Correct in 3 seconds or under. At this speed the fact is coming from memory, not calculation.

**🔄 Almost** — Correct in 4–6 seconds. The student knows it — it just isn't automatic yet.

**📚 Needs Practice** — Wrong answer, or no answer within the time limit.

The 3-second threshold comes from math fact automaticity research: below 3 seconds generally indicates direct memory retrieval; 4–6 seconds suggests the student is still calculating, even when they get it right. For students with documented processing speed differences, the threshold is adjustable. 5 seconds aligns with a 1.5× extended-time accommodation; 6 seconds with 2×. Results labels update to reflect whatever threshold is in use.

---

### Mastery

A fact isn't marked as mastered from one good session. Math Flash calls a fact mastered when a student answers correctly within the fluency threshold on 4 of their last 5 attempts, across at least 2 separate sessions, with consistent response times.

The two-session requirement is there because one good day isn't mastery. The consistency check matters because a student whose response times swing widely between attempts isn't retrieving automatically — they're somewhere in between.

---

### Results

After the round, the results screen shows what happened: fluent facts, developing facts, anything that went to Practice Quest. It's readable without a manual and printable if you want a record. No login, no dashboard, no waiting for a report.

---

### Settings

You choose the facts, the timer mode, the fluency threshold, and whether Practice Quest is on. Math Flash covers addition, subtraction, multiplication, and division, including tables up to ×15.

---

*Built by a teacher with a Master's in Educational Therapy and 15+ years working with students across public, private, and homeschool settings.*

**[Start →]**

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
