# Työjono 24 osa 9: FY9, ennen ja jälkeen

Jokaisessa kuvassa vasemmalla nykyinen sivu (`main`), oikealla uusi kuva samalla sivulla; sticky-palkki, valikko ja luvun valikkopaneeli piilotettu.
Tiedosto `<omistaja>_<nimi>_<kieli>_<leveys>.webp`: kielet `fi`, `en`, `fi-easy`, leveydet 360 px (2× tarkkuus) ja 1280 px.
30 kuvaa (26 + 4 Sovella): 180 kuvaa. Kuvatiedostot `assets/pics/fy9/` (30 WebP), asettelu `lessons/FY9/ASETTELU.tsv`.

Ennalleen (PAATOS.txt): `fy9-sahkokentta/etuvastus`, `fy9-ympyraliike/kaarre`; `fy2-4/grid` ja `fy7-2/track-sign` omistajamoduulin versiolla; 32 kuvaajaa/tunnistuskaaviota (ei piirretty uudelleen).

Sovella-kuvat (4: `fy9-harjoituskoe-s2-fbd`, `fy9-kaasut-s6-pysty`, `fy9-kaasut-s6-vaaka`, `fy9-sahkokentta-s1-fbd`) lisätty #805:n jälkeen (id `<jakso>-sovella/<nimi>`), kuvat ennen/jälkeen-kansiossa nimillä `<jakso>_<jakso>-s…_<kieli>_<leveys>`. Opettaja ei ole vielä nähnyt näitä; `approve-figures` ei ole ajettu niille.

EI VIETY: 11 voimakuviota `fy9-voimat/nimeton-N` (1, 2, 3, 5, 6, 8, 9, 10, 11, 13, 14): sivun voimakuviot syntyvät kirjastosta rakennettaessa, eikä niillä ole `figures.py`-kuvaa tai tunnistetta; `figimage` ei voi liittää niihin kuvaa. WebP:t ja rivit poistettu tästä PR:stä.

Huomiot:
- `fy9-harjoituskoe-s2-fbd`: oikean reunan taustakaista (34 px, ei-taustapikseleitä 0) rajattu lähde-PNG:stä ja `ASETTELU`-leveys 609,1 → 596,2, koska kuva ylitti viewBoxin oikealla 12,9 yks. ja `check_layout` kaatui (640–1920 px, "the picture is not in its figure"); `check_layout` kaikilla leveyksillä (360–1920) ja kielillä läpi. Lupa: opettaja koordinaattorin chatissa 2026-11-23 "Etene suositusten mukaisesti" (kirjaus työjonon kohdassa 24, koordinaattorin välittämänä); rajattu kuva odottaa opettajan hyväksyntää suoraan tähän sessioon (`approve-figures` ei ajettu).
- `figimage.py check` ja `flat` eivät tunne jaksojen kuvia (`figcat` ei hae `lessons/units/`): ilman taustaa -sarake laskettu samalla menetelmällä erillisellä skriptillä (`fy9-magnetismi-valo/ympyra` [7], `fy9-moderni/pallo` [3, 4], `fy9-ympyraliike/geo` [3]).
- `fy9-energia/ketju` ja `fy9-magnetismi-valo/rajakulma`: merkintöjen siirrot paketin mukaan.
- `fy9-energia/ketju`, `fy9-kaasut/kone`, `fy9-sahkokentta/levyt`, `fy9-ympyraliike/geo`: PAATOS.txt:n huomiot (mittasuhteita ei mitattu) hyväksytty sellaisinaan.
- viewBox-ylitykset (rajausta ei tehty, vaatii opettajan luvan), yksikköä: `fy9-moderni/pallo` 7,5; `fy9-sahkokentta/levyt` 7,5; `fy9-voimat/kalteva` 7,5; `fy9-magnetismi-valo/rajakulma` 7,0; `fy9-tasavirta/mokki` 5,9; `fy9-magnetismi-valo/ympyra` 5,0; `fy9-aallot/ominais` 4,0; `fy9-sailymislait/tuuli` 2,9; `fy9-sahkokentta/kipina` 1,2.
