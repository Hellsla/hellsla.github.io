VERDICT: DONE

Drafted fy6-3 Resistanssi ja Ohmin laki (round 1).

- `lesson.md`: Miksi (paahtimen lanka vs. jatkojohto), Ydinajatus (R = U : I, mittauskytkentä, elektronien törmäykset ja lämpötila), `## Kaava: Ohmin laki ja resistiivisyys` (R = U/I, U = RI, ominaiskäyrä, R = ρl/A, resistiivisyystaulukko), seitsenvaiheinen esimerkki (konstantaanilangan pituus), virhekäsitykset, tiivistelmä.
- `figures.py`: hero (leivänpaahdin), IEC-mittauskytkentä, mikromalli kylmä/kuuma, ominaiskäyrät vastus/lamppu, langan l ja A, tehtäväkuvat `lamp-curve` ja `resistor-points` (REUSE kirjattu; figcat rebuilt).
- `assets/sims/fy6/fy6-3/sim.js` + `lang/fi.json` sims.fy6-3: mittauspiiri (vastus, hehkulamppu, konstantaanilanka), mittarit näyttävät vain U ja I, (I, U)-kuvaaja merkittävine pisteineen, liikkuvat virtapisteet, nopeus, kapea pinottu asettelu; `tests/sims/fy6-3.json` 30 väitettä; `sim-spec.md`.
- `inquiry.json`: 2 ennustetta (lamppu, langan pituus), kokeet 1–4, johtopäätös, etsi virhe (tangentti vs. U : I), siirto, 3 tarkistusta, exit.
- `exercises/` 5/4/3 + täydelliset ratkaisut; `answers.py`, `lesson-answers.py`; `exit-ticket.json` 2 kysymystä.
- `glossary.json`: resistanssi, Ohmin laki, vastus, resistiivisyys, ominaiskäyrä.
