VERDICT: PASS
CONTENT-HASH: 43ce35828e573b26
SCOPE: delta added-exercise from 0712046380ca6300 base 81db4a6fd727

## Blocking

## Polish
- lessons/FY5/fy5-5/figures.py (planeetat) — kuvassa Maan arvo on 9,80 m/s², mutta kurssi käyttää arvoa 9,81 m/s². Lisätyt tehtävät eivät käytä Maan arvoa, joten tämä ei ole kiireellinen.

## Checked
- Hash oli sama alussa ja lopussa. Arvioin vain tehtävät L1-09 ja L2-09 (kierros 3).
- L2-09:n uusi luotain: h = R, joten r = 2R ja g = 24,8/4 = 6,20 m/s². Siitä F = 850 kg · 6,20 m/s² = 5270 N = 5,27 kN, sama kuin answers.py:ssä. Laskin myös toisin, M = g₀R²/γ ja F = γMm/(2R)², ja sain saman tuloksen.
- Periaate on oikea: etäisyys mitataan keskipisteestä, ja kenttä pienenee kääntäen verrannollisesti etäisyyden neliöön. Suhdemuoto g = g₀(R/r)² seuraa luvun kaavasta g = γM/r². Säteen valinta (päiväntasaajan säde, kuten kuvan arvossa) perustellaan.
- Toistoa ei ole: L2-03 ratkaisee korkeuden voimasta Maan gravitaatiolailla, ja L2-04 laskee prosenttimuutoksen. Kumpikaan ei lue kuvan arvoa. Kuvaa planeetat ei käytetä inquiry.json:ssa.
- Merkitsevät numerot: 5,27 kN on kolmen numeron tarkkuudella kuten 24,8 ja 7,15. L1-09: 85 · 3,71 = 315 N → 3,2·10² N, ja rajoittava tieto on 85 kg. Kumpikin vastaus on toleranssin 2 % sisällä.
- Järkevyystarkistukset ovat oikein: pinnalla voima olisi 21,1 kN, ja siitä neljäsosa on 5,27 kN. Marsissa 0,38 · 834 N ≈ 320 N.
