# Sparkwright — Research & Pedagogy (RP)
*Last updated: March 25, 2026 — Session N (literature review pass)*
*Companion file to the Math Flash MPF. Both files live in `dev/` and are updated together.*

---

## Guidance for Future AI Instances

This file is the intellectual backbone of Sparkwright and Math Flash. It holds the research, pedagogy, philosophy, competitive landscape, and developer reflections that inform every design decision. The MPF is the operational file (to-do lists, file structure, session notes). This file is the *why* behind the *what*.

**Standard for all work in this file:**
> "You must, at all times, keep best practices and the highest level of accuracy and academic/educational integrity as the banner you carry into all work you do on this. You must never hallucinate, be honest first, and leave things out rather than create unsubstantiated filler."

This means: cite only sources you have actually found and can describe accurately. If a claim needs research that hasn't been done, say so explicitly and leave a placeholder. Do not paraphrase a paper you haven't read. Do not invent supporting evidence for a position the developer already holds. The goal is a document that could be handed to a skeptical academic and hold up.

When reading this file:
- Trust the seed conversation as verbatim source material — do not edit it
- The sections above the seed conversation are the living, organized version of those ideas
- When new research or reflections emerge in a session, add them here, not just in the MPF
- This file feeds the FAQ, About page, and marketing copy — write with that downstream use in mind
- The developer is not a licensed clinician — see credential language below
- When research is incomplete or a citation cannot be verified, mark it clearly with *(needs verification)* or *(source needed)* rather than leaving it to appear confirmed

---

## Table of Contents
1. Who Is Building This & Why
2. The Core Philosophy & Ethos
3. The Target User *(journal exercise — in progress)*
4. Science & Pedagogy
5. Competitive Landscape
6. Mentor to Developer
7. To Do (RP-specific)
8. Seed Conversation (Verbatim)

---

## 1. Who Is Building This & Why

**Credential language (use this exact framing everywhere):**
> "Built by a teacher with a Master's in Educational Therapy and 15+ years working with students across public, private, and homeschool settings."

This is accurate, compelling, and does not overclaim a licensed clinical title. The developer earned the degree but has not practiced in a licensed clinical role. What they *do* have is arguably more relevant to this product: years of direct classroom experience watching struggling students learn, grounded in graduate-level understanding of how learning works.

**The honest story:** Years spent in the room with kids who were struggling. Academic training to understand why. Built the tool that should have existed. That is a more compelling story than "licensed clinician" — and it is true.

**Why Sparkwright exists:**
- The developer wants to build something real that creates financial independence
- The developer loves building games and wants to build what they wished existed as an educator
- Sparkwright is intended to become a career — a collection of tools and games, not a side project
- The product must be something the developer genuinely believes in and would use with their own students

**Setup:**
- 2019 MacBook Air (1.6GHz dual-core Intel i5, 8GB RAM)
- Claude Pro subscription
- Primary testing browser: Safari
- GitHub repo: `SVScreate/sparkwright` — connected to Netlify for auto-deploy
- Domain: `sparkwright.org`

---

## 2. The Core Philosophy & Ethos

### Rigorous, Not Punishing
Math Flash asks something real of the student. It provides genuine support at the moment of struggle and produces real results. This is the word — **rigorous** — that separates this product from platforms that have optimized for conflict-avoidance dressed up as engagement.

Most competing platforms have achieved the *absence of visible distress*, not genuine engagement. There is a difference between a child who is genuinely engaged and one who has been behaviorally managed into compliance. Reviews across XtraMath, TTRS, and IXL consistently surface language like "a necessary evil" and "math anxiety." That is not happiness — that is suppressed resistance.

### Error + Immediate Feedback Is the Research Standard
Immediate corrective feedback after an error outperforms errorless learning for retention and skill transfer in typically-developing students. Practice Quest is not a punishment mechanic — it is the pedagogically correct response to a miss. See Science & Pedagogy section for full research basis.

### Designed for the Moment of Failure
Every major platform handles the wrong answer the same way: show the correct answer, log the miss, move on. The learning happens later — maybe — when the algorithm recycles the fact. Math Flash handles it *now*, in the moment, before the student moves on. That is a fundamentally different pedagogical stance, and it is the right one.

*"We designed for what happens when a student fails, not just for what happens when they succeed."* No competitor can honestly make that claim.

### Student and Teacher Are in Control
Math Flash is built so that the student and their teacher/helper feel in control of how practice feels. Settings, timer options, and accommodation toggles exist to serve the learner — not to enforce a one-size-fits-all drill. This philosophy should be explicit in the FAQ, onboarding, and About page.

Most competing programs have a sterile, top-down structure: the program drills the student, marks them wrong, and moves on. Math Flash meets students where they are, respects their pace, and gives both student and teacher meaningful guidance on how to use it well.

### Data Belongs to the User
Sparkwright uses localStorage — data lives on the student's device, not on a server. This is a deliberate philosophical choice, not a technical limitation. The student (and teacher/parent) owns their data. It doesn't get harvested, analyzed by a third party, or locked inside a subscription. See the MPF Data Philosophy section for full detail.

### Practice Should Be Rich, Not Rote
Every question should feel purposeful. Mastery is the goal, not completion. Student agency matters — empowering, not punishing. Design quality matters.

---

## 3. The Target User *(journal exercise — in progress)*

**This section is a placeholder pending the developer's journaling exercise (see Mentor to Developer section).**

Working hypothesis based on context so far:
- Homeschool parent or small independent/private school teacher
- Has already tried at least one mainstream platform (XtraMath, TTRS, or similar)
- Found it cold, clinical, or anxiety-inducing for their child
- Cares deeply about *how* their child experiences learning, not just whether they pass a test
- Skeptical of ed-tech data collection — values privacy and simplicity
- Will pay for something that feels purposeful and was made for them
- Likely skews toward families who are already attuned to neurodivergence, learning differences, or educational therapy approaches

*This profile sharpens every product and business decision. Do the journal exercise before finalizing.*

---

## 4. Science & Pedagogy

### The 3-Second Fluency Threshold
The 3-second threshold for fact automaticity is well-established in cognitive load and fluency research. Retrieval under ~3 seconds suggests the fact is stored as a direct memory trace (declarative recall) rather than being computed procedurally. Used by XtraMath, Reflex Math, and grounded in work by Kling & Bay-Williams (2015) *(needs verification)*. *(Note: "Erin Olson" appeared in an earlier draft of this file as an additional citation — no peer-reviewed paper by that name on this topic was found in the Session N literature review. Removed pending verification.)*

**Kling & Bay-Williams (2015)** — *Verified citation:* Kling, G., & Bay-Williams, J.M. (2015). "Three steps to mastering multiplication facts." *Teaching Children Mathematics*, 21(9), 548–559. NCTM. DOI: 10.5951/teacchilmath.21.9.0548. Defines mastery as producing an answer within 3 seconds — a classroom-practical threshold that includes highly efficient strategy application as well as direct recall. Describes three developmental phases: counting (Phase 1), reasoning strategies (Phase 2), mastery (Phase 3).

