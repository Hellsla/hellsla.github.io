VERDICT: PASS
CONTENT-HASH: 42ba4c36bd92a300

## Blocking

## Polish
- exercises/solutions.md fy4-9-L2-08 Vastaus — "kaksi tai kolme merkitsevää numeroa kuvaajan lukuarvojen tarkkuudella" ei päätä tarkkuutta — kirjoita esim. "$4{,}5 \cdot 10^2\,\text{N}$, kaksi merkitsevää numeroa: huippu luetaan $100\,\text{N}$:n ruudukosta ja aika $2\,\text{ms}$:n jaotuksesta".
- exercises/solutions.md fy4-9-L2-08 Järkevyys — tarkistus toistaa kaavan ($F_\text{ka} = \tfrac{1}{2}F_\text{max}$) — lisää vaikka vertailu: suorakulmio $450\,\text{N} \times 12\,\text{ms}$ peittää saman pinta-alan kuin kolmio.

## Checked
- Kaikki 20 numeerista vastausta laskettu uudelleen omilla kaavoilla yhdessä ajossa (p = mv, I = FΔt, puolisuunnikkaat, L3-05 painon kanssa): täsmäävät answers.py:n kanssa; pyöristetyt vastaukset pysyvät toleranssin sisällä (esim. L2-04 $26$ vs $25{,}65$: 1,4 %).
- Uusi kuvatehtävä L2-08: `fy4-9/tarkistus-kolmio` piirtää kolmion (0, 0)–(6 ms, 900 N)–(12 ms, 0); huippu on $100\,\text{N}$:n ruutuviivalla ja ajat 2 ms:n jaotuksella, joten $450\,\text{N}$ luetaan selvästi ±2 %:n sisään. Kuvaus antaa samat luvut eikä vastausta.
- Kuvaa ei käytä muu harjoitustehtävä; L3-01 (`ex-potku`) on eri kuvaaja ja eri kysymys (nopeus impulssista), joten L2-08 ei toista tehtävää.
- Merkinnät: $F_\text{ka}$, $I$, $\Delta p$, $\overline{p}$ kuten luvun kaavaosiossa.
- Monivalinnat L1-06 ja L1-09: tasan yksi oikea, harhautinten palaute oikein (0,4 N ≈ 2 × paino 0,20 N; 4000 on teho W:na; 400 000 N grammoista).
- Etumerkit ja suunnat: L2-03, L3-03, L3-04 ja L3-05 valitsevat positiivisen suunnan ja käyttävät sitä johdonmukaisesti; L2-07:n kimpoaminen $+1{,}38\,\text{m/s} < 1{,}50\,\text{m/s}$ on fysikaalisesti järkevä.
- Mallin oletukset annettu tehtävissä (paino ohitetaan iskussa, kitka/ilmanvastus ohitetaan); L3-05 ottaa painon mukaan kuten tehtävä pyytää.
- Suuruusluokat realistisia (golfmaila $6{,}4\,\text{kN}$, turvavyö $58\,\text{km/h}$, törmäysnukke $50\,\text{km/h}$).
- Sisältö pysyy FY4:n keskeisissä sisällöissä (liikemäärä, impulssi); ei törmäyksiä eikä myöhempien kurssien fysiikkaa.
- Ratkaisut: symbolinen ratkaisu ennen sijoitusta, muunnokset ja pyöristysperusteet oikein.
