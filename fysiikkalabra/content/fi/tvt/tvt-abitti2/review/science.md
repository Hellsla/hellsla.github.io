VERDICT: PASS
CONTENT-HASH: bc7b41b9ee879b70

## Blocking
- None. The round 1 finding is fixed. The table column is now "Käyttö", so it no longer says that YTL is the source of each description. "Mafy-taulukot, MAOL digitaulukot | taulukot (koulu voi asentaa omalla koodillaan)" matches the source note. "PDF.js | PDF-lukija" is a plain description of the program and is not attributed to YTL.

## Polish
- Table, Vernier row: the source says Graphical Analysis Pro is something the school "asentaa omalla koodilla". It does not say "voi" for this program; "voi" is the source's word only for Mafy/MAOL. The new "koulu voi asentaa" is not wrong in practice, because step 3 tells students to ask whether it is installed. It is still a small departure from the source wording.
- Step 1: the sentence now reads "YTL kertoo, että Abitti 2 on otettu käyttöön …". The YTL page (14.8.2026) uses the future tense, "otetaan". By the reading date (28.11.2026) the autumn 2026 exam has been held, so the statement is true. It slightly rewords what YTL said, so it could also be written without "YTL kertoo".
- Lähteet (carried over from round 1): the Abitti page titles ("Kokelaalle", "Kokeeseen liittyminen", "Ylioppilaskokeet keväällä ja syksyllä 2026") are not in the source notes, so I could not check them.

## Checked
- Changes since round 1 (git diff HEAD~1, Finnish guide.md and guide.json), each checked against the verified source notes:
  - Step 1: Abitti 2 is in use from the autumn 2026 exam, and from 16.4.2026 it is the only system for practice.
  - Step 3: a school may install some programs with its own code.
  - Step 5: program files must be saved regularly so that they are backed up to the server.
  - Step 6: screenshots can be attached in open tasks. The new cross-reference to "Mitä tämä ohje ei vielä kerro" matches that section.
  - Step 7: "Siirry tarkastelemaan vastauksiasi" lets you go back to editing; "Päätä koe" cannot be undone.
  - The link label now matches the linked guide's title, "Taulukko ja lasketut sarakkeet".
  - guide.json: the goal "päättämään koe" is supported (Päätä koe).
- Unchanged claims, checked again against the notes:
  - The programs are in the application menu; using them needs no purchase or licence.
  - Every other table row is supported: Collabora Calc, Writer, Draw and Impress, GeoGebra (symbolinen laskenta), Abicus, Draw.io and Klecks.
  - Abicode, Ketcher and TI ExamCalc are on the list.
  - Mastering one program per purpose is enough.
  - Answer in the answer fields, which save automatically.
- Nothing the notes list as unconfirmed (formula editor, file attachment, how graphs are made, exam duration) is stated. The guide says that formulas, graph-making and file attachment are not covered. The 60-minute FY9 minikoe is this site's own exam, not a YTL claim.
- Dating: the reading date and the date each source page was updated are given, and there is a note to check the current pages. The guide has no physics content.
- Hash bc7b41b9ee879b70 (`scripts/guides.py hash tvt-abitti2`) is the same at the start and the end.
