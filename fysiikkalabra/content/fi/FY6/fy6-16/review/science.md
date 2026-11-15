VERDICT: FAIL
CONTENT-HASH: fe6754a0fcd417c3
## Blocking
- A (quantitative, internal consistency). lesson.md:184 now says "Sama 40 kWh:n lataus kestää pistorasiasta lähes vuorokauden". The paragraph just before it (line 177) says that losses exist and that the efficiency is 80–95 %. The 40 kWh is the energy into the battery (inquiry "tavat": "Akkuun pitää varastoida 40 kWh"). lesson-answers.py `t-socket-h` computes this sentence's number as 40 kWh : (0,85 · 1,84 kW) = 25,6 h. The inquiry solution, the "tavat" hint and the explain model answer all say about 26 h, "yli vuorokauden". "Almost a day" holds only without losses (40 : 1,84 = 21,7 h). That is exactly the value the inquiry's mistake feedback marks as "Unohdit häviöt". Across the stated 80–95 % range the time is 22,9–27,2 h. The three-phase "noin neljä tuntia" (4,03 h at η = 0,90) still includes losses, so the sentence now mixes two models. Fix: write "noin vuorokauden" (true across 80–95 %) or go back to "yli vuorokauden" (true at the inquiry's η = 0,85).
## Polish
- inquiry.json model answer: "yksivaiheisella noin 12 h" (12,1 h at η = 0,90) is fine; if the lesson sentence is reworded, keep the same efficiency in mind.
## Checked
batch delta review: one wording change at lesson.md:184. Recomputed 1,84 / 3,68 / 11,04 kW with and without losses against lesson-answers.py and inquiry "tavat". The new wording contradicts the lesson's own loss model and the inquiry. Figure and formula-name changes are the teacher's.
