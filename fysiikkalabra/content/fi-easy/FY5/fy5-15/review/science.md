VERDICT: PASS
CONTENT-HASH: bbd19d9b0ad3dd8b

## Blocking
None.

## Polish
1. sim-spec.md and lesson-answers.py docstring still write L = 10 dB · lg(I/I₀); glossary.json (outside the hash) too. Equivalent, not student-facing in the lesson; align with MAFY's form when next edited.

## Checked
Full review (fi-easy: lesson.md, inquiry.json, exit-ticket.json, figures, sim-spec.md, sim.js). The change: siirto hint 3 now in MAFY's form, L = 10 lg((I1+I2)/I0) dB = 80 dB + 10 lg(1,25) dB = 80,97 dB, consistent with the answer 0,97 dB (L − L1) and the solution. Law L = 10 lg(I/I0) dB and its solved forms correct; conditions stated where used (point source, no reflections or absorption, independent sources, free field for meter reading as intensity level; dB(A) and sound-pressure level described correctly). Recomputed in one script: worked example 3,98·10⁻³ W/m², P = 5,00 W; koe 1 (P = 50 mW, N = 1) 96,0/90,0/84,0/77,9 dB and 0,995 → 0,249 mW/m²; koe 2 (r = 2,0 m) 90,0/93,0/96,0/100,0 dB; 80+80 → 83,0 dB; 70+60 → 1,1·10⁻⁵ W/m², 70,4 dB; Kaava graph 90,0/84,0/78,0/71,9 dB; error item 3,16·10⁻⁶ W/m² vs 6,5 I0 ≈ 8 dB; transfer 0,969 dB, mistakes 3,01 and 1,76; check 2: 100 (mistakes 1,4, 20); exit 1,0·10⁻⁴ W/m², 84,8 dB; all match lesson-answers.py. Sim computes I = NP/(4πr²), L = 10 lg(I/I0) dB; simState gives ImW and L; koe 1 locks P, N, koe 2 locks P, r. Each prediction and check has exactly one correct option, distractor feedback right; answers, tolerances, keys and mistakes identical in fi, fi-easy and en.
