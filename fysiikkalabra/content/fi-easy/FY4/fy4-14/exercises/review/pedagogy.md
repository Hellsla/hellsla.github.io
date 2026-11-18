VERDICT: PASS
CONTENT-HASH: 7b61c71e80ac95f1
SCOPE: delta numbers from 4de8ceed5601dd99 base cabadc3e6179

## Blocking
None.

## Polish
1. exercises/solutions.md (Kaava of the falling-jumper tasks: "$\Sigma F = G - F_\text{v} = mg - F_\text{v}$") — the positive direction (down) is not named in most of them, only in the rise and fall task — add "Positiivinen suunta on alas." as in that task.
2. exercises/solutions.md (free-fall part b, Kaava) — "a = g" is derived after it has been used in $v^2 = v_0^2 + 2as$ — put "Ilman ilmanvastusta $\Sigma F = mg$, joten $a = g$" before the $v^2$ step.
3. exercises/solutions.md (Järkevyys of L2-08) — "poikkipinta-ala" is still not opened (earlier polish) — "suurempi poikkipinta-ala eli ala, johon ilma osuu".

## Checked
- Rewrite only: each Kaava opens with ΣF = ma, shows ΣF as the sum of named forces (G, F_v, F_r), sets it equal to ma (or 0 when a = 0), then solves; no number, answer or id changed.
- Equilibrium tasks now say a = 0 and so ΣF = 0, which makes "mg - F_v = 0" a result of a principle, not a given.
- The rise and fall task shows why the signs differ (both forces down on the way up, air resistance up on the way down) and stays correct: Δa = 2F_v/m.
- Terminal-speed table tasks: F_v = m(g - a) is derived from ΣF = G - F_v, and the case a = 0 is tied to ΣF = 0.
- Free-fall part b names v² = v0² + 2as with v0 = 0, a = g, s = h before v = √(2gh).
- Paragraph splits in Mallivastaus and Järkevyys are line breaks only.
- Captures not opened: only solution wording and formula order changed; judged from the packet's diff.
- Hash the same at start and end.
