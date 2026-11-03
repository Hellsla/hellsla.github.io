VERDICT: PASS
CONTENT-HASH: f2e1fe37fdab7ce1

## Blocking

## Polish
- lesson.md:179 and inquiry.json:403 (siirto, Periaate): "virtalain mukaan lähes koko virta kulkee johdinta pitkin" cites the wrong law. The bird's current is tiny by Ohm's law: millivolts across a large resistance. The current law only adds the currents up. Fix: "Ohmin lain mukaan linnun kautta kulkee häviävän pieni virta, joten virtalain mukaan lähes koko virta jatkaa johdinta pitkin".
- inquiry.json:457 (tarkistus-2, Järkevyys): the check says "napojen välinen jännite on edelleen 9,0 V", so it assumes that A is the plus pole. The prompt does not say so. Fix: say it in the prompt, or check with U_AB.
- inquiry.json:19 (hook): "jännite maahan nähden on kymmeniä kilovoltteja". For 110–400 kV lines the phase-to-earth voltage is about 64–230 kV. Fix: "kymmeniä tai satoja kilovoltteja".
- lesson.md, Potentiaali ("nousee … lähteen jännitteen verran"): this holds for an ideal source, and only the sim box says so. C here; a short "(ideaalinen lähde)" would help the later internal-resistance chapter.

## Checked
- One script recomputed the sim on load (20 Ω, 0,30 A, 3,0 V, 6,0 V, 0,20 A, 0,10 A), the koe-1 rows at R3 = 30, 60 and 120 Ω (I2 + I3 = I1 in every row), koe-3 (3,0 V and −6,0 V), the worked example, siirto (1,92 mV; its mistakes of 192 and 1920 mV are diagnosed right), virhe, tarkistus-2 and the exit ticket. All agree.
- Figures: the junction (current arrows in proportion), the circuit's potentials at A–F, and the potential graph (to scale, 20 px/V).
- sim.js implements the stated model: the ground shift, the graph path through R2, and simState keys for every experiment. The model box states the ideal source, wires and voltmeter.
- Each experiment isolates its varied parameter (R3, probe, ground), and the right parameters are locked.
- In every choice item exactly one option is correct, and each distractor's feedback gives the right reason.
- The current law rests on charge conservation in steady state, and the voltage law on a single-valued potential and energy. Both agree with the glossary.
- The bird's safety and the arc-flash warning are correct.
