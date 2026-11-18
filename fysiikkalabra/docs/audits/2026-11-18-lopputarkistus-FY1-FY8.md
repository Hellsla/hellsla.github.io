# Lopputarkistus FY1–FY8 (työjono 15, kevennetty): raportti

Päivä 2026-11-18, haara `claude/15-lopputarkistus`. **Vain raportti: lähdekoodia ja sisältöä ei muokattu.** Vertailuperusta LOPS 2019;
julkaistuja oppikirjoja ei käytetty; virheitä ei oletettu. Katselmoijien täydet raportit (`*-audit-*.md`) ovat kansiossa
`2026-11-18-lopputarkistus-FY1-FY8-katselmoinnit/`.

## Yhteenveto

- **Automaattiset läpikäynnit (1): ei kriittisiä löydöksiä.** Kaikki neljä ajoa läpi; neljä `physics_phrases`-varoitusta ovat todennäköisesti vääriä hälytyksiä.
- **Otos (2): tehty vain FY1–FY4.** Budjetin ($15) vuoksi FY5–FY8 jätettiin tekemättä (työjonon ohje: "jos ylittyisi, tee otos FY1–FY4 ja kirjaa loput").
- **Kriittisiä virheitä ei löytynyt** (Critical-luokkaa ei yhdessäkään raportissa) → laajennusta ei suositella (kohta 3). Neljä **Major**-löydöstä, kaikki yksittäisiä ja pieniä korjata.
- Katselmointitulokset: 12 ajoa, 8 PASS ja 4 FAIL (kaikissa FAIL-tapauksissa syynä Major tai Blocking-merkitty Minor).

## 1. Automaattiset läpikäynnit

| Ajo | Tulos |
|---|---|
| `coverage.py --all --check` | Kaikki 8 kurssiraporttia ajan tasalla (OK). Aukkoja: FY1 mallin valinta (2 p), FY2 kuvaajat ja kokeellinen päättely (1 p, kuvaajan laatiminen puuttuu Sovella-tehtävistä), FY3 kokeellinen päättely ja kuvaajan laatiminen (2 p), FY7 ja FY8 kuvaajan laatiminen (2 p). FY4–FY6 ei aukkoja. Kaikki ovat "ohut näyttö", ei virheitä. |
| `check_a11y.py site` | 817 sivua, ei saavutettavuusongelmia. |
| `physics_phrases.py` | 4 varoitusta `heat-into`: FY6 fy6-10 exercises.json ja solutions.md:147 ("varaus ei muutu lämmöksi" – kieltävä, oikea), FY6 sovella/solutions.md:207 (virheellinen väite lainataan arvosteltavaksi), fy9-lampo sovella/solutions.md:160 (FY9, kurssin ulkopuolella; "Energia säilyy"). Kaikki lauseyhteydestä arvioiden hälytyksiä, ei opetettua virhettä. Suositus: tiedeluku vahvistaa, ei korjausta. |
| `concepts.py list` | Vain laskuri (9 käsitettä, 346–2637 kohtaa, 12–97 lukua); ristiin­tarkistus vaatii tiedekatselmoijan käsitepaketin per käsite, mikä ylittäisi budjetin. **Ei ajettu: avoin.** Ehdotus: yksi käsite kerrallaan erikseen (esim. `internal-energy`, `uncertainty`) opettajan valinnan mukaan. |

## 2. Otos

Valitut luvut: FY1 fy1-6, FY2 fy2-4, FY3 fy3-6, FY4 fy4-4. FY5–FY8: **ei tehty (budjetti)**; ehdotetut luvut jatkoa varten: fy5-9, fy6-5, fy7-5, fy8-9.
Kaikilla luvuilla `round.py` antoi checks: ok. Katselmoijat: science-reviewer (Opus), pedagogy-reviewer ja visual-editorial-reviewer (Sonnet), täysi audit-tila.

| Luku | Tiede | Pedagogia | Visuaali |
|---|---|---|---|
| fy1-6 Putoamiskiihtyvyys | PASS (5 Minor) | PASS (2 Major, 5 Minor) | PASS (Minor) |
| fy2-4 Hyötysuhde | **FAIL** (1 Major) | **FAIL** (2 Major) | PASS (Minor) |
| fy3-6 Q = cmΔT | **FAIL** (1 Minor, Blocking) | PASS (1 Major, 6 Minor) | PASS (Minor) |
| fy4-4 Newtonin II laki | **FAIL** (1 Major) | PASS (5 Minor) | PASS (Minor) |

Pisteet (1–5): fysiikka 5 / 2 / 3 / 3 (fy1-6, fy2-4, fy3-6, fy4-4); kuvitus 4–5, typografia 4–5, suomen kieli 4–5, saavutettavuus 4 kaikissa.
Huom. pedagogia- ja visuaalikatselmoijat arvioivat paketista ilman sivukaappauksia osin (pedagogia ei saanut niitä); tehtäväsarjoja ei arvioitu tässä.

### Varmennetut virheet (Major)

