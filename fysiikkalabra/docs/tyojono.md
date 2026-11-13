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
