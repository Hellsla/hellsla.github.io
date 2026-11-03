VERDICT: PASS
CONTENT-HASH: 06e3cd81e22884a5

## Blocking

## Polish
- lesson.md (Lintu johdolla) and inquiry.json (hook, siirto): the line is described with DC reasoning, but power lines carry AC. For a 4 cm segment R I is still a fair model (C); a half-sentence ("hetkellisesti") is optional.

## Checked
- Round 3 change (narrow-screen layout of sim.js) touches no physics: solve(), simState, the ground shift and the graph path F → U → A → R1 → B → R2 → E → F are as in the passed round. The narrow branch only moves coordinates (XN, NARROW), draws the meter's leads as right-angled wires to the right points (black on the reference point, red on the probe) and doubles the graph's tick step (0, 6, 12 V; −12, 0, 12 V with B as reference), which loses no values: every potential is printed at its point.
- Test change: the narrow canvas height 780 → 966 is a layout constant that now equals NARROW.H in sim.js; it pins no physical quantity, behaviour or invariant, so it is not a weakening of any science check. The layout checks at 360/768/1280 px pass.
- Screenshots at 390 px (sim, koe-3): potentials A 9,0 V, B C 6,0 V, D E F 0 V; I1 0,300, I2 0,200, I3 0,100 A; loop sum 0,00 V; earth on the reference wire; probe level dashed at 9 V and ringed at A; graph labels F, U, A, R1, B, R2, E, F in the right places.
- One script recomputed with my own formulas: sim on load (R23 20 Ω, I1 0,30 A, U1 3,0 V, branch 6,0 V, I2 0,20 A, I3 0,10 A); koe-1 at R3 = 30/60/120 Ω (I1 0,36/0,30/0,265 A = I2 + I3); koe-3 with B as reference (V_A 3,0 V, V_F −6,0 V, U1 3,0 V); worked example (V_B 6,0 V, I3 0,20 A, I2 0,10 A); virhe (0,45 A > 0,30 A); siirto 1,92 mV and mistakes 192 and 1920 mV; tarkistus-2 3,0 V and mistake 15 V; exit ticket 0,15 A and 3,5 V. All agree with lesson-answers.py and the text.
- Ranges: U max 12 V and the potential axis 0…13 V (or −13…13 V) hold every reachable potential.
- Every choice item has exactly one correct option; distractor feedback names the right reason.
- Each experiment isolates its varied parameter (R3; probe; ground) with the rest locked; simState carries I1–I3, Vp, VA, VB, VF, U1.
- Model limits (ideal source, wires, voltmeter; model values, not measurements) are stated in the sim's model box, the theory and the conclusion.
- Scope inside the FY6 täsmennys; current law from charge conservation in steady state, voltage law from single-valued potential, as in the glossary.
