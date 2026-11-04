VERDICT: PASS
CONTENT-HASH: 2ec8cb5f6cf6e091

## Blocking

## Polish
- lesson.md:619 (Esimerkki, Tulos) — "kolme merkitsevää numeroa, kuten intensiteetissä 840 W/m²" names only the intensity; the angle 35° has two significant figures (carried over from fi; same polish as the fi review). — Fix: add "kulma 35° katsotaan tarkaksi".

## Checked
- Simplification against the passed fi version: inquiry.json, exit-ticket.json and lesson.md have the same structure, correct flags, experiment initial/locked/vary/measure keys and the same numbers in every string; the eight inline figures are geometrically identical to fi.
- The split sentences keep every condition: Malus only for polarised light and an ideal polariser, halving only in the first polariser, Brewster's angle from the normal with n₁ the medium of incidence and reflection, reflected light polarised parallel to the surface and perpendicular to the plane of incidence.
- Added explanations are correct: "intensiteetti on teho pinta-alaa kohti", "eriste on aine, joka ei johda sähköä", "absorboi eli imee itseensä", the analysaattori definition.
- One script recomputed every number: Malus 0,75/0,50/0,25; Brewster 53,1°/36,9°/56,3°; worked example 281,8 → 282 W/m²; ennuste 46,7/37,5/12,5 % and the linear 33,3 %; koe-1 37,5 % with mistakes 75/43,3/33,3; koe-2 12,5 %; virhe 25 W/m²; siirto 2,128 m (1,203/1,279); tarkistus-2 2,066 mW (3,214/1,033/2,934); exit ticket 56,3°.
- mittaus: least-squares fit A = 360,72 lx, B = 14,64 lx, ΔA = 2,37 lx as in the text; background symbol E_t used consistently.
- Each choice item has exactly one correct option and every distractor's feedback is right; the explain model answers and criteria match the theory.
- Sim strings (lang/fi-easy.json sims.fy7-15) equal the fi readout.
