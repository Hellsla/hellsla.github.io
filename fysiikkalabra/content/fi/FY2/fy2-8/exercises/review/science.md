VERDICT: PASS
CONTENT-HASH: 29e5ecd1dc7acc04

Round 2 (round 1: PASS, Polish only; L3-05 reworked).

## Blocking

## Polish
- solutions.md:199 (L3-05 Järkevyys) — the check uses 10 · 490 · 10⁶ g = 4900 t (9,4 %) for the share that is not removed. The exact difference with wind is 10 · (490 − 12) · 10⁶ g = 4780 t = 9,15 %, which equals the 9,2 pp found in c). Use the exact figure, and drop "edelleen".
- exercises.json L1-06, option 2 — "lämmittää sillä maanpintaa alhaalta päin" is physically meaningless, since the atmosphere is above the ground. Drop the words.
- exercises.json L1-07 — the stem says "Väitteet ovat esimerkkejä, eivät mittaustuloksia", but the correct option names a real normal period. Oulu's FMI January normal for 1991–2020 is about −9,6 °C, so "noin −10 °C" is fine. Name FMI as the source or keep the disclaimer.
- exercises.json L2-05 and L3-04 — the source is now named (NOAA, Mauna Loa annual means), and the rounded values match the NOAA file (380/390/401/414; 317/339/370/414). Add the retrieval year, as the FY2 data rule asks.
- docs/exercise-bank/FY2.md:50 (carried over) — the plan's temperature-anomaly graph task and the real Finnish sector data (L2-06 is still invented) are neither done nor recorded as dropped.

## Checked
- Round-1 Polish acted on: the L1-07 prefix is gone, L1-06 now says "ennen kaikkea", "esimerkkiaineisto" has been replaced by NOAA, the "piirretty pistejoukko" is removed, L3-05 names its coefficients and gives the sinks sentence, and L2-07 says 1,6 kg.
- Recomputed L2-05 independently: 34 ppm / 15 a = 2,27 → 2,3 ppm/a; the end intervals give 2,0 and 2,6 ppm/a.
- L3-04: rates 1,1/1,55/2,2 ppm/a; forecast 458 ppm (459 from the unrounded data, within tolerance); whole-data forecast 446 ppm, 12 ppm lower.
- L3-05: now 52 220 t; plan 24 680 t → 52,7 % → 53 %; full wind 19 900 t → 61,9 %; the difference is 9,2 pp. All agree with answers.py.
- L3-05 d): the sinks are now given in the task, and the physics is right (concentration is a stock).
- L1-06, L1-07, L2-07: exactly one correct option each, every distractor is wrong, and every feedback is right. Dropping "suurelta osin" from the correct L1-06 option is C, because it matches the teacher's worksheet wording.
- Scope: m = e·E, slopes, percentages; L1-08 480, L2-06 26,2 also agree.
- The hash was unchanged at the start and at the end.

## Follow-up (2026-11-04, teacher's edit of L1-06: exercises.json:69, solutions.md:125)
- exercises.json:69 and solutions.md:125 (L1-06): both now say what the lesson Ydinajatus says: +15 °C is the mean surface temperature, −18 °C the effective radiating temperature of a simple radiative balance model, and the difference illustrates the greenhouse effect. No claim that −18 °C is the surface temperature without greenhouse gases remains. Physics correct (definitions, model, causality).
- Recomputed: $+15-(-18)=33$, and a temperature difference is the same in °C and K, so $33\,\text{K}$ is right; −18 °C ≈ 255 K is the textbook effective radiating temperature (σT⁴ = S(1−α)/4 with α ≈ 0,3), +15 °C ≈ 288 K the mean surface temperature.
- The correct option, distractors and their feedback are unchanged; still exactly one correct option.
- Polish (C, not a finding): "…, kun yksinkertainen säteilytasapainomalli antaa …" can be read as "because/when"; "kun taas" or "mutta" (the lesson's word) makes the contrast explicit.
- Scope: only these two sentences; the rest of this report stands from the earlier round.
