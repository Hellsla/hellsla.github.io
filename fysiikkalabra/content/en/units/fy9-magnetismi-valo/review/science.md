VERDICT: FAIL
CONTENT-HASH: e09f46511f4167f8
SCOPE: delta: new Sovella tasks s8 (A laser experiment with an acrylic plate) and s9 (Flux through a coil and the induced current) and the changed intro; s1-s7 untouched, not re-judged.

## Blocking
- s9, common mistakes, line 2 (A, quantitative): "$\text{mWb}$ is not converted to $\text{Wb}$, so the voltage is a thousandth of the correct one" is the wrong way round. Using $8.0$ as webers gives $120 \cdot 8.0 / 0.40 = 2400\,\text{V}$, a thousand times the right value. Fix: "so the voltage comes out a thousand times too large ($2400\,\text{V}$)". The Finnish text has the same error.

## Polish
- s8, common mistakes, line 1: the inverted slope from the quoted points is $0.30 : 0.45 \approx 0.67$, not $0.30 : 0.44 = 0.68$ (that is one point's ratio). The conclusion ($n < 1$) holds.
- The section headings "Yleisiä virheitä" and "Hyväksytään myös" are in Finnish in solutions.md. I assume they are the required parser keys, so this is not a finding if the page shows them translated.

## Checked
- `units.py hash --lang en` gave e09f46511f4167f8 at the start and at the end. `practice.py check` OK.
- I read the English task text, parts, criteria and solutions of s8 and s9, and the intro.
- Numbers: every number in the s8/s9 solutions is the same multiset as in the Finnish text, decimal point aside (checked by script). My recomputation (refit of the fy7-10 data and an independent s9 computation) agrees:
  - s8: $1.5$; $2.0 \cdot 10^8\,\text{m/s}$; $0.75\,\text{ns}$; $41.8^\circ \approx 42^\circ$.
  - s9: $2.4$ and $1.8\,\text{V}$; $0.369 \approx 0.37\,\text{J}$; $0.25\,\text{s}$.
- Fidelity: the English matches the Finnish physics.
  - Snell's law, slope $= n$, $v = c/n$.
  - The critical angle as $\alpha_\text{c}$ (a symbol name only).
  - The Lenz directions and signs, and "the flux increases towards zero".
  - "Converted into internal energy".
- Physics as in the Finnish report: right. The self-inductance is left out, which is a fair simplification (C).
- Rubric points add up (s8 15, s9 12). The unit fields are language-neutral ("", "· 10⁸ m/s", "ns", "°", "V", "J").
- Intro: "Nine" problems, and the seventh is the source-based one. Correct.
