# Ydinpolun työmäärä FY1–FY4: pedagoginen arvio

*Pedagogiikka-arvioijan raportti opettajalle, 2026-10-31. Aika-arvioita **ei ole mitattu**: ne ovat karkeita arvioita, joiden oletukset kerrotaan kohdassa 2.*

## 1. Lyhyesti

| Kysymys | Vastaus |
|---|---|
| Onko opiskelijalla selkeä ydinpolku? | **Pääosin on.** Valinnaiset osat ovat suljetuissa, *Valinnainen*-merkityissä laatikoissa, sivun alussa lukee, montako niitä on, ja ydintehtävät on merkitty. Mekanismi toimii, mutta **viesti on ristiriitainen 18 luvussa** (ks. 4.1), ja **fy4-1:ssä ja fy4-2:ssa ei ole yhtään valinnaista osaa**, joten niistä puuttuu myös ydinpolkuhuomautus. |
| Erottuvatko ydintehtävät lisäharjoittelusta? | **Tehtävät-osiossa erottuvat** (*Ydintehtävä*-merkintä, tasojen johdannot). Ristiriita syntyy luvun omasta johdantotekstistä: "Taso 1 riittää perusosaamiseen; tasot 2 ja 3 ovat vapaaehtoisia", vaikka kaksi tason 2 tehtävää on merkitty ydintehtäviksi. |
| Onko turhaa päällekkäisyyttä? | **Kahdenlaista on.** (a) Luvun Miksi-kysymykseen kirjoitetaan ydinpolulla selitys kolmesti (Johtopäätös → Palaa ennusteisiisi → Tarkista 3) luvuissa fy1-3, fy2-1, fy4-2 ja fy4-7, ja kahdesti useissa FY4:n luvuissa. (b) Exit ticket kysyy usein saman yhden kaavan sijoituksen kuin tason 1 ydintehtävä, ja muutamassa tehtävässä on täsmälleen samat lähtöarvot kuin toisessa kohdassa (fy2-4, fy3-6). |
| Ovatko tutkivan oppimisen vaiheet perusteltuja? | **Simulaatioluvuissa pääosin ovat:** ennuste lukittuu, ja koe voi kumota sen. **Mekaanisia** ne ovat FY1:n ja FY2:n simulaatiottomissa luvuissa (fy1-7, fy1-8, fy2-5–fy2-8). Niissä Ennusta-vaiheen palaute "Oikein. …" kertoo vastauksen perusteluineen heti, ennen kuin Tutki-vaiheen aineisto on nähty. FY3:n simulaatiottomat luvut tekevät tämän paremmin. |
| Pääseekö avainsisältöön ilman lisätehtäviä? | **Pääsee.** Validaattori estää ydinosaa nojaamasta valinnaiseen kokeeseen, koko teoria on ydinpolulla, eikä yksikään ydintehtävä tarvitse valinnaista aineistoa. |
| Onko teorian ja tehtävien suhde kohtuullinen? | **On.** Näkyvää teoriaa ja esimerkkiä on noin 800–1000 sanaa luvussa. Karkean arvion mukaan lukeminen vie noin viidenneksen ydinpolun ajasta, ja loppu on tekemistä. Kuormaa ei lisää teoria vaan tehtävien määrä: FY4:ssä ja FY1:ssä on keskimäärin 14–15 ydinsyötettä luvussa, FY3:ssa 10. |

Karkea arvio (kohta 2): sivun ydinpolku ilman Tehtäviä vie keskimäärin noin 44 min (FY3) – 58 min (FY4), ja neljän ydintehtävän kanssa noin 66–80 min. Raskaimmat luvut ovat fy4-1, fy4-2, fy4-7 ja fy1-3, joissa sivun ydinpolku vie noin 67–72 min jo ennen Tehtäviä. Yhteen 75 minuutin tuntiin mahtuu silloin vain sivu, ei ydintehtäviä.

## 2. Menetelmä ja rajaukset

- **Laskentaskripti** (kertakäyttöinen apuskripti, ei repositoriossa) lukee jokaisesta luvusta tiedostot `inquiry.json`, `lesson.md`, `exit-ticket.json` ja `exercises/exercises.json`. Ydintehtävät se valitsee samalla säännöllä kuin `scripts/build.py core_ids` (`"core": true` tai tasojen 1–2 kaksi ensimmäistä; yksikään FY1–FY4:n luku ei käytä `core`-kenttää). Skripti laskee vaiheittain ydin- ja valinnaiset aktiviteetit, ennusteet, kokeet ja vaadittavat syötteet (valinta, laskun vastaus, kirjoitettu vastaus; kokeesta `min` kirjausta ja kokeen kysymys), sanamäärät sekä tehtävät tasoittain.
- **Sanamäärät**: SVG- ja HTML-merkinnät poistettu, yksi kaava = yksi sana. *Teoria* tarkoittaa lesson.md:n muita osioita kuin Esimerkkiä, myös Yleistä virhekäsitystä ja Tiivistelmää. *Tehtävät* tarkoittaa inquiry.jsonin näkyvää ydinpolun tekstiä (tehtävänanto, vaihtoehdot, kokeen ohje). *Piilossa* tarkoittaa palautteita, vihjeitä, ratkaisuja, malliratkaisuja ja simulaation laatikoita, jotka avautuvat vasta painikkeesta.
- **Aika-arvion oletukset (karkea arvio, ei mittaus):** näkyvä teksti 120 sanaa/min; valinta 1,5 min, ennuste 2, kokeen kirjaus ja kysymys 5, aineiston tulkinta 3, laskutehtävä 5, selitys 4, ennusteen tarkastelu 2, simulaation vapaa kokeilu 3, ilmiö 1, exit ticketin kysymys 2, ydintehtävä tasolla 1 noin 4 ja tasolla 2 noin 7 min. Piilotekstejä ei laskettu. Jos opiskelija lukee niistä puolet ja lukee teorian hitaammin (100 sanaa/min), arvio kasvaa noin 8–12 min. Luvut kertovat lukujen keskinäisen järjestyksen paremmin kuin todellisen keston.
- **Kokonaan luettu**: fy1-1, fy2-1, fy3-6 (teksti ja inquiry) sekä fy2-6, fy3-10, fy4-1, fy4-11 (teoria) ja fy4-13 (inquiry, esimerkki, exit). Poikkeamien vuoksi tarkastettiin lisäksi fy1-3, fy4-2, fy4-7, fy2-4 ja fy3-10. Kaikkien 48 luvun Sovella-, Tarkista-, exit- ja ydintehtävätekstit on luettu rinnakkain , ja moduulien Sovella itsenäisesti -tehtävät on käyty läpi tiedostosta `content/fi/<COURSE>/sovella/tasks.json`.

