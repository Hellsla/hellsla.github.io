VERDICT: FAIL
CONTENT-HASH: 262607ec813fe5a1

## Blocking
- inquiry.json:144 (sim `calc`) — **B.** It says "$x_\text{B} - x_\text{A}$ on B:n etumatka: se on positiivinen, kun B on edellä" for every case, but in case 1 (koe 1) the bodies meet head-on and B moves in the negative direction. A larger $x$ is not "ahead": this is the replaced error in another form. — Fix: "Lukema $x_\text{B} - x_\text{A}$ kertoo, kuinka paljon suurempi B:n paikkakoordinaatti on, ja se on nolla kohtaamishetkellä. Kun kappaleet liikkuvat positiiviseen suuntaan, se on B:n etumatka."
- inquiry.json:190, 191, 203 (koe 1 hints 2–3 and solution) — **B**, the same error. The separation in the head-on case is called "etumatka" (for example "Etumatka on aluksi 60 m"), but neither body is ahead. — Fix: write "välimatka" or "paikkojen ero $x_\text{B} - x_\text{A}$". Koe 3 can keep "etumatka": both bodies move in the $+x$ direction there.

## Polish
- lesson.md:462 (vt aria-label) — "Hetkeen t = 3,0 s asti pyöräilijä on edellä ja etumatka kasvaa" reads as if the cyclist leads only until 3,0 s. — Fix: "Pyöräilijä on edellä, ja hetkeen 3,0 s asti etumatka kasvaa".
- The en and fi-easy inquiry.json carry the same sentences. Regenerate them after the fix.
- The checker rule higher-line-ahead missed the "positiivinen, kun B on edellä" form.

## Checked
- lesson.md:338 uses the teacher's wording, and "edellä" is limited to motion in the $+x$ direction.
- No other claim that a higher line means "ahead" appears in lesson.md, the figure labels, the exit ticket, sim-spec, sim.js or the sim's readout strings.
- Every other use of edellä, takana and etumatka is in a situation with motion in the $+x$ direction.
- I recomputed every number and all agree:
  - head-on meeting: 12 s, 36 m
  - same-start pass: 6,0 s, 36 m, 2v, gap 9 m
  - example: 8,0 s, 64 m, 16 m/s, other root −2,0 s, 25 m
  - sim cases 1, 4 and 5: 50 m; −10 s; 1,55 s and 6,45 s
  - transfer task: 24 m/s
  - check-2: 6,0 s, with mistakes at 15, 30 and 10 s
- The sim implements the model and states its limits.
- Each choice item has exactly one correct option, and its feedback is right.
- The hash is unchanged from start to end.
