VERDICT: PASS
CONTENT-HASH: 78caa538200d885a
SCOPE: delta added-exercise from b59e199ba798ddff base 81db4a6fd727

## Blocking

## Polish
- exercises.json (L2-08) — tehtävä lukee kuvasta valokuva saman aallonpituuden λ = 1,5 m kuin Tarkista osaamisesi -tehtävä 2 (lesson-answers.py: tarkistus2, f = 1,8 Hz, v = 2,7 m/s). Kysytty suure (T, kun v on annettu) on eri, joten kyse ei ole toistosta, mutta lukeminen on jo tuttua.
- exercises.json (L1-10) — `kind: data` on väljä merkintä taulukkoarvon hakemiselle. Muutos on valinnainen.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-10 ja L2-08.
- L2-08 on muutettu. Nopeus 3,0 m/s annetaan, ja kuvasta luetaan λ = 2,0 − 0,5 = 1,5 m, jolloin T = λ/v = 0,50 s. Tulos vastaa answers.py:tä ja exercises.json:ia. Kaksi merkitsevää numeroa ja toleranssi 2 % sopivat.
- L2-08:ssa lasketaan v = λ/T valokuvasta eli (x, y)-kuvaajasta, kuten luvussa neuvotaan. Järkevyystarkistus fλ = 2,0 Hz · 1,5 m = 3,0 m/s on oikein.
- L1-10: λ = 5120 m/s / 1000 Hz = 5,12 m. Rautatangon äänen nopeus 5120 m/s on oikea pitkittäisen aallon nopeus ohuessa tangossa. Toleranssi ±4 % on tehtävässä.
- Kuvassa valokuva y = 4 cos(2π(x − 0,5)/1,5) cm, harjat ovat apuviivoilla 0,5, 2,0 ja 3,5 m, eikä λ:aa ole merkitty kuvaan. Alt-tekstissä on samat arvot.