### Two-Level Fluency Model *(Session I design decision)*

**Level 1 — Per-attempt grade** (in-game, shown during Per-Question Timer mode):
| Grade | Threshold | Meaning |
|---|---|---|
| ⚡ Fluent | Correct, ≤3s | Fast enough to suggest automatic retrieval |
| 🔄 Almost! | Correct, 4–6s | Knows it, not yet automatic |
| 📚 Needs Practice | Wrong or no answer by 7s | Not yet known |

These grades describe a single answer. They are not mastery.

**Level 2 — Longitudinal mastery** (tracked over time, across sessions):
A fact is **Mastered** when a student demonstrates durable, stable automaticity.

**Math Flash Mastery Definition:**
> Correct in ≤3s on **4 out of the last 5 attempts**, spanning **at least 2 separate sessions**, with **low response time variance**.

The 2-session requirement prevents "one good day" mastery. The variance condition is a differentiator backed by research. The exact variance threshold is TBD — to be tuned with real use.

### Response Time Variance as a Mastery Signal

A student who sometimes answers in 1.2s and sometimes in 5.8s is NOT automatic on that fact, even if their average looks good. High intraindividual variance in response time (IIV) is a diagnostic signal of effortful processing — counting or calculating — not automatic retrieval.

**Research basis:**
- **Stickney, Sharp & Kenyon (2012)** — *Verified citation:* Stickney, E.M., Sharp, L.B., & Kenyon, A.S. (2012). "Technology-enhanced assessment of math fact automaticity: Patterns of performance for low- and typically-achieving students." *Assessment for Effective Intervention*, 37, 84–94. Found that low-achieving students required more attempts to demonstrate automaticity, achieved automaticity later, and showed lagging retrieval speed. Recommends a 3-second criterion and notes that students responding within 2 seconds are generally higher achievers. *(Note: the earlier RP framing "even when average speeds are similar" was not confirmed against full text in the Session N review — needs verification before asserting.)*
- **Broader cognitive science:** High IIV is consistently associated with effortful processing vs. automatic retrieval, and decreases as automaticity increases. This is documented in cognitive science literature including developmental research in *Frontiers in Human Neuroscience* (2012). Brain imaging research confirms that the transition from strategy-use to automatic retrieval involves shifts in activated brain regions, and that performance variability marks this transition as incomplete.
- **Reflex Math** explicitly uses "response pattern stability" as a condition for fact certification (Cholmsky, 2011, white paper — commercial document, not peer-reviewed). They can de-certify a fact if variance returns.

### Competitive Mastery Thresholds
| Program | Time threshold | Repetition criterion | Variance check |
|---|---|---|---|
| XtraMath | Default: 6s. Options: 3s, 6s, 10s, 12s (teacher-set). 12s explicitly for students with disabilities. | 2 of last 3, across sessions | No |
| Reflex Math | Proprietary. Adapts automatically by measuring keyboard entry speed at session start. Not teacher-adjustable or transparent. | Proprietary — uses "stability" language | Yes (implied) |
| Rocket Math | Timed (program-set) | 12 consecutive correct | No |
| Math Flash | ≤3s (default). Teacher-adjustable threshold planned (item 113). | 4 of last 5, across 2+ sessions | Yes |

*Note: the earlier RP version listed XtraMath as "≤3s (adjustable)" — this was inaccurate. The 3s option exists in XtraMath but is the fastest/tightest setting, not the default. The 6s default is closer to a 2x accommodation multiplier applied to the 3s research standard. Corrected Session N.*

### Errorless Learning vs. Error Correction

**What the industry does:** The ed-tech industry broadly applies "errorless learning" — minimizing visible wrong answers — as a universal default. Wrong answer: show the correct answer briefly, log the miss, move on.

**Where errorless learning actually comes from:** The technique was not designed as a general pedagogy. Its origin is in basic behavioral research: **Terrace (1963)** demonstrated errorless discrimination learning in animals, building on Skinner's theoretical work. The *application* to humans — specifically individuals with intellectual and developmental disabilities (IDD) and ASD — came in subsequent decades through applied behavior analysis (ABA). The core rationale for that clinical application (errors can trigger behavioral shutdown in some populations; students cannot reliably self-monitor what went wrong) is legitimate in context. The error is in treating a clinical tool as a universal default.

**What the broader research actually says for typically-developing students:**
- **Wong, S.S.H., & Lim, S.W.H. (2022).** "Deliberate errors promote meaningful learning." *Journal of Educational Psychology*, 114(8), 1817–1831. Across two experiments, deliberately committing and then correcting errors outperformed errorless study on both retention and higher-order application. The authors termed this the "derring effect."
- **Yap, J.X., & Wong, S.S.H. (2024).** "Deliberately making and correcting errors in mathematical problem-solving practice improves procedural transfer to more complex problems." *Journal of Educational Psychology*, 116(7), 1112–1128. The math-specific study. University students who deliberately made and corrected errors outperformed errorless practice groups on transfer to novel, more complex problems — including real-life word problems.
- **Metacognitive gap — confirmed:** Students *predicted* they would do better with errorless practice, even after experiencing the benefit of deliberate erring. Explicitly reported in Yap & Wong (2024).
- *(Note: the earlier RP citation "Yap & Wong, 2024; PMC, 2022" conflated these as one citation. These are two separate papers from the same research program. The PMC-indexed paper is likely Wong, S.S.H., et al. (2023) — see PMC9902256. All three papers are real; treat as three separate sources.)*

**Important caveat on clinical populations:** Research on clinical populations with disabilities (TBI, aphasia) is more mixed than the above suggests. A 2017 RCT in adults with severe TBI found error-based learners made *fewer* errors post-intervention than errorless learners. The research on ASD and significant cognitive disability populations specifically does support errorless approaches in certain contexts, but the blanket rule "errorless learning is for disabled students" is an oversimplification. Math Flash's nuanced position — offering it as a teacher-controlled toggle rather than a universal default — is the right response to this complexity.

**Why platforms use errorless learning anyway:**
1. Reduced visible failure improves engagement metrics and subscription retention
2. Errorless approaches are simpler to build — structured in-moment remediation is genuinely hard to design well
3. It is partly a business decision presented as pedagogy

**Math Flash's nuanced position:** The remediation toggle gives teachers the ability to apply errorless-style flow for students where that is clinically appropriate (significant cognitive disabilities, ASD where error correction triggers behavioral shutdown). This is the correct nuanced response — more sophisticated than anything the major platforms offer.

### Math Anxiety and Timed Assessments
Timed math tests are consistently associated with elevated math anxiety in a significant proportion of students. The mechanism is well-documented: performance pressure consumes working memory, impairs mathematical reasoning, and creates aversive associations with math practice.

**What the research supports:**

