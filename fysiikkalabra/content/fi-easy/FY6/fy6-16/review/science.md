VERDICT: FAIL
CONTENT-HASH: 5cef466e8945a470
## Blocking
- A (quantitative, internal consistency). lesson.md:184 now says "Sama 40 kWh:n lataus kestää pistorasiasta lähes vuorokauden". The text before it states the losses (efficiency 80–95 %), and the inquiry "tavat" stores 40 kWh into the battery. lesson-answers.py `t-socket-h` gives 40 : (0,85 · 1,84) = 25,6 h. The inquiry solution says 26 h and "Lataus kestää yli vuorokauden", and the explain model answer also gives about 26 h. "Lähes vuorokauden" holds only without losses (21,7 h), the value the inquiry's mistake feedback marks as "Unohdit häviöt". The 80–95 % range gives 22,9–27,2 h, and the three-phase "noin neljä tuntia" (4,03 h) includes losses. Fix: "noin vuorokauden" or back to "yli vuorokauden", the same as the fi version.
## Polish
## Checked
batch delta review: one wording change at lesson.md:184. Recomputed with and without losses against lesson-answers.py and the inquiry. The new wording contradicts the lesson's own loss model. Figure and formula-name changes are the teacher's.
