VERDICT: PASS
CONTENT-HASH: 25bbfd343e7ee2c9

## Blocking

## Polish
- solutions.md:88 (L2-04, Vastaus) — "480 kW, jonka kaksi ensimmäistä numeroa ovat varmoja" is still only an assertion: the trailing zero of 480 is ambiguous. — Say that the answer takes as many figures as 480 kW, or write the power with three figures and answer 720 kW with three, as in L1-03.
- solutions.md:99 (L3-01, Järkevyys) — "sen häviöt ovat vain savukaasuissa" is too strong: a boiler also loses heat through its walls and through incomplete combustion. — Write "pääosin savukaasuissa".
- solutions.md:98 (L3-01, Vastaus) — typo "polttoatehon". — Write "polttoainetehon".
- answers.py:11, 15, 34–36 — the comments are still stale ("-> 37 %", "-> 22 %", "0,40", "6,0 l", "0,75", "-> 12 kW") and do not match the task data and answers (37,2 %, 21,7 %, 0,400, 6,00 l, 0,750, 12,0 kW). The arithmetic is right. — Update the comments.

## Checked
- Hash 25bbfd343e7ee2c9 at the start and at the end. Since the round-2 PASS (379ae91), git shows one change in the lesson: the L3-03 Sijoitus in solutions.md. Nothing else changed.
- L3-03 recomputed: W = ηρVH = 0,280 · 0,750 kg/l · 6,00 l · 43,0 · 10⁶ J/kg = 5,418 · 10⁷ J (exact). t = 100 km / 80,0 km/h = 1,25 h = 4500 s. P = W/t = 12 040 W = 12,04 kW, which rounds to 12,0 kW and matches the stored 12.0 and answers.py (12.04). The intermediate W is the same quantity as W = ηQ₁ in the Periaate and in the Kaava P = W/t = ηρVH/t, so the symbolic chain still holds and the result is unchanged. The Vastaus and the Järkevyys still hold: fuel power 43,0 kW, waste 31 kW, 53,75 kWh ≈ 54 kWh of petrol, 15,05 kWh of work, and 15/0,90 ≈ 17 kWh for the electric car.
- One script recomputed all 12 exercises. The stored answers, answers.py and my values agree for every task: 12,0 kJ; 172 J; 37,2 %; 170 kJ; 21,7 %; 41,0 %; 9,0 %; 500 J; 720 kW; 120 MW; 9,60 MWh; 12,0 kW.
- The findings from the round-2 Checked section still hold for the unchanged files: the principles and conversions, the rounding reasons, the worked example (38,0 %, 88,0 %, 310 MW, 60 MW), the inquiry values and feedback, the exit ticket, the scale of the figures, the sim model ΔV = 2Q/(5p₁), and the scope against FY3.
