VERDICT: PASS
CONTENT-HASH: 012dc69df8b5c15b
ROUND: 3

## Blocking

## Polish
- L1-08 vs L1-01 (carried over) — L1-08 is still close to a duplicate of L1-01: same 20 V range, same ±(0,5 % + 2), a voltage reading, and only the U ± ΔU notation added. Add the plan's relative-error part, e.g. "Kuinka monta prosenttia lukemasta virheraja on?"
- exercises.json:208 (L2-06 correct feedback, carried over) — "... koska mittarissa on erillinen liitin suurille virroille" gives the wrong reason for opening the circuit. Write "Virta katkaistaan tai piiri avataan ennen johdon siirtämistä, koska johtoa ei irroteta liittimestä virran kulkiessa; suurille virroille on mittarissa oma liittimensä."
- exercises.json:220 (L2-07, carried over) — the rest voltage (lepojännite) is defined for a battery that has stood without load. Add "Auto on ollut sammutettuna useita tunteja", so that comparing with 12,60 V is valid.
- solutions.md:179 (L3-04 Järkevyys, carried over) — "lähes kymmenesosan" should be "kymmenesosan": R₂ : R_m = 0,10 exactly, and 0,571 μA : 5,714 μA = 0,100.

## Checked
- Hash 012dc69df8b5c15b at start and end (the packet gives the same). Counts 8/7/5.
- Only change since round 2 (HEAD d48687e6): solutions.md:141, L1-08 Järkevyys.
- Round-2 Blocking resolved: the line now says "noin kolmasosa alueesta 20 V (5,98 : 20 = 0,30)". 0,30 is right, and "noin kolmasosa" is a fair description.
- Rest of the line is still right: ΔU = 0,0299 V + 0,02 V = 0,0499 V ≈ 0,05 V, which is 0,83 % of 5,98 V, so it is under 1 %. The two parts, 0,03 V and 0,02 V, are of the same order.
- No other task changed, so the round-1/2 checks of the other 19 tasks still hold.