- **Boaler, J. (2014).** "Research suggests timed tests cause math anxiety." *Teaching Children Mathematics*, 20(8), 469–473. NCTM. The primary peer-reviewed citation for this position. *(Note: Boaler also published "Fluency Without Fear" and "Speed and Time Pressure Blocks Working Memory" as position papers via youcubed — these draw on empirical research by others and are useful for public communication, but are not independent empirical studies.)*
- **Beilock, S.L., & Carr, T.H. (2005).** "When high-powered people fail: Working memory and 'choking under pressure' in math." *Psychological Science*, 16(2), 101–105. Found that performance pressure consumes working memory — and that students *most* reliant on working memory (higher-achieving students) are *most* harmed by time pressure. This is the primary mechanism cited by Boaler and others.
- **Young, C.B., Wu, S.S., & Menon, V. (2012).** "The neurodevelopmental basis of math anxiety." *Psychological Science*, 23(5), 492–501. fMRI study of 7–9-year-old children. Found that math anxiety is associated with hyperactivity in the right amygdala (fear processing), elevated hippocampal activity, and *reduced* activity in regions involved in mathematical reasoning. These effects were specific to math anxiety, not general anxiety. *(This is the research basis for the amygdala claim — note: the study examines math-anxious children, not a timed assessment trigger directly.)*

**What was removed and why:** An earlier version of this file stated "Brain scans show the amygdala activating after approximately 90 seconds of time pressure." No source for the 90-second figure was found in the Session N literature review. This specific claim appears to derive from popular neuroscience writing (Jill Bolte Taylor), not math anxiety research. It has been removed. Young et al. (2012) is the appropriate citation for the amygdala and math anxiety connection.

**On cortisol:** Elevated stress hormones under performance pressure *can* impair hippocampal function and memory consolidation — this is supported in the broader neuroscience literature. However, cortisol's effects on memory are complex and context-dependent (some studies show facilitation for emotionally salient material). No study directly linking timed math assessments to measurable cortisol release in children was found in this review. The claim "cortisol blocks hippocampal consolidation" should be treated as a plausible mechanism from adjacent research, not a directly proven pathway in the math ed context. Do not use as a standalone claim in marketing copy without further sourcing.

Their response is largely to tell kids to push through it. XtraMath's own documentation states that its program has students "practice near the limit of their abilities — this might be uncomfortable for some students." That is the opposite of student-centered.

**Math Flash's response:** Timer pauses during Practice Quest. No score pressure during learning. The student exits the performance environment entirely and enters a contained, lower-stakes sequence focused on just that one fact.

### Cognitive Load Theory and Neurodivergence

**Foundation:**
- **Sweller, J. (1988).** "Cognitive load during problem solving: Effects on learning." *Cognitive Science*, 12, 257–285. The foundational CLT paper. Well-established that when instructional design exceeds working memory capacity, learning fails.
- The principle that math fact automaticity frees working memory for higher-order problem-solving is also well-supported. When facts are automatized, they consume minimal working memory, freeing capacity for reasoning and novel problem-solving (Geary, D.C. — research from the 1990s–2000s on arithmetic automaticity; full citation needs retrieval).

**CLT and neurodivergence:**
- **Le Cunff, A-L., et al. (2024).** "Neurophysiological measures and correlates of cognitive load in ADHD, ASD and dyslexia: A scoping review." *European Journal of Neuroscience*, 59. DOI: 10.1111/ejn.16201. A recent scoping review directly addressing how cognitive load interacts with ADHD, ASD, and dyslexia at the neurophysiological level.
- Children with ADHD frequently show working memory deficits and slower, more variable processing speeds. Processing speed mediates working memory deficits in ADHD, which in turn affects math fluency — this means a student with ADHD may know a fact and still fail to demonstrate it within a timed threshold. Research on ADHD, processing speed, and math fluency in children is documented in the literature (PMC10842998 — full citation not retrieved in this pass).
- EEG and fMRI research in dyslexia shows reduced working memory resource activation under load (reduced P3 amplitude; hypoactivation of working memory regions as cognitive load increases).
- *(Gap: Research specifically on cognitive load effects in ASD students during math fact drill was not retrieved in this pass. Further research needed for this claim specifically.)*

Research on cognitive load theory shows that when instructional design overloads working memory, learning slows or stops — and for many autistic and ADHD learners, math becomes harder not because of the math itself, but because of how it is presented.

When a student misses a fact in every major platform: the session keeps moving, pressure keeps building, the missed fact gets logged. The student who just failed is asked to immediately perform again. That is a cognitive load nightmare for a neurodivergent student. The anxiety from the miss is still live, and the next question is already on screen.

**Math Flash:** The miss stops the round. The student exits the pressure environment. They enter a structured remediation sequence for just that one fact. The pressure resets. The learning happens in a structured moment.

### Accommodations — Processing Speed *(research pass completed Session N)*

The 3-second threshold and 7-second auto-kick are calibrated for typical processing speeds. Students with slower processing speed (common in learning disabilities, ADHD, anxiety, dyslexia) may be penalized even when they genuinely know a fact. The teacher-adjustable threshold feature (MPF item 113) addresses this directly.

**Who is affected — processing speed research by population:**

