VERDICT: PASS
CONTENT-HASH: 5922d63d970900d2

## Blocking

## Polish
- content/fi/FY5/fy5-11/exercises/solutions.md:15, 25, 129, 219 (L1-02, L1-03, L2-06, L3-05) — These Kaava steps keep the old inline "josta"/"ja suhde" form, while the rest of the set now uses aligned blocks. The physics is right; only the form is uneven.

## Checked
- Delta: the Kaava steps of L1-05, L1-08, L2-01…L2-05, L2-07, L3-02…L3-04 and L2-10 are now aligned blocks. They start from $s = vt$ and the echo path ($s = 2d$, $2L$, $3L$), the Huygens path difference $s = d\sin\alpha$, the law of reflection $\beta = \alpha$, $v = f\lambda$ with the stated condition $\lambda = b$, and the constant-offset model $t = 2d/v + t_0$. Each ends at the form the Sijoitus uses. Every rearrangement is algebraically right. The packet's diff collapsed the line breaks; I read the file on disk.
- L2-05: $t_0$ cancels in $t_4 - t_1$, so the method is right.
- L3-03: the path to the far end, back and to the far end again is $3L$.
- L2-10: $\lambda' = v/(2f) = \lambda/2$ holds because the task assumes $v$ is constant.
- One script recomputed every changed task. L1-05 240,1 m, L1-08 48 ms, L2-01 0,75 s, L2-02 5,0 m/s, L2-03 188,65 m, L2-04 381,1 Hz, L2-05 342,9 m/s, L2-07 32°, L3-02 22,02°, L3-03 4,5 s, L2-10 3,0. All match the Sijoitus lines and answers.py, which are unchanged.
- The paragraph splits in L1-06, L2-06, L3-01, L3-04 and L3-05 change no wording. The diffraction claims in them are unchanged and right: bending depends on $b/\lambda$; the AM wave bends round the mountain, while FM, TV and light leave a shadow.
- The changes to the figure fy5-11/rako-ruudukko and to the captions in exercises.json were approved by the teacher, and the values L2-09 and L2-10 read from the figure are unchanged.
- Hash 5922d63d970900d2 at the start and at the end.
