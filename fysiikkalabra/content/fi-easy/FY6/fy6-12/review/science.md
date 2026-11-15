VERDICT: PASS
CONTENT-HASH: df631311125c85b1

## Blocking
(none)

## Polish
- lesson.md:38 (Elektronivoltti) — "Hiukkasen varauksen suuruus on alkeisvaraus $e$" is stated as general. The lesson's own alpha particle has $2e$ (koe-2, conclusion). Fix: "Protonin ja elektronin varauksen suuruus on alkeisvaraus $e$." This is a B-type wording issue. It is not blocking, because the paragraph then treats only e-charged particles, and koe-2 and the formula $|q|U$ immediately show the general case.
- sim.js plates() — the electron is filled with VELC, the velocity blue (FY4 colour code). A student may read the blue dot as velocity. Fix: use a neutral negative-charge tint (for example NEGL) for the particle.
- lesson.md:46 — "Vihreä valo tulee hapesta" could say "happiatomeista" to match the atoms and molecules named just before. Optional.

## Checked
- One Python script recomputed every lesson-answers.py value with my own formulas: figure field 5000 V/m; worked example 4,806·10⁻¹⁶ J, 3,25·10⁷ m/s, 0,108 c; koe-1 E and t (162/323/646 ns), with E_k = 500 eV from the work theorem; koe-2 speeds 309 / 13 262 / 220 km/s and the ratio 42,9; siirto 42,0 km/s and its three mistakes; tarkistus-2 300 eV; the hook's 5 keV → 4,19·10⁷ m/s (≈ 40 000 km/s); the sim's limits 0,063 c and gravity ≥ 4,9·10⁹ times smaller; the exit ticket −50 eV and 4,8·10⁻¹⁶ J. All agree. The xenon-ion mass 2,18·10⁻²⁵ kg matches 131,3 u.
- The proofreading fixes are correct. The Kaava fence names $V = E_\text{p}/q$ (sähkökentän potentiaali) with $E_\text{p} = qV$ under it, and the symbols are named. The lightning caption is physically right: potential energy turns into light, sound and internal energy of the air, which is then transferred as heat. The section title names the law.
- Signs: $E_\text{p} = qV$ with $q = -e$ for the electron, $W_{AB} = q(V_A - V_B)$, and the field points from higher to lower potential. Both charges start toward lower potential energy. The energia figure (proton 200 → 0, electron 0 → −200 eV) and the lightning-strikes caption agree with this.
- The worked example is solved symbolically first. Two significant figures follow 3,0 kV. The classical $\tfrac12 mv^2$ is justified at 11 % of c (γ − 1 ≈ 0,6 %).
- Figures: tasapotentiaali has equal 1,0 cm / 50 V spacing between 200 V and 0 V. vx-graph runs (0; 0) → (4; 200), with a triangle of 100 V over 2,0 cm, giving 5000 V/m. In kentta the field is green and the force red; mg and qE point down, in the field direction for +q.
- sim.js: $F = |q|E$, constant-acceleration steps with an exact arrival time, $E_\text{k}$ from v (not from $|q|U$), and $V = Ex$ measured from the negative plate. The force and velocity arrows point toward the + plate for the electron. simState has E, tns, EkeV, EpeV and vkms. The adapter has U, d and hiukkanen. Every experiment value lies within the slider ranges.
- The experiments isolate their parameter: koe-1 locks U and the particle; koe-2 locks U and d.
- Every choice item (kertaus, ennuste 1–2, virhe, tarkistus-1) has exactly one correct option, and each distractor's feedback is right.
- Magnitudes: lightning at up to hundreds of MV, the auroral acceleration of a few kV at thousands of km, emission at 100–300 km, a plasma lamp at several kV, ion-thruster exhaust about 10 times a chemical rocket's. All are realistic.
- Scope: potential energy and potential in a homogeneous field are FY6 central contents, and the eV is a natural tool here. The definitions match the glossary and the chapter *Kirchhoffin lait ja potentiaali virtapiirissä*.
