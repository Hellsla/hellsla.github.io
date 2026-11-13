VERDICT: FAIL
CONTENT-HASH: c95e1237c66d7edf
SCOPE: delta added-exercise from 5cd3571020c4ddc7 base 81db4a6fd727

## Blocking
- fy5-14/exercises/exercises.json (L2-08) — **A** (assessment). The check cannot tell a right answer from a wrong one. The answer is 519 Hz, and the page always accepts at least ±2 % (±10 Hz). It therefore accepts the classic wrong side, 523 + 4 = 527 Hz (1,5 % off), and any beat reading from 0 to 14 Hz. So neither the figure reading nor the higher/lower decision is assessed. No tolerance can fix this. Fix: ask for the number the figure gives, the beat frequency f_h, and keep "which fork is 519 Hz" as the reasoning step in the solution. Alternatively, ask "Kuinka monta hertsiä toisen ääniraudan taajuus poikkeaa 523 hertsistä, ja kumpaan suuntaan?" with a choice for the direction.

## Polish
- lessons/FY5/fy5-14/figures.py (beats_task docstring) — The docstring says 440 Hz and 444 Hz, but the task uses 523 Hz and 519 Hz. The drawn envelope (Δf = 4 Hz) fits both, but the generator should name the task's numbers (guardrail "a figure generator holds the same numbers").
- fy5-14/exercises/solutions.md (L1-10, Vastaus) — "kolme merkitsevää numeroa kuten kuvaajasta luettu taajuus": the reading is exact to the 100 Hz grid lines. Say instead that the peaks lie on grid lines.

## Checked
- L1-10: the spectrum figure has peaks at 200·k Hz (k = 1…5) and its strongest at 400 Hz. The peaks are narrow (σ 9 Hz) and lie on the 100 Hz grid lines, so f₁ = 200 Hz is read exactly. The strongest-peak trap is the intended one, and the solution names it.
- L1-10: the claim that the perceived pitch follows f₁ is correct. Nothing in the figure or its alt text gives f₁ away.
- L2-08: the envelope |cos(π·4t)| has maxima every 0,25 s, so f_h = 4,0 Hz and f₁ = 523 − 4 = 519 Hz (recomputed). The alt text gives the same moments.
- answers.py agrees with exercises.json. The notation f_h = |f₂ − f₁| and f_n = nf₁ is the lesson's.
- The hash was the same at the start and at the end.
