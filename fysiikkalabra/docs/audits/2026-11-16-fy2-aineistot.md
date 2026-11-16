# FY2: aineistotehtävien FY2-A1…A5 lähdeaineisto (luettu 16.11.2026)

Työjonon kohta 19, FY2. Toimeksianto: `docs/audits/2026-11-16-aineistotehtavat.md` (FY2-A1…A5). Tässä tiedostossa on,
mitä lähteistä luettiin 16.11.2026, miten lähteitä korjattiin ja mihin lukuun kukin tehtävä sijoitetaan. Tehtävien
taulukot (`"data"`) ovat näitä päivättyjä lukemia, joten tehtävät toimivat myös myöhemmin, kun reaaliaikainen data on muuttunut.

## Lähteiden tarkistus
- **Electricity Maps** (app.electricitymaps.com): palvelu ei avautunut tarkistettavaksi (Cloudflare esti automaattisen
  pääsyn 16.11.2026, myös selaimella). Sisältöä ei voitu tarkistaa, joten se korvattiin:
  - A1: maiden vertailu → Our World in Data (Ember), vuoden 2025 elinkaaripäästöt; tuotetun ja kulutetun sähkön ero → Fingrid.
  - A5: tuulivoima ja päästöt → pelkkä Fingrid (sivulla on tuulivoima ja kulutetun sähkön CO₂-päästöarvio samalla hetkellä).
- **Fingrid, Sähköjärjestelmän tila** https://www.fingrid.fi/sahkomarkkinat/sahkojarjestelman-tila/ : toimii. Sivun selitteet:
  "Suomen sähköjärjestelmän reaaliaikainen tuotetun/kulutetun sähkön CO₂-päästöarvio. Laskenta perustuu reaaliaikaisiin
  tuotanto-, tuonti- ja vientitietoihin sekä tuotantomuotokohtaisiin päästökertoimiin." Aluehinta on "ilman veroja ja
  sähkön siirtokustannuksia". Sivu ei sano, että päästöarvio olisi elinkaariarvio. Tuonti − / vienti + (netto).
