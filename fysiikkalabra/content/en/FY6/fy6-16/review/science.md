VERDICT: PASS
CONTENT-HASH: db324a986b213d71

## Blocking
- none

## Polish
- content/en/FY6/fy6-16/lesson.md:473 (summary) — "its own residual current device: charging is a long, large load, and outdoors the insulation of a cable can be damaged" still reads as if the RCD were justified by outdoor use, while tarkistus-1 now says, correctly, that it is required indoors and outdoors (and lesson.md:269 says the standard requires it for every charging point) — e.g. "every charging point needs its own residual current protection, indoors and outdoors; outdoors damage to the insulation is also more likely".

## Checked
- tarkistus-1 (inquiry.json:269): the correct option is right. Charging is a long, high-power load, so it needs its own sized circuit, and residual current protection is required for every charging point whatever its location (SFS 6000-7-722). The feedback says how an RCD works (leakage to earth, for example through a damaged cable and a person) the same way as the lesson and the fy6-15 chapter.
- Exactly one option is correct. "Own circuit speeds up charging" and "RCD prevents the main fuse from blowing" are still wrong, and their feedback is correct: an RCD responds to the difference current (30 mA), not to the load, and load management protects the main fuse.
- No numbers changed. The 30 mA tripping limit is the same as in fy6-15.
- Rest of the lesson unchanged since the last PASS (git diff); content hash the same at start and end.
