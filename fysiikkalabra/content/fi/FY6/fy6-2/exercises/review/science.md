VERDICT: FAIL
CONTENT-HASH: f9e998c9ae9437e4
ROUND: 2

## Blocking
- solutions.md:141 (L1-08 Järkevyys) — A, wrong number: "koska lukema on yli kolmasosa alueesta 20 V" is false, because 5,98 V : 20 V = 0,30, which is less than a third (6,67 V). The reasonableness check therefore states a wrong fact. Fix: "koska lukema on noin kolmasosa alueesta $20\,\text{V}$ ($5{,}98 : 20 = 0{,}30$), joten numeroiden osuus $0{,}02\,\text{V}$ on vain $0{,}3\,\%$ lukemasta ja koko virheraja $0{,}83\,\%$."

## Polish
- L1-08 vs L1-01 (carried over): the rewritten task is still a near-duplicate of L1-01. It uses the same 20 V range, the same ±(0,5 % + 2) and a voltage reading, and adds only the U ± ΔU notation. The plan's "suhteellinen virhe" part, for example "Kuinka monta prosenttia lukemasta virheraja on?", would set it apart. (L2-01 does that at 10 A, so a voltage version fits level 1.)
- exercises.json:208 (L2-06 correct feedback) — "Virta katkaistaan ... koska mittarissa on erillinen liitin suurille virroille" gives the wrong reason. The separate jack is why the lead is moved. The circuit is opened first because the lead must not be pulled out of a jack while current flows through it. Write "Virta katkaistaan tai piiri avataan ennen johdon siirtämistä, koska johtoa ei irroteta liittimestä virran kulkiessa; suurille virroille on mittarissa oma liittimensä."
- exercises.json:220 (L2-07) — a rest voltage (lepojännite) is defined for a battery that is not under load and has stood for a while. Add to the task "Auto on ollut sammutettuna useita tunteja", so that comparing the reading with 12,60 V is valid.
- solutions.md:179 (L3-04 Järkevyys) — "lähes kymmenesosan" should be "kymmenesosan", because R₂ : R_m = 0,10 exactly, and 0,571 μA : 5,714 μA = 0,100.

## Checked
- Hash f9e998c9ae9437e4 at start and end. Counts 8/7/5.
- Round-1 Blocking resolved. L3-04 now gives I = U : R in the task, and the parallel-combination check is replaced by a back-substitution (6,29 μA = 5,714 + 0,571 μA, correct). L2-07 now uses the rest voltage of a fully charged battery, 12,60 V, in the task, in d) and in the solution.
- Round-1 Polish resolved: in L3-04 "ilman mittaria, 6,00 V"; L2-06 now says to switch off first; L3-05 d) adds the voltmeter current, 4,52 V : 10 MΩ = 0,45 μA, which is 0,0012 % of 38,4 mA. That is right.
- L3-04 b): the symbolic solution U = U₀ : (1 + R₁/R₂ + R₁/R_m) = 5,714 V is correct.
- L1-08 recomputed: ΔU = 0,005 · 5,98 V + 2 · 0,01 V = 0,0499 V, so the result is 5,98 V ± 0,05 V. The tolerance accepts 0,05.
- I recomputed every answer from answers.py in one script and checked each new task with my own formulas: L2-05 11,235 mV, L2-07 0,08245 V, L3-04 4,76 %, L3-05 2,90 Ω. All agree with exercises.json.
- MC L1-06, L1-07 and L2-06: only the order changed (answer positions). There is still exactly one correct option, with correct feedback.
