VERDICT: PASS
CONTENT-HASH: 8a3a2c048540e528
SCOPE: delta, Kaava steps rewritten (basic equation, then simplified symbolically)

## Blocking
(none)

## Polish
1. solutions.md:191 and :227 (Järkevyys of the painter task, Sijoitus of the ladder) — the sums were turned into display blocks in the middle of a sentence ("massojen ja paikkojen tulojen summa on [block], ja kokonaismassalla…"). The 1280 px capture of 2-19 and 2-20 shows a sentence broken into fragments, with a comma and "ja" stranded on their own lines. The task said Sijoitus and the checks stay unchanged. Put these chains back on one inline row, or give each its own sentence.
2. solutions.md:95 and :199 — the `\quad` continuation rows ("&\quad + F_h r_h") split a short equation by hand. Keep each equation on one row; the rule says only a phone wraps.
3. solutions.md:187 (painter) — the chain `x − x_2 = r_2 = …` is correct but the step "r_2 = m_L r_1/m_m" reads better with x itself solved last ("x = x_2 + r_2").
4. solutions.md:225 (ladder) — the Kaava gives the formula for s using N_s, but does not say that f = μN holds only at the limit. Periaate now says so, which is enough.

## Checked
- Each Kaava now starts from the basic condition (ΣM = 0, ΣF = 0, M_1 = M_2), then gives the equation with the moments, then simplifies it. The ladder takes ΣF_y, ΣF_x and ΣM in turn. The order follows the house rule: basic equation, then derived formula.
- Every Kaava is simplified symbolically to the end (r_2, N_1, T, a, s, x_h) before Sijoitus. The Sijoitus and the final answers are unchanged.
- The centre of mass tasks start from M_1 = M_2 and derive x_pp. This is better than quoting the formula.
- Shelf and cable-and-sign tasks: Periaate and Kaava stay in step, and the components of T are explained before the equation.
- Split paragraphs in Periaate and Vastaus are short, with one idea each, and the content is unchanged.
- Rows at 1280 px, in the captures I opened, are aligned and not clipped.
- Chair task (2-17b): Kaava mixes the interpolation formula with the centre of mass formula under one heading, acceptable at level 3.
