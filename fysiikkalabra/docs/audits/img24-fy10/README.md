# Työjono 24 osa 10: FY10, ennen ja jälkeen

Jokaisessa kuvassa vasemmalla nykyinen sivu (`main`), oikealla uusi kuva samalla sivulla; sticky-palkki ja valikko piilotettu.
Tiedosto `<tutkimus>_<nimi>_fi_<leveys>.webp`, leveydet 360 px (2× tarkkuus) ja 1280 px. Tutkimuksilla on vain suomenkielinen sivu (ei en- eikä fi-easy-versiota).
62 kuvaa 27 tutkimuksessa (23 kuvitusta, 39 kaaviota): 124 tiedostoa. Kuvatiedostot `assets/pics/fy10/` (62 WebP, 1,4 Mt, pisin sivu ≤ 1600 px), asettelu `lessons/FY10/ASETTELU.tsv`.
Kuvat ovat vain tutkimuksissa; tvt-ohjeet eivät kuulu FY10-pakettiin.

Ennalleen: PAATOS.txt:n 5 "ei piirretty uudelleen" -kuvaa (`fy10-hyppy/hero`, `fy10-kondensaattori/hero`, `fy10-liikemaara/hero`, `fy10-liukukitka/hero`, `fy10-aanennopeus/signal`), kuvaajat ja muut kuvat, joilla ei ole riviä.

Huomiot:
- Paketin `ASETTELU.tsv`:ssä `fy10-liikemaara/setup`-rivin siirroissa oli `"union": true` (ei merkinnän siirto); jätetty pois, siirto `{"6":[-45,0]}` ennallaan.
- Sarake `ilman taustaa`: ajettu `figimage.py flat` (FY10-tutkimuksille tilapäisellä ajurilla, koska `figimage.py flat|check` ei vielä hae tutkimusten kuvia figcatin kautta); vain `fy10-induktio/flux` merkintä 4.
- PAATOS.txt: `fy10-kondensaattori/circuit` plusmerkki näkyy hieman kahdentuneena; `fy10-uppokuumennin/setup` osoitusviivat puuttuvat tekstien luota (hyväksytty sellaisenaan).
- viewBox-ylitykset (37 riviä: kuvan laatikko ylittää kuvan viewBoxin): suurimmat fy10-liukukitka/setup 17.9; fy10-valaistus/setup 8.8; fy10-tuulivoimala/circuit 8.0; fy10-aanennopeus/setup 7.8,; fy10-mikroaaltouuni/standing 7.5; fy10-hissi/vaiheet 7.4; loput alle 10 yksikköä, melkein kaikki alareunasta. Rajausta ei tehty (vaatii opettajan luvan).
