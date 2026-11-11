VERDICT: PASS
CONTENT-HASH: 84abdaa36d4ebf09

## Blocking

## Polish
- lesson.md:232 (Ydinajatus, "Paine kasvaa kolmella tavalla") — the three bullets do not say "kun muut suureet pysyvät samoina". The Kaava section gives the condition later through $p \propto NT/V$, so this is C, not B — add "kun muut pysyvät samoina" to the lead sentence.
- inquiry.json siirto solution, Järkevyys — the "about 700 kg lighter than the displaced outside air" step assumes outside air at 20 °C, which the task does not give — say "jos ulkoilma on $20\,{}^\circ\text{C}$".
- inquiry.json taulukko, correct feedback — "tästä vakiosta tulee moolinen kaasuvakio $R$" glosses over the step from $pV/(NT)$ (relative units, ≈ 1) to $R$ through $N = nN_\text{A}$ — this is fine at the level; optionally write "vastaava vakio".

## Checked
- One script recomputed every number with my own formulas: the weighing m/M (0,2075; 0,2064; 0,2076; 0,2068 mol), R from the mean (8,32 → 8,3) and from helium (8,302), the laske-r mistakes (121,7; 8302; 0,008302), the worked example (0,2073 mol; 0,83 g; air 6,0 g), virhe (1,2 → 0,083 mol), siirto (2645 kg → 2,64·10³; mistakes 9870, 2,64), check-c2 (1,068), check-2 (3,0; 2,25; 1,69), koe-2 (50; 70,7), the exit ticket (0,601 mol). All agree, and so does lesson-answers.py.
- Significant figures: each answer is rounded by its really limiting datum. The worked example is solved symbolically first and has all seven stages.
- sim.js physics: in 2D, the impulse per unit perimeter gives $p = NkT/A$ exactly when $\langle v_x^2\rangle = \langle v_y^2\rangle$. thermalize() enforces that, T rescales the speeds by √T, a change of V keeps the speeds (isothermal), and P_REF comes from the model.
- Playwright run of the sim (20 s runs): the mean $p/p_\text{ref}$ equals $(N/100)(T/300)(100/V)$ within 0,5 % for 9 states, the taulukko rows included (its 1,05; 2,00; 0,98; 5,11 are plausible model values). The spread at N = 20 is about 5 % (1σ), which fits the "±10 %" claim.
- exp-1 and exp-2: locking T and V isolates N, and simState has pMeasured and hitRate. At 600 K, N = 50 gives 1,00 ± 0,02. The new tolerance 0,1 (45–55) still rejects 40, 60, 71, 25 and 200.
- Every choice item has exactly one correct option, and each distractor's feedback names the right mechanism (hit rate, momentum per hit, kelvin zero point).
- The figures are to scale: the He/air arrow ratio is 2,67 against √(29/4) = 2,69, the mole-mass bars are 14 : 101,5 : 154 = 4 : 29 : 44, and in the 2T panel the arrows are about √2 longer.
- The ideal-gas conditions are stated (high pressure, low temperature), and kelvin and the units are explained. Scope stays within FY3, with no FY4 mechanics.
- The hash was the same at the start and the end of round 2.