## 3. Lukukohtaiset luvut

Sarakkeet: **P E Tu Te So Ta** = vaiheiden Pohdinta, Ennusta, Tutki, Teoriatiivistelmä, Sovella ja Tarkista osaamisesi (exit ticket mukaan lukien) aktiviteetit muodossa *ydin+valinnainen*. Esimerkiksi Sovella sisältää Esimerkin, ja Tehtävät-aktiviteettia ei ole laskettu mukaan. **Ennusteet** = lukittuvat ennusteet (`reveal`). **Kokeet** = ohjatut simulaatiokokeet. **Ydinsyötteet** = vastaukset, joita ydinpolku vaatii (suluissa valinnaisten osien). **Kirjoitus** = ydinpolun kirjoitetut selitykset ja pohdinnat. **Tehtävät** = määrä tasolla (suluissa ydintehtävät). **Valinnaiset** = valinnaisten laatikoiden määrä; **0** = ei yhtään, jolloin sivulla ei näy ydinpolkuhuomautusta; ⚠ = Tehtävät-johdannossa lukee "Taso 1 riittää …" eli ristiriitainen ydinviesti. **Arvio** = karkea arvio minuuteissa: sivun ydinpolku / sama ja 4 ydintehtävää / valinnaiset laatikot / muut 8 tehtävää.

