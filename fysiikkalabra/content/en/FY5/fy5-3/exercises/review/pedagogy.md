VERDICT: PASS
CONTENT-HASH: fd9908d0a3796bfd
none

## Blocking
(none)

## Polish
- solutions.md:67 (the gondola, L2-02) — r = d/2 comes last in the chain, after it has been used in T = 2πr/v; put r = d/2 first or add T = πd/v. Not an error: the Conversions step computes r first.
- solutions.md:283 (the CD, L3-05) — r_av appears in s = N·2πr_av without its own line r_av = (r_1 + r_2)/2; add it to the chain.
- solutions.md:185 (the carousel seat, L2-… with ten revolutions) — the Kaava is still a row of separate formulas (t_av, T, v). The data task fits that, but T = t_av/10 could be substituted into v = 2πr/T to give one final symbolic expression.

## Checked
- The diff in the packet shows the new Kaava steps flattened to one line; the file has them as aligned rows, one equation per row, in the order basic equation → rearrangement → last form.
- The blade tip, record and test tube tasks start from v = 2πr/T and T = 1/f before v = 2πrf; the frequency form is derived rather than assumed.
- The proportion tasks (the blade point and the runners) write each speed from the basic equation, divide them and end with v_2 = (r_2/r_1) v_1; the cancellation of T (or t) is visible.
- The puck first gets s = vt, then the Pythagorean step, and d = sqrt(r² + (vt)²).
- The bicycle task derives the chain speed, then f_r, then u, and ends with the symbolic form u = 2πR (r_f/r_r) f_f used in the substitution.
- The latitude task ends in v = 2πR cos φ / T, and the Substitution uses it.
- The sprockets of the record player: same pattern. Principle paragraphs are split into one idea each; no reasoning is lost.
- Substitution, answers and tolerances unchanged; the figure karuselli is unchanged.
- The content hash at the start and end is the same as the packet's.
