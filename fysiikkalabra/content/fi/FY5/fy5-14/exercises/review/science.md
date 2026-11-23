VERDICT: PASS
CONTENT-HASH: 206ea06db80075c7

## Blocking

## Polish
- solutions.md:85 (L2-03): $v_\text{rel}$ is a symbol the lesson does not use. The lesson says only that the fronts approach at speed $v + v_\text{H}$. Writing $f = \tfrac{v + v_\text{H}}{\lambda}$ directly would keep to the lesson's notation.
- solutions.md:105 (L3-01): the chain uses $T_0$ in $\lambda_1$ and $\lambda_2$ but never writes $T_0 = \tfrac{1}{f_0}$, unlike L1-04, L2-04 and L2-07. Add it as its own row for consistency.

## Checked
- The diff rewrites only the Kaava steps as aligned chains and splits some paragraphs (L3-02 Periaate, L3-03 Mallivastaus, L3-04 Periaate, L3-05 Vastaus). The split paragraphs keep their wording. Sijoitus, answers and tolerances are unchanged.
- I read the file on disk: the packet's diff dropped `&` and `\\`, but each Kaava is a proper `aligned` block.
- Moving source (L1-04, L2-04, L2-06, L2-07): f = v/λ with λ = (v ∓ v_L)T_0 and T_0 = 1/f_0 gives f_0·v/(v ∓ v_L), with the right sign for approaching and receding. This is the lesson's derivation. L2-04 gives v_L = v(f_0/f − 1) and L2-06 gives v_L = v(1 − f_0/f_ka); both have the right sign.
- Moving listener (L2-03): λ = vT_0 is unchanged, the fronts meet the listener at v + v_H, and f = f_0(v + v_H)/v, as the lesson says.
- L3-01: the ratio f_1/f_2 = (v + v_L)/(v − v_L), cross-multiplied, gives v_L = v(f_1 − f_2)/(f_1 + f_2). Right.
- L3-04, the reflection with two shifts: Δf(v − v_v) = 2f_0v_v, so v_v = vΔf/(2f_0 + Δf). Right.
- L1-01 (s = 2d, v = s/t), L2-01 (beats), L2-02 (same f in both media) and L3-05 (λ_1 = 2L, v = 2Lf_1) are right.
- Recomputed in one script: 340,59; 397,46; 259; 3,70; 697,79; 23,07; 27,82; 30,41 m/s; 0,475 m/s; 254,8. All agree with the solutions.
- Hash 206ea06db80075c7 at the start and at the end.