| Luku | P | E | Tu | Te | So | Ta | Ennusteet | Kokeet | Ydinsyötteet (valinn.) | Kirjoitus (ydin) | Exit | Teoria / esim. / tehtävät (sanaa) | Piilossa (sanaa) | Tehtävät T1/T2/T3 (ydin) | Valinnaiset | Arvio: sivu / +ydinteht. / valinn. / muut teht. (min) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| fy1-1 | 1+1 | 2 | 3+2 | 2 | 3+2 | 4+1 | 2 | 2+1 | 17 (9) | 1 | 2 | 1304 / 163 / 575 | 1447 | 5(2)/4(2)/3(0) | 6 ⚠ | ~52 / ~74 / ~23 / ~56 |
| fy1-2 | 1+1 | 2 | 5 | 1+1 | 2+2 | 4+1 | 2 | 2 | 13 (5) | 1 | 2 | 694 / 146 / 567 | 1307 | 5(2)/4(2)/3(0) | 5 | ~54 / ~76 / ~12 / ~56 |
| fy1-3 | 2 | 2 | 5+1 | 2 | 3+1 | 5 | 2 | 2+1 | 20 (5) | 3 | 3 | 959 / 225 / 826 | 1724 | 5(2)/4(2)/3(0) | 2 ⚠ | ~70 / ~92 / ~8 / ~56 |
| fy1-4 | 1+1 | 2 | 5 | 1+1 | 3+1 | 4+1 | 2 | 3 | 18 (4) | 1 | 2 | 577 / 277 / 683 | 1143 | 5(2)/4(2)/3(0) | 4 | ~57 / ~79 / ~14 / ~56 |
| fy1-5 | 1+1 | 2 | 4 | 1+1 | 3 | 4+1 | 2 | 2 | 16 (3) | 1 | 1 | 445 / 218 / 545 | 1056 | 5(2)/4(2)/3(0) | 3 | ~49 / ~71 / ~8 / ~56 |
| fy1-6 | 2 | 2 | 5+1 | 1+1 | 2+1 | 5 | 2 | 3 | 21 (3) | 2 | 1 | 401 / 201 / 583 | 1387 | 5(2)/4(2)/3(0) | 3 ⚠ | ~58 / ~80 / ~8 / ~56 |
| fy1-7 | 1+1 | 2 | 4 | 1 | 2+1 | 4+1 | 0 | 0 (ei sim.) | 10 (3) | 1 | 2 | 695 / 165 / 637 | 1089 | 5(2)/4(2)/3(0) | 3 | ~47 / ~69 / ~8 / ~56 |
| fy1-8 | 1+1 | 1 | 3 | 1+1 | 3+2 | 4+1 | 0 | 0 (ei sim.) | 8 (5) | 1 | 2 | 721 / 185 / 612 | 929 | 5(2)/4(2)/3(0) | 5 | ~39 / ~61 / ~16 / ~56 |
| fy2-1 | 1 | 2 | 5 | 2 | 2+1 | 5 | 2 | 2 | 18 (1) | 3 | 2 | 599 / 195 / 624 | 1284 | 5(2)/4(2)/3(0) | 1 ⚠ | ~60 / ~82 / ~2 / ~56 |
| fy2-2 | 1+1 | 2 | 5 | 1+1 | 2+1 | 4+1 | 2 | 2 | 12 (4) | 1 | 2 | 421 / 148 / 433 | 847 | 5(2)/4(2)/3(0) | 4 | ~51 / ~73 / ~10 / ~56 |
| fy2-3 | 1+1 | 1 | 4+1 | 1+1 | 2+1 | 5+1 | 1 | 1+1 | 12 (8) | 1 | 1 | 532 / 170 / 512 | 939 | 5(2)/4(2)/3(0) | 5 | ~44 / ~66 / ~16 / ~56 |
| fy2-4 | 2 | 1+1 | 3+1 | 1+1 | 3 | 4+1 | 1+1 | 1+1 | 12 (7) | 1 | 3 | 735 / 170 / 460 | 1205 | 5(2)/4(2)/3(0) | 4 | ~49 / ~71 / ~14 / ~56 |
| fy2-5 | 1+1 | 2 | 3+1 | 1+1 | 2+1 | 5+1 | 0 | 0 (ei sim.) | 10 (5) | 1 | 1 | 646 / 169 / 457 | 941 | 5(2)/4(2)/3(0) | 5 | ~41 / ~63 / ~14 / ~56 |
| fy2-6 | 1+1 | 1 | 4 | 1+1 | 1+2 | 6 | 0 | 0 (ei sim.) | 10 (4) | 2 | 1 | 543 / 127 / 466 | 837 | 5(2)/4(2)/3(0) | 4 | ~41 / ~63 / ~11 / ~56 |
| fy2-7 | 1+1 | 2 | 4 | 1+1 | 2+1 | 4+1 | 0 | 0 (ei sim.) | 10 (4) | 1 | 1 | 640 / 174 / 599 | 1096 | 5(2)/4(2)/3(0) | 4 | ~44 / ~66 / ~10 / ~56 |
| fy2-8 | 1+1 | 2 | 5 | 1+1 | 4+1 | 5+1 | 1 | 1 | 16 (4) | 1 | 2 | 857 / 133 / 925 | 1731 | 5(2)/4(2)/3(0) | 4 | ~63 / ~85 / ~10 / ~56 |
| fy3-1 | 1+1 | 1+1 | 5 | 1+1 | 1+2 | 4+1 | 1+1 | 2 | 10 (6) | 1 | 1 | 538 / 218 / 423 | 662 | 5(2)/4(2)/3(0) | 6 | ~43 / ~65 / ~18 / ~56 |
| fy3-2 | 1+1 | 2+1 | 5 | 1+1 | 1+2 | 3+2 | 1+1 | 2 | 10 (7) | 1 | 1 | 487 / 228 / 474 | 609 | 5(2)/4(2)/3(0) | 7 | ~40 / ~62 / ~23 / ~56 |
| fy3-3 | 1+1 | 2+1 | 3+1 | 1+1 | 1+2 | 4+1 | 2+1 | 1+1 | 8 (8) | 1 | 1 | 613 / 339 / 404 | 706 | 5(2)/4(2)/3(0) | 7 | ~39 / ~61 / ~23 / ~56 |
| fy3-4 | 1+1 | 2+1 | 3+1 | 1+1 | 1+2 | 4+1 | 1+1 | 1+1 | 9 (8) | 1 | 2 | 643 / 303 / 358 | 843 | 5(2)/4(2)/3(0) | 7 | ~39 / ~61 / ~23 / ~56 |
| fy3-5 | 1+1 | 2 | 4 | 1+1 | 1+2 | 3+2 | 2 | 2 | 10 (6) | 1 | 2 | 529 / 228 / 572 | 1022 | 5(2)/4(2)/3(0) | 6 | ~40 / ~62 / ~21 / ~56 |
| fy3-6 | 1+1 | 2 | 4 | 1+1 | 1+2 | 4+1 | 2 | 2 | 10 (5) | 1 | 2 | 699 / 270 / 409 | 736 | 5(2)/4(2)/3(0) | 5 | ~46 / ~68 / ~16 / ~56 |
| fy3-7 | 1+1 | 2+1 | 4 | 1+1 | 1+2 | 4+1 | 2+1 | 2 | 10 (6) | 1 | 2 | 619 / 232 / 461 | 873 | 5(2)/4(2)/3(0) | 6 | ~45 / ~67 / ~18 / ~56 |
| fy3-8 | 1+1 | 2+1 | 4+1 | 1+1 | 1+2 | 4+1 | 2+1 | 1+1 | 9 (8) | 1 | 1 | 653 / 250 / 529 | 910 | 5(2)/4(2)/3(0) | 7 | ~42 / ~64 / ~23 / ~56 |
| fy3-9 | 1+1 | 2+1 | 5 | 1+1 | 1+2 | 5 | 2+1 | 2 | 14 (5) | 2 | 1 | 661 / 186 / 690 | 1250 | 5(2)/4(2)/3(0) | 5 | ~53 / ~75 / ~14 / ~56 |
| fy3-10 | 1+1 | 1 | 9 | 1+1 | 1+2 | 4+1 | 1 | 2 | 15 (5) | 1 | 1 | 674 / 236 / 724 | 1504 | 5(2)/4(2)/3(0) | 5 | ~58 / ~80 / ~16 / ~56 |
| fy3-11 | 1+1 | 2 | 4 | 1+1 | 2+2 | 5 | 2 | 2 | 14 (4) | 2 | 2 | 918 / 300 / 717 | 1445 | 5(2)/4(2)/3(0) | 4 | ~58 / ~80 / ~11 / ~56 |
| fy3-12 | 1+1 | 2 | 4 | 1+1 | 1+2 | 4+1 | 0 | 0 (ei sim.) | 9 (5) | 2 | 1 | 604 / 250 / 671 | 1073 | 5(2)/4(2)/3(0) | 5 | ~41 / ~63 / ~17 / ~56 |
| fy3-13 | 1+1 | 2 | 4+1 | 1+1 | 1+2 | 3+2 | 0 | 0 (ei sim.) | 8 (7) | 1 | 2 | 541 / 372 / 617 | 939 | 5(2)/4(2)/3(0) | 7 | ~37 / ~59 / ~24 / ~56 |
| fy3-14 | 1+1 | 1+1 | 3+1 | 1+1 | 1+2 | 4+1 | 1+1 | 1+1 | 9 (9) | 1 | 2 | 744 / 328 / 402 | 1134 | 5(2)/4(2)/3(0) | 7 | ~40 / ~62 / ~24 / ~56 |
| fy3-15 | 1+1 | 2 | 4+1 | 1+1 | 1+2 | 4+1 | 0 | 0 (ei sim.) | 9 (6) | 1 | 1 | 749 / 264 / 617 | 986 | 5(2)/4(2)/3(0) | 6 | ~41 / ~63 / ~19 / ~56 |
| fy3-16 | 1+1 | 2 | 3+1 | 1+1 | 1+2 | 4+1 | 0 | 0 (ei sim.) | 8 (6) | 1 | 2 | 784 / 341 / 625 | 883 | 5(2)/4(2)/3(0) | 6 | ~41 / ~63 / ~20 / ~56 |
| fy4-1 | 2 | 3 | 6 | 2 | 3 | 4 | 3 | 3 | 21 (0) | 2 | 3 | 516 / 233 / 942 | 1839 | 5(2)/4(2)/3(0) | **0** ⚠ | ~72 / ~94 / ~0 / ~56 |
| fy4-2 | 2 | 2 | 6 | 2 | 3 | 4 | 2 | 3 | 22 (0) | 3 | 3 | 693 / 238 / 747 | 1647 | 5(2)/4(2)/3(0) | **0** | ~71 / ~93 / ~0 / ~56 |
| fy4-3 | 1+1 | 2 | 4 | 1+1 | 2+1 | 4 | 2 | 1 | 13 (3) | 2 | 2 | 697 / 229 / 531 | 1305 | 5(2)/4(2)/3(0) | 3 ⚠ | ~49 / ~71 / ~6 / ~56 |
| fy4-4 | 1+1 | 2+1 | 4+1 | 1+1 | 3 | 4 | 2+1 | 2+1 | 12 (6) | 2 | 3 | 554 / 189 / 442 | 1079 | 5(2)/4(2)/3(0) | 4 ⚠ | ~55 / ~77 / ~12 / ~56 |
| fy4-5 | 1+1 | 2 | 3+2 | 1+1 | 4 | 4 | 2 | 1+1 | 12 (6) | 2 | 3 | 901 / 225 / 502 | 1303 | 5(2)/4(2)/3(0) | 4 ⚠ | ~56 / ~78 / ~13 / ~56 |
| fy4-6 | 1+1 | 2 | 4+1 | 1+1 | 4 | 4 | 2 | 2 | 15 (3) | 2 | 3 | 946 / 258 / 471 | 1487 | 5(2)/4(2)/3(0) | 3 ⚠ | ~60 / ~82 / ~7 / ~56 |
| fy4-7 | 2 | 2 | 5+1 | 2 | 3 | 4 | 2 | 3+1 | 20 (3) | 3 | 3 | 742 / 188 / 656 | 1434 | 5(2)/4(2)/3(0) | 1 | ~68 / ~90 / ~5 / ~56 |
| fy4-8 | 1+1 | 2+1 | 4+1 | 1+1 | 2+1 | 4 | 2+1 | 2+1 | 12 (6) | 2 | 2 | 1001 / 250 / 475 | 1137 | 5(2)/4(2)/3(0) | 5 ⚠ | ~57 / ~79 / ~13 / ~56 |
| fy4-9 | 1+1 | 2 | 4+1 | 1+1 | 2+1 | 4 | 2 | 2+1 | 13 (5) | 2 | 2 | 873 / 209 / 475 | 1233 | 5(2)/4(2)/3(0) | 4 ⚠ | ~55 / ~77 / ~11 / ~56 |
| fy4-10 | 1+1 | 2+1 | 4+1 | 1+1 | 2+1 | 4 | 2+1 | 2+1 | 13 (6) | 2 | 2 | 950 / 233 / 541 | 1328 | 5(2)/4(2)/3(0) | 5 ⚠ | ~57 / ~79 / ~14 / ~56 |
| fy4-11 | 1+1 | 3 | 5+2 | 1+1 | 1+2 | 4 | 3 | 2+1 | 14 (8) | 2 | 3 | 970 / 178 / 597 | 1217 | 5(2)/4(2)/3(0) | 6 ⚠ | ~59 / ~81 / ~20 / ~56 |
| fy4-12 | 1+1 | 3 | 5+1 | 1+1 | 2+1 | 3+1 | 3 | 2+1 | 15 (8) | 1 | 3 | 745 / 253 / 591 | 1220 | 5(2)/4(2)/3(0) | 5 ⚠ | ~58 / ~80 / ~16 / ~56 |
| fy4-13 | 1+1 | 1+1 | 3+2 | 1+1 | 3 | 4 | 1+1 | 1+1 | 11 (8) | 2 | 3 | 645 / 272 / 506 | 1158 | 5(2)/4(2)/3(0) | 5 ⚠ | ~50 / ~72 / ~16 / ~56 |
| fy4-14 | 1+1 | 3 | 4+1 | 1+1 | 2+1 | 4 | 3 | 2+1 | 14 (5) | 2 | 3 | 727 / 226 / 596 | 1336 | 5(2)/4(2)/3(0) | 4 ⚠ | ~55 / ~77 / ~15 / ~56 |
| fy4-15 | 1+1 | 2 | 3 | 1+1 | 2+1 | 4 | 2 | 0 (ei sim.) | 9 (3) | 2 | 3 | 701 / 196 / 559 | 952 | 5(2)/4(2)/3(0) | 3 ⚠ | ~46 / ~68 / ~9 / ~56 |
| fy4-16 | 1+1 | 2 | 3 | 1+1 | 3 | 4 | 2 | 0 (ei sim.) | 10 (2) | 2 | 3 | 920 / 289 / 711 | 1328 | 5(2)/4(2)/3(0) | 2 ⚠ | ~55 / ~77 / ~4 / ~56 |

