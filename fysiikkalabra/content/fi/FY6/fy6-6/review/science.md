VERDICT: FAIL
CONTENT-HASH: ba8b7d0172ca4e9b

## Blocking
- inquiry.json:237 (johtopaatos `model`) — **B**: "Yhteinen suure oli virta, joten teho $P = RI^2$ kasvoi resistanssin mukana" holds only when two resistors are compared in the same row, at the same current. In koe-1 the student varies $R_2$ with $R_1 = 4\,\Omega$, and the student's own table shows $P_2$ falling as $R_2$ grows: 9,0 W (4 Ω), 8,0 W (8 Ω), 5,76 W (16 Ω), because $I$ drops from 1,5 A to 0,60 A. The model answer contradicts the data it says it summarises and plants "larger series R always gets more power". — Fix: compare within a row, for example "samalla virralla suuremman resistanssin vastus sai suuremman tehon ($P_2 > P_1$ joka rivillä, jossa $R_2 > R_1$)", and optionally note that raising $R_2$ lowers the common current.
- glossary.json:1938 (term **sähköenergia**, shown for this lesson) — **A**: "käytössä takaisin esimerkiksi lämmöksi" makes heat a form that energy turns into. Heat is energy in transfer (guardrails; FY6 rule "sisäenergiaksi, joka siirtyy lämpönä", never "muuttuu lämmöksi"). It also contradicts the lesson's own correct wording (lesson.md Joulen laki, Kaava). — Fix: "… ja käytössä esimerkiksi sisäenergiaksi, joka siirtyy lämpönä, valoksi tai liike-energiaksi". The term is shared, so check which chapters use it.

## Polish
- lesson.md:171 — "yli tuhat kertaa pienempi" follows from 59 Ω : 0,050 Ω ≈ 1200, not from "kymmeniä ohmeja / sadasosia ohmista" in general (20 Ω : 0,05 Ω = 400). Put the ratio after the numbers.
- lesson.md:210 — "Pienemmällä jännitteellä … teho on pienempi, koska $P = U^2 : R$": add "kun resistanssi pysyy likimain samana". A filament's R falls when it is cooler, and the conclusion still holds.
- inquiry.json:387 (tarkistus-3 model) — "luovuttaa yhtä paljon lämpöä kuin siihen tulee sähköenergiaa" → "yhtä nopeasti", the wording of the theory and the summary.
- sim.js beaker(): the coil glow saturates at 36 W (`P / 36`) but the bar at 72 W. In parallel at 12 V, a 4 Ω and a 2 Ω coil glow equally, although the second has twice the power. Scale the glow to PMAX.

## Checked
- Every number recomputed in one script: Ydinajatus 6,0 W; series 4/8 W and parallel 36/18 W; toaster 58,8 Ω, 3,91 A, cord 0,77 W; example 9,6 W, 4,8 W, 4320 J ≈ 4,3 kJ; siirto 37,2 min and mistakes 2235, 77,6, 447; tarkistus-1 1322/529 Ω; tarkistus-2 12,8 W, 1,6, 320; exit ticket 5,0 A and ×4; kertaus 0,20 A.
- The jako bar chart and the P(I) graph are to scale. The pixel positions match 4, 8, 36, 18 W and 4, 16, 8, 32 W. The steady-state figure is schematic and says so.
- Joule mechanism (collisions → ion vibration → internal energy → heat to the surroundings) and the energy wording are right in the lesson text.
- ennuste-1/2, virhe, tarkistus-1: exactly one option is correct, and each distractor's feedback is right.
- koe-1/koe-2 lock U, R1 and kytkentä and vary R2. The measured keys exist in simState. The circuit drawing is correct for series and parallel (1280 px capture).
- sim.js implements the stated model: ideal source, constant R, no losses, linear ΔT, exact stop at 80 °C. The model box states these limits.
- E for energy follows the FY6 notation outside the battery chapter. The example's sig figs are justified.
