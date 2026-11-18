VERDICT: PASS
CONTENT-HASH: 719473bcd792b302

## Blocking

## Polish
- The prompt "$3{,}0\,\textsf{l} 100\,\text{kPa}$:n paineessa" puts two quantities in one math span with no word between them. It reads better as "$3{,}0\,\textsf{l}$ heliumia $100\,\text{kPa}$:n paineessa" or with "ja".
- The comment in lesson-answers.py still says "helium balloon ... squeezed", but the task now uses a piston cylinder. Update the comment so it matches the task.

## Checked
batch delta review: the Kertaa Boyle choice was rewritten as a piston cylinder, and it now holds 150 kPa realistically. The prompt states that temperature and the amount of gas stay constant, which is the condition Boyle's law needs. I recomputed p₂ = p₁V₁/V₂ = 100 · 3,0/2,0 = 150 kPa. Exactly one option is correct (150 kPa). Each distractor's feedback names its real error: 67 kPa is the inverted ratio (100 · 2,0/3,0 = 66,7), 100 kPa assumes pressure stays constant, and 200 kPa treats the volume as halved instead of using the ratio 1,5. The lesson-answers.py values kertaus-p2 = 150 and kertaus-kaanteinen = 66,67 agree with my recomputation. The lesson.md change is presentation only.
