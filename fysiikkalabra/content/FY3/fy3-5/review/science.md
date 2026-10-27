VERDICT: PASS
CONTENT-HASH: 36f39a7f6c8d0487
## Blocking
## Polish
- solutions.md:58 (L2-01) and inquiry.json siirto Vastaus — the result is a difference/sum, but the reason cites the figures of the data ("kuten tiedoissa 0,20 m ja 45 J"; "kuten tiedoissa 0,60 J ja 8,0 cm"). The count is right; the NOTES §2 reason is the precision of the terms: "$60\,\text{J}$ ja $45\,\text{J}$ tunnetaan joulen tarkkuudella, joten erotus $-15\,\text{J}$ myös, kaksi merkitsevää numeroa" (siirto: $6{,}0\,\text{J}$ tunnetaan 0,1 J:n tarkkuudella, joten $5{,}4\,\text{J}$).
- solutions.md:114 (L3-03) — "lämpötila ja määrä samat, joten … sisäenergia samat" holds for an ideal gas (the volumes of A and B may differ); add "kun kaasua pidetään ideaalikaasuna" or "mikromallin mukaan", as the Ydinajatus does.
- solutions.md:109 (L3-02) Järkevyys — the 0,24 K aside uses $c = 4190\,\text{J/(kg·K)}$, introduced only in the next chapter; either name the chapter or drop the aside (the 12 · 83 J ≈ 1000 J check is enough).
## Checked
- Hash 36f39a7f6c8d0487 at start and end; diff since my round-1 review (bf9755f9a0d272c5) is solutions.md only.
- Round-1 Blocking L2-03 fixed: $800\,\text{J} = 0{,}8\,\text{kJ}$, difference known to 100 J, one significant figure — correct by NOTES §2.
- Round-1 Blocking L3-02 fixed: constant speed, so $F = G = mg$, rope/wheel work $W_1 = Fh = mgh$, $\Delta U = nmgh$, $Q = 0$; no $E_k$/$E_p$; inside FY3 scope (G = mg, W = Fs).
- Round-1 Polish all taken: L1-05, L2-02 (180 kJ − 20 kJ known to 10 kJ), L2-04 (W = 10 kJ known to 1 kJ) now name the limiting datum; L1-01 Periaate no longer claims "mekaaninen energia ei muutu".
- L3-01, L3-03 Periaate now reason from the task's stated constant temperature and amount; L3-03 Vastaus (310 J, sum known to 1 J) right.
- One script: all 12 answers.py values = my formulas = exercises.json within tolerance (L3-02 1,699 m → 1,7 m); siirto 5,4 J, check-2 30 J, example 110 J, exit 180 J.
- Every reasonableness check recomputed: L2-02 89 % and 240 kJ·¾ = 180 kJ; L2-04 48 s without heat; L3-02 83 J · 12 ≈ 1000 J; balances in L1-03/04, L2-01/03, L3-01/03.
- Sign convention ΔU = Q + W (work on the system) consistent throughout.
- Unchanged since round 1 and re-confirmed: sim physics and Playwright readings (13,1/19,1/12,4 J, 2,79 K/J, (4/3)^0,4 → 329 K, C·ΔT = 12,8 J), predictions' correct options, experiment isolation, figures.
