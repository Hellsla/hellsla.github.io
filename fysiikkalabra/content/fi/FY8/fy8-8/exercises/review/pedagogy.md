VERDICT: PASS
CONTENT-HASH: 041806ccd347a404
## Blocking
## Polish
- solutions.md L2-01 Sijoitus — "$1{,}8796$" in the denominator gives $1{,}9865/1{,}8796 = 1{,}0569$, but the line prints $1{,}0568$ — write $1{,}0569\,\text{pm}$ (and "$1{,}057\,\text{pm}$" stays correct).
- solutions.md L2-01 Järkevyys — the recoil explanation for $1173{,}3$ vs $1173{,}2\,\text{keV}$ is a detour for a level 2 student — shorten to "Ero $0{,}1\,\text{keV}$ johtuu rekyylistä ja tasojen pyöristyksestä."
- Earlier polish (question last in L1-04, L2-03, L3-02, no equation-writing or gamma task, L2-03 repeats the example's Cs-137 photon) was not part of this diff and still stands.
## Checked
- Diff only: L2-01 now uses levels 2505,8 and 1332,5 keV, matching the lesson's data; difference 1173,3 keV; answer 1,06 pm unchanged and correct (1,0568 pm exact).
- answers.py comment and computation match the text and solution.
- The five "Vastaus" rewordings ("Tulos on tarkka kokonaisluku") are grammatical Finnish and keep the values (143, 218, 7, 10, 82, 138, 4, 87).
- Task text ends with the question and gives all constants; no trap added.