**Kursseittain** (keskiarvot, karkea arvio):

| Kurssi | Lukuja | Teoria+esim. (sanaa, ka.) | Ydinsyötteitä (ka.) | Valinnaisia (ka.) | Arvio sivun ydinpolku (min, ka. ja vaihteluväli) | Arvio + 4 ydintehtävää (min, ka.) |
|---|---|---|---|---|---|---|
| FY1 | 8 | 922 | 15.4 | 3.9 | ~53 (39–70) | ~75 |
| FY2 | 8 | 782 | 12.5 | 3.9 | ~49 (41–63) | ~71 |
| FY3 | 16 | 925 | 10.1 | 6 | ~44 (37–58) | ~66 |
| FY4 | 16 | 1015 | 14.1 | 3.4 | ~58 (46–72) | ~80 |

Kaikissa luvuissa tehtäviä on 5/4/3, ja ydintehtäviä on 2 + 2 + 0. Joka luvussa on yksi seitsenvaiheinen esimerkki. Yhdessäkään luvussa teoriaa ei ole merkitty valinnaiseksi.

## 4. Havainnot

### 4.1 Ydinpolku on olemassa, mutta luvut kertovat siitä eri tavoin

**Toimii hyvin (pohjan ansiota):** valinnaiset osat ovat suljetuissa `details`-laatikoissa, joissa on *Valinnainen*-merkki. Sivun alussa lukee "Ydinpolku: etene vaiheiden mukaan … Valinnaisia tehtäviä n" ja Tehtävissä "Aloita ydintehtävistä …". Lisäksi tehtävissä on *Ydintehtävä*-merkinnät, eikä yksikään vaadittu ennuste tai johtopäätös voi nojata valinnaiseen kokeeseen (`scripts/inquiry.py`).

