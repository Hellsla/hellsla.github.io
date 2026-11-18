VERDICT: PASS
CONTENT-HASH: 5b99d8f82d884a08

## Blocking

## Polish
- content/fi-easy/FY4/sovella/solutions.md fy4-s3 d) Periaate — "Kappaleen nopeus muuttuu vain, kun siihen vaikuttaa voima (Newtonin ensimmäinen laki)": the law speaks of a non-zero total force; write "kokonaisvoima".
- solutions.md fy4-s3 b) Järkevyys — "Noin $40\,\%$ siitä kuluu peltien rutistumiseen": the loss is $67\,\text{kJ}$ of $158\,\text{kJ}$ ($42\,\%$), and the energy is not used up; "muuttuu peltien muodonmuutoksessa sisäenergiaksi" matches the chapter's wording.
- solutions.md fy4-s2 a) Kaava — the new lead names the law, but Periaate already says why it applies; the repeated "Lähtölavalla … levossa" sentence could be cut to one clause (taste).

## Checked
- Hash 5b99d8f82d884a08 at the start and the end; since 062f457c28^ only seven `**Kaava:**` lines of solutions.md changed (s1 c, s2 a–c, s3 a–c); tasks.json, answers.py, numbers, answers, points and ids unchanged.
- Every rewritten Kaava now starts from the basic law ($\Sigma F = ma$ with $F_\mu = \mu N$; $E_{\text{p}0} + E_{\text{k}0} = E_\text{p} + E_\text{k}$; $E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}$ with $W = -F_\text{vast}s$ and $W = -\mu mg s$, signs right; $p_\text{ennen} = p_\text{jälkeen}$; $I = F_\text{ka}\Delta t = \Delta p$), simplifies symbolically and substitutes into the last form.
- Recomputed independently: s1 $a_\text{A} = 0{,}39$, $a_\text{B} = 0{,}245\,\text{m/s}^2$, $g\sin\alpha = 0{,}684$, $g\cos\alpha = 9{,}786\,\text{m/s}^2$, $\mu_\text{A} = 0{,}030$, $\mu_\text{B} = 0{,}045$, $a_0 = 0{,}449$, $\mu_\text{A0} = 0{,}024$; s2 $17{,}2\,\text{m/s} = 61{,}8\,\text{km/h}$, $F_\text{vast} = 29{,}1\,\text{N}$, lost $0{,}574$, $13{,}6\,\text{m/s}$; s3 $7{,}86$, $13{,}6\,\text{m/s} = 49\,\text{km/h}$, $4455\,\text{N}$ ($6{,}7\,mg$), friction impulse $2605\,\text{N·s}$ ($11\,\%$), $v_\text{B,max} = 15{,}2\,\text{m/s}$: all equal answers.py.
- s1 d–e: air resistance biases both $\mu$ upward and A more (faster run); systematic, not removed by repetition; conclusion holds. Correct.
- s2: cable force perpendicular to motion does no work (frictionless model); d) friction ∝ mass, air resistance not; true speed between the two estimates; brake sized on the larger value with safety margins stated.
- s3: momentum across the short collision only, kinetic energy not; e) friction during collision makes the estimate a lower bound; $\mu$ needed for 40 km/h ≈ 0,50.
- Every part answerable with FY4 chapters; assumptions stated in the task texts.
- Captures: none opened (fi-easy judged from text and the packet).
