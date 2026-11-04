VERDICT: FAIL
CONTENT-HASH: 76206f426c2e0dce

## Blocking
- solutions.md:179 (fy6-3-L3-04 Sijoitus) and :180 (Vastaus) — A, missing step: task a) asks R = U : I at every voltage where the current is not zero, but component C's point 1,0 V / 0,1 mA (exercises.json:341) is skipped; the parenthesis names only 0,5 V. Vastaus then says C falls "600 Ω:sta 31 Ω:iin", hiding the most diode-like value — fix: add "$1{,}0\,\text{V} : 0{,}1\,\text{mA} = 10\,\text{k}\Omega$" to C's list and write "pienenee $10\,\text{k}\Omega$:sta $31\,\Omega$:iin" in Vastaus.
- solutions.md:190 (fy6-3-L3-05 Vastaus) — A, wrong rounding reason: "kaksi merkitsevää numeroa kuten virrassa 0,362 A", but 0,362 A has three significant figures — fix: "kaksi merkitsevää numeroa, koska prosenttikasvu on kahden lähes yhtä suuren resistanssin erotus suhteessa $R_{20}$:een" (or give 38,1 % and round to 38 % with that reason).

## Polish
- solutions.md:150 (L2-05) — "kolme merkitsevää numeroa kuten virtalukemissa": the voltages have two and 6,6 mA has two; justify 150 Ω by the estimated ±2 Ω instead. Call ΔR "pisteiden hajonnasta saatu arvio".
- solutions.md:156 (L2-06 Periaate) — "Pienen suhteen R5,0 : R1,0 avulla" reads as a typo; "Resistanssien suhteen".
- solutions.md:125 (L1-06 Mallivastaus, last sentence) — "on juuri se, mitä Ohmin laki kuvaa, eikä se todista..." contradicts itself; say: simultaneous growth alone does not show proportionality, the constant ratio U : I does.
- exercises.json:359 (L3-04, C at 3,0 V = 98 mA) — an indicator LED is usually rated about 20–30 mA; end the series at 2,5 V or say "teho-LED" so the data stay realistic.

## Checked
- Hash 76206f426c2e0dce at start and end; counts 8/7/5; ids, kinds and levels match docs/exercise-bank/FY6.md fy6-3.
- Recomputed in one script: L1-08 0,30 A; L2-05 LSQ slope through origin 149,97 → 150 Ω, point ratios 148,1–151,5 Ω, residuals ≤ 0,38 mA; L2-06 10,2…20,2 Ω, ratio 1,976 → 2,0; L2-07 mean 4,934 → 4,9 Ω; L3-04 A ≈ 75 Ω, B 16→37 Ω, C 600 Ω, B at 1,5 V 26,3 Ω, ratio 23; L3-05 38,1 %. All agree with exercises.json and answers.py.
- L1-06/L1-07: exactly one correct option, each distractor wrong with correct feedback; resistivity vs resistance kept apart.
- L3-05 iron data imply α ≈ 0,0063 1/K, realistic; R(T) formula correctly left out; variables, meter connection, lacquer insulation and self-heating source right.
- L3-04 "työpisteessä U : I, ei jyrkkyys" matches the lesson; render of L3-04 solution at 1280 px fine.
- Ohm's-law condition (constant temperature) stated where used.
