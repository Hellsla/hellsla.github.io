VERDICT: PASS
CONTENT-HASH: fd4eb60f56237477

## Blocking
- (none)

## Polish
- (none)

## Checked
- Round 3. Situation C (exercises.json:98) is now a 500-turn coil around the iron core of a large electromagnet with constant current, with 8,0 mWb per turn. This is realistic: about 1 T over a core of about 80 cm² (9 cm × 9 cm), below iron's saturation at about 1,5–2 T. A bar magnet is no longer claimed to give this flux.
- Physics: the current is constant and the coil does not move, so ΔΦ = 0 and e_C = 0. The task states the condition ("virta on vakio"), and solutions.md gives the same reason.
- The trap works again. The wrong rule "e from the flux itself" gives N·Φ = 500 · 8,0 mWb = 4,0, above B's 3,0 V, so C moves to the end. That matches the new solution sentence ("C siirtyy väärin järjestyksen loppuun").
- Recomputed: A 1,2 V, B 3,0 V, C 0, D 0,60 V, E 2,0 V. The order C, D, A, E, B matches `order`, `answer` and the answers.py comment.
- The forgotten-N check still holds: A 6,0 mV and B 60 mV sit straight after C. Järkevyys (E changes fastest, 2,0 Wb/s; B has the largest voltage) is correct.
- Notation matches the brief, and the rest of the chapter's answers are unchanged and within tolerance.
- Text only, not rendered: the inline chains are short (estimated under 250 px).
- The hash was identical at the start and at the end.
