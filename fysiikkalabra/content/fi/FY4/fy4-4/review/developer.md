VERDICT: DONE

Round 1, draft of fy4-4 *Newtonin toinen laki*. `check_lesson.py fy4-4`: every line ok (inquiry 75/75); `check_solutions.py`, `check_choices.py FY4` clean for fy4-4.

- `lesson.md`: Miksi (lastattu kuorma-auto) + hero; Ydinajatus (kokonaisvoima, massa/hitaus, vastaus Miksi-kysymykseen); `## Kaava: Newtonin toinen laki` (ΣF̄ = mā, newtonin määritelmä, kokonaisvoima kiihtyvyyden suuntaan, ensin voimat sitten yhtälö); Esimerkki nosturista (8 vaihetta, Voimakuvio mukana); virhekäsitys; tiivistelmä.
- `figures.py`: hero (kaksi puutavara-autoa liikennevaloissa), kokonaisvoima (esimerkki A + vaakasuora kiihtyvyys, ΣF̄ erillään), a–ΣF-kuvaaja, nosturi 2×2 (esimerkki E: lepo, tasainen, kiihtyvä, hidastuva), esimerkki, valitse-a…d (select), malli-kirja (draw). Kaikki voimakuviot `fbd.py`:llä.
- `inquiry.json`: hook, kertaus (identify), 3 ennustetta, sim + 3 koetta (F, m, voiman suunta liikettä vastaan), johtopäätös, valitse (select), siirto (equations), checks identify/equations/draw, exit.
- Uusi simulaatio `assets/sims/fy4/fy4-4/sim.js`: kärry radalla, voimakuvio mittakaavassa, (t, v_x)-kuvaaja, kiihtyvyys sovitetun suoran kulmakertoimena; `tests/sims/fy4-4.json` 16 väitettä; `lang/fi.json` sims.fy4-4.
- Tehtävät 5/4/3, `solutions.md`, `answers.py`, `lesson-answers.py`, `exit-ticket.json`, `sim-spec.md`, meta glossary.
