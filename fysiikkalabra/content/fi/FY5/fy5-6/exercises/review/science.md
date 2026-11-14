VERDICT: PASS
CONTENT-HASH: 63025e53f5a57e21
SCOPE: delta added-exercise from 1ae57cce87a7a6fc base 81db4a6fd727

## Blocking

## Polish
- exercises.json (L1-11 ja L1-05) — molemmissa luotain kiertää Kuuta lähes samalla säteellä (1840 km ja 1847 km). Toistoa ei ole, koska L1-05 kysyy ratanopeutta ja L1-11 kentän voimakkuutta taulukkoarvolla.

## Checked
- Hash oli sama alussa ja lopussa. Kierros 6: tarkistin kierroksen 5 korjaukset. Diffissä muuttuivat vain L1-11:n unit ja vihje sekä L1-10:n järkevyystarkistus.
- exercises.json:136 (L1-11): unit on nyt "m/s²" ja vastaa tehtävää. g = γM/r² = 6,674·10⁻¹¹·7,346·10²²/(1,840·10⁶)² = 1,448 m/s² → 1,45, kuten answers.py:ssä.
- L1-11: Kuun massa on mafy-arvot.tsv:n VERIFIED-riviltä. Toleranssi 4 % kattaa myös arvon 7,35·10²² kg (1,449 m/s²). Vihje on yksikössä, koska haettava arvo on vain massa.
- L1-10: "alle tuhannesosa" on oikein, koska 5,93·10⁻³/9,81 = 6,0·10⁻⁴. Vastaus 5,934 mm/s² → 5,93 on ennallaan.
- L2-08: √(5250/88) = 7,724 → 7,7, ennallaan.
- Kaikkien kolmen kieliversion answer, unit ja tolerance ovat samat.
