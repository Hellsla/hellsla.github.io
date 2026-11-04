VERDICT: PASS
CONTENT-HASH: 321eee9838d818f2

Round 2 (delta review of round 1 fixes; round 1 hash c908c7c1c4a5b48e)

## Blocking (round 1) — verified
1. s5 b mug sign: fixed. solutions.md Vastaus now says the group's formula would credit heat taken by the mug to the ice (result too large), and that the 1890 J gap would need about 70 J/K (recomputed 1890/25,7 = 73,5 J/K) while a styrofoam mug has a few J/K. The wrong "Yleisiä virheitä" line is replaced by "Muki hyväksytään selitykseksi arvioimatta…". tasks.json s5-b `conclusion` matches. Seen in the preview at 390 and 1280.
2. s1 ice/water density: fixed. tasks.json now says water is sprayed in layers "yhteensä 3,00 cm:n kerros"; solutions.md Annettu "vesikerroksen paksuus"; answers.py comment updated. Recomputed: m = 54 000 kg, Q = 21,88 GJ, t = 17,4 h, unchanged and now consistent.
3. "vakiopaineessa" added in unit.md Kaava (line 183).

## Polish (round 1) — verified
4. Expansion validity condition added (unit.md line 272). 5. Exit ticket item 2 now states wood shortens much less along the grain; 12e-6·10·35 = 4,2 mm. 6. s3 d now 13 % (600/530 = 1,132). 7. s5 c ties weighing by difference to ice melting or dropping during handling.

## New problems
None found. Recomputed s5 a/b (370,8 and 333,0 kJ/kg), aineisto tolerance 0,07 (−15 °C → +6,7 %, −17 °C → −5,9 %, both accepted). s6 d no longer uses "pumppaustyö"; the friction-plus-cooling explanation is correct.

## Polish (new, optional)
- tasks.json s1 `source_note` still says "Jääkerroksen paksuus"; the task now gives the water layer. Harmless (3,3 cm ice is the same order), could read "Vesikerroksen paksuus".

## Checked
build.py fy9-lampo; Playwright 390 and 1280 with all details open: no console errors, no .katex-error, no raw $, no overflow.
