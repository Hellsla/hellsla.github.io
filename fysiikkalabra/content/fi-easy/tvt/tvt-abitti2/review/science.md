VERDICT: FAIL
CONTENT-HASH: 16fa2a30a29a80d1

## Blocking
- A (claim not in the source, attributed to YTL). Step 4: "YTL ohjeistaa vastaamaan suoraan kysymysten **vieressä** oleviin vastauskenttiin." The source note quotes YTL as "Vastaa suoraan kysymysten **yhteydessä** oleviin vastauskenttiin", and the Finnish guide says "yhteydessä". "Vieressä" says where the field is on the screen. No source says that, and YTL is named as saying it. Fix: "kysymysten yhteydessä oleviin vastauskenttiin" (or something plain that gives no position, e.g. "kunkin kysymyksen omaan vastauskenttään").

## Polish
- Step 2, end: "Valitse siis yksi ohjelma ja opettele se kunnolla." The sentence before says "yksi ohjelma kutakin tarkoitusta varten", but on its own this one can be read as "one program in total". Suggest: "Valitse siis yksi ohjelma kuhunkin tarkoitukseen ja opettele se kunnolla."

## Checked
- The hash is 16fa2a30a29a80d1 (`scripts/guides.py hash tvt-abitti2 --lang fi-easy`), the same at the start and at the end.
- I compared each step with the Finnish source guide (science PASS): no step is lost. All 7 work steps are there in the same order, as are the practice section, all four common mistakes, the "not covered" section and the sources.
- Checked against sources.md:
  - Abitti 2 is used in the exams from autumn 2026, and from 16.4.2026 it is the only system for practice (YTL 14.8.2026).
  - Your own school gives the instructions for practice exams.
  - The programs are in the application menu.
  - No purchase or licence is needed.
  - Every row of the table and the extra programs Abicode, Ketcher and TI ExamCalc are in the YTL list of 27.11.2026, including which programs a school installs with its own code (GA Pro, Mafy/MAOL).
  - The sentence "one program per purpose is enough" matches the source.
  - Answers in the field are saved automatically, and you save program files yourself regularly so that they are backed up.
  - Screenshots can be added from an extra program in open tasks.
  - The flow "Siirry tarkastelemaan vastauksiasi" → back to editing → "Päätä koe" with no return matches the source.
- Only plain explanations were added ("vastauskenttään eli kenttään, johon vastaus kirjoitetaan", "päivittyy eli muuttuu uudemmaksi", "Kaikkia ei tarvitse osata"). None adds a fact about the system.
- The three things not confirmed by any source (the formula editor, how to attach a file, how to make a graph in the programs) are said to be not covered and are never described. The guide states no exam duration (the 60 min belongs to the FY9 mini exam, which is course material).
- guide.json: the title, the learning goals, kind and order are the same as in the Finnish version, and the plainer description adds no claim.
- The source list and the reading date 28.11.2026 match sources.md.
