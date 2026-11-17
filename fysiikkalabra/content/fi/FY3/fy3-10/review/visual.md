VERDICT: PASS
CONTENT-HASH: 719473bcd792b302

## Blocking

## Polish
- [Minor] Kertaa: Boylen laki, kehote — `\textsf{l}` renders as a bare vertical stroke, no longer like the digit 1 (round 1 fixed). At 1280 px "$3{,}0\,\textsf{l}$ $100\,\text{kPa}$:n" reads almost like "3,0 | 100 kPa". The litre convention is project-wide, so no change to it; reword to put a word between, e.g. "Mäntäsylinterissä on heliumia $3{,}0\,\textsf{l}$, ja sen paine on $100\,\text{kPa}$."
- [Minor] Sama kehote, kolmas lause: "tilavuus on $2{,}0\,\textsf{l}$." — the full stop after the bar-like l is easy to miss; the same rewording helps.

## Checked
batch delta review (round 2): own captures of the Kertaa card (#kertaus) with feedback open at 390 px and 1280 px, for the correct choice and for a wrong one (/tmp/claude-0/s/fy3-10-390-0.png, -390-1.png, -1280-0.png, -1280-1.png, from preview/fy3-10.html): the fraction chain aligned, litre unit legible as a unit in the chain, no clipping; the "3,0 : 2,0" colon change is in the feedback of the 200 kPa choice (source diff read, not triggered in a capture).
