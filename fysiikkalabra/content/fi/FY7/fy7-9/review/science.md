VERDICT: PASS
CONTENT-HASH: 07ed966810533665

## Blocking

## Polish

## Checked
- Round-1 polish is fixed. Microwaves now make the molecules "kääntyilemään edestakaisin". The Etsi virhe feedback says that $b T$ has the unit m·K², not m. The sim.js header now says 800 K, as the code does. The text and hints use 273,15 K.
- I recomputed everything in one script from my own formulas. c = fλ: 3,0 m and 12,2 cm. Wien: 9,66, 9,44 and 3,62 µm, and 502 nm gives 5773 K (IAU 2015: 5772 K). 900 °C gives 2,47 µm, against 3,22 µm with the wrong °C, and b·900 = 2,61 m·K². 2430 °C gives 1072 nm (mistake 1193 nm). The lava gives 1380 K = 1106,85 °C (mistakes 1380 and 1653,15). All of these match the lesson, inquiry.json and lesson-answers.py.
- Planck curve (my own dense scan): the peaks are 300 K 9660 nm, 3000 K 966 nm, 4500 K 644 nm and 6000 K 483 nm, and λ_max·T = 2,898·10⁻³ m·K every time. The figure "curves" heights 100,1, 40,2 and 13,2 MW/(m²·µm) match its caption, and the figure is to scale.
- Visible share: 300 K ≈ 7·10⁻²² % (so "alle 0,01 %" holds), 800 K ≈ 10⁻⁵ %, 2700 K 7,0 % and 5800 K 43,9 %. sim.js integrates over 380–750 nm and divides by σT⁴. The 1280 px capture agrees.
- The sim finds λ_max from the curve (golden-section search), not from Wien's law, so koe-1 really tests the prediction. Both experiments lock the range and vary T, and every peak they ask for is inside the shown range. simState gives lmax.
- Each prediction, Etsi virhe and check-1 has exactly one correct option. Every distractor's feedback names the right physics with model values.
- The sources are right: an accelerating charge radiates, and a resting or uniformly moving one does not. The spectrum table's band limits are right, and so is the ionising part. Kirchhoff (shiny metal emits less) is right. Stefan–Boltzmann 2⁴ = 16 and the statement that a hotter curve lies everywhere above a colder one are correct.
- The black-body condition and the Kelvin requirement are stated wherever Wien's law is used. The model answers, the exit ticket (⅓) and the summary agree with the theory.
- The hash was the same at the start and at the end.
