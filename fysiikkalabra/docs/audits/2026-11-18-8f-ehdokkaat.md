# 8f Animoitu kuva: ehdokasluettelo (2026-11-18)

Vaihe 1 (vain luettelo; ei kuvia eikä sisältömuutoksia). Pohja: `docs/figures/catalog.json` (diagram-kuvat FY1–FY9),
kuvauksen perusteella ja `figcat.py`-lähteen mukaan. Vain Python-figuurit (`lessons/*/figures.py`); kuvituskuvat
(`illustration`, `pics/`) on jätetty pois, koska opettaja piirtää ne uusiksi. FY9:n luvut käyttävät FY1–FY8:n kuvia
(`fy9-*-sovella` ovat kuvaajia), joten niille ei löytynyt omia ehdokkaita.

**Tekniikka ja sen rajat.** Pilotti (`Fig(anim=True)`, `vibrate()`) osaa nyt vain vaakasuuntaisen edestakaisen
värähtelyn (CSS, ±amp, jakso, vaihe). Se riittää kohtiin 1–3 sellaisenaan (S). Kulkevat aallot, kiertoliike ja
hiukkasten siirtymä tarvitsevat uuden primitiivin (`travel()`/`orbit()`/`drift()` figlibiin, yksi kertainen yhteinen
muutos, joka tehdään yksin ja ennen sisältöä: CLAUDE.md sääntö 3). Työmäärä S = vain `vibrate()`, M = uusi
primitiivi + yksi kuva, L = useita primitiivejä tai monta tilaa. Kaikki ehdokkaat noudattavat pilotin vaatimuksia:
▶/❚❚-painike, `prefers-reduced-motion` ja tuloste = nykyinen still-kuva; uusi piirros tarvitsee opettajan
hyväksynnän ja tiedekatselmoinnin.

## Järjestys (hyödyn mukaan)

