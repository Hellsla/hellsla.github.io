VERDICT: PASS
CONTENT-HASH: ca309097b118a6c4

## Blocking

## Polish
- lesson.md:150 — the derivation says θ is the angle between the velocity and the field and gets $BA \cdot 2\pi f \sin\theta$. It never connects this to $e = e_0\sin(2\pi f t)$. — Add one clause: the velocity points along the coil's normal, so θ is also the rotation angle, $\theta = 2\pi f t$.
- lesson.md:257 and inquiry.json:260 (virhe, third option feedback) — "Teho on positiivinen kummallakin virran suunnalla" is stated without a load. It holds for a resistor (as at lesson.md:164) but not for every AC circuit. — Add "vastuksessa" (or "resistiivisessä kuormassa").
- sim-spec.md:1 (and the sim.js comments) — calls the violet dot and cross "induktiovirta", but the sim's `model` box says that no current flows (no load) and that the symbols only show the direction of the induced voltage. — Align the internal wording with the student-facing box.
- inquiry.json:73 (ennuste-taajuus) — the prompt gives no N or B, but the feedback quotes $1{,}26\,\text{V}$ and $2{,}51\,\text{V}$. That works because the feedback is shown after koe-1, but saying "kokeen 1 arvoilla" in the feedback would tie the numbers to their source.
- derive figure (lesson.md:149 ff.) — labels the current I although the derivation is about the emf with no load. The direction is correct (v×B), so the label is harmless. Optionally label the direction "induktiojännitteen suunta".

## Checked
- Recomputed every number in one script. Worked example: e₀ = 6,786 V and U = 4,798 V (4,8 V). Pysähdy items: 0,0020 Wb, 0,050 s, 1,4 A. koe-1 e₀ = 1,257 / 2,513 / 5,027 V and T = 1,0 / 0,50 / 0,25 s. koe-2 e₀ = 1,257 / 2,513 / 3,770 V. e₀ : f = NBA·2π = 1,257 V·s. siirto 15,99 V and all four mistakes (22,62; 959,7; 31,99; 2,546 V). Kettle 12,30 A (mistakes 8,696 and 6,149 A). 325 V, 0,20 Hz. Wind share 19,8 TWh / 24 % ≈ 82 TWh consumption, plausible.
- Derivation: v = πfb, two sides, A = lb gives e₀ = NBA·2πf. Units T·m²/s = V.
- Sim: Φ = BA cos θ; e = −NΔΦ/Δt by central difference (numerical peak at 1 Hz = 1,25664 V, matching the formula, so the result emerges and is not hard-coded). The sweep stays continuous when a control changes. Graph scales cover the maximum (18,85 V, 0,6 mWb).
- Sim geometry: the side velocity lies along the normal. At θ = 90° the right side moves up, so v×B points into the page (×) for e > 0. Matches the 1280 px capture (θ = 93°, e = e₀).
- Experiments: koe-1 locks N and B and varies f; koe-2 locks N and f and varies B. The slider steps reach every requested value. simState exposes e0 and T.
- Figures: the Φ/e graph is a cosine and a sine with the coil icons in the right orientations. The power graph is P₀sin² with its mean at P₀/2. In the derive figure the side currents agree with v×B.
- Predictions: exactly one correct option in each, and every distractor's feedback is correct. The check-1, virhe and retrieval items are correct.
- The effective-value definition, P = UI limited to resistive loads, and the mains 230 V / 325 V / 50 Hz agree across theory, summary, glossary, exit ticket and checks.
- Power plant: rotating field magnet with the large current taken from stationary windings without sliding contacts (correct). The wind turbine's frequency converter and 10–15 r/min are plausible.
- Scope: generator and AC generation per LOPS FY7; no self-induction or later-course physics.
