VERDICT: FAIL
CONTENT-HASH: 1f38648415996384

## Blocking
- lesson.md:38 — **A.** The Key idea says "Fill a 5.00 litre balloon … In an example weighing the masses of the gases are 0.83 g …". You cannot get a gas's mass by weighing a flexible balloon in air: the buoyancy of the displaced air is about as large as the gas's own weight, and a helium balloon would weigh less than the empty one. The Finnish "pallo" here means the rigid glass flask of inquiry.json:80 ("thin-walled 5.00 litre glass flask … pumped empty"), which was already corrected to "flasks" in the activity title. — Write "a rigid 5.00 litre glass flask, first pumped empty, is filled …" so the text matches the weighing activity. Keep "balloon" only for the hook and the worked example.
- inquiry.json:511 (check-2 solution, Principle) — **B/A.** "At every moment $pV = NkT$ holds". The lesson never introduces $k$ (it uses only $n$, $R$ and $p \propto NT/V$). In the simulation the pressure visibly fluctuates, and the relation holds only for the time-averaged pressure. — Write "By the equation of state, with $n \propto N$, the (averaged) pressure is $p \propto NT/V$." The same sentence is in the Finnish source ("Jokaisella hetkellä pätee $pV = NkT$"): fix it there too.

## Polish
- inquiry.json:106 (punnitus, Reasonableness) — "5.00 l contains about 5.00 · 0.041 ≈ 0.21 mol of any gas" uses a molar volume (0.041 mol/l) that the student meets only later, in the equation of state. As a check it is fine, but it uses the conclusion the activity is building towards. Consider checking backwards only.
- inquiry.json:326 (laske-r, Principle) — "the same for all ideal gases, because the gas laws do not depend on the type of gas" is close to circular. "Because $m/M$ was the same for every gas at the same $p$, $V$, $T$" names the evidence.
- inquiry.json virhe, third option feedback — `\text{l}` where the rest of the lesson uses `\textsf{l}`.

## Checked
- I recomputed every number in one script with my own formulas, and all of them agree: the weighing masses against n = pV/(RT) (scatter ≤ 0.022 g), m/M for the four gases, mean n 0.2071 mol, R ≈ 8.32 → 8.3, the laske-r answer 8.302 and its three mistakes, the worked example (0.2073 mol, 0.83 g, 6.0 g of air, 24.1 l/mol), virhe (1.2 / 0.083 mol), siirto (91 200 mol, 2645 kg, mistakes 9870 and 2.64, 3360 → 2640 kg), check-c2 1.068, check-2 3.0 (mistakes 2.25 and 1.69), exit ticket 0.601 mol, kertaus 200 kPa.
- The taulukko rows' pV/(NT) are 1.05, 1.00, 0.98, 0.98 and 0.99 as stated. Their scatter is plausible: I ran an independent 2D re-run of the simulation's model, and at N = 100 the 2 s averages have σ ≈ 2 %, range 0.93–1.08.
- The sim claim "N ≈ 20 gives about ±10 %" holds (σ 6 %, extremes ±18 %).
- sim.js: impulse 2m|v⊥| per unit perimeter, P_REF = NkT/A with ⟨vx²⟩ = kT/m, the exact thermalisation after a change of N, v ∝ √T, and a volume change that leaves the speeds unchanged (as the model box says). The time averaging is speed-independent, and 2 s simulated is 4 s real at 0.5×, as the intros say.
- exp-1 and exp-2 lock T and V and vary N. hitRate and pMeasured are in simState, and exp-2 at 600 K gives 2.0, then N = 50 gives 1.00 (slider step 10 reaches 50).
- In every choice item exactly one option is correct, and each distractor's feedback is physically right. That includes the pred-1 helium feedback: more frequent but weaker hits, a 2.69 speed ratio, the same pressure.
- Figures: the helium-to-air arrow ratio is about 2.7 (√(29/4) = 2.69), and the mole-masses bars are in the ratio 14 : 101.5 : 154 = 4 : 29 : 44, to scale as stated.
- The model's conditions are stated: point particles, no interaction energy, failure at high p and low T, R valid for dilute gases, T in kelvins.
- The scope fits the FY3 central content "ideaalikaasun tilanyhtälö".
- The diff since the last PASS is LaTeX typesetting only, with no change in value.
