# Tehtäväpankki FY1–FY8: täydennyssuunnitelma

Lauri 2026-11-04: jokaisessa FY1–FY8-luvussa vähintään 20 tehtävää, kolme tasoa (perus, soveltava, haastava;
lähtökohta 8 + 7 + 5), runsaasti hyviä laskutehtäviä ja niiden rinnalla aineistotehtäviä (useimmissa luvuissa 2–3,
pääosin soveltavissa), käsitteellisiä monivalintoja, laadullisia päättelytehtäviä, kokeellisia tutkimustehtäviä,
virheanalyysiä, kuvaajien tulkintaa ja perusteluja. Haastavissa YO-kokeen ongelmanratkaisu, mallintaminen ja
aineiston tulkinta. Kaikilla uusilla tehtävillä täydellinen malliratkaisu tai perusteltu mallivastaus.

**Säännöt kaikille luvuille**

- Nykyiset tehtävät, niiden id:t ja ratkaisut säilyvät. Uudet saavat tasonsa seuraavat vapaat id:t
  (`fyX-Y-L1-06` …) ja tulevat tason loppuun.
- Laskut ja aineistot pysyvät luvun sisällössä (`curriculum.json`, LOPS 2019). Tason 3 tehtävä saa yhdistää
  aiempien lukujen asioita.
- Aineistotehtävä = mittaustaulukko (`"data"`) tai kuvaaja (`"figure"`), jota luetaan, johon sovitetaan, jonka
  mallia arvioidaan tai jonka epävarmuutta pohditaan. Aineisto on uskottava: realistinen hajonta, oikeat
  merkitsevät numerot, lähde tai mittausjärjestely kerrottu. Ei keksittyjä tilastoja todellisina: tilasto on joko
  lähteellinen (Tilastokeskus, Energiavirasto, Fingrid …, vuosi mainittu) tai sanotaan malliaineistoksi.
- Monivalinta (`"choices"`) 3–5 vaihtoehtoa; väärät vaihtoehdot ovat tyypillisiä virhekäsityksiä, ja jokaisella on
  oma palautteensa.
- `"kind"` merkitään jokaiseen uuteen tehtävään (data, graph, experiment, error, concept, reasoning, model);
  `python scripts/exercise_bank.py FY1` näyttää jakauman.
- Uusien tehtävien vakiopaketti luvulle, jossa on nyt 5/4/3 (ellei luvun rivi muuta sano):
  - **Taso 1 (+3 → 8):** 1 käsitteellinen monivalinta, 2 laskua uusiin tilanteisiin (tai 1 lasku + 1 lyhyt perustelu).
  - **Taso 2 (+3 → 7):** 2 aineistotehtävää, 1 kokeellinen tai virheanalyysitehtävä (tai kuvaajan tulkinta).
  - **Taso 3 (+2 → 5):** 1 YO-tyyppinen monivaiheinen tehtävä (mallintaminen tai aineiston tulkinta), 1 laadullinen
    perustelutehtävä tai virheanalyysi. Haastava aineistotehtävä voi korvata toisen.
- Kaikki uudet tehtävät käännetään samassa erässä englanniksi ja selkosuomeksi (check_i18n vaatii saman rakenteen).

**Toteutusjärjestys ja erät** (yksi PR per erä, ei yhdistetä mainiin itse)

| Erä | Luvut | Huomio |
|---|---|---|
| 0 | tekniikka + fy1-4 (kokeilu) | monivalinta- ja taulukkotuki, raportti, mittaa kustannuksen |
| 1 | fy1-1, fy1-2, fy1-3 | |
| 2 | fy1-5, fy1-6, fy1-7, fy1-8 | FY1 valmis → `exercise_total: 20` |
| 3 | fy2-1 … fy2-4 | |
| 4 | fy2-5 … fy2-8 | FY2 valmis |
| 5–8 | FY3 neljän luvun erissä opetusjärjestyksessä | |
| 9–12 | FY4 neljän luvun erissä | |
| 13–17 | FY5 3–4 luvun erissä | |

Prioriteetti luvun rivillä: **P1** keskeinen YO-sisältö ja suuri tyyppivaje (aineisto- ja käsitetehtävät puuttuvat
kokonaan), **P2** tärkeä, **P3** soveltava tai jo monipuolisempi luku. Erien sisällä P1 ensin.

Suunnitelmat: [FY1](FY1.md) · [FY2](FY2.md) · [FY3](FY3.md) · [FY4](FY4.md) · [FY5](FY5.md). FY6–FY8 tehdään,
kun niiden avoimet PR:t (#222, #228, #232) on yhdistetty.
