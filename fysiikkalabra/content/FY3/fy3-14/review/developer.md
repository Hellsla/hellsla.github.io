VERDICT: DONE

Round 2. All checks ok (lint, latex, build, sims 63 pass, inquiry 60, layout).

- exit-ticket.json: every calculation in items 1 and 3 is LaTeX with units (`\tfrac`, `\text`, `{,}`).
- lesson.md: example stage 4 has a substitution row with units (2100 J/(kg·K) · 0,050 kg · 8,0 K + 334 000 J/kg · 0,050 kg) before 840 J + 16 700 J.
- inquiry.json: koe-1 prompt now says to bracket with the slider (step 0,5 °C) and then calculate the exact temperature (26,6 °C). The sim's howto box now holds the case sentences and the thermometer behaviour that left the readout.
- sim.js: readout loses the verdict and "Lämpömittarit nyt" lines (three lines remain). In case 1 after the ice is gone, the "vesi" label shows the mixed temperature (equals T_f at the end; simState.TW unchanged). Case 4: cubes are hidden once all the water is frozen.
- tests/sims/fy3-14.json: four readout assertions (indices 38-41) checked the removed prose. Their numbers (T, ice left, kJ values) stay; the case and the 75,3 g / 88,0 g are now asserted from simState (tapaus, meltedG), and the thermometer values from the canvas labels. Nothing weaker in what is verified; the tests were rewritten, not loosened.
