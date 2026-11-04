VERDICT: PASS
CONTENT-HASH: 798dbae32cd6fe06

## Blocking
(none)

## Fixed
- exercises.json L2-07: "Kahdesta tasalaatuisesta metallista, A:sta ja B:stä, valmistettiin kummastakin eri tilavuuksisia saman aineen kappaleita." (one heavy sentence, "tasalaatuinen" unexplained) -> three short sentences; "tasalaatuisia eli samaa ainetta joka kohdasta". Formulas, data, answer unchanged.
- solutions.md L3-04: "ekstrapoloiden" explained in the sentence ("eli jatkamalla suoraa mitatun alueen ulkopuolelle"); "kimmoinen alue" explained ("Kimmoisella alueella jousi palaa entiseen pituuteensa, kun kuorma otetaan pois."). Same physics as the Finnish.

## Polish
- L3-05 task — "Pisteiden joukkoon mahtuu jyrkin suora" is slightly abstract for S2; acceptable because the solution's "Kuvaajan lukeminen" restates it with the same points.

## Checked
- Mode: full translation review of the whole exercise set against the reviewed Finnish set (content/fi, PASS), Round 1. check_i18n fi-easy 0 errors.
- Programmatic comparison fi vs fi-easy: all 20 ids identical; answer, unit, tolerance, data tables, kind, level and correct flags identical (L1-06, L1-07 answers are translated option texts); every LaTeX formula in tasks, choices and feedback and every formula/display block in solutions.md identical, none lost.
- New exercises L1-06...08, L2-05...07, L3-04...05: recomputed with own regression: L1-08 b = 7,0 - 1,5*3,0 = 2,5 cm; L2-05 k = 0,0797 -> 0,080 mm/g; L2-06 b = 0,83 m (LSQ 0,829); L2-07 kA 2,71, kB 7,84, ratio 2,89 -> 2,9 (LSQ 2,89); L3-04 first five points k = 0,0802 mm/g (LSQ), points 600/700 g deviate; L3-05 kmax 0,55, kmin 0,40, dk/k = 15,8 -> 16 %, student used full difference (32 %).
- MC feedback of L1-06, L1-07 is faithful: one correct option, each distractor wrong with the right reason (end-point fit, polyline, b vs k, inverted unit, no unit).
- Solutions complete: Annettu/Kysytty/Periaate/Kaava/Sijoitus/Vastaus/Järkevyys, symbolic before numbers, rounding reasons, same sequence as Finnish.
- Plain language (§12): no sentence of 24+ words outside formula-heavy Annettu lines; common words; glossary terms kept (kulmakerroin, vakiotermi, tiheys, lineaarinen malli) and difficult words explained inline (ylikuormittuu eli venyy..., tasalaatuinen, ekstrapoloiden).
- Pedagogy: situation first and question last in each new task; 8 new tasks keep the levels (L1 8, L2 7, L3 5), none repeats the kettle example, all practise slot goals (fit, slope, constant term, linear range, uncertainty); error-finding task L3-05 asks for the mistake before the correct value; solutions explain the principle and read the graph step by step; same teaching sequence as the Finnish.
