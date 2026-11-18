VERDICT: PASS
CONTENT-HASH: 2c79b025b43f5d01

## Blocking
- none

## Polish
- none

## Checked
- The lesson changed twice while I was reviewing it (6762f2ae… → c3f5dc6c… → 2c79b025…: commits 87bff84aaa feedbacks, 4d6b371f72 lesson-answers clean-up). I reviewed it again against the current files, and the hash is the same at the end.
- Pohdinta retrieval prompt (inquiry.json:28): neon is the atom that lases in a helium-neon laser, and 633 nm is a transition between atomic levels. The round-1 finding (atomic levels used for a diode laser) is resolved.
- Both feedbacks (l. 33 correct option, l. 37 "energy of upper level" distractor) now say $633\,\text{nm}$ and $\approx 1.96\,\text{eV}$, which matches the prompt. In the packet's diff they still said 650 nm / 1.91 eV, but that was already fixed on disk.
- Recomputed with h = 6.626e-34 J s, c = 2.998e8 m/s, e = 1.602e-19 C: 633 nm gives 1.959 eV. `kert-633-eV` = 1.958921 agrees. The stale `kert-656-eV` / `kert-650-eV` keys are gone, and no text refers to them.
- Assessment: exactly one correct option ($hf = E_2 - E_1$). The upper-level distractor is wrong, and its feedback gives the right reason. The same-direction distractor's feedback (spontaneous emission goes in random directions; "light that atoms emit by themselves spreads in all directions") is right and fits "returns by itself" in the prompt.
- Consistency: the worked example (lesson.md l. 281, 322: 1.96 eV, 633 nm, 1.0 mW) and the He-Ne photo caption (633 nm) agree with the retrieval item.
- Other numbers in lesson-answers.py that this delta touches still print unchanged (mis-650 1.91 eV, ex-lambda 632.65 nm).
