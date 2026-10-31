VERDICT: PASS
CONTENT-HASH: b191ea9ccf473f7b

Round 1 (delta). The diff is terminology only: "suhteellinen virhe" becomes "suhteellinen epävarmuus" (L2-01 Periaate) and "virhe-arvio"/"virhe" becomes "epävarmuus" (L3-02 Järkevyys).

## Blocking
- none

## Polish
- solutions.md L2-01 Vastaus — "virhearviossa" but the lesson and the rest of the set write "virhe-arviossa" (the lesson also mixes the two): "yksi merkitsevä numero kuten virhe-arviossa $0{,}09\,\text{s}$".
- solutions.md L2-01 Kysytty — still "suhde keskiarvoon"; name the term the Periaate now uses: "satunnaisvirheen arvion $\Delta t$ suhde keskiarvoon eli suhteellinen epävarmuus $\varepsilon$ prosentteina". The task text also stays at "Kuinka monta prosenttia se on keskiarvosta?"; fine at level 2, but add "(suhteellinen epävarmuus)" if the teacher wants the term practised.
- solutions.md L3-02 Järkevyys — "suhteellinen epävarmuus noin 2 %" is correct (2 µm / 100 µm), but say what is compared: "yhden arkin epävarmuus 2 µm on noin 2 % arkin paksuudesta".

## Checked
- L2-01 Periaate: "suhteellinen epävarmuus" matches the lesson's name for ε and its formula; the answer 4,83 % (tolerance 0,04 relative, so 5 % passes) agrees with the Vastaus "5 %" that the solution gives.
- L3-02 Järkevyys: 0,5 mm / 0,1 mm = 500 %, and the stack divides the relative uncertainty by 250; numbers and the new wording agree.
- No remaining "suhteellinen virhe" or "virheeksi" in exercises.json or solutions.md; the terms epävarmuus (uncertainty of a result) and virhe (error) are used to the lesson's distinction.
- Wording is clear for a 16-19-year-old; no task text changed, so the situation-first, question-last form is intact.
- Rest of the set unchanged since the previous PASS; L1-03 figure and its description unchanged.
- No captures were listed in the packet, so phone fit is judged only by the passed 360 px layout check.