| # | Luku | Kohta | Ongelma | Korjausehdotus | Tarkistus korjauksen jälkeen |
|---|---|---|---|---|---|
| M1 | fy2-4 | `inquiry.json:396`, check-patteri, väärä vaihtoehto "Alle 100 %, koska minkään laitteen hyötysuhde ei voi olla 100 %" | Puolustettavissa rinnan oikean vaihtoehdon "Lähes 100 %" kanssa; palaute ("ei aina sen alle") ristiriidassa avaimen kanssa; `lesson.md:91` tukee väärää vaihtoehtoa. | Vaihda väärän vaihtoehdon väite selvästi erilaiseksi (esim. "Noin 50 %, koska johdot lämpenevät") ja palaute vastaavasti. | science, uusi round.py |
| M2 | fy2-4 | `inquiry.json` ennuste-1 / koe-1 | Koe vain toistaa simulaation syötteen η; koe-1:n johdanto kertoo 25 % valmiiksi; koe vaihtaa vain aikaa, joten ennustetta ei voi kumota. | Ennusteeksi η:n aikariippumattomuus tai laitteiden vertailu samalla $P_o$:lla; poista 25 % koe-1:n johdannosta. | pedagogy |
| M3 | fy2-4 | `inquiry.json` johtopäätös | Kysyy η:n riippuvuutta ajasta, mutta aikaennuste (ennuste-2), koe-2 ja pohdinta ovat valinnaisia; ydinajatus ei tule ydinpolulla ennustetuksi. | Tee ennuste-2 pakolliseksi tai muuta johtopäätöstä. | pedagogy |
| M4 | fy4-4 | `lesson.md:622`, Tulos-vaihe | "Kokonaisluku 480 kg tulkitaan tarkaksi arvoksi" on väärä sääntö (NOTES P7: mitatun massan loppunolla lasketaan); vastaus 1,02 m/s² on oikein, vain perustelu väärä. | Poista lause; nimeä 480 kg, 5,20 kN ja 9,81 m/s² kolmen numeron lähtöarvoiksi. | science |

### Minor/mahdolliset ja parannusehdotukset (poimintoja)

**fy1-6:** Dataväite "noin 0,1 m/s" poikkeamaksi, vaikka pisteet ovat ≤ 0,04 m/s päässä suorasta (`inquiry.json:339`, tehtävä Major valinnaisessa, tiede Minor); `siirto` vastaus 11.1 vs ratkaisu 11 m/s; kokeet 1–2 toistavat vain mallin sisäänrakennetun v = gt (esitetty avoimesti, hyväksytty); sim-malliruudusta puuttuu noste; kuvaajassa tunnisteeton `v : t`; suorat lainausmerkit Ydinajatuksessa.
**fy2-4:** Yksiköt tekstinä (`(J)`, `(W)`), Alkutila-rivin sekamuoto (`tex_name`, jaettu); tehtävävalinnan vihreä reunus väärälle valinnalle (jaettu komponentti); hyötysuhdetaulukolle ei lähdettä; `sim.js:48` nuolten paksuus "saman laitteen".
**fy3-6:** `lesson.md:326` Tiivistelmän ensimmäisestä luettelokohdasta puuttuu ehto "kun olomuoto ei muutu" (tiede FAIL, luokka B Minor); `lesson.md:175,177` täsmennykset; `siirto`-vastaus 29.1 vs 29 kg; "kalorimetrinen mittaus" toteutuu vain ideaalisessa simulaatiossa (ei tuntematonta c:tä mittaavaa koetta); koe-2 vihjaa vastauksen (0,50 kg); virhekäsityskohta vaikeaselkoinen; kuva (vedenkeitin) ei tue ydinajatusta.
**fy4-4:** `lesson.md:595` Kaava ratkaistuna ei lähde $\Sigma F = ma$:sta; `inquiry.json:516` N ≈ 11,8 → 12 N (kaksi merkitsevää); `valitse_d`-kuvassa toinenkin virhe ("yksi virhe" -tehtävä); koe-2 vain kaksi pistettä; hook-lause kaksitulkintainen; esimerkki 4/6: aligned-rivitys ja `\tfrac{m}{s^2}`.

Toistuvat teemat (kannattaa tehdä yhdellä ratkaisulla): (a) kokeet, joissa simulaatio palauttaa syötetyn arvon, tai joissa on vain kaksi mittauspistettä, antavat heikon kokeellisen päättelyn (pisteet 2–3); (b) yksikkö/sekamuoto tekstinä kaavojen vieressä; (c) taulukoiden vastaukset 29.1 / 11.1 vs ratkaisun merkitsevät numerot (sama `answer`-kenttäkäytäntö kolmessa luvussa); (d) pienet simulaatiokanvaksen tekstikoot (jaettu komponentti, 8–9 px).

## 3. Laajennus

Kriittisiä (Critical) virheitä ei löytynyt, joten **laajennusta ei suositella**. Suositus: korjataan M1–M4 ja Minor-lista kurssi kerrallaan opettajan luettua (`/quality-audit <id> --fix`), ja jos opettaja haluaa, otos FY5–FY8 tehdään erikseen (≈ 12 katselmointia, budjetti noin $8–10).

## Kustannus ja rajaukset

Arvio: noin 12 katselmoijaa (4 Opus tiede, 8 Sonnet), yhteensä noin 0,85 M syöte-/tulostokenttää raporttien mukaan; FY5–FY8 jätettiin budjetin vuoksi. Pedagogiakatselmoijat eivät saaneet sivukaappauksia; visuaalikatselmoijat avasivat valikoiman kaappauksia eivätkä kaikkia (kunkin raportin "Checked"-kohta). Mitään korjausta ei tehty.
