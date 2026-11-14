VERDICT: PASS
CONTENT-HASH: 346b5d0621afee41

## Blocking
None.

## Polish
1. glossary.json (outside the lesson hash, not shown on the page): "huojunta" still says f_h and "Doppler-ilmiö" v_s, v_h and "∓/±"; update to f_H, v_L, v_H and the four cases so any later use matches the lesson.
2. inquiry.json siirto, Järkevyys: "kuulee äänen huojuvan … kaksi kertaa sekunnissa" uses the word of beats for a pitch wobble; write "korkeuden vaihtelevan".
3. lesson-answers.py docstring still names v_s, v_h, f_h (code comment only).

## Checked
Full review (lesson.md, inquiry.json, exit-ticket.json, figures.py, sim-spec.md, sim.js with lang sims.fy5-14). The four Doppler formulas equal MAFY's, each with the right sign and the sentence saying when it applies; conditions stated (air at rest, motion along the line, only one moves, v_L < v). v_L, v_H, f_H, T_H defined where first used and the same in text, figures (v̄_L, v̄_H, T_H, aria text "T H"), sim labels and summary. Beat physics, harmonic series, octave, 17 m-1,7 cm, FFT resolution 10 Hz and Nyquist correct. Recomputed in my own script: worked example 341,10 / 285,78 / 55,32 Hz (+30, -25 Hz), predictions 444/440, 571/520 Hz, lambda 0,765/0,595/0,85 m, error item 586 to 659 Hz, buzzer 2077 (min 1929, r/T mistake 2012) Hz, check 2: 342,9 m/s (mistakes 0,343, 686), beats graph 4,0 Hz (mistakes 2,0, 0,25), exit 3 Hz / 438,5 Hz; all match lesson-answers.py. Sim: arrival-time geometry and spacing (v -/+ u)T0 derived by hand, correct for both cases; simState gives fA, fB, lamA at the experiments' values; tila and f0 locked, u varied; limits in Mallin oletukset. Each prediction has one correct option and its distractor feedback is right.
