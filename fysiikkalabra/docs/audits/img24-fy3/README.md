# Työjono 24 osa 3: FY3, ennen ja jälkeen

Jokaisessa kuvassa vasemmalla nykyinen sivu (`main`), oikealla uusi kuva samalla sivulla. Tiedosto
`<kuvan id, / → _>_<kieli>_<leveys>.webp`: kielet `fi`, `en`, `fi-easy`, leveydet 360 px (2× tarkkuus) ja 1280 px.
61 kuvaa × 3 kieltä × 2 leveyttä = 366 kuvaa. Kuvatiedostot ovat `assets/pics/fy3/` (WebP, 1,7 Mt), asettelu
`lessons/FY3/ASETTELU.tsv`; merkinnät ovat edelleen `figures.py`:n LaTeX-`foreignObject`eja.

Ei tässä PR:ssä (avoin kohta, koordinaattorin päätös): seitsemän käsin `lesson.md`:hen liimattua SVG:tä, jotka eivät ole
`figures.py`:ssä: `fy3-13/~lesson-2`, `fy3-14/~lesson-2`, `fy3-14/~lesson-3`, `fy3-15/~lesson-2`, `fy3-15/~lesson-5`,
`fy3-16/~lesson-2`, `fy3-16/~lesson-4`. Ne jäävät ennalleen.

Opettajan päätöksen (`PAATOS.txt`) huomiot koskevat mm. `fy3-12/earth-flows` (kuva rajattu eri tavalla kuin alkuperäinen).

`fy3-4_water-column_leikkaus_1280.webp` ja `fy3-12_earth-flows_leikkaus_1280.webp`: vasen nykyinen, keskellä uusi sivulla
(leikattuna), oikealla koko kuvatiedosto ilman merkintöjä, punainen katkoviiva = kuvan (viewBox) reuna. Rivin laatikko
ylittää viewBoxin: water-column 18 px oikealle ja 19 px alas (1280 px:llä), earth-flows 9 px alas; leikkautuva osa on
molemmissa pelkkää paperin väriä, piirros ei leikkaudu.
