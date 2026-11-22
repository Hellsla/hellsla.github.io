# Työjono 24 osa 6: FY6, ennen ja jälkeen

Jokaisessa kuvassa vasemmalla nykyinen sivu (`main`), oikealla uusi kuva samalla sivulla; sticky-palkki ja valikko piilotettu.
Tiedosto `<omistaja>_<nimi>_<kieli>_<leveys>.webp`: kielet `fi`, `en`, `fi-easy` (koe vain `fi`), leveydet 360 px (2× tarkkuus) ja 1280 px.
79 kuvaa (75 lukukuvaa, `fy6-koe/fy6-k1-switch`, `fy6-k3-circuits`, `fy6-k6-setup`, `fy6-sovella/fy6-s2-circuit`): 462 kuvaa.
Kuvatiedostot `assets/pics/fy6/` (79 uutta WebP, 1,6 Mt, pisin sivu ≤ 1600 px), asettelu `lessons/FY6/ASETTELU.tsv`.

Ennalleen: PAATOS.txt:n 9 "alkuperäinen pidetään" -kuvaa (`fy6-1/hero`, `fy6-1/virhe-kaavio`, `fy6-3/measure-circuit`, `fy6-3/wire`, `fy6-4/parallel`,
`fy6-8/model`, `fy6-9/latauspiiri`, `fy6-sovella/fy6-s1-circuit`, `fy6-sovella/fy6-s3-field`), 5 kuvaajaa (ei piirretty uudelleen) ja käsin liimattuja SVG:itä FY6:ssa ei ole.

Huomiot:
- `fy6-11/abc` ja `fy6-15/askel`: paketin `{"nobg": [...]}` siirretty sarakkeeseen `ilman taustaa` (kaikki merkinnät, opettajan kommentti "taustavärit pois"); `fy6-11/abc`: merkintöjen siirrot (2, 3) ennallaan.
- `fy6-15/luokat`: PAATOS.txt: suojausluokan III tunnuksesta puuttuu numero III (vinoneliö tyhjä); kuva silti vaihdettu (ei "pidä alkuperäinen" -listalla) — opettajan katsottava.
- `check_layout.py` 1280 px: kaikki 16 lukua + FY6-koe + FY6-sovella OK (fi/en/fi-easy).
- ASETTELU.tsv:n rivin ylitys viewBoxista (57 riviä, 0–12 yksikköä; yli 5 yksikköä melkein kaikki alareunasta). Leikkautuva kaista on joka rivillä pelkkää taustaa (ei-taustapikseleitä 0, taustaksi kuvan kulmapikseli ±24):
  suurimmat `fy6-9/energia` alas 12,0; `fy6-10/kentta` alas 11,7 (+ sivut 1,3/1,7, ylä 1,3); `fy6-8/connections`, `fy6-11/electron`, `fy6-12/kentta`, `fy6-15/askel` alas 11,2;
  `fy6-13/eriste` alas 10,5 (+ sivut 1,3/1,7, ylä 1,3); `fy6-14/suunnat` alas 10,5; `fy6-15/ryhma` alas 10,0. Pienimmät sivu/ylä 0,6–1,9 (`fy6-11/pick-*`).
  Tyhjän reunan rajaus vaatii opettajan luvan, ei tehty. 1 yksikkö ≈ 1 px 600 px leveällä kuvalla.
