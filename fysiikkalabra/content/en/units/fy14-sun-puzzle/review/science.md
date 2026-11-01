VERDICT: FAIL
CONTENT-HASH: 8e99d0c59ea3fbba

Science review of fy14-sun-puzzle, 2026-11-01 (full review). I recomputed every number, and checked the Kelvin and Curie–Laborde facts in Kragh, arXiv:1609.02834 (full text).

## Blocking
1. **A, `unit.md`, Worked example, *Reasonableness*.** "some hydrogen outside the core mixes in" is the wrong mechanism. The Sun's core is radiative, so there is practically no mixing between the core and the envelope during the main sequence. Fix: "and the burning region slowly grows outwards".
2. **A, `teacher.md`, Common difficulties.** The note blames the old oxygen-16 scale for the gap between Eddington's "1 part in 120" and today's 0.71 %. That is not the cause. A change of mass scale multiplies all masses by almost the same factor, so the fraction stays the same. The cause is that he took helium as "just 4": 4·1.008 against 4 gives 0.79 %, about 1 part in 126. On the chemical scale helium was 4.003, which gives 0.72 %. Fix: "His helium value was rounded to 4; with helium's measured 4.003 (or today's masses) the loss is 0.71 %."

## Polish
1. `unit.md`, *Candidates*: the radium figure "about 200 000 times as much as the same mass of burning coal" holds only for the total heat over the whole decay, with the decay products. The rate per hour is far smaller. Kragh's wording is "about 200,000 times more than the total burning of coal". My own estimate of the total is ≈ 2.6·10⁵. Fix: add "over its whole decay". (B)
2. `unit.md`, *Key idea*: "Quantum tunnelling (George Gamow, 1928) solved this". Name the full story here as fy14-fusion-reactions does: Gamow's tunnelling was for alpha decay, and Atkinson and Houtermans applied it to stars in 1929.
3. `inquiry.json`, `check-explain` model: "A helium nucleus has about 0.7 % less mass than the four hydrogen atoms" compares a nucleus with atoms. Fix: write "A helium atom".
4. `inquiry.json`, Kelvin discussion prompt: "In the 1860s–1890s, Kelvin said … at most a few tens of millions of years". In 1862 his figure was 100 million years. Fix: "from 1862 to the 1890s, Kelvin lowered his limit from about 100 million to a few tens of millions of years".

## Checked
- **Numbers.** Coal: 5350 a (and the mistake values). Contraction: GM²/R = 3.80·10⁴¹ J, so 3.14·10⁷ a, which is 146 times shorter than 4.6 Ga. Fusion: E = 1.27·10⁴⁴ J, so 1.05·10¹⁰ a. The Sun converts 4.26·10⁹ kg/s, with 6·10¹¹ kg of hydrogen fused per second. Mass lost so far: 6.2·10²⁶ kg, 0.03 %. Mc²/L gives 1.48·10¹³ a. The fraction is 0.712 %. The hook ("more than half a million years" of humankind's energy) is right: 6.5·10⁵ a at 590 EJ/a.
- **History.** Helmholtz 1854. Kelvin 1862 (100 Ma) and 1887 (20 Ma). Pierre Curie and Laborde 1903. Eddington in Cardiff, 24 August 1920, and the three quotations. Eddington's life: Plumian professor from 1913, Príncipe 1919, the 1926 book. Oliphant 1934 is cited as the first laboratory fusion, which matches fy14-fusion-reactions.
- **Choices and order.** Exactly one correct option everywhere. The timeline order is correct.
- **Figure.** The log-scale estimates use the same values as the text.
