VERDICT: PASS
CONTENT-HASH: bee0a2a95499a900
SCOPE: delta added-exercise from 1ae57cce87a7a6fc base 81db4a6fd727

## Blocking

## Polish
- solutions.md (L1-11, Vastaus) — perustelu "kolme merkitsevää numeroa kuten taulukon massassa" ei pidä, koska massassa 7,346·10²² kg on neljä merkitsevää numeroa. Rajoittava tieto on korkeus 100 km. — Nimeä perusteluksi korkeus.
- solutions.md (L1-10, Järkevyys) — "noin tuhannesosa" putoamiskiihtyvyydestä on karkea arvio: 5,93·10⁻³/9,81 ≈ 6·10⁻⁴. — Kirjoita "alle tuhannesosa" tai "noin 0,06 %".
- exercises.json (L1-11 ja L1-05) — molemmissa luotain kiertää Kuuta lähes samalla säteellä (1837 km ja 1847 km). L1-11 kysyy kiertoaikaa ja vaatii taulukkohaun sekä kaavan r = R + h, joten tehtävä ei ole toisto. Ne ovat kuitenkin lähellä toisiaan.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-10, L1-11 ja L2-08 (kierros 3).
- L1-10: r = (147,1 + 152,1)/2 milj. km = 1,496·10¹¹ m, ja a = γM/r² = 5,934·10⁻³ m/s² = 5,93 mm/s². Tulos on sama kuin answers.py:ssä. Tämä on eri lasku kuin L1-08:ssa (v = 2πr/T), joten toistoa ei ole.
- L1-11: Kuun massa 7,346·10²² kg ja säde 1737 km ovat docs/mafy-arvot.tsv:n riveiltä 60–61, joiden tila on VERIFIED. r = 1,837·10⁶ m, v = 1634 m/s ja T = 7065 s = 117,8 min, sama kuin answers.py:ssä. Toleranssi 4 % sopii taulukkotehtävään.
- L2-08: √(5250/88) = 7,724 → 7,7, ja rajoittava tieto on 88 milj. km. Ratkaisu sanoo, että ympyräradat ovat kuviteltuja ja että todellinen rata on ellipsi.
- Kuvan radat lukemat (147,1–152,1 ja 88–5250 milj. km) ovat kuvan tekstissä ja alt-tekstissä. Ellipsit on piirretty mittakaavassa.
- Fysiikka on luvun mukaista: gravitaatio on ainoa voima, r = R + h, ja merkinnät γ, M ja r ovat luvun.
