# Työjono 24 osa 5: FY5, ennen ja jälkeen

Jokaisessa kuvassa vasemmalla nykyinen sivu (`main`), oikealla uusi kuva samalla sivulla. Tiedosto
`<omistaja>_<nimi>_<kieli>_<leveys>.webp`: kielet `fi`, `en`, `fi-easy`, leveydet 360 px (2× tarkkuus) ja 1280 px.
87 kuvaa × 3 kieltä × 2 leveyttä = 522 kuvaa. Kuvatiedostot `assets/pics/fy5/` (87 uutta WebP, 2,5 Mt, pisin sivu 1600 px),
asettelu `lessons/FY5/ASETTELU.tsv`; merkinnät ovat edelleen `figures.py`:n LaTeX-`foreignObject`eja.
Monivalintojen vaihtoehtokuvat (`fy5-3/opt-*`, `fy5-4/pick-*`, `fy5-4/valitse-a…d`) vaihdettu koko tehtävä kerrallaan.

Ei tässä PR:ssä (94 kuvasta 87):
- `fy5-9/heiluri`, `fy5-17/maapallo`: PAATOS.txt suosittelee alkuperäistä (fysiikan virhe uudessa kuvassa), ennallaan.
- Koe ja Sovella (erikseen, opettajan luvalla): `fy5-koe/fy5-k2-board`, `fy5-k2-fbd`, `fy5-k3-fbd`, `fy5-k5-modes`, `fy5-sovella/fy5-s1-crane`.
- Kuvaajat ja 21 ohitettua kuvaa ennallaan. Käsin liimattuja SVG:itä FY5:ssä ei ole (kaikilla on `data-fig`, kaikki figures.py:ssä).

Huomiot:
- `fy5-5/vuorovaikutus`: paketin `{"nobg":[0]}` siirretty sarakkeeseen `ilman taustaa` ([0]).
- `fy5-10/types`: paketin merkinnän korvaus "harvennus" → "harventuma" EI tehty (figures.py, glossary.json ja käännökset vanhalla sanalla; opettajan päätös 19.11. odottaa sanan vaihtoa kaikkialla).
- `check_layout.py` 1280 px: kaksi kuvaa kaatuu (`svg-image`, kuva ei ole kuvassaan): `fy5-3/karuselli` (laatikko ylittää viewBoxin oikealle 24,4 ja alas 18,8 yksikköä; sivulla 16 px) ja `fy5-4/muutos` (vasen 3,9, ylä 2,6, oikea 17,9, ala 21,4 yksikköä; 5 px). Leikkautuva osa on pelkkää taustaa.
- Muut 56 riviä ylittävät viewBoxin 0,5–14,5 yksikköä (lähes kaikki alareunasta); leikkautuva osa on pelkkää taustaa, paitsi `fy5-2/lauta`: alareunan 7,5 yksikön kaistasta ~5 % pikseleistä on piirrosta (veden alareuna), sivulla OK.
