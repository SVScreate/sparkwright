# Sparkwright — Brand Identity v1
*Created: 2026-03-29 — Pip (Brand & Visual Design agent)*
*Status: Working draft — in progress with Kimberly*

---

## Brand Essence

Three words from the definitions anchor everything:

> **"A metaphorical initiator of energy."**

That phrase from the Sparkwright search result is the brand in six words. It's not a school tool. It's not a drill. It's the thing that starts something — in a student, in a session, in a brain. The logo, the palette, the typography — everything should feel like initiation, not administration.

**The two halves of the name tell the full story:**
- *Spark* — ignition, electricity, a tiny animating amount of something like hope or talent
- *Wright* — skilled craftsman, maker, builder, someone who works with precision and care

Together: someone who crafts sparks with intention. A teacher, really.

---

## Brand Personality Keywords

From the definitions + developer brief:

| Energy | Craft | Learning |
|---|---|---|
| Ignite | Handmade | Alchemy |
| Flash | Precise | Neuroscience |
| Electric | Maker | Initiation |
| Activate | Deliberate | Transformation |
| Animating | One at a time | Hope |

The visual language should carry *all three columns simultaneously*. Warmth from energy, precision from craft, magic from learning.

---

## Color Palette — Formal Brand System

### Naming philosophy
Named for what they evoke, not what they are. These are the nine brand colors — the game's full UI palette (a1–a7) extends from here and is game-specific. The brand anchors here.

---

### Foundation — The Dark

| Name | Hex | Usage |
|---|---|---|
| **Void** | `#0c0c18` | Primary background — the night before the spark |
| **Deep** | `#13132a` | Surface / card backgrounds |
| **Layer** | `#1c1c38` | Elevated surfaces, modals |

*These are working well. Keep them. The deep navy-purple reads as sophisticated, not cold — the purple undertone is doing important work by keeping it from reading as pure tech/space.*

---

### Brand Accents — The Spark

| Name | Hex | Role | Notes |
|---|---|---|---|
| **Ember** | `#ff9f43` | **Primary brand color** | The spark itself — warm amber-orange. Fire, alchemy gold, the moment of ignition. Hero color. |
| **Flash** | `#ffd93d` | **Secondary brand color** | Peak of a spark — bright gold-yellow. Used for highlights, the "got it" moment, achievement. |
| **Electric** | `#4d96ff` | **Tertiary brand color** | The wright/neuroscience side — cool electric blue. Precision, intelligence, synaptic firing. |
| **Arc** | `#c77dff` | **Brand accent** | The alchemy/magic — violet-purple. Mystery, transformation. Use with restraint. |

**Primary brand triad: Ember + Flash + Electric.** Arc is the bonus — used sparingly for magic moments.

The existing `--a5` (`#c77dff`) purple border glow already establishes Arc as the ambient energy of the dark UI. This is correct. Leave it as atmosphere; Ember and Flash are the foreground.

---

### Text System

| Name | Hex | Usage |
|---|---|---|
| **Ghost** | `#e8e4f0` | Primary text — warm white with purple undertone |
| **Mist** | `#9a93b5` | Secondary text, labels, captions |
| **Dusk** | `#5a5375` | Tertiary text, dividers, placeholders |

*The slight purple undertone in Ghost (`#e8e4f0`) is important — it keeps text from reading as pure clinical white on the dark background. It belongs. Don't flatten it to `#ffffff`.*

---

### Color Use Principles

1. **Ember leads.** In any branded context (logo, headers, CTAs) Ember is the primary pop. Flash amplifies it for high-energy moments (correct answers, achievements). Electric is for the intellectual/craft moments.
2. **The dark is not empty.** Void and Deep aren't "background" in the bland sense — they're part of the brand. The darkness before the spark. Don't fill them.
3. **The purple glow is atmosphere.** The Arc-tinted borders and glows are the ambient energy field. They should feel like something is about to happen.
4. **Don't gradient everything.** The existing Ember→Flash gradient in the logo mark is intentional and unique. Use it for the logo and peak moments only — not as a default decoration.

---