**Ristiriita.** Pohjan teksti (`lang/fi.json` `lesson.exercise_path`) neuvoo tekemään ydintehtävät eli kaksi tason 1 ja kaksi tason 2 tehtävää. Taso 3 on valinnainen. Luvun oma Tehtävät-johdanto (`inquiry.json`, `exercises.text`) sanoo kuitenkin 18 luvussa: **"Taso 1 riittää perusosaamiseen; tasot 2 ja 3 ovat vapaaehtoisia ja syventäviä"**. Näin lukee luvuissa fy1-1, fy1-3, fy1-6, fy2-1, fy4-1, fy4-3, fy4-4, fy4-5, fy4-6, fy4-8, fy4-9, fy4-10, fy4-11, fy4-12, fy4-13, fy4-14, fy4-15 ja fy4-16. Molemmat tekstit näkyvät sivulla peräkkäin, esimerkiksi `site/fy4-8.html`, joten opiskelija saa kaksi eri vastausta kysymykseen "mitä minun pitää tehdä".

**Valinnaiset puuttuvat kokonaan** luvuista fy4-1 ja fy4-2, ja fy2-1:ssä niitä on vain yksi. Juuri fy4-1 ja fy4-2 ovat koko aineiston raskaimmat: niissä on 21–22 ydinsyötettä ja kolme ennustetta, kolme koetta, kaksi aineistoa, pohdinta, virheen etsintä, siirtotehtävä, kolme tarkistusta ja kolme exit-kysymystä, kaikki pakollisia. FY4:n scope-huomautuksen mukaan "FY4.1 … stays as it is", joten fy4-1:n merkinnät ovat opettajan päätettävissä.

**Mikä on valinnaista, vaihtelee kursseittain.** FY3 noudattaa järjestelmällisesti NOTES §5:n ydinpolkusääntöä (2026-10-26): kertaus, Palaa ennusteisiisi, Etsi virhe, siirtotehtävä ja kolmas tarkistus ovat valinnaisia. FY4:ssä siirtotehtävä ja kolmas tarkistus ovat yleensä pakollisia. Osin syy on perusteltu: voimakuviosuunnitelma vaatii vähintään yhden itse piirretyn kuvion (`"draw": true` luvuissa fy4-3–fy4-6, fy4-13 ja fy4-14). Pohdinta on pakollinen luvuissa fy1-1, fy1-3, fy2-1, fy4-1, fy4-2 ja fy4-7, muualla valinnainen. Saman kurssin sisällä opiskelija ei siis voi oppia, mitä tietyntyyppinen osa yleensä edellyttää.

**Sivun "loppu" on kahdessa paikassa.** Exit ticket alkaa sanoilla "Lopuksi … nopeaa kysymystä", mutta sen jälkeen tulevat Tehtävät ja niissä neljä ydintehtävää. Ydinpolkuhuomautuksessa ei sanota, kuuluvatko ydintehtävät tunnilla tehtävään polkuun vai kotitehtäviin. Arvion mukaan tällä on käytännön merkitystä: sivun ydinpolku vie FY4:ssä noin 58 min ja ydintehtävien kanssa noin 80 min.

### 4.2 Ydintehtävät erottuvat lisäharjoittelusta Tehtävät-osiossa

Tasot ja *Ydintehtävä*-merkinnät ovat selkeitä, ja tasojen johdannot sanovat "Ydintehtävät ensin, loput lisäharjoitusta". Ainoa ongelma on 4.1:n ristiriitainen johdanto. Inquiry-vaiheissa ydin ja lisä erottuvat valinnaisuuslaatikoista, ja ne ovat näkyviä ja johdonmukaisia.

### 4.3 Päällekkäisyys

**(a) Sama Miksi-selitys kirjoitetaan monta kertaa.** Kirjoittaminen on ydinpolun hitain osa (noin 4 min/selitys, arvio).
- **Kolme kertaa ydinpolulla:** fy1-3 (Johtopäätös: mitä keskiarvo korjaa → Palaa ennusteisiisi: mitä toistaminen korjaa → Tarkista 3: mitä toistaminen satunnais- ja systemaattiselle virheelle tekee; lisäksi exit 2 kysyy saman). Samoin fy2-1 (minne pallon energia meni: Johtopäätös → pohdinta → Tarkista 4 → exit 2), fy4-2 ja fy4-7. Kahdessa viimeksi mainitussa sekä pohdinta että Tarkista 3 alkavat sanoilla "Palaa alun …" tai "Selitä alun ilmiö".
- **Kaksi kertaa:** FY4:n luvuissa fy4-1, fy4-8, fy4-9, fy4-10, fy4-11 ja fy4-15 kolmas tarkistus pyytää selittämään alun ilmiön, jonka Johtopäätös on jo selittänyt (fy4-1:ssä Johtopäätöksen sijaan pohdinta). Silloin tarkistus mittaa juuri kirjoitetun muistamista eikä siirtoa. FY3 tekee saman paremmin: fy3-11:n ja fy3-12:n kolmas tarkistus on muotoa "Ystäväsi väittää …", eli sama idea uudessa tilanteessa.
- **fy2-6:** "tuulivoimaa ei voi säätää ja nimellisteho ei kerro tuotantoa" kysytään Johtopäätöksessä, tarkistuksissa 1, 2 ja 3 sekä exit ticketissä. Tarkista-vaiheessa on viisi pakollista osaa, kun ohje sanoo kolme.