| # | Luku | Kuva (figcat) | Mikä liikkuu ja miksi auttaa | Työ | Väärinkäsityksen riski |
|---|------|---------------|------------------------------|-----|------------------------|
| 1 | fy5-10 | `fy5-10/birth` | Narun pää heiluu ja pulssi etenee: neljä peräkkäistä still-kuvaa korvautuu yhdellä silmukalla; näkyy, että hiukkanen vain värähtelee paikallaan ja aalto kulkee. Aallon ydinkäsite. | M (`travel()`) | Matala. Merkitään yksi hiukkanen (väri), ettei näytä aineen siirtyvän. |
| 2 | fy5-10 | `fy5-10/types` | Poikittainen ja pitkittäinen aalto vierekkäin: ainehiukkasten värähtelysuunta vs. etenemissuunta. Still-kuva ei erota suuntia. | M | Matala–keski. Pitkittäisessä tihentymät ≠ hiukkasten siirtyminen; yksi seurattu hiukkanen. |
| 3 | fy5-13 | `fy5-13/superpositio`, `fy5-13/solmut` | Vastakkain kulkevien aaltojen summa ja seisova aalto: solmut pysyvät, kupu värähtelee. Kolmen still-hetken sijaan jatkuva. | M–L (kaksi kuvaa) | Keski. Seisova aalto ei "seiso" energian mielessä; teksti kertoo energian siirtymättömyyden vain vertauksena. Solmut merkittävä pysyviksi. |
| 4 | fy5-7 | `fy5-7/ympyra`, `fy5-7/osat` | Pisteen kiertoliike ympyrällä ja sen projektio jousipunnuksen värähtelyksi (vaihe, A, T). Vaikeasti hahmotettava still-kuvasta. | M (`orbit()`) | Matala. Projektio on vain vertaus; ei väitetä, että punnus kiertäisi. |
| 5 | fy3-9 / fy3-3 | `fy3-9/micro-boyle`, `fy3-3/micro-model` | Kaasuhiukkaset liikkuvat satunnaisesti ja törmäävät seinään; pienempi tilavuus → tiheämmät iskut → suurempi paine. Pilotin jatko, sama hiukkasmalli. | M (`drift()`) | Keski. Hiukkasten koko liioiteltu ja liike satunnaista, ei kaikki samaan suuntaan; "ei mittakaavassa" -merkintä säilyy. |
| 6 | fy3-10 | `fy3-10/paine-ja-tekijat` | Neljän sylinterin hiukkasnopeus/lukumäärä/tilavuus: iskutiheys näkyy suoraan. | M–L (neljä paneelia) | Keski, sama kuin 5. |
| 7 | fy6-3 | `fy6-3/micro` | Elektronien ajautuminen ionihilassa kentän vaikutuksesta: nopea satunnaisliike + hidas ajautuminen, ionit värähtelevät (vastus). Tärkein sähkövirtamalli. | M–L | **Korkea**: ajautumisnopeus on pieni, mutta animaatio näyttää liian nopealta. Elektronit liikkuvat kentälle vastakkaiseen suuntaan; virran suunta = sopimus. Vaatii huolellisen science-katselmoinnin. |
| 8 | fy5-14 | `fy5-14/pitkittainen`, `fy5-14/doppler` | Ääni ilmassa (tihentymät) ja Dopplerin siirtymä: liikkuvan lähteen aaltorintamat tihenevät edessä. Aaltorintamat näyttävät ilmiön, still vain lopputuloksen. | M | Matala–keski. Ilmahiukkaset eivät kulje lähteestä korvaan; yksi seurattu hiukkanen. |
| 9 | fy5-12 | `fy5-12/kuvio` | Kahden lähteen rengasaallot altaassa: solmu- ja kupuviivat muodostuvat. Näyttää interferenssin syntymisen. | L (kaksi lähdettä, laskettu kenttä) | Keski. Solmuviivat paikallaan, vaikka aallot liikkuvat. |
| 10 | fy4-10 | `fy4-10/vuorovaikutus`, `fy4-10/tyypit` | Kaksi vaunua törmää: liikemäärät ennen ja jälkeen, kimmoinen/täysin kimmoton. Sopii vaiheittaiseen (▶ + paluu). | M | Matala. Törmäyksen aikainen voima ei saa näyttää lopulliselta; nuolten pituudet mittakaavassa. |
| 11 | fy7-9 | `fy7-9/wave` | Sähkömagneettinen aalto: E ja B värähtelevät kohtisuoraan ja etenevät. Still-kuva näyttää vain yhden hetken. | M | **Korkea**: E- ja B-nuolet kuin liikkuisivat tilassa; kuvaa vain yhtä suoraa pitkin; ei aallon "muotoa avaruudessa". |
| 12 | fy7-2 | `fy7-2/circle-path` | Varattu hiukkas kiertää ympyrärataa magneettikentässä; voima aina kohtisuoraan, nopeus ei kasva. | M (`orbit()`) | Keski. "Voima ei tee työtä" -väärinkäsitys: nuolet voimakuvassa pysyvät kohtisuorina. |
| 13 | fy5-3 | `fy5-3/tangent`, `fy5-3/release` | Kiertoliikkeen nopeuden suunta tangentin suuntaan ja irtoaminen radalta. | M | Matala. Irrotuksessa kappale jatkaa suoraan, ei ulospäin. |
| 14 | fy8-4 | `fy8-4/buildup` | Kaksoisrakokoe: yksittäiset osumat kertyvät kuvioksi. Aika on olennaista, still näyttää vain kolme vaihetta. | M | Keski. Satunnaisuus: osumakohta arvottu, ei "valittu"; kuvio on todennäköisyysjakauma. |
| 15 | fy3-7 | `fy3-7/micro-model` | Kiinteän aineen hiukkasten värähtely paikallaan (pilotin kaltainen, ei lämpötilaa). Luontevin `vibrate()`-jatke. | S | Matala. Mutta osittain päällekkäinen pilotin kanssa; ehkä yhdistettävä fy3-8:aan. |

(Taulukossa 15 riviä; opettajan raja oli 10–15. Rivejä 13–15 voi jättää pois, jos budjetti on tiukka.)

## Ei-ehdokkaat ja perusteet
- FY1–FY2: `fy1-6/free-fall`, `fy1-5/motion` jne. ovat stroboskooppikuvia (eri hetkien paikat samassa kuvassa); liikkeen
  animointi piilottaisi juuri tarkoitetun vertailun. Energiakuvat (`fy2-*`, `fy3-11`) ovat Sankey-virtauksia, ei liikettä.
- FY6 kytkentäkaaviot ja kenttäviivakuvat (`fy6-10/11`, `fy7-1/3`): staattisia kenttiä; "virran suunta" -animaatio
  ruokkisi vanhaa virtamallia. `fy6-1/virta` (elektronit johtimessa) on kohdan 7 yksinkertaisempi esikuva.
- FY8 energiatasot, ydinkaaviot: tilakaavioita, joissa liike olisi koristetta.
- FY9-kokonaisuuksien omat kuvat ovat kuvaajia (`graph`) ja harjoituskokeen/Sovella-kuvia; animointi ei lisää niille.

## Ehdotettu järjestys toteutukselle
1. Yhteinen primitiivi (`travel()`) yksin ja ensin (sääntö 3) → kohdat 1–2 (aalto).
2. `drift()` → 5, 6 (kaasu), sitten 7 (virta) vasta tiedekatselmoinnin kanssa.
3. `orbit()` → 4, 12, 13.
4. Loput tarpeen mukaan. Yksi kurssi kerrallaan (FY5 ensin: 1, 2, 3, 4, 8, 9, 13).
