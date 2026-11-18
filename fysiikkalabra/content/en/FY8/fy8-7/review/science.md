VERDICT: FAIL
CONTENT-HASH: 6762f2ae91326a1a

## Blocking
- A (quantitative correctness, internal consistency): content/en/FY8/fy8-7/inquiry.json:33 and :37, Pohdinta retrieval "Review: the photon of a transition". The prompt (l. 28) now says a helium-neon laser's neon atom emits at $633\,\text{nm}$, but both feedbacks (the correct option and the "energy of the upper level $E_2$" distractor) still say "the wavelength $650\,\text{nm}$ corresponds to the energy $\tfrac{hc}{\lambda} \approx 1.91\,\text{eV}$". The student is told a wavelength the task does not give, with an energy that does not belong to the He-Ne transition. Fix: in both feedbacks write $633\,\text{nm}$ and $\approx 1.96\,\text{eV}$ (recomputed $hc/\lambda = 1.959\,\text{eV}$; `kert-633-eV` in lesson-answers.py already gives this, and lesson.md l. 281 and l. 322 use $1.96\,\text{eV}$ and $633\,\text{nm}$ for the same laser).

## Polish
- lessons/FY8/fy8-7/lesson-answers.py:37–38 — `kert-656-eV` and its comment "hydrogen 3 -> 2" belong to the version before last; no text uses them any more — remove them, or relabel them if something else still does.

## Checked
- Hash 6762f2ae91326a1a (`--lang en`) at start and end; the delta was judged in context (prompt, the three changed choices, lesson-answers.py, lesson.md He-Ne passages).
- Prompt physics: neon is the lasing atom of a He-Ne laser, the 633 nm line is an atomic level-to-level transition, so the round-1 finding (a diode laser described with atomic levels) is resolved.
- Recomputed with h = 6.626e-34 J s, c = 2.998e8 m/s, e = 1.602e-19 C: 633 nm → 1.959 eV, 650 nm → 1.908 eV, 656 nm → 1.890 eV; `kert-633-eV` agrees.
- Exactly one correct option ($hf = E_2 - E_1$); the "energy of upper level" distractor is wrong and its feedback names the reason correctly; the same-direction distractor's feedback (spontaneous emission in random directions) is right and fits "returns by itself" in the prompt.
- Consistency with the worked example (1.96 eV, 1.0 mW, 633 nm) and the He-Ne photo caption: agree once the feedback numbers are fixed.