**(b) Exit ticket ja tarkistukset toistavat ydintehtävää tai luvun omaa esimerkkiä.** `docs/inquiry.md` sanoo, että exit ticket kysyy, mitä tarkistukset eivät kysy. Ydintehtäviä tämä ei kuitenkaan koske, ja niissä toisto näkyy.
- **Exit-kysymys on sama yhden kaavan sijoitus kuin tason 1 ydintehtävä**, joka tehdään heti perään: fy1-5 ($s = vt$), fy1-7 ($\rho = m/V$ ja litrat), fy2-2 (kJ → J), fy2-5 ($E = Hm$), fy2-6 ($E = Pt$), fy3-6 ($Q = cm\Delta T$), fy3-8 ($\Delta l$), fy3-9 (ruisku ja Boylen laki, lähes sama tilanne kuin L1), fy3-10 ($n = pV/RT$), fy3-12 (U-arvo), fy3-13 (kulmakerroin), fy3-14 (sulamislämpö), fy3-15 (hyötysuhteiden ketju), fy4-1 (etumerkillinen siirtymä) ja fy4-10 (ilmakivääri sekä exitissä että L2:ssa). FY4:n exit-kysymykset ovat muuten useimmiten käsitteellisiä, ja se toimii hyvin.
- **Samat lähtöarvot:** fy2-4:n pakollinen Etsi virhe (ledi 8,0 W → 2,4 W, hyötysuhde väärin päin) ja ydintehtävä L1-02 (sama ledi, samat luvut) ovat käytännössä sama tehtävä. Lisäksi Etsi virheen palaute näyttää oikean laskun. fy3-6:n tarkistus 2 (1,0 kg 80 °C:n vettä ja 3,0 kg 20 °C:n vettä → 35 °C) on lasku, joka on ratkaistu jo Yleinen virhekäsitys -osiossa, joten se mittaa muistamista eikä osaamista. Samaan suuntaan menee fy2-7:n valinnainen Etsi virhe (500 MWh, 4 %), jossa on samat luvut kuin L1-01:ssä.
- **fy4-6:n exit 3** (massa ja paino Kuussa) ja ydintehtävä L1-01 (astronautti Kuussa) toistavat FY3:n luvun *Voima ja paino* asiaa eivätkä mittaa kitkaa, josta luku kertoo.
- **fy4-13** käsittelee samaa kärry–punnus-systeemiä ennusteessa, kokeessa, johtopäätöksessä, esimerkissä, Etsi virheessä, siirtotehtävässä, tarkistuksessa 2 (sama kysymys kuin esimerkissä, eri luvuin), exit-kysymyksissä 1 ja 3 sekä ydintehtävissä. Yksi kanoninen systeemi on aiheeseen sopiva valinta, mutta tarkistus 2 ja exit 3 eivät tuo enää mitään uutta.

Tavoiteltavaa päällekkäisyyttä on myös: sama idea eri esitysmuodossa, eli ennusteesta kuvaajaan, laskuun ja selitykseen. Sitä ei kannata karsia.

### 4.4 Ovatko vaiheet perusteltuja vai mekaanisia?

- **Ennusta → Tutki simulaatioluvuissa: perusteltu.** Ennuste lukittuu, ja sen palaute avautuu vasta, kun koe on kirjattu (`reveal.after`). Kokeissa vain yksi muuttuja muuttuu ja muut on lukittu, joten koe pystyy kumoamaan ennusteen. Esimerkiksi fy3-6:ssa ja fy4-1:ssä tämä toimii mallikkaasti.
- **Ennusta simulaatiottomissa FY1–FY2-luvuissa: mekaaninen.** Seuraavien lukujen ennusteissa ei ole `reveal`-kenttää, ja oikean vaihtoehdon palaute "Oikein. …" kertoo vastauksen perusteluineen heti valinnan jälkeen: fy1-7 (ennusteet 1 ja 2), fy1-8, fy2-5 (1 ja 2), fy2-6, fy2-7 (1 ja 2) ja fy2-8 (ennuste 2). Tutki-vaiheen aineisto vain vahvistaa jo kerrotun. Esimerkiksi fy2-6 kysyy "Mikä energialähde tuotti eniten sähköä vuonna 2024?", ja palaute vastaa siihen ennen taulukkoa. FY3:n simulaatiottomat luvut tekevät tämän paremmin: fy3-12, fy3-13, fy3-15 ja fy3-16 vastaavat "Tutki-vaiheen taulukko testaa tätä …" eivätkä kerro vastausta.
- **Tutki: perusteltu, paikoin raskas.** fy3-10:ssä on yhdeksän pakollista Tutki-aktiviteettia ja kaksi todistusaineistoa (punnitus ja simulaatio). Molemmille on syy, mutta koe 2 (lämpötila kaksinkertaistuu, hiukkasmäärä puolitetaan) ja taulukko "Mikä pysyy samana?" osoittavat saman yhdistetyn riippuvuuden, ja lämpötilariippuvuus on jo luvun pohjatiedoissa.
- **Teoriatiivistelmä: perusteltu.** Teoria tulee todisteiden jälkeen ja vastaa alun kysymykseen (esimerkiksi fy4-11: "Tästä saadaan vastaus alun kysymyksen ensimmäiseen osaan"). Kappaleet ovat lyhyitä ja väliotsikoituja. fy1-1 on poikkeus: teoriaa on noin 1300 sanaa viidessä osiossa. Osio *Aurinkokunnan reuna* (heliosfääri, Oortin pilvi) ei liity yhteenkään tehtävään.
- **Sovella FY3:ssa: ydinpolulla pelkkää lukemista.** FY3:n kaikissa 16 luvussa Etsi virhe ja siirtotehtävä ovat valinnaisia, joten Sovella-vaiheen ydin on porrastettu esimerkki. Ohjattu soveltaminen siirtyy siis ydintehtäviin. Tämä on johdonmukaista NOTES §5:n kanssa, ja FY3 on muutenkin kevein kurssi (noin 44 min arvio). Tällä vaiheella on silti vähemmän omaa tehtävää kuin muissa.
- **Tarkista: perusteltu, mutta määrä vaihtelee.** Tarkistuksia on FY3:ssa 2–3, FY4:ssä 3, FY1:ssä 3–4 ja FY2:ssa 3–5. Lisäksi exit ticketissä on FY4:ssä yleensä 3 kysymystä ja FY3:ssa 1–2, joten FY4:ssä kertauskysymyksiä on kuusi ennen ydintehtäviä.

