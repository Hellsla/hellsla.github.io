VERDICT: PASS
CONTENT-HASH: b2e495e2487ce941

## Blocking

## Polish
- lesson.md:47 (Geiger caption) — the caption says the counter counts "ionisoivia hiukkasia", while the Aktiivisuus paragraph now says "ionisoivista hiukkasista ja fotoneista". For consistency the caption could say "hiukkasia ja fotoneja". This is not an error, because the paragraph states it correctly.
- lessons/FY8/fy8-9/lesson-answers.py:71 — the comment says "97,62 MBq", but 550 · 0,5^(20,0/8,02) = 97,646 MBq. The comment should say 97,65. It is a comment only, and the rounded 97,6 is correct.

## Checked
- The detector paragraph now says the counter counts pulses from ionising particles and photons that hit the sensor, plus background. This is right for a GM tube (α, β and γ). "Säteilykvanteista" no longer appears in lesson.md, inquiry.json or the lesson code.
- Caption: the pulse rate is proportional to the activity after the background is subtracted, with a fixed geometry. This is now the right condition (B fixed), and it agrees with the paragraph's background sentence and with the exercises' net counts.
- Worked example: 20,0/8,02 = 2,4938, (1/2)^2,4938 = 0,17754, and 550 · 0,17754 = 97,646 MBq, which rounds to 97,6 MBq. That is three significant figures, as the Tulos stage states. The Tulos and Järkevyys stages already used 97,6, so the chain now agrees with them. The reasonableness check (between 138 and 69 MBq) holds.
- The hash was b2e495e2487ce941 at the start and at the end.
