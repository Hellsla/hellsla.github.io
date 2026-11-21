# Työjono 24 osa 4: FY4, ennen ja jälkeen

Jokaisessa kuvassa vasemmalla nykyinen sivu (`main`), oikealla uusi kuva samalla sivulla. Tiedosto
`<kuvan id, / → _>_<kieli>_<leveys>.webp`: kielet `fi`, `en`, `fi-easy`, leveydet 360 px (2× tarkkuus) ja 1280 px.
72 kuvaa × 3 kieltä × 2 leveyttä = 432 kuvaa. Kuvatiedostot ovat `assets/pics/fy4/` (WebP, 72 tiedostoa, 1,8 Mt, pisin sivu
1600 px), asettelu `lessons/FY4/ASETTELU.tsv`; merkinnät ovat edelleen `figures.py`:n LaTeX-`foreignObject`eja.

Ei tässä PR:ssä:
- Kolme kuvaa, jotka eivät ole luvun kuvia vaan koe- ja Sovella-sarjan: `fy4-koe/fy4-k1-fbd`, `fy4-koe/fy4-k3-fbd`,
  `fy4-sovella/fy4-s3-collision`. `figimage.code_of` ei tunnista omistajaa `fy4-koe`/`fy4-sovella` (jaettu tiedosto), joten
  ne jäävät ennalleen. Kuvapaketin 75 kuvasta tässä on 72.
- 11 kuvaajaa ja ohitettua kuvaa (`PAATOS.txt`) ennallaan. Käsin `lesson.md`:hen liimattuja SVG:itä FY4:ssä ei ole.

Huomiot (piirroksia ei muutettu):
- `fy4-2/strobe`: opettajan siirtämä otsikko "hidastuva liike" (`{"3":[0,9]}`) menee 3–4 px päällekkäin merkinnän $\overline{v}$
  kanssa (`check_layout.py` svg-text, kaikilla kielillä, 360 ja 1280 px).
- `fy4-13/virhe`: rivin laatikko ylittää viewBoxin (oikealle 13,4, alas 20,0, vasemmalle 5,2 kuvan yksikköä; 1280 px:llä
  `svg-image` 6 px, `check_layout.py` FAIL). Leikkautuva osa on pelkkää taustaa, piirros ei leikkaudu.
- `fy4-7/hero`: laatikko (12,4; 17,3; 1188,1 × 599,0) ylittää viewBoxin 0,5 px oikealle ja 16,3 alas; alareunasta leikkautuu
  noin 3 % kuvan ei-taustapikseleistä (kuvitusta, ei tyhjää), vasempaan ja yläreunaan jää 12 ja 17 yksikön kaista ilman kuvaa.
  Opettajan huomio "1/4 h taustaväri pois" toteutettu (`ilman taustaa` [3, 4]).
- Muut rivit ylittävät viewBoxin enintään 20 yksikköä, ja leikkautuva osa on pelkkää taustaa (`check_layout.py` OK).
