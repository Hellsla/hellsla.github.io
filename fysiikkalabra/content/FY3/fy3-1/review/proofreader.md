VERDICT: PASS
CONTENT-HASH: 5eb1c5404fa22d24

# Proofreader, fy3-1, review round 4 (first pass)

## Blocking
None.

## Polish
1. lesson.md:22 — "Kuu on paljon pienempi ja kevyempi kuin Maa": "kevyempi" borrows weight vocabulary for a body's mass, in the paragraph that separates mass from weight — "massaltaan ja kooltaan paljon pienempi" (in the diff).
2. lesson.md:38 — "kuudesosa Maan arvosta" is clumsy — "Maan arvon kuudesosa" (in the diff).
3. lesson.md:3, 22, 38 — "painaa Kuussa" is colloquial verb use while line 50 warns against "painan 70 kiloa"; correct here (a force, no unit), optional: "astronautin paino Kuussa on vain kuudesosa".
4. lesson.md:8 — calibration paragraph is still long (about 170 words); optional split after "...2,5 N venyttää sitä 1,0 cm."

## Diff
```diff
--- a/lesson.md
+++ b/lesson.md
@@ -19,7 +19,7 @@
   <text x="302" y="96" fill="currentColor">voiman mukaan</text>
 </svg>
 
-Kappaleen paino on Maan ja kappaleen välisen vuorovaikutuksen voimakkuuden mitta. Se on voima, ja sen yksikkö on newton. Massa on aivan eri asia: se kertoo, kuinka paljon ainetta kappaleessa on, ja sen yksikkö on kilogramma. Massa on sama kaikkialla, mutta paino riippuu siitä, missä kappale on. Kuu on paljon pienempi ja kevyempi kuin Maa, joten Kuun ja astronautin välinen vuorovaikutus on heikompi kuin Maan ja astronautin, ja astronautti painaa Kuussa vähemmän.
+Kappaleen paino on Maan ja kappaleen välisen vuorovaikutuksen voimakkuuden mitta. Se on voima, ja sen yksikkö on newton. Massa on aivan eri asia: se kertoo, kuinka paljon ainetta kappaleessa on, ja sen yksikkö on kilogramma. Massa on sama kaikkialla, mutta paino riippuu siitä, missä kappale on. Kuu on massaltaan ja kooltaan paljon pienempi kuin Maa, joten Kuun ja astronautin välinen vuorovaikutus on heikompi kuin Maan ja astronautin, ja astronautti painaa Kuussa vähemmän.
 
 ## Kaava
 Kaksi samanlaista kappaletta venyttää voimamittarin jousta kaksi kertaa niin paljon kuin yksi, joten paino on suoraan verrannollinen massaan:
@@ -35,7 +35,7 @@
 | Maa | 9,81 |
 | Jupiter | 24,8 |
 
-Kuun g on noin kuudesosa Maan arvosta (1,62/9,81 ≈ 0,17), joten sama massa painaa Kuussa noin kuudesosan siitä, mitä Maassa. Tämä vastaa alun kysymykseen astronautista.
+Kuun g on noin Maan arvon kuudesosa (1,62/9,81 ≈ 0,17), joten sama massa painaa Kuussa noin kuudesosan siitä, mitä Maassa. Tämä vastaa alun kysymykseen astronautista.
 
 ## Esimerkki
 Tutkimusrobotin massa on 120 kg. Mikä on sen paino Maassa ja Marsissa?
```

## Checked
- L1-04 new data (4,0 N, 2,5 cm, 6,0 cm, answer 9,6 N): exercises.json text and solutions.md wording, N:n inflection, decimal commas and units correct; 4,0·6,0/2,5 = 9,6 agrees.
- lesson.md:22 and the new sentence at :38: grammar, case and the link back to the opening question are correct; 1,62/9,81 ≈ 0,17 is fine as ≈.
- exit-ticket.json: ticket 1 answer (29 N:sta, 4,9 N:iin, interaction reason) and ticket 3 ("vesi painaa" inside ”…” as the example of imprecise wording, with the correction in the answer) are correct Finnish.
- solutions.md: ≈ used only for rounded values (L2-01, L3-01, L3-02, L3-03); exact steps keep =; decimal commas and units fine.
- glossary.json "putoamiskiihtyvyys": the standard Finnish term, definition grammatical, g in m/s² (the N-per-kg remark is a number reading, not a unit for g); meta.json glossary list matches the lesson.
- Terminology paino/massa/voima/vuorovaikutus/voimamittari/newton matches glossary.json; weight is always a force.
- sim.js Finnish strings, sim-spec.md, exercises L1-01..L3-03 text: spelling, inflections, no N/kg for g.
- lint_lesson.py: 0 errors, 0 warnings. Hash at start and end: 5eb1c5404fa22d24.
