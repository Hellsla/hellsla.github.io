VERDICT: PASS
CONTENT-HASH: e7d898f05aacd758
## Blocking

## Polish
- solutions.md:206 (following distance, $35{,}94\,\text{m}$) Kaava — "Autot eivät törmää, jos $d$ ja edellä ajavan pysähtymiskohta yltävät takana ajavan pysähtymiskohtaan" is hard to read. Fix: "Autot eivät törmää, jos takana ajavan kulkema matka $s_2$ on enintään $d + s_1$; rajatapauksessa $d + s_1 = s_2$."
- solutions.md:248 (crash dummy) — Periaate names the impulse principle, the new Kaava derives $F = m\,\Delta v/\Delta t$ from $\Sigma F = ma$ and $a = \Delta v/\Delta t$. Both are right; pick one so Periaate and Kaava agree.
- solutions.md L3 calculator task, Kuvaajan lukeminen (unchanged context) — "$40\,\text{km/h} 11\,\text{m}$" lacks a separator (colon) between speed and distance, four times.
- Kaava rows — "…, joten …, joten …" twice in one sentence (seat belt, airbag). Fix: second "joten" → "ja".

## Checked
- Captures: none opened (judged from text; the diff is text-only).
- Every rewritten Kaava now starts from the basic laws: $v = s/t$; $I = F\,\Delta t$, $p = mv$, $I = \Delta p$; $\Sigma F = ma$, $F_\mu = \mu N$, $N = mg$; $s_\text{j} = \tfrac12 v_0 t_\text{j}$ with $t_\text{j} = v_0/a$, as the brief's lesson derives them; each derived form is right.
- Braking-distance tasks (131,1 m; 81,46 km/h; $a = 1/(2k)$; $k^2$ scaling; 31,5 m): symbolic form right and the one substituted.
- Child task: $d = u t_\text{r} + u^2/(2a)$, then $v_0^2/(2a) = (d - v_0 t_\text{r}) + v^2/(2a)$; 36,7 km/h unchanged.
- L3 0,600 m stop: substitution now into $F_\text{ka} = m v_0^2/(2s)$; recomputed $70{,}0 \cdot 13{,}889^2 / 1{,}200 = 11\,253\,\text{N}$, as before; $\Delta t$ kept as a side result.
- Following distance: rear car never slower than the front one until it stops, so the end-point condition suffices; 35,94 m unchanged.
- $(v, s_\text{p}/v)$ linearisation and quadratic root: algebra right.
- Two-test airbag: $F_\text{A} - F_\text{B}$ written as two fractions; 10,5 kN unchanged.
- Paragraph splits change no wording or number; no answer, tolerance, task or id changed.
- Hash e7d898f05aacd758 at the start and at the end.
