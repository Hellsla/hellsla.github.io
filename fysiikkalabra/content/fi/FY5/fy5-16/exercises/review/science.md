VERDICT: PASS
CONTENT-HASH: dacf6bcb0f4a71eb
SCOPE: delta added-exercise from 9b2ee0bf44613b3e base 81db4a6fd727

## Blocking

## Polish

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-09 ja L2-09 (kierros 3).
- L2-09 käyttää nyt korvatulppia. Kuvasta luetaan 105 dB, ja korvassa taso on 105 − 12 = 93 dB. Siitä n = 8/3 ja t_v = 480 min / 2^(8/3) = 75,6 min. Tulos on sama kuin answers.py:ssä. Vastaus 76 min eroaa siitä 0,5 %, joten se on toleranssin 2 % sisällä.
- Toistoa ei ole: L2-07 (109 dB ilman suojaimia) on eri tehtävä. L3-05 yhdistää etäisyyden ja tulpat, mutta siinä ei lueta kuvaa. Kuvaa scale-tehtava ei käytetä inquiry.json:ssa.
- L1-09: 8 h / 2^(5/3) = 2,52 h → 2,5 h, ero 0,8 %.
- Malli on luvun mukainen: t_v = t₀/2ⁿ, ja tulpat vähentävät korvan tasoa vaimennuksensa verran. Vertailuaikaa ei kutsuta sallituksi tai turvalliseksi ajaksi, kuten ohjeistus vaatii.
- Järkevyystarkistus on oikein: 8 dB on 6 dB:n (120 min) ja 9 dB:n (60 min) välissä. Ilman tulppia aika olisi 4,7 min, ja 12 dB vastaa 2⁴ = 16-kertaista aikaa.
- Kuvan merkit ovat tarkasti kohdissa 90 dB ja 105 dB, ja arvot on kirjoitettu kuvaan. Alt-teksti antaa samat arvot.
