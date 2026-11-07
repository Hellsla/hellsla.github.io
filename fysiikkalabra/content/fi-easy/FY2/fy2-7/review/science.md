VERDICT: PASS
CONTENT-HASH: 6a0dcba838f38427
Mode: light (teacher 2026-11-07, "kevyt katselmointi": the editorial-correction diff since origin/main only)

## Blocking
- none

## Polish
- lesson.md line 393 adds the gloss "Sisäenergia on aineen hiukkasten liikkeen energiaa". This is incomplete: internal energy also includes the particles' interaction energy (docs/physics-guardrails.md, particles section; FY3 fi-easy uses both). Suggest "hiukkasten liikkeen ja niiden välisten vuorovaikutusten energiaa". fi and en have no such gloss. Not blocking at this level (the sentence is about a conductor warming), but worth fixing.

## Checked
- Diff `git diff origin/main...HEAD` of lesson.md, inquiry.json, exit-ticket.json (fi-easy); content hash recomputed and equal to the brief's.
- lesson.md, inquiry.json, exit-ticket.json: loss mechanism stated as electrical energy -> internal energy of conductors -> transferred as heat to surroundings; district heating: energy passes as heat from the hot water through pipes and insulation. Consistent with guardrail "heat is energy in transfer" in every changed sentence (theory, misconception box, summary, prediction options and feedback, exit ticket); correct option and distractor feedback still right. "Energy can be moved in many ways; this chapter treats two" is correct. No numbers changed.
- Selkeä suomi changes carry the same physics as fi.