### 4.5 Pääseekö avainsisältöön ilman lisätehtäviä?

Pääsee kaikissa 48 luvussa. Koko teoria on ydinpolulla, ja pakolliset ennusteet ja johtopäätökset nojaavat vain pakollisiin kokeisiin (validaattori). Lisäksi jokaisella oppimistavoitteella on vähintään yksi pakollinen tarkistus. Valinnaisia osia on keskimäärin 3–6, ja ne ovat aidosti syventäviä: kertaus, lisäkoe, Etsi virhe ja siirtotehtävä. Moduulin lopun Sovella itsenäisesti -tehtävät (FY1 3, FY2 1, FY3 3 ja FY4 3 tehtävää, 12–19 pistettä kukin) ovat oma sivunsa eivätkä kuulu lukujen ydinpolkuun.

### 4.6 Teorian ja tehtävien suhde

Näkyvää teoriaa ja esimerkkiä on keskimäärin 782 (FY2) – 1015 (FY4) sanaa. Arvion mukaan sen lukeminen vie noin 7–9 min, kun ydinpolun tehtävät vievät noin 28–38 min ja ydintehtävät noin 22 min. Suhde sopii tutkivaan oppimiseen. Raskaus tulee tehtävien määrästä, kun sama asia kysytään moneen kertaan (4.3), ei tekstistä. Piilossa olevaa tekstiä (palautteet, vihjeet ja malliratkaisut) on keskimäärin noin 1150 sanaa luvussa. Se on hyvä tuki, mutta se kasvattaa todellista aikaa sen mukaan, kuinka paljon siitä opiskelija lukee.

## 5. Suositukset tärkeysjärjestyksessä

Suosittelen vain rakenteellisia muutoksia. Mitään perustelua tai syy-askelta ei poisteta, eikä tekstejä lyhennetä mekaanisesti. **Pohja** tarkoittaa yhteistä toteutusta (`lang/fi.json`, `scripts/inquiry.py`, `scripts/build.py`, `scripts/lint_lesson.py`, `docs/inquiry.md`, `NOTES.md`), **luku** yksittäisen luvun tiedostoa.

**1. Yksi yhtenäinen ydinpolkuviesti.** *(Pohja ja 18 lukua, pieni työ, suurin hyöty.)*
- *Luvut:* poistetaan tasopolitiikka ("Taso 1 riittää … tasot 2 ja 3 ovat vapaaehtoisia …") `inquiry.json`-tiedoston `exercises.text`-kentästä luvuissa fy1-1, fy1-3, fy1-6, fy2-1, fy4-1, fy4-3–fy4-6 ja fy4-8–fy4-16. Luvun omat neuvot jätetään ("Piirrä ensin voimakuvio …").
- *Pohja:* `lang/fi.json` `inquiry.core_path` kertoo yhdellä lauseella, mitä ydinpolkuun kuuluu: vaiheiden merkitsemättömät osat, exit ticket ja neljä ydintehtävää. Exit ticketin "Lopuksi" ei saa antaa ymmärtää, että luku päättyy siihen. `lint_lesson.py` varoittaa, jos `exercises.text` määrittelee tasojen pakollisuuden, koska sen tekee pohja.
- *Miksi:* opiskelijan tärkein kysymys on "mitä minun pitää tehdä". Nyt sivu vastaa siihen kahdella tavalla.

**2. Miksi-selitys kirjoitetaan ydinpolulla kerran, ja kolmas tarkistus on siirtotehtävä.** *(Luvut ja pohjan ohje.)*
- *Luvut:* fy1-3, fy2-1, fy4-2 ja fy4-7. Pohdinta muutetaan valinnaiseksi kuten muissa luvuissa, tai kolmas tarkistus muutetaan. Luvuissa fy4-1, fy4-8, fy4-9, fy4-10, fy4-11 ja fy4-15 kolmas tarkistus ("Selitä alun ilmiö …") muutetaan selitykseksi uudessa tilanteessa, mallina fy3-11 ja fy3-12, tai siitä tehdään valinnainen. fy2-6:ssa Tarkista karsitaan viidestä kolmeen niin, että nimellisteho ja säädettävyys kysytään kerran.
- *Pohja:* `docs/inquiry.md` ja NOTES §5 saavat lauseen: tarkistusten selitys on siirtotehtävä eikä alun ilmiö uudelleen, jos Johtopäätös jo selittää sen. Halvan varoituksen voisi antaa lint, kun pakollinen Tarkista-selitys viittaa "alun" ilmiöön ja pakollinen Johtopäätös on olemassa.
- *Miksi:* kirjoittaminen on ydinpolun kallein osa. Siirto mittaa ymmärrystä paremmin kuin juuri kirjoitetun toistaminen, ja juuri siirtoa yo-koe ja Sovella itsenäisesti vaativat.

**3. Exit ticket ja tarkistukset eivät saa olla samoja kuin ydintehtävät tai luvun omat esimerkit.** *(Luvut ja pohjan tarkistus.)*
- *Luvut:* exit-kysymys, joka on sama sijoitus kuin tason 1 ydintehtävä (fy1-5, fy1-7, fy2-2, fy2-5, fy2-6, fy3-6, fy3-8, fy3-9, fy3-10, fy3-12, fy3-13, fy3-14, fy3-15, fy4-1 (opettajan päätös, ks. kohta 5) ja fy4-10), korvataan käsitteellisellä yhteenvetokysymyksellä FY4:n tapaan. Toinen vaihtoehto on vaihtaa ydintehtäväksi saman tason toinen tehtävä merkinnällä `"core": true`. fy2-4:n Etsi virhe tai L1-02 vaihdetaan niin, etteivät lähtöarvot ole samat. fy3-6:n tarkistukselle 2 annetaan omat luvut. fy4-6:n exit 3 vaihdetaan kitkaa mittaavaksi.
- *Pohja:* `docs/inquiry.md` laajennetaan muotoon "exit ticket kysyy, mitä tarkistukset **ja ydintehtävät** eivät kysy". Kaksi samaa lähtöarvoa samassa luvussa voidaan havaita deterministisesti: sen voisi lisätä varoituksena `check_lesson.py`:hin.
- *Miksi:* toistaminen vie aikaa eikä kerro opiskelijalle mitään uutta osaamisestaan.

