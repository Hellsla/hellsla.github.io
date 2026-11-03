VERDICT: FAIL
CONTENT-HASH: e2630ff9d12af4aa

## Blocking
- exercises/solutions.md:65 (fy7-9-L2-02) — A: the graph reading says the peak is "kolme ruutua ($3 \cdot 0{,}2\,\mu\text{m}$) luvun $1$ oikealla puolella", which is 1,6 µm. The figure's peak (T = 2415 K) is on the gridline at 1,2 µm, one 0,2 µm square right of 1. — Write "yksi ruutu ($0{,}2\,\mu\text{m}$) luvun $1$ oikealla puolella".
- exercises/exercises.json:91 (fy7-9-L3-02) — A: "Kamera näkee parhaiten kappaleet, joiden säteilyn spektrin huippu osuu tälle välille" is false. A hotter black body emits more at every wavelength, which the lesson itself states. Planck band power in 8–14 µm: 383 W/m² at 89 °C and 978 W/m² at 200 °C, so a 200 °C body is seen better. — Drop the sentence, or replace it with a true premise, e.g. "Kameran aallonpituusväli on valittu niin, että tavallisten kappaleiden säteilyn spektrin huippu osuu sille."

## Polish
- exercises/solutions.md:19 (L1-02) — the reasonableness line "samaa suuruusluokkaa kuin uunin sisätila, mikä sopii siihen, että seinät heijastavat aallot" is not a real check. — Compare the result to the microwave band 1 mm–1 m (already there) and drop the cavity remark.
- exercises/solutions.md (L2-03) — three significant figures are justified "kuten lämpötiloissa kelvineinä, 300 K ja 600 K", but 27 °C has two. — Either give 4,8 µm or justify three figures from the 1 °C resolution of the data.

## Checked
- One script recomputed all twelve answers with my own formulas. All match exercises.json and answers.py: 3,19 m; 12,2 cm; 9,44 µm; 9,99·10³ K; 564 THz; 4,01 µm; 2415 K; 4,83 µm; 5796 K; 1,063 mm; 89,1 °C; 3,84·10⁵ km.
- Task figure spectrum-task: the Planck curve at 2415 K peaks at 1200,0 nm with height 1,057 MW/(m²·µm), matching its description. The answer is not given away.
- Every Wien task states the black-body assumption and converts °C to K. L2-04 correctly says "aallonpituudella, jolla taajuus on …", which avoids the frequency-peak trap.
- CMB 2,7255 K (Fixsen 2009) is real data with a source. 1,06 mm is correctly placed in the microwave band. L3-03 lunar ranging: the round trip is halved and the magnitude is realistic.
- All 7-step solutions are complete and solve symbolically first. Conversions are right, and tolerance 0,02 fits the data.
- Hash was the same at start and end.
