# Työjono

Opettajan päättämät tulevat työt, joita ei ole vielä aloitettu. Jokainen kohta tehdään omana pull requestinaan;
valmis kohta poistetaan tästä samassa pull requestissa.

## FY8: Elektronisieppaus ja Vaimennuskerroin oppituntien tekstiin (opettaja 2026-11-13)

Molemmilla on käsitekortti luvun pakassa (`kortit/fy8.json`: `fy8-elektronisieppaus` luvussa fy8-8,
`fy8-vaimennuskerroin` luvussa fy8-12), mutta kumpaakaan ei käsitellä lukujen teoriassa, joten build ei voi
alleviivata niitä (PR #526).

- **fy8-8** (*Atomiydin ja radioaktiivinen hajoaminen*): elektronisieppaus hajoamislajina beetahajoamisten rinnalle: ydin sieppaa
  elektronin, protoni muuttuu neutroniksi ja syntyy neutriino; reaktioyhtälö ja esimerkki.
- **fy8-12** (*Ionisoiva säteily ja elimistö*): vaimennuskerroin $\mu$ ja $I = I_0 e^{-\mu d}$ nykyisen
  puoliintumispaksuuden muodon $I = I_0 \left(\tfrac{1}{2}\right)^{d/d_{1/2}}$ rinnalle, yhteys $\mu = \ln 2 / d_{1/2}$.
  Samalla "säteilyn vaimeneminen" itsenäisenä terminä tekstiin, jotta kortti `fy8-sateilyn-vaimeneminen` alleviivautuu.

Tehdään oppitunnin muokkauksena (`/lesson fy8-8`, `/lesson fy8-12`): sisältömuutos vanhentaa luvun katselmoinnit,
joten se vaatii uudet tiede-, pedagogiikka- ja ulkoasukatselmoinnit. Tarkista MAOL-taulukoista ja `docs/lops2019/`:sta,
että merkinnät vastaavat MAFY:ä.

## FY7: tehtävä fy7-16-L2-09 tehdään uudelleen (opettaja 2026-11-13, PR #528)

Kenttäviivoja laskemalla saatu vastaus ($2{,}1\,\text{V}$) poikkeaa todellisen vuosuhteen antamasta ($\approx 2{,}3\,\text{V}$),
eikä väljä toleranssi riitä. Tehtävä kirjoitetaan uudelleen niin, että mallin antama vastaus on oikea (fi, en, fi-easy).
Tehdään #528:n haarassa ennen sen tehtäväsarjojen katselmointia. fy6-1-L2-08:n selkosuomi (sama kuin suomenkielinen
teksti) kelpaa sellaisenaan.

## Kuva- ja MAFY-taulukkotehtävät FY8, FY9, FY10 ja FY14 (opettaja 2026-11-13)

Sama tahti kuin FY4:stä alkaen: jokaisessa luvussa vähintään kaksi kuvatehtävää ja MAFY-taulukkotehtävä noin joka
kolmannessa luvussa (#521, #528). Arvot vain `docs/mafy-arvot.tsv`:stä, uudet rivit lähde-URL:n kanssa.

## Kaavat MAFY-muotoon FY5–FY8, FY10 ja FY14

FY1–FY4 ja FY9 on tehty (#501, #522, #527, #529). Keskinopeuden tunnus on kaikkialla $v_\text{k}$, ei $v_\text{ka}$
(opettaja 2026-11-13).

## Puute: englanninkieliset käsitekortit FY6 ja FY8 (opettaja 2026-11-13: tehdään myöhemmin)

`kortit/en/` ei sisällä tiedostoja `fy6.json` ja `fy8.json`, joten englanninkielisillä FY6- ja FY8-sivuilla ei ole
käsitekortteja eikä alleviivauksia.

## Kirjattu päätös: luvut ilman käsitekortteja (opettaja 2026-11-13)

Luvut fy3-13, fy3-14, fy3-16 ja fy4-16 jäävät ilman omia kortteja ja alleviivauksia (#526:n siirtojen jälkeen).
Kortteja ei lisätä niihin.
