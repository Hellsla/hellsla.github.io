# docs/decisions: siirretty päätöshistoria ja toteutuksen kuvaus

Työjono 0b (2026-11-17). `fysiikkalabra/CLAUDE.md` latautuu jokaiseen istuntoon ja agenttiin, joten siihen jäivät
voimassa olevat säännöt lyhyesti; päivätyt päätökset ja toteutuksen kuvaus ovat tässä kansiossa. Tiedostojen teksti on
siirretty CLAUDE.md:stä sana sanalta. Yhtään sääntöä ei ole poistettu tai muutettu. `tyojono.md`:n valmiit kohdat ja opit
ovat `../tyojono-loki.md`:ssä, kirjatut päätökset `tyojono-paatokset.md`:ssä.

## Sääntö → uusi paikka

| Entinen CLAUDE.md:n kohta (rivit) | Nyt CLAUDE.md:ssä | Koko teksti |
|---|---|---|
| What this repo is, Audience, Physics and maths conventions, Lesson form 1–7, Readability, Exam readiness, Never | sellaisenaan tai tiivistettynä, samat säännöt | (ei siirretty) |
| Courses and scope: lukiokohtaiset opintojaksot, Jaksopohja, Ahjo, Dronelabra (9–11) | "School-specific courses" | `kurssit-ja-jaksot.md` |
| Lesson page 1–9 (40–54): yksi lukupalsta, Pohdinta, Ennusta, sim-teksti, Teoria/Esimerkit, kaavojen nimet, exit ticket, Tehtävät, kuvitus | "Lesson page" 1–9 | `oppituntisivu.md` |
| Concept cards, Ääneenluku (myös äänitetty ääni), Yritä ensin, Every chapter gets automatically (56–62) | "Parts specified in …" | `oppituntisivun-osat.md` |
| Design audit, suunta B (64–74) | "Design audit, direction B" | `design-audit-suunta-b.md` |
| Opettajan läpikäynti 2026-11-13 (86–118) | samat kohdat yhden rivin muodossa | `lapikaynti-2026-11-13.md` |
| Exercise levels, Lesson folder and assets (120–142) | "Exercise levels, lesson folder, assets" | `tehtavapankki-ja-simulaatiot.md` |
| Pipeline: komennot, fysiikan tarkkuus, katselmointisääntö ja carry-luokat, CI:n rajaus (153–160) | "Pipeline, reviews and CI" | `katselmointi-ja-ci.md` |

Tiivistämisessä jätettiin pois vain historiallinen perustelu, päivämäärät eivät-sääntö-osista ja toteutuksen
tiedostokohtainen kuvaus (esim. `lesson.js`:n osat, ääniskriptin yksityiskohdat); ne ovat yllä olevissa tiedostoissa.
