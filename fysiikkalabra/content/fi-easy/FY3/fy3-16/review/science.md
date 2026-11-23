VERDICT: PASS
CONTENT-HASH: 989af167e9a36da4

## Blocking

## Polish
- lesson.md:331 (Tiivistelmä): $t = sm/(UA\Delta T)$ appears here without its conditions. The Kaava section states them (inside at $0\,{}^\circ\text{C}$, contents already at $0\,{}^\circ\text{C}$, all wall energy melts ice), and the worked example shows the time changes once warm drinks are added. Fix: add "kun sisällä on $0\,{}^\circ\text{C}$ eikä muuta lämpöä tule".
- lesson.md:231 (step 4): the case where the energy is more than enough is not written out (all the ice melts, then the water warms above the melting point). The guardrail asks for all three cases. Step 3 implies it, but stating it in one clause would make it exact.
- inquiry.json kayra: pred-1 says the bag holds "jääpussi ja juomia", but the curve after the plateau was computed for 1.0 kg of water only ($C \approx 4190\,\text{J/K}$; my recomputation matches to 0.1 px). The plateau is not affected. Fix: say the drinks are left out, or say "1,0 kg jäätä" in pred-1 as well.
- lesson.md:103 "Lähde on joko teho …": the source is the energy $Pt$ delivered at power $P$, not the power itself. Suggest "teholla $P$ tuleva energia $Pt$".
- lesson.md:131 "Seos kestää … kuumuutta": glycol raises the boiling point only a little; the main reason the coolant does not boil is that the circuit is pressurised. This is fine at the C level; optionally soften it to "kiehuu hieman korkeammassa lämpötilassa".

## Checked
- One Python run recomputed every number in lesson.md, inquiry.json, exit-ticket.json and lesson-answers.py from the task data: example 41 900 J, 33,6 W, 2,4 h (and 2,8 h without the drinks), 19 K/h; sauna 67/452 kJ; mixing 126 kJ, 63 kJ, 0,19 kg; check-2 213→210 kJ; exit ticket 175,5 kJ; siirto 64,9 s. All agree.
- The theory graph is to scale: $t_0$ = 2,41 h, the exponential rise with $\tau = C/UA$ at 1,5 kg of water fits the plotted points. The Tutki graph is to scale: $t_0$ = 3,68 h.
- Table rows ($UA = 0{,}90$ W/K): all five durations are correct. pred-2's 2,9 h option is correct; the 2,2 h distractor and its feedback are right.
- Numeric tasks: every mistake value (92,5; 5,55; 14,3; 6,0; 8,4; 56,5; 200; 12,6) matches the error its feedback names, and the tolerances separate them from the answers.
- Every choice item has exactly one correct option, and every distractor's feedback is physically correct (ice conducts heat better than water; the weighted mean is independent of the temperature scale).
- Boundary cases for melting and mixing, net energy transfer, condensation releasing energy, and $Q = cm\Delta T$ used without a phase change: all consistent with the guardrails.
- Cool-bag bars (334/42/335 kJ) are proportional. The cooling circuit's flow direction, $T_2$ going to the radiator and the equal $P$ in and out are correct.
- Scope: $P = UA\Delta T$ (from Lämmön siirtyminen) and $P = c(m/t)\Delta T$ stay within FY3 energy transfer.
- check-3 criteria and model answer: 12,9 % ≈ 13 %, and the mechanism is correct.