**4. Simulaatiottomien FY1–FY2-lukujen ennusteet testataan, ei kerrota.** *(Luvut, pohja tukee jo.)*
- *Luvut:* fy1-7, fy1-8, fy2-5, fy2-6, fy2-7 ja fy2-8 (ennuste 2). Ennusteelle lisätään `reveal: {"after": "<teoriaosio>"}`, tai palaute muotoillaan FY3:n tapaan: "Tutki-vaiheen taulukko testaa tätä …". Varsinainen vastaus siirretään Johtopäätöksen malliratkaisuun.
- *Miksi:* nyt Tutki-vaihe vain vahvistaa jo kerrotun, ja vaihe on mekaaninen.

**5. Valinnaisuus merkitään raskaimpiin lukuihin.** *(Luvut, opettajan päätös.)*
- fy4-2, fy2-1 ja fy1-3 (arvion mukaan noin 70 min sivulla) merkitään NOTES §5:n ydinpolkusäännön mukaan. Pohdinta, Etsi virhe tai siirtotehtävä muutetaan valinnaiseksi, ellei luvun tavoite vaadi niitä. fy4-1:ssä sama sääntö tarkoittaisi pohdintaa ja toista aineistoa (*Edestakainen liike* tai *Robotti*), mutta scope-huomautuksen mukaan luku säilyy ennallaan, joten päätös on opettajan.

**6. Harkittavat pienet muutokset.** *(Luvut, vain jos pilotti tukee.)*
- fy3-10: koe 2 tai taulukko "Mikä pysyy samana?" muutetaan valinnaiseksi (4.4).
- fy1-1: *Aurinkokunnan reuna* muutetaan valinnaiseksi teoriaksi (`theory`, `optional: true`), koska mikään tehtävä ei käytä sitä.
- FY3: pakolliseksi muutetaan se Etsi virhe, joka kohdistuu luvun päävirhekäsitykseen, jos pilotti osoittaa, että Sovella jää lukemiseksi. FY3 on kevein kurssi, joten tilaa on.

**Ei suositella:** tekstin lyhentämistä, tehtävämäärien tasaamista lukujen välillä (NOTES: "Lengths are not equalised") tai Tehtävät-osion siirtämistä takaisin ennen exit ticketiä (opettajan päätös 2026-10-26).

## 6. Pilottisuunnitelma (sivusto ei kerää tietoa)

**Periaate:** sivustolle ei lisätä mitään mittausta, lomaketta, analytiikkaa tai tallennusta. Kaikki tieto syntyy luokassa paperilla tai opettajan havainnoista, nimettömänä ja vapaaehtoisesti osana tavallista opetuksen kehittämistä. Henkilötietoja ei kerätä, joten erillistä tutkimuslupaa ei tarvita. Jos tulokset halutaan julkaista, toimitaan koulun ohjeiden mukaan.

**Mitä mitataan**
1. **Kesto vaiheittain:** kuinka kauan Pohdinta–Tutki, Teoriatiivistelmä–Sovella, Tarkista ja exit sekä ydintehtävät vievät.
2. **Ymmärsikö opiskelija, mitä ydinpolku vaatii:** "Tiesin, mitkä tehtävät olivat pakollisia" (kyllä / osittain / ei).
3. **Mitkä valinnaiset osat avattiin** ja miksi (rastit).
4. **Toiston kokemus:** "Tuntuiko jokin tehtävä samalta kuin aiempi?" ja mikä.
5. **Kuormitus** asteikolla 1–5 ja **yksi epäselvin kohta** (muddiest point).
6. **Exit ticketin tulos** opiskelijan itsearvioimana: oikein / osittain / ei.

**Miten**
- **Kulkukortti paperilla** (A5): vaiheiden nimet ja ruutu kellonajalle, johon opiskelija kirjoittaa ajan, kun aloittaa vaiheen. Lisäksi rastit valinnaisista osista ja kohdat 2–6. Ei nimeä, ei ryhmätunnusta. Opettaja kerää kortit nimettöminä laatikkoon ja laskee jakaumat (mediaani ja vaihteluväli).
- **Opettajan havainnot:** missä kohdassa luokka on 20, 40 ja 60 minuutin kohdalla, ja missä kysytään apua.
- **Ei** näyttökuvia, äänitallenteita tai opiskelijoiden laitteiden `localStorage`-tietojen lukemista.

**Mitkä luvut** (2–3 tuntia, kahdessa kierroksessa)
- Kierros A ennen muutoksia: raskas luku (fy4-2), kevyt mallikas luku (fy3-6) ja simulaatioton FY2-luku (fy2-6).
- Kierros B suositusten 1–3 jälkeen samoista luvuista seuraavan ryhmän kanssa tai vastaavista luvuista. Vertaa kestoa, kohtaa 2 ja toiston kokemusta. Ryhmät ovat pieniä ja erilaisia, joten tulokset ovat suuntaa antavia, eivät todisteita.

**Päätössäännöt (ehdotus):** jos sivun ydinpolun mediaani ylittää noin 60 min, luvusta tarkastellaan suositukset 2, 3 ja 5. Jos alle 80 % vastaa kohtaan 2 "kyllä", korjataan pohjan ydinpolkuviestiä. Jos valinnaista osaa ei avaa juuri kukaan eikä sitä tarvita Sovella itsenäisesti -tehtävissä, se on oikein valinnainen. Jos osa on usein avattu ja hyödylliseksi koettu, harkitaan sen siirtämistä ydinpolulle.
