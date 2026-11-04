VERDICT: PASS
CONTENT-HASH: b2f0b8b8cd894742

## Blocking
(none)

## Polish
- Sähköinen koe: the paragraph now has three hedges ("yleensä", "yleinen rakenne", "vaihtelevat kokeesta toiseen"); one is enough: "Tämä on yleinen rakenne; Osan I kohtien määrä ja kysymysmuodot voivat vaihdella, joten tarkista ajantasainen rakenne ylioppilastutkintolautakunnan ohjeista."
- The Ajankäyttö time budget (60 / 35 / 55 min) is stated as fact right after; add "esimerkiksi" before it so a student does not take it as the exam's own timing.

## Checked
Delta of the Sähköinen koe wording since origin/main: the student is told the structure is general and is sent to the official source, which is the right pedagogical stance; numbers (11 tasks, 120 p, 4 of 7, 2 of 3) unchanged and consistent with the Ajankäyttö section and the sister units; earlier fixes (teet päätelmiä, osissa II ja III valitset itse) read naturally.

## Follow-up (4.11.2026, hash 4ff9fa1cddf8ae89)

Delta: teacher.md "Kertaustestin käyttö" lost the bullet "FY7:n luvut eivät ole vielä sivustolla, joten FY7:n tehtävien palaute nimeää vain moduulin. Ohjaa oppikirjaan tai omaan materiaaliin." (b6de518c4). The remaining three bullets and the rest of teacher.md and unit.md read coherently; no text still says the FY7 chapters are missing.

### Blocking
- The deletion is right only if the FY7 feedback now names a chapter, and it does not. teacher.md tells the teacher that the feedback names the chapter ("… jokaisen väärin menneen tehtävän luku; palaute nimeää sen") and the lesson plan has students record "väärin menneiden lukujen nimet" (42–62 min). In inquiry.json all 8 FY7 feedbacks (testi-19, testi-20, testi-21) still end "Kertaa tämä moduulissa FY7." with no chapter, so a student who misses an FY7 item cannot do what the teacher note says, and the teacher no longer has the caveat. Fix (inquiry.json, as for the other modules): testi-19 → "Kertaa luvussa [*Valon heijastuminen ja taittuminen*](fy7-10.html).", testi-20 → "[*Sähkömagneettinen induktio*](fy7-5.html)", testi-21 → "[*Voima virtajohtimeen: sähkömoottori ja kaiutin*](fy7-4.html)". Also update developer.md (line 17: "FY7 feedback says 'moduulissa FY7' without a link").

### Polish
- Earlier Polish items stand.

## Follow-up 2 (4.11.2026, hash b2f0b8b8cd894742)

Delta: the 8 FY7 feedbacks (testi-19/20/21) now name their chapter, with link targets and titles matching meta.json (fy7-10, fy7-5, fy7-4); developer.md line 17 updated. This resolves the Follow-up 1 Blocking item. teacher.md's "palaute nimeää sen" and the 42–62 min step ("kirjaa väärin menneiden lukujen nimet") now hold for every module. grep FY7: no remaining text says the chapters are missing.

### Blocking
(none)

### Polish
- See visual.md Follow-up 2. In numeric items, the common-mistake feedback shows the link as raw Markdown, for example "[*Valon heijastuminen ja taittuminen*](fy7-10.html)". This affects all modules, not just FY7. The chapter name is still readable, so a student can still record it, but the link can't be clicked.

## Follow-up 3 (4.11.2026, hash b2f0b8b8cd894742)

The Polish note in Follow-up 2 is resolved: numeric mistake feedback now renders its chapter link (checked at 390 px in preview, see visual.md Follow-up 3). Every FY7 feedback now names and links its chapter.