## Typography

### Current state
- **Comfortaa** — display/headings on landing page
- **Nunito** — body / nav

### Assessment
Both are from the same rounded-geometric family. Comfortaa has more personality; Nunito is more neutral. The combination is slightly soft — works for the "safe for students" read, but undersells the energy and alchemy angles.

*Developer said: not sold on Comfortaa but likes it for the most part.*

### Recommendation

**Option A — Swap the logo/display font only (lowest disruption):**
Replace Comfortaa in the wordmark/logo with **Outfit** (Google Fonts). Keep Comfortaa for headings on the site, Nunito for body. Outfit is geometric and clean but has more forward energy than Comfortaa — it reads modern without going cold. The logo gets the stronger font; the UI stays approachable.

**Option B — Replace Comfortaa throughout:**
Use **Outfit** for all headings and the logo, keep **Nunito** for body. Outfit has enough range (weights 100–900) to cover all heading use cases. More cohesive; slightly more work to implement.

**Option C — Stay with Comfortaa:**
It's working. It's warm and friendly and already loaded. If the primary concern is the logo, solve it with the mark rather than the type.

*My strong preference: Option A. The logo should feel different from the UI — it's the brand anchor, not a UI element. Give it Outfit, let the site stay Comfortaa.*

---

### Font Stack (recommended final)

| Role | Font | Weight | Notes |
|---|---|---|---|
| Logo wordmark | Outfit | 600 (SemiBold) | Clean, energetic geometric sans |
| Page headings | Comfortaa OR Outfit | 700 | Comfortaa if staying; Outfit if switching |
| Body text | Nunito | 400, 600 | Keep — it's reading well |
| Game UI | System stack | varies | Leave game fonts as-is |

---

## Logo — Concept Direction

### The mark: a 4-pointed spark

A 4-pointed star / sparkle — the universal visual symbol for a spark of light or electricity. It's also the symbol for a star in alchemy. It appears in your screenshots: the Google AI Overview icon uses this exact glyph. That's not a coincidence — it's become the visual shorthand for "intelligent ignition."

The Sparkwright version is warmer and slightly asymmetric (taller than wide — sparks shoot upward) to distinguish it from the corporate version. It carries the Ember→Flash gradient: amber at the base, gold at the tips.

Two or three tiny scatter dots trail off from the upper-right of the star — tiny sparks breaking away. This gives motion and suggests energy being released, not just contained.

### The wordmark: "spark" + "wright"

The compound nature of the name is a visual asset. Two treatments to consider:

**Treatment 1 — Color split:** "spark" in Ember (`#ff9f43`), "wright" in Ghost (`#e8e4f0`). Reads cleanly, names both halves of the brand identity explicitly.

**Treatment 2 — Weight split:** all in Ghost, with "spark" slightly bolder or tracked differently. Subtler, more unified.

*Treatment 1 is stronger. The color split reinforces the brand story: the spark is warm and energetic; the wright is the steady hand that shapes it.*

### Lockup options
- **Horizontal (primary):** mark left, wordmark right. Standard usage.
- **Stacked (secondary):** mark top, wordmark below. For square contexts, social, etc.
- **Mark only:** for favicon, app icon, small contexts where wordmark would be illegible.

---

## Logo File

See `dev/sparkwright_logo_v1.svg` — first concept. Open in a browser (not Finder preview) for accurate font rendering.

To view: run local server and open, or drag the SVG file into Safari.

---

## Open Questions for Kimberly

1. **Font direction**: Option A, B, or C above? This affects how much work Wright needs to do on the site.
2. **Color split vs. weight split** in the wordmark: do you want "spark" in amber and "wright" in white, or unified?
3. **Logo use cases coming up**: favicon, game title screen, landing page header? Knowing where it lands first helps prioritize lockup versions.
4. **"sparkwright" vs "Sparkwright"**: lowercase wordmark reads more modern/indie; title case reads more formal. Preference?

---

*Next steps: Kimberly reviews concept, gives feedback, Pip iterates. Once locked, flag to Wright to implement color tokens and load any new fonts.*