- **Our World in Data, Electricity Mix** https://ourworldindata.org/grapher/electricity-mix?metric=carbon_intensity : toimii.
  "Lifecycle carbon intensity of electricity", gCO₂e/kWh tuotettua sähköä, elinkaariperusteinen (myös tuotantoketju ja
  rakentaminen), kaikki kasvihuonekaasut; lähde Ember (2026), päivitetty 30.6.2026, vuodet 1990–2025.
  Tuotantorakenne: sama kaavio, mittari "Share of electricity" (https://ourworldindata.org/grapher/electricity-mix).
- **Yle** https://yle.fi/a/74-20045312 : toimii. Otsikko "Vaasan sähkö ei hyvitä miinukselle painuvaa pörssisähkön hintaa
  asiakkailleen, vaikka moni niin tekee – näin yhtiö perustelee ratkaisua", Sebu Björklund, Yle Pohjanmaa, 16.8.2023.
  Sisältö: pörssisähkön hinta voi painua miinukselle, jos tuotantoa on kulutusta enemmän; Vattenfall, Oomi ja Seinäjoen
  energia hyvittävät negatiiviset tunnit laskulla, Vaasan sähkö käsittelee negatiivisen tuntihinnan nolla senttiä
  maksavana; välityspalkkiot Oomi $0{,}25$, Seinäjoen energia $0{,}40$, Vaasan sähkö $0{,}41$ ja Vattenfall $0{,}50$ snt/kWh.
  Artikkeli on yli kolme vuotta vanha (sivu sanoo sen itse); tehtävä käyttää sitä hinnanmuodostuksen periaatteen lähteenä.

## Luetut arvot

### OWID / Ember, elinkaaren aikainen päästökerroin, gCO₂e/kWh (luettu 16.11.2026)
| Maa | 2000 | 2025 |
| --- | --- | --- |
| Suomi | 246,82 | 57,47 |
| Ruotsi | 44,89 | 35,26 |
| Puola | 954,6 | 588,6 |
| Tanska | 627,89 | 114,41 |

### OWID / Ember, sähköntuotannon osuudet (%)
| Maa, vuosi | hiili | kaasu | öljy | ydin | vesi | tuuli | aurinko | bio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Suomi 2000 | 12,1 | 14,5 | 7,8 | 32,1 | 21,0 | 0,1 | 0 | 12,3 |
| Suomi 2025 | 0,2 | 1,2 | 2,3 | 39,9 | 15,1 | 27,4 | 1,2 | 12,6 |
| Ruotsi 2025 | 0 | 0,1 | 1,2 | 27,6 | 40,0 | 22,8 | 2,6 | 5,8 |
| Puola 2000 | 94,9 | 0,6 | 2,8 | 0 | 1,5 | 0 | 0 | 0,2 |
| Puola 2025 | 50,4 | 14,3 | 3,8 | 0 | 1,0 | 14,2 | 11,3 | 4,9 |
| Tanska 2000 | 46,5 | 24,5 | 13,5 | 0 | 0,1 | 11,8 | 0 | 3,6 |
| Tanska 2025 | 2,7 | 2,4 | 3,7 | 0 | 0,1 | 57,7 | 13,4 | 20,1 |

### Fingrid, Sähköjärjestelmän tila, 16.11.2026 klo 10.48 (sivun lukemat)
Kulutus $11\,603\,\text{MW}$, tuotanto $11\,341\,\text{MW}$, tuonti − / vienti + (netto) $-210\,\text{MW}$, aluehinta
$29{,}95\,€/\text{MWh}$, tuotetun sähkön CO₂-päästöarvio $16\,\text{g/kWh}$, kulutetun $15\,\text{g/kWh}$. Tuotanto:
ydinvoima $2594$, yhteistuotanto (teollisuus) $853$, yhteistuotanto (kaukolämpö) $329$, muu $73$, tehoreservi $0$,
tuulivoima $5571$, aurinkovoima $56$, vesivoima $1823$, sähkövarastot $71\,\text{MW}$.

### Fingrid, sama sivu, näkymä "Tänään" 16.11.2026, tasatuntien lukemat (Suomen aikaa)
| Kello | tuulivoima (MW) | tuotanto (MW) | kulutus (MW) | netto, vienti + (MW) | kulutetun sähkön CO₂ (g/kWh) |
| --- | --- | --- | --- | --- | --- |
| 1.00 | 7639 | 12 791 | 10 647 | +2142 | 9,8 |
| 8.00 | 6716 | 12 570 | 11 406 | +1124 | 13,7 |
| 10.00 | 5885 | 11 610 | 11 737 | −152 | 15,0 |
Ydinvoima koko ajan noin $2590\,\text{MW}$, vesivoima $1520$ → $1920$ → $1780\,\text{MW}$.

## Sijoitus (tunnisteet säilyvät raportissa)
| Tunniste | Luku | Tehtävä | Vastauslaatikko |
| --- | --- | --- | --- |
| FY2-A4 | fy2-3 Teho | fy2-3-L2-09 | b) kustannus $8{,}0\,\text{kWh} \cdot (-5{,}0\,\text{snt/kWh}) = -40\,\text{snt}$ |
| FY2-A2 | fy2-7 Energian siirtäminen | fy2-7-L2-10 | b) $E = P\Delta t = 11\,603\,\text{MW} \cdot 1\,\text{h} \approx 11{,}6\,\text{GWh}$ |
| FY2-A1 | fy2-8 Energiantuotanto, ympäristö | fy2-8-L2-10 | c) Puola $5{,}0\,\text{kWh} \cdot 589\,\text{g/kWh} \approx 2{,}9\,\text{kg}$ |
| FY2-A5 | fy2-8 | fy2-8-L2-11 | b) klo 10.00 $10\,\text{kWh} \cdot 15{,}0\,\text{g/kWh} = 150\,\text{g}$ |
| FY2-A3 | fy2-8 | fy2-8-L3-06 | b) Suomi $(57 - 247) : 247 \approx -77\,\%$ |

Päästöt lasketaan luvun *Energiantuotanto, ympäristö ja ilmastonmuutos* päästökertoimella (glossary.json:
päästökerroin; lähteen sana "päästöintensiteetti" / "carbon intensity" mainitaan lähteen nimenä).
