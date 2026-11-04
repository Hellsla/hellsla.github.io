VERDICT: FAIL
CONTENT-HASH: 9069a8122f6961ad

## Blocking
- solutions.md fy8-6-L2-06 Järkevyys — "Suoran jatke … ja sen $h$ on lähimpänä hyväksyttyä arvoa" is false (A): Eero is −4,5 % and Salla +3,65 %, so Salla's value is the closest. b) is answered only in Järkevyys. — Delete the clause. In Vastaus, answer b) and add: "Sallan arvo osuu sattumalta lähemmäs, koska hänen ylimääräinen noin $0{,}16\,\text{V}$ kumoaa osan siitä, että kynnysjännite on yleensä noin $0{,}1\,\text{V}$ pienempi kuin $\tfrac{hf}{e}$. Lähellä taulukkoarvoa oleva tulos ei todista lukutapaa oikeaksi; suoran jatke ei riipu valitusta virrasta, ja jäljelle jäävä ero poistuu kulmakertoimesta."
- solutions.md fy8-6-L2-07 Vastaus — two errors (A). First, "puolet intensiteetistä tulee fotoneista, joiden energia on välillä 1,91–2,03 eV" is wrong: the half-maximum points bound the band where the intensity is above half its maximum, and that band holds about 76 % of the table's intensity. — Write "intensiteetti on yli puolet maksimista, kun fotonin energia on välillä …". Second, "energia-aukko ei ole tarkka arvo" contradicts L1-04 and the brief, where E_g is a material constant. — Write "energia-aukko on materiaalin ominaisuus, mutta elektronit ja aukot ovat vöissä lämpöliikkeen vuoksi hieman eri energioilla, joten fotonien energiat jakautuvat kapealle välille energia-aukon kohdalle".

## Polish
- exercises.json fy8-6-L2-07 data — a FWHM of 40 nm (0,125 eV) is about twice that of a typical red LED (15–25 nm). — Put the half-maximum points at about 620 and 640 nm.
- solutions.md fy8-6-L3-04 Vastaus — "on aina hieman pienempi kuin $\tfrac{hf}{e}$" → "yleensä", as in the brief. The plan's "h tyypillisesti liian suuri" is not covered and does not match the brief's direction. — Fix the plan.
- solutions.md fy8-6-L2-05 Sijoitus — the raw point (2,00 V; 8,8 mA) is called "suoran piste". — Use the fit's mean point (2,10 V; 14,92 mA), as answers.py does.
- exercises.json fy8-6-L1-07 — this is the same step as L2-01 reversed, one level lower, and L1-08 is not in the plan. — Align the levels or the plan.

## Checked
- One-script recompute of all 20 answers, all equal to answers.py. New answers: 539,1 nm; 6,242·10¹⁶ 1/s; 1,857 V; +3,645 % (Aino and Eero −11,6 and −4,5 %); 0,1251 eV; 6,742·10⁻³⁴ J s (intercept −0,062 → −0,112 V); 486,0 nm (direct 504,1 nm, Δλ 9,5 nm).
- In L3-04 the zero error shifts only the intercept; in L3-05 the line includes b. L1-06 has exactly one correct option.
- The renders are clean. Hash is the same at start and end.
