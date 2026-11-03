VERDICT: FAIL
CONTENT-HASH: e6b0231aeaa552c8

## Blocking
- lesson.md:251 — B: "Fotonin energia elektronivoltteina on sama luku kuin kynnysjännite voltteina" holds only if $eU_\text{k} = hf$ exactly; the sentence before it says the measured 1,88 V is below the 1,97 V of $hc/(e\lambda)$, so the text contradicts itself — write "on likimain sama luku" (or "elektronin saama energia elektronivoltteina on sama luku kuin jännite voltteina").

## Polish
- lesson.md:202 (lessons/FY8/fy8-6/figures.py:87) — the spectrum figure draws and captions the laser diode line as about 2 nm wide; the text, glossary and exit-ticket.json:7 say about 1 nm — use one value (1–2 nm is fine, but say the same everywhere).
- inquiry.json:337 (siirto, Järkevyys) — "pitäisi olla hieman lyhyempi, koska kynnysjännite on noin 0,1 V pienempi … tyypillisesti noin 940 nm": with a 0,1 V offset $\lambda \approx 1240 : 1{,}40 \approx 890$ nm; 940 nm corresponds to only 0,02 V — soften to "hieman lyhyempi" without tying 940 nm to the 0,1 V figure.
- inquiry.json:59, :91 — "virtaa kulkee vasta, kun jännite riittää fotonin synnyttämiseen" makes photon creation the gate of conduction; the lesson's energy argument is fine (C), but "energian säilymisen vuoksi elektronin on saatava vähintään likimain fotonin energia" would avoid the reversed causal picture.
- exit-ticket.json:3 — "vähintään kytkettävä" with a model answer saying the measured threshold is usually a little lower than 3,06 V; "Arvioi kynnysjännite" avoids the contradiction.
- lessons/FY8/fy8-6/lesson-answers.py:56 — stale comment "0,02 / 0,24 / 1,37" for 1,70/1,80/1,90 V; the code gives 0,011 / 0,188 / 1,98 mA (the inquiry text uses the right 0,19 mA).

## Checked
- Six LEDs: f, hc/(eλ), offsets −0,06…−0,12 V; LSQ fit k = 4,054·10^-15 V s, b = −0,050 V, h = 6,49·10^-34 J s (−2,0 %): figure, table, interpret answer and mistakes 4,05e-15 and 1,22e-6 agree.
- Sim model I = (s/R)ln(1+e^{(U−U_k)/s}): koe-1 currents 17,8/13,9/11,1/0,11/≈0/0 mA; koe-2 table and extrapolation 1,88 V (five-point fit 1,879 V); mistake 1,70 V.
- Experiments isolate the varied parameter (U locked in koe-1, λ in koe-2); simState gives I.
- Worked example h = 6,515·10^-34 J s, −1,7 %, symbolic first, 3 s.f. justified.
- tarkistus-2: 6,675·10^-34 J s, +0,7 %; mistakes right; siirto 954 nm and mistakes.
- Every prediction/choice has exactly one correct option; distractor feedback correct; tarkistus-1 and virhe options right.
- Band picture, colour vs voltage, offset shifts line not slope; scope within FY8.
- Exercise findings reported separately in exercises/review/science.md.
