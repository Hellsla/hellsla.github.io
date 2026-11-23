# Työjono 24 osa 8: FY8, ennen ja jälkeen

Jokaisessa kuvassa vasemmalla nykyinen sivu (`main`), oikealla uusi kuva samalla sivulla; sticky-palkki ja valikko piilotettu.
Tiedosto `<luku>_<nimi>_<kieli>_<leveys>.webp`: kielet `fi`, `en`, `fi-easy`, leveydet 360 px (2× tarkkuus) ja 1280 px.
55 kuvaa (luvut fy8-1…fy8-16): 330 kuvaa. FY8:lle ei ole koe- eikä Sovella-kuvia vaihdettavana (`fy8-sovella/fy8-s1-levels` on kuvaaja, ennallaan).
Kuvatiedostot `assets/pics/fy8/` (55 uutta WebP, 1,6 Mt), asettelu `lessons/FY8/ASETTELU.tsv`.

Ennalleen: 26 kuvaa, jota PAATOS.txt ei piirtänyt uudelleen (kuvaajat ja taulukot), ei käsin liimattuja SVG:itä FY8:ssa.

Huomiot:
- Kuvat on suurennettu kuvankäsittelyllä (PAATOS.txt 18.11.: Lanczos ja kevyt terävöinti, ~1,57 Mpx). Sivulla reunat ovat hieman pehmeämmät kuin vektorikuvassa; vakavaa pehmeyttä ei havaittu kaappauksissa (ydin, beeta, string, ketju tarkistettu).
- `fy8-11/ketju` ja `fy8-16/laajeneminen`: paketin ASETTELU.tsv:ssä siirtosarakkeessa `{"union": true}`, jota `figimage.py convert` ei tunne (ValueError). Jaettua koodia ei muutettu; avain poistettiin paketin kopiosta. Kuvan paikka (x, y, leveys, korkeus) ja merkinnät ovat rivin ja figures.py:n mukaiset, ja merkinnät `g = 0, 1, 2` sekä `ennen`/`myöhemmin` näkyvät valkoisella alueella kuten PAATOS.txt kuvaa.
- `ilman taustaa` (`figimage.py flat`): `fy8-5/string` [6], `fy8-12/gm` [4]; muilla rivillä ei merkintöjä ilman taustaa; kaikki indeksit ovat kuvan todellisia merkintöjä.
- viewBox-ylitykset (ASETTELU.tsv:n rivin ylitys figuurin alueesta, yksikköä; 1 yksikkö ≈ 0,69 px 1280 px:llä kapeassa kuvasarakkeessa): 37 riviä, suurimmat
  `fy8-15/valittaja` oikea 18,6 ja ala 21,8 (≈ 13 ja 15 px); `fy8-7/cavity` ala 17,2; `fy8-1/energia` ala 14,7; `fy8-5/string` ala 13,0; `fy8-8/isotopes` ala 12,5;
  `fy8-12/gm` ala 11,8; `fy8-15/beeta` ala 11,8; `fy8-11/ketju` oikea 11,5. Loput ala 0,5–11,2, osa sivuilta 0,5–2,5.
  Opettaja 2026-11-22: ylityksiä ei rajata. Poikkeus: `check_layout.py` (`svg-image`, sivusuuntainen ylitys enintään 3 px) kaatui kahteen kuvaan, joten `fy8-15/valittaja` (oikea 18,6 yks.) ja `fy8-11/ketju` (oikea 11,5 yks.) leikattiin oikean reunan tausta-kaistalta (viewBoxin ulkopuolella oli vain taustaa; näkyvä kuva ei muutu); rivien leveys 618,6→600 ja 588,2→576,7. Näiden kahden kuvan `approve-figures` ajetaan uudelleen vasta opettajan luvalla.
- Kaappauksissa kuvaajat (esim. `fy8-4/buildup`, satunnaispisteet) eivät kuulu tähän; vain asettelun 55 kuvaa on mukana.
