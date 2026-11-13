VERDICT: FAIL
CONTENT-HASH: b0d264e365e5c2be

## Blocking
- exercises.json:48 (L2-09) — A: yksikkö on väärä. Tehtävä kysyy nyt suurinta nopeutta ("Anna vastaus metreinä sekunnissa"), ja vastaus 0,47 on yksikössä m/s, mutta kentässä `"unit"` lukee yhä "N/m". Arvo jäi edellisestä versiosta, jossa kysyttiin jousivakiota. Sivu näyttäisi vastauksen 0,47 N/m. — Korjaa muotoon `"unit": "m/s"`.

## Polish
- answers.py:3 (docstring) — teksti "Mars 3,71 m/s²" on ristiriidassa L1-09:n MAFY-arvon 3,72 m/s² kanssa. Ratkaisu selittää, että taulukoiden arvot poikkeavat hieman toisistaan, joten tämä ei ole virhe.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-09, L1-10 ja L2-09.
- L2-09 ja sen ratkaisu: v_max = 2πA/T = 2π·0,030 m / 0,40 s = 0,471 m/s, josta vastaus 0,47 m/s. Kaava johdetaan luvun kaavoista ½mv_max² = ½kA² ja T = 2π√(m/k). Kaksi merkitsevää numeroa vastaa lukemia A = 3,0 cm ja T = 0,40 s, ja järkevyystarkistus (keskinopeus 0,30 m/s) on oikein.
- L1-09: 2π√(1,00/3,72) = 3,258 s. L1-10: ½·120·0,030² = 0,054 J. Kumpikin vastaa answers.py:tä ja exercises.json:ia.
- Kuva kuvaaja-k on myös Tarkista osaamisesi -tehtävän 2 kuva. lesson-answers.py:n mukaan se tehtävä kysyy jousivakion k massasta 0,25 kg ja jaksonajasta T. L2-09 kysyy nyt nopeutta v_max ja L1-10 energiaa E, joten kumpikaan ei toista tarkistusta. Kierroksen 1 huoli on poistunut.
- Kuvassa x = 3 cos(2πt/0,40) cm, ja huiput osuvat apuviivoille. Alt-teksti antaa samat arvot.
