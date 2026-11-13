VERDICT: FAIL
CONTENT-HASH: 6d39d0db9b9030ff

## Blocking
- exercises.json fy6-2-L2-10 (answer 2.98, tolerance 0.1) — the solution of L2-09 teaches rounding the error limit to one figure (0,03 V); a student who carries that into L2-10 gets 0,08 : 0,03 = 2,67, which is 10,5 % from 2,98 and is marked wrong although the method and conclusion are right. The data (0,5 %, 1,37 V, 0,01 V) do not justify a one-figure intermediate, but the page teaches it one task earlier — fix: widen tolerance to 0.12 (2,67 and 2,98 both accepted), or add to the task "Älä pyöristä virherajaa ennen jakolaskua" and a line in the solution.

## Polish
- L2-09 and L2-10 share the figure and the whole setup (read the display, compute ΔU); L2-10 only adds a comparison. Acceptable since the second idea (is the difference larger than the limit) is new; the mix of level 2 stays varied (data, error, experiment tasks).
- L2-10 text: "Kuinka monta kertaa lukeman virheraja mahtuu ... erotukseen?" is stiff. Better: "Kuinka moninkertainen valmistajan arvon ja lukeman erotus on lukeman virherajaan verrattuna?"
- L2-10 solution Vastaus gives "noin $3{,}0$ kertaa" while the key is 2,98; fine, but state "noin $2{,}98$" so key and text match.

## Checked
- L2-09: situation first, question last; figure supplies reading 1,37 V and 20 V range, description matches, does not state the error limit or answer.
- L2-09 solution: 0,005 · 1,37 + 2 · 0,01 = 0,02685 V correct; formula in symbols first, conversion of % stated, sanity check sound.
- L2-09 answer 0.02685 with tolerance 0.12 accepts the one-figure 0,03 V stated in the solution.
- L2-10 arithmetic: 0,08 : 0,02685 = 2,98; interval 1,34–1,40 V check correct; conclusion (not compatible) follows.
- Level 2 fits both (two steps, reading from a figure); neither repeats the worked example or L2-05/L2-07.
- Finnish otherwise correct; units LaTeX; no clipped long lines in text-only changes.
