VERDICT: PASS
CONTENT-HASH: 2cf75b92f149d281

## Blocking

## Polish
- lesson.md (Lintu johdolla) and inquiry.json (hook, siirto): the line is described with DC reasoning, but power lines carry AC. For the 4 cm segment Ohm's law with R I is still a fair model (C), so this stays as is. A half-sentence such as "hetkellisesti" or "vaihtovirrankin tapauksessa" is optional.

## Checked
- Round-1 polish items are fixed: the bird's tiny current now comes from Ohm's law and the current law adds up the currents (lesson.md:178 ff., siirto Periaate); tarkistus-2 now places A on the plus-pole wire, so its −6,0 V / 9,0 V check holds; the hook says "kymmeniä tai satoja kilovoltteja"; the ideal source is stated where the potential rise is taught (lesson.md:133).
- One script recomputed everything with my own formulas: sim on load (R23 20 Ω, I1 0,30 A, U1 3,0 V, branch 6,0 V, I2 0,20 A, I3 0,10 A); koe-1 at R3 = 30/60/120 Ω (I2 + I3 = I1 in every row: 0,36; 0,30; 0,265 A); koe-3 (V_A 3,0 V, V_F −6,0 V); worked example (V_B 6,0 V, I3 0,20 A, I2 0,10 A); virhe (0,45 A > 0,30 A); siirto 1,92 mV and its mistakes 192 and 1920 mV; tarkistus-2 3,0 V and mistake 15 V; exit ticket 0,15 A and 3,5 V. All agree with lesson-answers.py and the text.
- Figures: junction arrows 3 : 2 : 1 in width; circuit potentials A–F right; potential graph to scale (20 px/V), drops placed over R1 and R2, loop path through R2 matches the circuit. Prediction figures (junction-q, circuit-q) do not reveal the answers.
- sim.js implements the stated model (ideal source, wires and voltmeter), the ground shift by a constant, the graph path F → U → A → R1 → B → R2 → E → F; simState carries I1–I3, Vp, VA, VB, VF and U1 for the experiments.
- Each experiment isolates its varied parameter (R3; probe; ground) with the others locked; reveal minimums match the experiments' minimums.
- Every choice item has exactly one correct option; each distractor's feedback names the right reason (same voltage, not same current, in parallel; current not consumed; voltage divides in series only).
- Current law rests on charge conservation in steady state, voltage law on a single-valued potential and energy per charge; both match the glossary and the summary.
- Scope: Kirchhoff with one junction and branching circuits, potential and potential graph, inside the FY6 täsmennys; no internal resistance or simultaneous loop equations.
- Bird safety statement and the arc-flash warning are correct.
