VERDICT: PASS
CONTENT-HASH: 1f46e7478f93fd99

## Blocking

## Polish
- inquiry.json:177 (johtopaatos prompt) — "miksi sama sulake ei suojaa ihmistä?" still uses the absolute wording. The model answer qualifies it correctly; the prompt could read "ei huomaa ihmisen kautta kulkevaa virtaa".

## Checked
- Delta 45327c18: the earthing figure's fault-current label changes from I_vika to I_v (figures.py, lesson.md:310), the same symbol as in the RCD figure (lesson.md:394–395). This is physically consistent: the text and glossary call both currents vikavirta (the current that reaches earth through the fault). The arrow, its direction along PE and the "sulake laukeaa" text are unchanged.
- Since my round-2 PASS (8a49e138), the only other content change is the solutions wording on heat leaving a coiled cord (energy transferred as heat), which is correct.
- The round-1 safety fixes stand. The fuse protects a person only together with protective earthing. The RCD compares the L and N currents and misses an L–N contact. Colours apply to new installations, and a colour never shows that a conductor is dead. The shoe conditions are stated and shoes are no protection. Replacing a fuse with a larger one is forbidden. The Tukes and layperson limits are correct.
- The body-current thresholds 0,5 / 10 / 30 / >50 mA agree with IEC 60479-1 and with the vaikutukset figure.
- The numbers were verified in round 2 and are unchanged; this change touches only a figure label.
- The fy6-16 cross-check is resolved: fy6-16 now calls IP54 a kotelointiluokka (IP-luokka).
