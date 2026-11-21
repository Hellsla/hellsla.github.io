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

Huomiot (opettaja hyväksyi suositukset 2026-11-21, koordinaattorin viesti; piirroksia ei muutettu):
- `fy4-2/strobe`: otsikon "hidastuva liike" siirto muutettu `{"3":[0,9]}` → `{"3":[0,3]}`, jotta se ei mene $\overline{v}$:n päälle (`check_layout.py` OK).
- `fy4-13/virhe`: tyhjä reuna rajattu kuvatiedostosta (1552 × 588 px), rivin laatikko = viewBoxin sisälle (0; 2,6; 600 × 227,4); `check_layout.py` OK.
- `fy4-7/hero`: hyväksytty sellaisenaan: laatikko ylittää alas 16,3 yksikköä, alareunasta leikkautuu ~3 % ei-taustapikseleistä; "1/4 h taustaväri pois" toteutettu (`ilman taustaa` [3, 4]).
- Muut rivit ylittävät viewBoxin enintään 20 yksikköä, ja leikkautuva osa on pelkkää taustaa (`check_layout.py` OK).
