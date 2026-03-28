# Sparkwright — Legal Copy Draft
*Created: 2026-03-28 — Session R*
*Author: Spark (Research & Pedagogy agent)*
*Status: Working draft — should be reviewed by an attorney before or shortly after commercial launch*

---

## Notes for Wright

This file contains three things:
1. **Website legal pages** — Terms of Use and Privacy Policy (full draft copy, ready for dedicated pages)
2. **Footer copy** — updated footer text with legal links and copyright
3. **A brief pre-launch legal checklist** at the bottom for the developer

**Build instructions:**
- Create `terms.html` and `privacy.html` as standalone pages in the site root, matching the existing site aesthetic (same nav, same footer, dark background, readable body text)
- Update the footer in `index.html` and `games/mathflash/index.html` to include the new links and copyright notice (see Footer section below)
- No special functionality needed on these pages — they are static text

---

## ⚖️ Pre-Launch Legal Checklist

*(What's needed before taking money — and what can wait)*

| Item | Required before payment? | Notes |
|---|---|---|
| Terms of Use page | **Yes** | Draft below. Link in footer. |
| Privacy Policy page | **Yes** | Draft below. Link in footer. |
| Payment processor (Stripe/Gumroad/etc.) | **Yes** | They handle credit card compliance. You don't carry that risk. |
| Attorney review of ToS/Privacy | No — but do within 3 months | The drafts below are honest and appropriate; an attorney review is protective, not required to start. |
| USPTO trademark filing ("Sparkwright") | No — do within 6 months of first sale | Common law trademark rights begin at first use in commerce. Filing formalizes it. |
| IP attorney consultation (AI copyright question) | No — do before scaling | Not a launch-day concern. Becomes relevant if you ever need to enforce your copyright against someone. |
| Entity formation (LLC vs. sole proprietor) | No — but soon | As a sole proprietor, you're personally liable. A single-member LLC separates that. ~$50–200 to file, state-dependent. Talk to a CPA. |
| DMCA policy | No — add when relevant | Only needed if users can submit content. Not applicable to current product. |
| Cookie consent banner | No — current site is minimal | Google Fonts makes external requests; no analytics, no tracking. Low risk. Note in Privacy Policy is sufficient for now. |

---

## Footer Copy

### Current footer (in both `index.html` and `games/mathflash/index.html`):
```
Sparkwright · sparkwright.org · An independent learning project.
```

### Updated footer — replace with:

**Left side:**
```
© 2026 Sparkwright
```

**Center or right — links:**
```
Privacy Policy · Terms of Use
```
*(link to `/privacy.html` and `/terms.html` respectively)*

**Right side (or below on mobile):**
```
An independent learning project.
```

**Wright — full footer HTML suggestion:**
```html
<footer>
  <div class="wrap">
    <div class="footer-left">
      <span class="footer-wordmark">Sparkwright</span>
      <span class="footer-sep">·</span>
      <span class="footer-copy">© 2026</span>
    </div>
    <div class="footer-center">
      <a href="/privacy.html" class="footer-link">Privacy Policy</a>
      <span class="footer-sep">·</span>
      <a href="/terms.html" class="footer-link">Terms of Use</a>
    </div>
    <div class="footer-right">An independent learning project.</div>
  </div>
</footer>
```
*Add `.footer-link` styling to match existing `.footer-copy` muted text — underline on hover, no underline at rest.*

*Note: the Math Flash game footer (or bottom of title screen) should also include these links, or at minimum the Privacy Policy link.*

---

---

# Terms of Use

*For sparkwright.org and all Sparkwright tools and games*
*Effective: [DATE]*

---

**The short version:** Sparkwright tools are built for learning. Use them for that. Don't copy them, resell them, or claim them as your own. We're not responsible if something goes wrong technically. That's it, mostly.

---

## 1. What Sparkwright Is

Sparkwright (sparkwright.org) is an independent collection of educational tools and games designed for use in home, tutoring, and small classroom settings. These tools are built to support learning — they are not clinical services, therapeutic interventions, or substitutes for professional evaluation or instruction.

The tools are built by a teacher with a background in educational therapy. That background informs the design. It does not make Sparkwright a licensed clinical practice, and nothing on this site should be interpreted as a medical or therapeutic recommendation.

## 2. Accepting These Terms

By using sparkwright.org or any Sparkwright tool, you agree to these Terms of Use. If you're using a Sparkwright tool with a child, you're responsible for ensuring that use is appropriate for that child's needs.

These terms may change. If they change in a meaningful way, we'll update the date at the top of this page. Continued use of the site after a change means you accept the updated terms.

## 3. Who Can Use Sparkwright

Sparkwright tools are designed for use by adults (parents, teachers, tutors, educational therapists) with or on behalf of students. Students may use the tools directly, but account for this is the responsibility of the supervising adult.

## 4. What You Can Do

- Use Sparkwright tools for personal, educational, and small-group instructional purposes
- Print session results for educational records or share them with other educators working with the same student
- Share links to Sparkwright tools with other educators and families

## 5. What You Cannot Do

- Copy, reproduce, or distribute any Sparkwright tool, game, page, or underlying code without written permission
- Claim any Sparkwright content — including the tools, games, design, educational methods, or written materials — as your own work
- Use any Sparkwright tool for commercial purposes without a license (e.g., reselling access, including them in a paid product or curriculum package)
- Attempt to reverse-engineer, scrape, or systematically extract content from Sparkwright tools
- Use Sparkwright tools in any way that violates applicable law

## 6. Intellectual Property

All content on sparkwright.org — including the tools, games, design, copy, educational methodology, and visual elements — is the property of Sparkwright. All rights reserved.

The educational methods and pedagogical design reflected in Sparkwright tools (including the Practice Quest remediation approach and the two-level fluency model in Math Flash) represent original work by the developer. While the underlying research is cited and credited, the application, design, and implementation are Sparkwright's own.

## 7. Your Data

Sparkwright tools store session data in your browser's local storage. See the Privacy Policy for details. Short version: your data stays on your device. We don't collect it, store it on a server, or share it with anyone.

## 8. No Warranties

Sparkwright tools are provided as-is. We make no guarantees about uptime, error-free operation, or specific educational outcomes. Learning is complex and no tool produces identical results for every student.

We believe these tools are well-designed and grounded in solid research. That's a different thing from a warranty.

## 9. Limitation of Liability

To the extent permitted by law, Sparkwright is not liable for any indirect, incidental, or consequential damages arising from your use of these tools — including data loss, educational outcomes, or technical failures.

Your data is stored in your browser. If you clear your browser data, that history is gone. That's the tradeoff of local storage. Back up what you need to keep.

## 10. Governing Law

These terms are governed by the laws of the State of Colorado, United States.

## 11. Contact

Questions about these terms: Use the contact form at sparkwright.org/contact — or email contact@sparkwright.org.

---

---

# Privacy Policy

*For sparkwright.org and all Sparkwright tools and games*
*Effective: [DATE]*

---

**The short version:** We don't collect your data. Session data lives in your browser. We use Google Fonts, which makes an external request when you load the page. That's about it.

---

## 1. What This Policy Covers

This Privacy Policy describes how sparkwright.org handles information when you use our site and tools. The short answer is: we handle very little, and what we do handle stays on your device.

## 2. Information We Do Not Collect

Sparkwright does not:
- Require you to create an account
- Collect your name, email address, or any other personal information to use the tools
- Store any session or practice data on our servers — there are no servers holding your data
- Use advertising trackers or analytics that identify individual users
- Sell or share data with third parties

## 3. Local Storage — How Session Data Works

Sparkwright tools use your browser's **local storage** to save session history, profile names, and practice data. This data lives entirely on your device, in your browser.

**What this means:**
- Your practice history doesn't go anywhere. We can't see it. No one can, except you.
- If you clear your browser's local storage or site data, that history is gone. It cannot be recovered.
- Data does not transfer between devices or browsers automatically. If you use Math Flash on two different computers, the histories are separate.
- If multiple students share a device, the profile system keeps their data separate within the same browser.

We chose local storage deliberately — not as a technical shortcut, but because we believe your practice data belongs to you.

## 4. Third-Party Services

**Google Fonts.** Sparkwright uses Google Fonts (fonts.googleapis.com / fonts.gstatic.com) to load typefaces. When you load a Sparkwright page, your browser makes a request to Google's servers to fetch these fonts. This is standard web practice, but it means Google receives your IP address as part of that request. Sparkwright does not control what Google does with that information. See [Google's Privacy Policy](https://policies.google.com/privacy) for details.

We currently use no other third-party services that receive user data (no analytics, no advertising, no social tracking).

## 5. Children's Privacy

Sparkwright tools are designed for use with children in educational settings, under the supervision of a parent, teacher, or other adult. We do not knowingly collect personal information from children — or from anyone, for that matter, because we don't collect personal information at all.

Because Sparkwright tools use local storage only and require no account creation or personal information to operate, they are designed to be compatible with family and educational privacy expectations, including COPPA (Children's Online Privacy Protection Act). *(Developer note: if you ever add server-side features — accounts, cloud sync, analytics — COPPA compliance will require a formal review before going live.)*

## 6. Payments

When Sparkwright tools are purchased, payment processing is handled by a third-party service (such as Stripe or Gumroad). Sparkwright does not receive or store your payment information. The payment processor's own privacy policy governs how that data is handled. *(Developer: add the specific processor name and link once payment is set up.)*

## 7. Changes to This Policy

If this policy changes in a way that affects how your data is handled, we'll update the date at the top of the page. Given the local-storage-only model, meaningful changes are unlikely unless Sparkwright adds server-side features in the future.

## 8. Contact

Questions about this policy: [contact email] *(Developer: add contact method before publishing.)*

---

---

# Cookie Policy (Brief)

*This can be a short section on the Privacy Policy page rather than a separate page.*

---

Sparkwright does not use advertising cookies, tracking cookies, or analytics cookies.

The site uses **Google Fonts**, which may result in a session cookie or cached font files being stored in your browser as a standard part of web font loading. This is a technical byproduct of how fonts are delivered on the web, not a tracking mechanism.

No cookie consent banner is currently required for Sparkwright's use case under most jurisdictions' interpretations of applicable law, given the minimal nature of the data involved. *(Developer note: if you add analytics, advertising, or EU-targeted marketing in the future, a consent banner will be required under GDPR/ePrivacy.)*

---

---

## Legal Notes for the Developer

*(Not published on site — internal only)*

### Entity / Business Structure
Currently operating as a sole proprietor. Personal liability is not separated from business liability. Before revenue becomes meaningful, consider forming a single-member LLC in your state. Consult a CPA — the cost is low and the protection is real.

### Trademark
"Sparkwright" is a distinctive coined word. Common law trademark rights begin at first use in commerce (your first sale). USPTO federal registration is a separate step — not required to have rights, but it formalizes them and makes enforcement significantly easier. Filing cost: approximately $250–350 per International Class, done online at USPTO.gov. File in International Class 41 (education and entertainment services). Can be done yourself; an IP attorney makes the process cleaner. Recommended: file within 6 months of first commercial sale.

### Copyright and AI-Assisted Development
US copyright law requires human authorship. The Copyright Office has declined to register works where AI is the primary author. The argument for Sparkwright's copyright is reasonable: the developer makes every creative, pedagogical, and product decision; Claude executes them at a technical level. This argument has not been definitively tested in court. Before enforcing copyright against a copycat (i.e., before you'd ever need to sue someone), have an IP attorney assess the ownership position. Not a launch-day concern.

### Terms of Use — Sections Needing Developer Input Before Publishing
- Section 10: Insert your state
- Section 11: Insert contact method (email address or contact form link)
- Privacy Policy Section 6: Insert payment processor name and link once payment is configured
- Privacy Policy Section 8: Insert contact method
- Both pages: Insert effective date

### Email — contact@sparkwright.org
Decided Session R. Set up via Zoho Mail (free) or ImprovMX forwarding — both require adding MX or forwarding records in the Netlify DNS dashboard. Do this before publishing the legal pages (so the contact address is live). The contact form on the site (Netlify Forms — see Wright's handoff) sends notifications to this address.

### Payment Processor Recommendation
Gumroad and Stripe are both appropriate for Sparkwright's use case. Gumroad is simpler for one-time digital product sales (handles the sales page, delivery, and payment in one). Stripe requires more setup but gives more control. Both handle credit card compliance (PCI DSS) — you don't carry that burden. Decide before launch.

---

*This file is a working draft. The developer should have these documents reviewed by an attorney before or shortly after commercial launch. Legal copy that has not been attorney-reviewed is better than no legal copy — but reviewed copy is better still.*
