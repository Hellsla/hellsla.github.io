# Työjono 24 osa 9: FY9, ennen ja jälkeen

Jokaisessa kuvassa vasemmalla nykyinen sivu (`main`), oikealla uusi kuva samalla sivulla; sticky-palkki, valikko ja luvun valikkopaneeli piilotettu.
Tiedosto `<omistaja>_<nimi>_<kieli>_<leveys>.webp`: kielet `fi`, `en`, `fi-easy`, leveydet 360 px (2× tarkkuus) ja 1280 px.
26 kuvaa (12 kuvitusta, 14 kaaviota): 156 kuvaa. Kuvatiedostot `assets/pics/fy9/` (26 WebP), asettelu `lessons/FY9/ASETTELU.tsv`.

Ennalleen (PAATOS.txt): `fy9-sahkokentta/etuvastus`, `fy9-ympyraliike/kaarre`; `fy2-4/grid` ja `fy7-2/track-sign` omistajamoduulin versiolla; 32 kuvaajaa/tunnistuskaaviota (ei piirretty uudelleen).

EI VIETY (jaettu muutos puuttuu, kerrottu koordinaattorille):
- 11 voimakuviota `fy9-voimat/nimeton-N` (1, 2, 3, 5, 6, 8, 9, 10, 11, 13, 14): sivun voimakuviot syntyvät kirjastosta rakennettaessa, eikä niillä ole `figures.py`-kuvaa tai tunnistetta; `figimage` ei voi liittää niihin kuvaa. WebP:t ja rivit poistettu tästä PR:stä.
- 4 Sovella-kuvaa (`fy9-harjoituskoe-s2-fbd`, `fy9-kaasut-s6-pysty`, `fy9-kaasut-s6-vaaka`, `fy9-sahkokentta-s1-fbd`): `practice.py` antaa `figimage.apply`:lle tunnisteen `units/<yksikkö>-sovella/<nimi>`, jolla ei ole riviä (`code_of` ei tunnista). Rivit poistettu.

Huomiot:
- `figimage.py check` ja `flat` eivät tunne jaksojen kuvia (`figcat` ei hae `lessons/units/`): ilman taustaa -sarake laskettu samalla menetelmällä erillisellä skriptillä (`fy9-magnetismi-valo/ympyra` [7], `fy9-moderni/pallo` [3, 4], `fy9-ympyraliike/geo` [3]).
- `fy9-energia/ketju` ja `fy9-magnetismi-valo/rajakulma`: merkintöjen siirrot paketin mukaan.
- `fy9-energia/ketju`, `fy9-kaasut/kone`, `fy9-sahkokentta/levyt`, `fy9-ympyraliike/geo`: PAATOS.txt:n huomiot (mittasuhteita ei mitattu) hyväksytty sellaisinaan.
- viewBox-ylitykset (rajausta ei tehty, vaatii opettajan luvan), yksikköä: `fy9-moderni/pallo` 7,5; `fy9-sahkokentta/levyt` 7,5; `fy9-voimat/kalteva` 7,5; `fy9-magnetismi-valo/rajakulma` 7,0; `fy9-tasavirta/mokki` 5,9; `fy9-magnetismi-valo/ympyra` 5,0; `fy9-aallot/ominais` 4,0; `fy9-sailymislait/tuuli` 2,9; `fy9-sahkokentta/kipina` 1,2.