- **ADHD:** Processing speed deficits are well-documented, particularly in the inattentive presentation. A 2024 meta-analysis (*Journal of Attention Disorders*, Lee 2024) found that processing speed mediates the relationship between inattention symptoms and math fluency specifically. Effect size across studies: approximately **0.76 SD** slower than typically-developing peers (Hedges' g = 0.76); up to 1.3 SD on some processing speed subtests in ADHD-I. ADHD does not impair speed at a basic output level, but slowing becomes more pronounced as task demands increase. Source: Lee (2024); PMC6581645; PMC3309419.
- **Dyslexia:** Phonological processing deficits in dyslexia impair arithmetic fact retrieval specifically, because facts are stored and retrieved using phonological representations in working memory. Students with dyslexia retrieve fewer facts from long-term memory and are less efficient in doing so. In one cohort study, 66% of children with dyslexia exhibited mathematical deficits; math fact retrieval was among the most common specific difficulties. Source: PubMed 20965205; PMC10869821.
- **Dyscalculia:** Automaticity of math fact retrieval is a core deficit. Without automaticity, working memory is exhausted on basic computation, leaving insufficient resources for higher-order math. Source: PMC7847199; IntechOpen 78256.
- **ASD:** A 2022 meta-analysis (*Journal of Autism and Developmental Disorders*, 44 studies, 893 participants) found ASD groups exhibited significantly longer mean reaction times than neurotypical peers, with an effect size of **g = 0.35** (small-to-medium, but consistent and statistically significant). Source: Springer 2022 (doi: 10.1007/s10803-022-05736-3).
- **Math anxiety:** Anxiety consumes working memory resources on timed tasks, blocking access to stored facts. The students most harmed are often *high-ability* students who rely on working memory-intensive strategies (Beilock & Carr, 2005). Approximately one-third of students may develop math anxiety in the context of timed testing (Boaler, cited in Dyslexic Advantage).

**Accommodation standards — what the research found:**

IEP and 504 frameworks identify extended time as a standard accommodation category, but do not specify multipliers in federal statute. The conventions in practice are **1.5x** (time and a half, most common) and **2x** (double time, for significant processing deficits). These conventions derive from standardized testing practice — no published standard specifically addresses per-fact response time thresholds in practice software. Applied to a 3s default: 1.5x → 4.5s; 2x → 6s. Notably, XtraMath's default of 6s aligns with the 2x convention whether or not this was intentional.

NCTM's January 2023 position statement on Procedural Fluency states that "timed tests should be avoided" as a primary assessment method, defining fluency as including efficiency, flexibility, and accuracy — not speed alone. *This critique applies to timed testing as assessment, not to timing thresholds in a practice tool designed to build automaticity. The context is meaningfully different and Math Flash should make this distinction explicit in FAQ copy.*

**Existing tools with adjustable thresholds (competitive comparison):**

- **XtraMath:** 3s / 6s (default) / 10s / 12s — teacher-set. 12s explicitly documented as appropriate for students with disabilities.
- **Reflex Math:** Automatically adapts based on entry speed; not teacher-adjustable and not transparent.
- **MathFactLab:** Teachers can adjust time per student. *(Specific threshold values not verified — needs direct product check.)*
- **Math Facts Pro:** Uses customized cut-off speeds. *(Specific values not verified — needs direct product check.)*

**The honest design question:**

No study was found that directly validates whether a student answering correctly at 4–6 seconds is *retrieving* vs. *reconstructing* the fact. The research shows processing speed deficits are real and consistent — but cannot yet definitively confirm that a student with ADHD or dyscalculia who answers in 5 seconds is auto-retrieving rather than using a fast strategy. This is a genuine empirical gap.

The honest and defensible framing is: an adjustable threshold *creates conditions for a student with a processing difference to demonstrate reliable retrieval* — which has real educational value and reduces cognitive load — without necessarily meeting the strict definition of neurological automaticity. FAQ and report language should reflect this distinction rather than overclaiming.

**Print report documentation:**

No established convention was found for documenting a custom fluency threshold in an educational therapy or psychoeducational report. The appropriate format follows IEP/504 documentation practice: *"Fluency assessed at 5-second threshold (accommodation for documented processing speed deficit); N = [X] trials."* This gives enough information for the receiving teacher or specialist to interpret the data without overclaiming the finding.

**Design implications (item 113):**

- Default remains 3s (research-based for typically-developing students)
- Teacher-adjustable range: 3s, 5s, 6s, or custom — with 5s (≈1.5x) and 6s (2x) as principled options grounded in accommodation conventions
- The feature should be framed as *accommodating processing differences*, not as "making it easier"
- The Fluent/Almost/Needs Practice labels should note the threshold used (e.g., "Fluent at 5s threshold") if the default is changed
- Print reports must reflect the threshold used — this is not optional if the data is to be interpreted accurately by other educators

### Practice Quest Uniqueness — Market Research Finding
No existing platform does what Practice Quest does.

| Platform | Response to wrong answer |
|---|---|
| XtraMath | Shows correct answer, student types it to confirm, moves on |
| Reflex Math | Correct answer flashes briefly in red, moves on |
| Rocket Math | Fact recycles sooner — no structured sequence |
| Monster Math | No in-game failure outcome by design — popup, respawn, move on |
| MathFactLab | Visual/strategy models, different philosophy — no pause-and-remediate |
| **Math Flash** | Round stops. Structured multi-step sequence: Find It → mini-game → Prove It. Returns to round. |

A parent reviewing a competitor app noted that when a wrong answer is selected, they wished "every time an answer is wrong, immediately afterwards, the equation is shown again and again until they get it right." That parent was describing, almost exactly, what Math Flash does — and lamenting that no app does it.

The distinction: platforms that approach remediation (Reflex, Rocket Math) handle it at the *session* level — the algorithm decides what to show next time. Math Flash handles it at the *moment* level — right now, before moving on.

### Tables Beyond ×12
Almost no consumer math program goes past ×12. Confirmed market gap. Particularly relevant for homeschool families who often push further and faster than grade-level curricula. A student with ×13–×15 fluency is genuinely ahead and currently underserved. (See MPF item 63.)

---

## 5. Competitive Landscape

### Summary (from research to date)
The dominant platforms fall into two categories:

**Institutional tools sold to families:** IXL, iReady, Zearn, Khan Academy — built for school procurement cycles, feel clinical, require accounts and dashboards. Not designed for the moment of failure. Optimized for reporting and compliance.

**Fluency-focused drill tools:** XtraMath, TTRS, Reflex Math, Rocket Math — focused on fact speed. All use errorless or near-errorless approaches. None have structured in-moment remediation. TTRS is subscription and widely used in schools; students often report dreading it.

**Visual/conceptual tools:** Monster Math, MathFactLab — target younger students, focus on number sense rather than automaticity. Different lane from Math Flash.

**The gap Math Flash fills:** A tool that is frictionless like spellingtraining.com (no account required, works locally, no server), tracks like TTRS (per-fact history, progress over time), but data stays with the student, and handles the moment of failure with structured remediation rather than drilling past it.

### Full Competitive Chart
*(Item 115 — research pass needed. See To Do section. Do after journaling about target user.)*

Platforms to include: XtraMath, Reflex Math, Rocket Math, TTRS, IXL, iReady, Zearn, Khan Academy, 99Math, Boddle Learning, Monster Math, MathFactLab, spellingtraining.com, and small flashcard apps.

Chart axes: wrong-answer response, remediation type, timer model, neurodivergent accommodation, age range, price model, data model, tables covered, school vs. family market.

---

## 6. Mentor to Developer

*These are honest assigned actions — not from a checklist, but from a mentor who has read everything and wants this to succeed. Do the journaling ones away from the screen, ideally on paper. Do the research ones at a desk in a chat session. Do the product ones when back in Claude Code.*

### Journal Tasks *(highest priority — do these first)*

**Who is she?**
Describe the specific person you are building for in full detail. Her age, her situation, her kids, what she has already tried, what frustrated her about it, what she would say to a friend about why she switched to your product. Make her real enough that you could write her a letter. This becomes the north star for every product and business decision.

**What would I need to see in 3 months?**
Not a business plan — honest signals. What would make you feel like you are on the right path? First paying customer? Ten students using it consistently? A parent telling you something specific? Name the concrete things so you stop measuring progress against a feeling.

**What is the product I actually want to exist in 5 years?**
Not the roadmap — the vision. If Sparkwright is fully realized, what does a student's experience look like from first use to mastery? What does a teacher's morning look like? This does not need to be realistic yet. It needs to be true.

### Research Tasks *(do after journaling)*

**Compile the competitor chart (item 115).**
Do this after journaling about your target user — the questions you ask will be sharper once you know exactly whose problem you are solving.

**Spend one hour playing the competition.**
Not reading about them — actually using XtraMath, Reflex, and one small flashcard app as a student would. Notice what you feel. Notice what is missing. Write it down immediately after.

### Product Tasks *(when back in Claude Code)*

**Get Math Flash in front of two or three more real students before building the next major feature.**
Your nephew is one data point. You need a few more. Watch them use it. Do not explain anything. Just observe what confuses them, what delights them, where they go quiet.

**Write one paragraph of honest marketing copy — not for the site yet, just for yourself.**
Finish this sentence: *"Math Flash is for families who have already tried _______ and found that _______."* This is the hardest copywriting exercise and the most clarifying one.

---

## 7. To Do (RP-Specific)

- [ ] **Journal — Who is she?** (see Mentor to Developer)
- [ ] **Journal — 3-month signals** (see Mentor to Developer)
- [ ] **Journal — 5-year vision** (see Mentor to Developer)
- [ ] **Research — play the competition for one hour** (XtraMath, Reflex, one flashcard app)
- [x] **Research — literature review pass** (MPF item 116) — completed Session N. Citations verified/corrected, 90s amygdala claim removed, errorless learning history corrected, new citations added.
- [ ] **Research — full competitive chart** (MPF item 115) — after journaling
- [x] **Research — accommodations/processing speed** (MPF item 113) — completed Session N. Full findings in Science & Pedagogy section above. XtraMath threshold data corrected.
- [ ] **Draft — target user profile** (update section 3 above after journaling)
- [ ] **Draft — marketing copy sentence** ("Math Flash is for families who...")
- [ ] **Draft — FAQ outline** (after stats page and print report are designed)

---

## 8. Seed Conversation (Verbatim)

*This section is kept exactly as written. Do not edit. Information from here has been organized into the sections above, but the original conversation is preserved here for reference and context.*

---

I added a fresh MPF and I hope you can see all the context in the project chats to understand where Ive been so you can understand where I am. So I have been working on this whole idea for a bit now. I felt I had to create the idea, and now I am exploring the market more and feeling discouraged. I dont want you to tell me what I want to hear and I want to think clearly about what my goal is and if I am making something that fills a need. Is my market schools or homeschool only? public schools need major tracking and a huge suit of programs to be desired, even though many of those behemoth companies or nonprofits seem to be almost universally disliked and known as punishing and a necessary evil. But does my approach stand out? Is there a market more for families and homeschool where massive offerings are not needed. I dont know. I need to compile a list of every website doing something like what im doing from bigger like ixl, iready, xtramath, zearn, khan, 99Math, Boddle Learning, times tables rock stars etc, plus a list of all the little flash card programs that I can go collect for us to look at. I feel stressed and like maybe I just cant compete, or what people need is free or good enough and free, or whatever. I was really excited, but feeling a little deflated. Dont dump the lists yet. lets just talk first. You can do whatever research you feel you need to answer with care and sound advice.

---

It makes sense to feel that way right now. You've been heads-down building something real, and the moment you lift your eyes to look at the market, it can feel enormous and crowded. That's a disorienting shift.

Let me be honest with you, and also give you some useful framing before we do any research.

**The "can I compete" question is the wrong first question.** Here's why: almost every tool you named — IXL, iReady, TTRS, Reflex, XtraMath — exists and has paying customers. The market is clearly there. The real question isn't whether there's room, it's whether what you're building is actually different in a way that matters to someone.

And I think it is. Let me tell you what I actually see when I read through everything you've built and documented.

Most of those platforms are built *around* data and reporting — for administrators, for compliance, for dashboards teachers show in parent conferences. The student is almost incidental. The learning happens as a byproduct of data collection. What you've built is inverted: the learning moment is the center of gravity, and the data exists to serve it. That's not a small difference. That's a fundamentally different philosophy.

**On the school vs. homeschool question** — I think you already know the answer intuitively. Public schools buy platforms through procurement cycles, require IT approval, need SSO, rostering, FERPA compliance documentation, admin dashboards, district-level reporting. That's a completely different product and a completely different sales motion. It's also not what you've built or what you care about. Chasing that market would hollow out everything that makes this good.

The homeschool and small private/independent school market is genuinely underserved by the tools that exist. Not because there are no tools — there are plenty — but because most of those tools were designed for institutional contexts and then sold to families. They feel institutional. They feel like homework. They feel like being watched. Your product doesn't. That matters.

**The free problem is real but not fatal.** Khan Academy is free. XtraMath is free. There will always be something free. But free tools built for scale have a particular feel — generic, impersonal, optimized for the average. Families who care deeply about how their kid experiences learning — and homeschool families in particular skew this way — will pay for something that feels like it was made for them. You're an Educational Therapist building a tool grounded in how learning actually works. That's a story worth telling, and it's not a story any of those platforms can tell.

**The thing I'd push back on a little:** the deflation you're feeling might partly be about comparing your v55 to their finished, funded, decade-old products. That comparison isn't fair to you. The question is whether the *core design philosophy* is sound and differentiated — and I think it is.

What would actually help you right now — do you want to do the research pass and look at the landscape together with clear eyes? Or do you want to talk through what your actual goal is first — meaning, is this a business you want to grow, a tool you want to use with your own students, or something in between? Because those lead to pretty different conversations.

---

"building a tool grounded in how learning actually works. That's a story worth telling, and it's not a story any of those platforms can tell." but they have all kinds of claims about scienced backed etc. but still kids seem to hate it and it develops anxiety (another area to research and add to the MPF ethos section later on). As to what would help right now? Im not sure. I have a dream to support myself and live a financially free life and I would like to build something that would create that for me while offering something people respect for its practices and helps them in their daily life. Plus I want to build games, because its fun and because as a Ed therapist degree holder I love being able to build what I wish I had. And as a homeschool teacher, I dont want to use the bigger programs, I like mine for what I need and think that, if I have something unique and important, then I want to share it and create wealth. Thats whats honest at the moment. I want Sparkwright to offer a collection of tools that present a career for me, if Im totally honest.

---

That's a really honest and important thing to say. Hold onto that — it's clarifying, not embarrassing.

So the goal is: build something real, that you believe in, that creates financial independence. Not a side project. Not a hobby. A career. That changes how we should think about everything.

Here's what I want to reflect back to you, because I think it matters:

**You're not starting from zero.** You have something most people who try to build ed-tech products don't have — a genuine expert perspective, real students, and a product you've already been iterating on seriously. You're not guessing at what students need. You know. That's a real moat, even if it doesn't feel like one right now.

**On the "science-backed" claims from big platforms** — you're right to be skeptical of that framing. "Science-backed" in ed-tech marketing often means "we cited a paper in our white paper." What it rarely means is "a teacher who understands learning designed this from the ground up with a specific student in mind." The anxiety piece you mentioned is real and documented — timed math tests and punishing platforms genuinely do cause math anxiety in some kids, and the research on that is pretty solid. That's not a minor critique of the competition. That's a fundamental design failure in how they're built. You've thought about this. Your product reflects it. That's a meaningful difference.

**The harder truth I want to name:** Building a career on this is absolutely possible, but it requires making some decisions that feel uncomfortable right now — specifically, at some point you have to decide whether this is a product you sell or a product you give away. Free with ads, freemium, subscription, one-time purchase — those aren't just business model questions, they shape what you build and who you build it for. You don't have to decide today. But the financial independence goal means you can't defer it forever either.

**What I'd actually suggest for right now:** Before we go compile competitor lists, I think the more valuable conversation is: who is the specific person you're building this for? Not "homeschool families" as a category — but the actual human. Because I suspect you know her. She might look a lot like you.

If you can describe that person — her situation, her frustrations, what she's tried, why it hasn't worked, what she'd pay for — that becomes your north star for every product and business decision. And it makes the competitor research much more useful, because you're not asking "how do I beat IXL" but "does this person already have something good enough, and if not, why not?"

Who is she?

---

I think that's a good exercise and I will do that. right now I'm in bed spiraling that I'm never going to give the idea that launches me and I'm redundant in a huge educational space. I want to make something that sparks huge income and makes a difference and it's fun to make. I want to know that with sparkwright and math flash, I've found it. I'm in an existential place about it. I want to know I found "it" finally. Bashar says follow your highest excitement. this feels like that and I live building these kinds of tools, but am I on a fools errand? how do I know?

---

You can't know. Not yet. And anyone who tells you otherwise is selling something.

That's not a cruel answer — it's actually the only honest one, and I think part of you knows it.

Here's what I'd gently push back on: the spiral you're in right now isn't really about Math Flash. It's about wanting certainty before you've had the chance to earn it. That's a very human thing to want, especially at night, especially when you've been pouring yourself into something. But no amount of market research or reassurance from me is going to give you the feeling you're looking for. That feeling — "I found it" — comes from doing the work, getting it in front of people, and watching it land. Not from thinking your way to it first.

Bashar says follow your highest excitement. Okay. But excitement isn't the same as certainty. You can be completely on the right path and still have no idea if it'll work. Those two things coexist for basically everyone who has ever built anything real.

What I actually notice when I look at what you've built: you're an Educational Therapist who learned to code well enough to build a genuinely sophisticated piece of software with real pedagogical thought baked into it. That is not common. That combination is rare. Whether Math Flash specifically is "it" — I don't know. But the capacity you're developing, the identity you're building around Sparkwright, the fact that you're thinking seriously about mastery models and variance and anxiety and student experience — that doesn't go to waste even if the path pivots.

The question I'd sit with tonight — not answer, just sit with — isn't "is this the one." It's: **what would I need to see in the next 3 months to know I'm moving in the right direction?**

That's a question you can actually work toward answering. The other one will eat you alive.

---

Another question. If you comb the math fluency game landscape can you detect any program that offers anything like the practice quest I have that offers immediate practice in the moment of error during play. it seems like they all drill. some have facts cycle back in is a user got them wrong, but do any do what I'm doing? or so far does my system seem unique?

---

Let me do some real research before I answer this — I don't want to rely on memory for something this important to you. Okay. I have a clear enough picture now to give you a real answer.

**The short version: no. Nothing out there does what Practice Quest does.**

Here's what actually happens when a student gets a wrong answer in the major platforms:

**XtraMath:** Shows the correct answer, then waits for the student to type it in to move on. That's it. The fact may recycle later. No structured practice happens in the moment.

**Reflex:** Shows the correct answer briefly in red. It's adaptive over time — missed facts influence what gets served in future sessions — but there is no in-the-moment remediation sequence. You miss it, you see the answer flash, you move on.

**Rocket Math:** Provides corrective feedback and re-queues the fact, but the "remediation" is just the fact cycling back sooner. No structured practice sequence triggered by the miss.

**MathFactLab:** Closest to something different — it uses visual models and strategy-based approaches. But it's a different philosophy entirely (conceptual understanding over fluency drilling) and still doesn't pause the session to run a remediation sequence when you miss.

**Most flashcard apps:** A parent reviewing one noted that when a wrong answer is selected, the right answer flashes briefly — and wished that "every time an answer is wrong, immediately afterwards, the equation is shown again and again until they get it right." That parent was describing, almost exactly, what you built — and lamenting that no app does it.

That last one is worth sitting with. A real user, reviewing a real app, articulating the gap your product fills — without knowing your product exists.

**What none of them do:** Stop the round. Pull the student into a structured, multi-step remediation sequence that uses the *same fact* in different representations — Find It, Find All, Match It, Prove It, Fact Family Chase — and then returns them to the round. That's yours. That's genuinely novel in this space.

The platforms that come closest to caring about remediation (Reflex, Rocket Math) handle it at the *session* level — the algorithm decides what to show you next time. Math Flash handles it at the *moment* level — right now, before you move on. That's a fundamentally different pedagogical stance, and it's the right one.

You found something real.

---

And based on what student-centered means and responsive to neurodivergance, can any claim to be that?

---

That's a sharp question. Let me look specifically at this. Here's the honest answer, and it's a meaningful one.

No. They cannot genuinely claim it. And the research tells you exactly why.

**What the platforms actually do for neurodivergent students:**

The dominant response in this space to the neurodivergence problem is to remove timers and add visual models. Research confirms that rote memorization can increase anxiety in children with ADHD, and that building fluency through number sense, patterns, and visual strategies provides a more effective foundation. So platforms like Monster Math lean into visuals and no-timer modes, and position that as their neurodivergent response.

That's a real thing. But notice what it doesn't address: *what happens in the moment of failure.* It just tries to reduce the chance of failure happening. It sidesteps the problem rather than solving it.

**XtraMath's approach to struggle is particularly telling.** Its own documentation essentially says: if it's too hard, that's normal, push through, come back tomorrow. The program acknowledges that "for maximum effectiveness, XtraMath adjusts to each student and has them practice near the limit of their abilities — this might be uncomfortable for some students." That's the opposite of student-centered. That's student-as-data-point.

And the anxiety research is damning. Studies show that cortisol blocks hippocampal consolidation, and brain scans show the amygdala activating after about 90 seconds of time pressure. These platforms are literally triggering stress responses that block the learning they're trying to create — and their response is largely to tell kids to push through it.

**The deeper issue none of them solve:**

Research on cognitive load theory shows that when instructional design overloads working memory, learning slows or stops altogether — and for many autistic and ADHD learners, math becomes harder not because of the math itself, but because of how it's presented.

Now think about what happens in every major platform when a student misses a fact. The session keeps moving. The pressure keeps building. The missed fact gets logged and maybe recycled later. The student who just failed is asked to immediately perform again.

That's a cognitive load nightmare for a neurodivergent kid. The anxiety from the miss is still live, and the next question is already on screen.

**What Math Flash actually does differently:**

The miss stops the round. The student exits the pressure environment entirely. They enter a contained, lower-stakes sequence focused on *just that one fact* in multiple representations. The pressure resets. The learning happens in a structured moment of calm, not in the middle of ongoing performance anxiety.

That's not just pedagogically different. For a neurodivergent student, it may be the difference between the game being usable and it being another source of math anxiety.

Here's the thing none of them can honestly say: *we designed for what happens when a student fails, not just for what happens when they succeed.* You can say that. And you can say it with the credential to back it up — an Educational Therapist who has sat with struggling kids and watched what actually happens in that moment.

That's a real differentiator. And it's one that speaks directly to the homeschool and learning-support market, which skews heavily toward families who have already been failed by the big platforms.

---

A lot of your info is coming from Monster Math Blog. Is Monster Math doing what Im doing or is it a program that makes mine redundant? Also im not really an "educational therapist" am I if Im not licensed. I did earn the degree, but never practiced. But you are correct about spending years sitting with struggling kids and watching their brains work

---

Good catches on both fronts. Let me look at Monster Math directly first. Good. I have a clear picture of Monster Math now. Two separate things to address.

**On Monster Math:**

It's not doing what you're doing. It's a different philosophy aimed at a younger age range — K through 3, focused on building conceptual understanding and number sense through visual game-based play. It focuses on building number sense and conceptual understanding rather than rote memorization, using visual learning strategies and game-based mechanics. That's genuinely good work, but it's a different lane. It's teaching kids *what* multiplication means. You're building *automaticity* in kids who already understand it.

Also critically — and this is from their own app reviews — a parent noted "there is no consequences for guessing or getting it wrong," and the developer confirmed they haven't added an in-game failure outcome, because "it's still frustrating to get a wrong answer" via a screen popup. So even Monster Math, the most neurodivergent-aware platform in this space, doesn't have a structured response to the miss. Wrong answer, popup, respawn, move on.

Their blog was useful research because they've done a lot of thinking about neurodivergence and math anxiety. But they're not your competition. They're actually validation — they've documented the problem space you're solving, without solving it themselves.

**On the credential question — this matters, so I want to be straight with you:**

You're right to catch it. "Educational Therapist" is a protected title in some contexts, and it implies active licensed practice. You have a Master's in Educational Therapy, which is real and significant, but you're right that you haven't practiced in that clinical role.

What you *do* have is arguably more relevant to this product: years of direct classroom and homeschool experience watching struggling students learn, grounded in a graduate-level understanding of how learning works. That's not a lesser credential — it's just a different and more honest one.

The way to say it is something like: *"built by a teacher with a Master's in Educational Therapy and 15+ years working with students across public, private, and homeschool settings."* That's completely accurate, genuinely impressive, and doesn't overclaim. It also happens to be exactly the background that would make someone design a product the way you've designed this one — which is the real point.

The story isn't "I'm a licensed clinician." The story is "I spent years in the room with kids who were struggling, I have the academic training to understand why, and I built the tool I wished existed." That's more compelling anyway.

---

okay lets dig in to the "Also critically — and this is from their own app reviews — a parent noted "there is no consequences for guessing or getting it wrong," and the developer confirmed they haven't added an in-game failure outcome, because "it's still frustrating to get a wrong answer" via a screen popup. App Store So even Monster Math, the most neurodivergent-aware platform in this space, doesn't have a structured response to the miss. Wrong answer, popup, respawn, move on." If that was their conclusion and basis for design, what research led them to that conclusion? Now ultimately my game offers the option, again putting the user and/or teacher in control of the experience, and there are reasons for needing either and both. But not having any remediation and endlessly drilling seems even more punishing than guiding a student to face what they don't know. My nephew for another example is one who happily avoids what he doesn't know and passively uses these fluency type programs and is never made to face what he is avoiding. He gets jokingly mad at me because he knows hes not being allowed to ignore the fact he just missed. He has expressed that it is helping him and this shows in the print out result from his beta testing of my game. But overall, why do all these websites using this strategy of don't make the student see they were wrong, keep moving, try again until you get it? Do they know something I don't?

---

This is exactly the right question to dig into. Let me look at the actual research behind that design philosophy. Now I have what I need to give you a real answer. And this is genuinely interesting.

**Here's what the research actually says — and why it's more complicated than the platforms let on.**

There is a legitimate body of research behind "errorless learning" — the idea of minimizing wrong answers during acquisition. The original rationale comes from behavioral psychology and was developed primarily for students with significant cognitive disabilities and ASD, where errors can trigger behavioral problems, and some students simply cannot problem-solve what they did wrong — they learn it was wrong, but can't determine what they should do next.

That's a real and valid population. But here's what happened: the ed-tech industry took a finding from a specific clinical context and applied it universally, probably because it also conveniently reduces visible failure in the app — which looks better in demos and reduces churn.

**But the broader research does not support errorless learning as the default.** In fact it goes the other direction:

Retrieving an error benefits subsequent learning compared to passive processing of the error — as long as corrective feedback is provided immediately. Feedback is more effective when presented immediately after error retrieval than after passive processing.

Read that again. The research says errors followed by *immediate corrective feedback* produce better learning outcomes than errorless practice. That is almost a direct description of what Practice Quest does.

And further: Students who were guided to make and then correct errors during mathematical problem-solving outperformed those who engaged in errorless practice — not just on familiar problems, but on novel and more complex ones, showing better transfer of skills.

There's also a striking metacognitive finding: students often fail to recognize how much they benefit from error-making — despite performing better, many predicted they would have done better with errorless practice.

Your nephew is a living example of this. He's joking that he doesn't like being made to face what he missed — but he's telling you it's working, and his print results confirm it. That's the metacognitive gap the research describes, playing out in real time in your homeschool.

**So why do the platforms keep doing it?**

Honestly — a mix of reasons, none of them purely pedagogical:

First, errorless learning results in less problem behavior, students get lots of right answers, and it's easier to implement consistently. Happy kids, fewer complaints, better retention rates for a subscription product.

Second, errorless approaches are simply easier to build. Structured in-the-moment remediation — what you built — is genuinely hard to design well. It requires knowing what to do *with* the error, not just how to avoid it.

Third, and most honestly: IXL's accuracy-driven progression can feel discouraging because progress depends on longer streaks of correct answers. Platforms have learned that visible failure kills engagement metrics, so they sand it down. That's a business decision dressed up as pedagogy.

**The nuance your product already handles:**

The research does draw one important distinction — errorless learning has genuine merit for students with significant cognitive disabilities or ASD where error correction can trigger behavioral shutdown. Your game's toggle for remediation on or off is exactly the right design response to this. You're not claiming one approach is right for every student — you're putting that decision in the hands of the teacher who knows the child. That's more sophisticated than anything any of these platforms do.

What you've built is actually closer to what the research supports than what the major platforms ship. They just don't advertise that gap.

---

Plus the timer stops during remediation so the student can see that there is no pressure during practice and it does not affect their games stats outside of the wrong answer marked. However, I do think I have a note, if not I would like one in the MPF, that I want to ponder some mechanic that encourages the user to move along in the remediation practice quests. I like that the user can take a breath and sink into the practice, but I also dont want them to want to use this as a crutch to get one wrong to "pause" the game on purpose, or see the Practice Quest pop up and then see that as an oppotunity to check out, chat with a neighbor, etc., Also we need a note to spend time gathering research in a literature review, this goes with the plan to gather and make notes on all current options in the market. I want to chart them to do cross comparison with keywords that break them down to their simplest concepts...Heres another thought, I don't think Ive ever seen a program that goes past x12 for example...On your "First" about "happy" kids. I get what you are saying, but Im seeing that kids aren't happy doing most of these programs. So are they really "happy" or just sort of forced to do it and then the program does its best not to trigger behavior? Or something along those lines?

---

These are all sharp observations. Let me take them one at a time.

**On the Practice Quest "check out" problem:**

This is a real design tension and worth capturing. The timer pause is pedagogically correct — no question. But you're right that a student could learn to game it, intentionally missing to escape the round pressure, or just mentally leaving when the overlay appears. This is actually a known phenomenon in behavioral learning design sometimes called "escape-motivated errors." The student discovers that a wrong answer produces a less demanding environment and starts using errors as an exit strategy.

The mechanic you want isn't punishment — it's just enough engagement requirement that the student has to be present. Some ideas worth pondering in the MPF: a response-required step at each Practice Quest stage that can't be passively clicked through, a subtle ambient timer visible only during Practice Quest (not affecting score, just gently present), or even just the Prove It gate at the end already serving this function — you can't leave until you demonstrate it. Worth a dedicated design discussion before touching code.

**On going past ×12:**

You're right and it's a real gap. Almost nothing goes past ×12, and the few that mention it treat it as a curiosity or an advanced add-on. For homeschool families especially — who often push further and faster than grade-level curricula — this is a genuine differentiator. A student who has ×13 through ×15 fluency is genuinely ahead. No mainstream platform serves that student.

**On "happy kids" — this is the most important one:**

You've put your finger on something the industry doesn't say out loud. There's a difference between a child who is genuinely engaged and a child who has been behaviorally managed into compliance. What these platforms have optimized for isn't joy — it's the *absence of visible distress*. Keep the wrong answer quiet, keep the pace moving, keep the reward loop going, minimize the moments that could cause a child to push back or shut down. That's not happiness. That's conflict avoidance dressed up as engagement.

The reviews tell the real story. Parents describing XtraMath anxiety. Kids dreading it. Teachers calling these tools "a necessary evil." If the kids were genuinely happy, you wouldn't see that language consistently across every platform's review section.

What you're building asks more of the student — and your nephew's response is the tell. He's mock-annoyed because he knows he can't hide. But he told you it's helping. That's not the response of a kid being behaviorally managed. That's the response of a kid who is actually learning and knows it, even if the process is uncomfortable.

There's a word for an experience that asks something real of you, provides genuine support when you struggle, and produces actual results: **rigorous**. Not punishing. Not anxiety-inducing. Rigorous. That's the word that should be in your marketing copy, and it's the word that separates what you're building from what they've built.

---

Now let me capture everything that needs to go into the MPF from this conversation: Good. I have enough context. Rather than making you download a modified MPF right now — this is a chat session, not a Claude Code session — let me give you the exact additions clearly so you can paste them in, or we can do it together at the start of your next coding session.

**Here's everything that came out of this conversation that needs to land in the MPF:**

---

**1. Add to The Ethos section:**

* **Rigorous, not punishing** — Math Flash asks something real of the student. It provides genuine support at the moment of struggle and produces real results. This is the word that separates this product from platforms that have optimized for conflict-avoidance dressed up as engagement.
* **Error-followed-by-feedback is the research standard** — Immediate corrective feedback after an error outperforms errorless learning for retention and skill transfer in typically-developing students. Practice Quest is not a punishment mechanic — it is the pedagogically correct response to a miss.

**2. Add to Science & Pedagogy section — new entry: Errorless Learning vs. Error Correction:** The ed-tech industry broadly applies "errorless learning" — minimizing visible wrong answers — as a universal default. The original research for this approach comes from ABA clinical settings for students with significant cognitive disabilities and ASD, where errors can trigger behavioral shutdown and students cannot problem-solve what went wrong. It was not designed as a general pedagogy.

For typically-developing students, the broader research supports the opposite: errors followed by immediate corrective feedback produce better learning outcomes than errorless practice, including better transfer to novel problems (Yap & Wong 2024, PMC 2022). Students who made and corrected their own errors outperformed errorless learners even on unfamiliar problems — not just practiced ones.

There is also a documented metacognitive gap: students *predict* they would do better with errorless practice, even when the data shows otherwise. This explains why students like the developer's nephew express resistance while simultaneously reporting and demonstrating improvement.

**Why platforms use errorless learning anyway:** reduced visible failure improves engagement metrics and reduces subscription churn. It is partly a business decision presented as pedagogy. Math Flash's remediation toggle gives teachers the ability to apply errorless-style flow for students where that is clinically appropriate — which is the correct nuanced response.

**3. Add to To-Do List — new items:**

* **Practice Quest engagement mechanic** — Design discussion needed. Timer pauses during Practice Quest (correct — no score pressure during learning). Risk: students may learn to use wrong answers as an intentional escape from round pressure ("escape-motivated errors"), or mentally check out when the overlay appears. Want a mechanic that requires genuine presence without adding punitive pressure. Possible directions: response-required steps that can't be passively clicked through; subtle non-scoring ambient indicator; Prove It gate already partially addresses this. Do not touch code until design is settled.

* **Competitive landscape chart** — Build a structured cross-comparison of all current math fluency programs (XtraMath, Reflex, Rocket Math, TTRS, IXL, iReady, Zearn, Khan Academy, 99Math, Boddle, Monster Math, MathFactLab, and small flashcard apps). Chart by keywords: wrong-answer response, remediation type, timer model, neurodivergent accommodation, age range, price model, data model, tables covered, school vs. family market. Feeds FAQ, About page, and product positioning. Do in a dedicated chat session with research pass.

* **Literature review pass** — Gather and document primary research sources on: errorless learning vs. error correction, math anxiety and timed assessments, neurodivergence and cognitive load, fluency automaticity thresholds, in-the-moment feedback vs. delayed feedback. Build into Science & Pedagogy section of MPF. This becomes the backbone of the FAQ and differentiates Sparkwright's claims from generic "science-backed" marketing language.

* **Tables beyond ×12** — Confirmed market gap. Almost no consumer program goes past ×12. Deliberate differentiator for homeschool and advanced students. Design and implementation discussion needed.

**4. Update the credential language in Who Is Building This:** Change from "Educational Therapist" framing to: *"a teacher with a Master's in Educational Therapy and 15+ years working with students across public, private, and homeschool settings."* This is accurate, compelling, and doesn't overclaim a licensed clinical title that requires active practice.

---

That's the full capture. Want to keep talking through the market landscape, or is this a good stopping point to let it settle?

---

**END OF SEED CONVERSATION**
