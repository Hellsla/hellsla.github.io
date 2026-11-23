VERDICT: PASS
CONTENT-HASH: 6559f6723de456c3
SCOPE: delta numbers,reflow,typography from 81b5cf5d2daaa058 base 4b05399

## Blocking

## Polish
- exercises/solutions.md:76 (L1-05 Kaava) — "$E = hf$, josta:" is followed by $f = \tfrac{c}{\lambda}$, which does not follow from $E = hf$ alone but from the wave equation $c = \lambda f$. Fix: "$E = hf$ ja $c = \lambda f$, joten:" (the same wording as fy8-15).
- exercises/solutions.md:470 (L3 activity task Kaava) — "$R = \ldots$, josta:" leads into $T = (\tfrac{1}{2})^{d/d_{1/2}}$, which is a separate law and is not derived from $R$. Fix: "…, ja seinän läpäisevä osuus on:" or "ja".

## Checked
- Hash 6559f6723de456c3 (`reviews.py hash fy8-12 --exercises --lang fi-easy`) at the start and the end.
- The packet's diff view joins the rows of each aligned block into one line. I judged the file on disk: every new Kaava block is a separate aligned row per equation, so the joined chains such as "$f = \tfrac{c}{\lambda} E = \ldots$" are an artefact of the packet only.
- `git diff origin/main`: only solutions.md changed, and every removed line is a `**Kaava:**` line. Givens, Muunnokset, Sijoitus, answers, answers.py and tolerances are unchanged.
- Every new block starts from the basic law (vaimenemislaki, $E = hf$, $N_\text{netto} = N - N_\text{t}$, $R_\text{kok} = N/t$) and ends with the same solved form as before.
- I checked each derived form numerically: $d_{1/2} = d\ln 2 / \ln\tfrac{N_0-N_\text{t}}{N-N_\text{t}}$ puts the value back into the law exactly. So do $d = d_{1/2}\ln(1:p)/\ln 2$, $d = d_{1/2}\ln\tfrac{R_0-R_\text{t}}{R_\text{t}}/\ln 2$ (with $(\tfrac12)^{d/d_{1/2}} = R_\text{t}/(R_0-R_\text{t})$) and the two-barrier product of the fractions.
- The equal-attenuation condition $(\tfrac12)^{d_\text{b}/d_{1/2,\text{b}}} = (\tfrac12)^{d_\text{Pb}/d_{1/2,\text{Pb}}}$ gives the right equality of exponents.
- The activity chain $A = R/(T\eta)$ keeps the stated assumption of one photon per decay.
