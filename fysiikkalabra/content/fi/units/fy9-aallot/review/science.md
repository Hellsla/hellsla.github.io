VERDICT: PASS
CONTENT-HASH: 87d88a068c43750c

Science review of fy9-aallot. Round 2 (delta review of round 1 fixes; round 1 hash 510226a7fdf49c1d).

## Blocking fixes verified (sources and built preview)
1. inquiry.json `jousitus` Periaate: now "koriin ja kuljettajaan vaikuttavat paino ja jousten harmoninen voima. Paino vain siirtää tasapainoasemaa …". Consistent with s6 d. Fixed.
2. s4 a: solutions.md model answer and tasks.json `assumptions` criterion both read "Malli on karkea arvio: ilma ja maasto vaimentavat ääntä, mutta myötätuuli ja heijastukset voivat nostaa tasoa." No "yläraja" left. Fixed.
3. s4 b: "Bassot eivät välttämättä ole voimakkaampia: vaikka … yhtä voimakkaita, aita vaimentaa korkeat." Fixed.
4. s5 b: step is $343 - 0{,}6 \cdot 15$ ≈ 334 m/s; answers.py `s5-v5C` = `343 - 0.6 * (20 - 5)` = 334,0. Fixed.

## Polish fixes verified
5. s3 c hand timing 0,1–0,2 s (1–2 % of t10 ≈ 10–20 s, 2–4 % of T²); conclusion (0,3 % difference) holds.
6. s3 intercept: read-off points give b = 0,46 − 4,0375·0,10 = 0,05625 s²; b model "0,055–0,056", d Annettu explains 0,056 vs 0,055; l = 0,9768 m (0,976 with rounded k, b). Consistent.
7. s5 a: half-range wording as the guardrail asks.
8. tarkistus-3: "kaava pätee pienillä heilahduksilla".
9. unit.md Ydinajatus: cause wording fixed.
10. s2 c: the bat's double role is explained.

## Recomputed (one Python call)
k = 4,0375 s²/m, g = 9,778 m/s², l-intercept −0,0139 m, l(T = 2,00 s) = 0,9768 m; 343 − 0,6·15 = 334 m/s, difference 2,6 % ≈ 3 %; echo time 2·85/354 = 0,48 s, 0,02 s → 4 %; jousitus k = 110 363 N/m, f = 1,472 Hz. All agree with the page.

## New problems
None. Build has no errors; Playwright 390 and 1280: no console errors, 0 katex-error, no raw $.

## Polish (optional)
- s3 d Sijoitus uses 0,0563 s² while Annettu says 0,056 s²; harmless extra digit of an intermediate value.
