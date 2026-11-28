VERDICT: PASS
CONTENT-HASH: fd4df10b9ccf9625

## Blocking
None.

## Polish
- Introduction: the new plain explanation says "Vastauskenttä on kysymyksen kohdalla oleva tila". "Kohdalla" (at the question) is close enough to YTL's "yhteydessä". The sentence is not attributed to YTL and describes no screen layout, so it is not an error. If you want it to match the source exactly, write "kysymyksen yhteydessä oleva tila".

## Checked
- The hash is fd4df10b9ccf9625 (`scripts/guides.py hash tvt-abitti2 --lang fi-easy`), the same at the start and at the end.
- The round 1 blocking item is fixed. Step 4 now says "kysymysten yhteydessä oleviin vastauskenttiin", which is YTL's wording in Koetilaisuuden kulku (27.4.2026).
- The round 1 polish item is fixed. Step 2 now says "Valitse siis yksi ohjelma kuhunkin tarkoitukseen", which matches YTL's "yhden samaan tarkoitukseen suunnatun ohjelmiston".
- I checked every other change in `git diff HEAD` against sources.md:
  - "ei tarvitse hyväksyä ohjelmien käyttölupaa eli lisenssiä" matches "ei vaadi hankintaa tai lisenssin hyväksymistä".
  - "piirtäminen (vektorigrafiikka)" for Draw matches the YTL list, which says vektorigrafiikka.
  - "Tallenna tiedostot säännöllisesti. Silloin niistä tulee varmuuskopio … palvelimelle" keeps the source's reason ("jotta ne varmuuskopioidaan palvelimelle") and adds no new fact.
  - Under common mistakes, "Tarkastele" became "Tarkista". This changes only the wording. The steps "Siirry tarkastelemaan vastauksiasi" → "Päätä koe" with no return are still in step 7.
- No new claim about the system was added. The things no source confirms (the formula editor, how to attach a file, how to make a graph in the programs, the exam's length) are still listed under "Mitä tämä ohje ei vielä kerro" and are not described anywhere. The 60 min is the FY9 mini exam's length (course material), not the length of the YTL exam.
- guide.json is unchanged since round 1, when it was checked against the Finnish version.
- The parts I passed in round 1 (all 7 steps, the practice section, the common mistakes, the sources and the reading date 28.11.2026) were not changed in this diff, apart from the wording above.
