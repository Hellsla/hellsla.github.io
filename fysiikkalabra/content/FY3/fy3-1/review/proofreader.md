VERDICT: PASS
CONTENT-HASH: fc5375c46d696bd5

# Proofreader, fy3-1, round 2

Checked: lesson.md, exercises.json (text), solutions.md, exit-ticket.json, sim-spec.md, Finnish strings in sim.js, meta.json, glossary entries for fy3-1 (voima, voimamittari, vuorovaikutus, paino, massa, newton).

Result: no spelling, grammar, punctuation or terminology errors found. Hash was fc5375c46d696bd5 before and after the review.

Checked and fine:
- "jousivaaka" no longer appears anywhere; "voimamittari" is used consistently and is a glossary term (glossary and meta.json lists agree, alphabetical order kept).
- Decimal comma in text and `{,}` in math; space between number and unit everywhere; units inflected correctly (12 N:n, 6,0 N:n painolla, 22,0 kg:n, 0,20 kg:n, 3,0 kg:na, 29 N:sta, 4,9 N:iin, 15 N:n voimalla); no "25 m matka" type constructions.
- Finnish quotation marks ”painan 70 kiloa” in lesson.md and exit-ticket.json.
- Reading level suits 16-19-year-olds; paino/massa distinction kept (no "pitää painoa").
- sim.js strings and sim-spec.md are correct Finnish; decimal comma via fi().

Issues by kind:
1. Wording (minor, solutions.md, not published): L2-01 "Järkevyys" says "Noin 10 N painaa yhtä kilogrammaa", where subject and object are reversed. Diff below. Not a FAIL.
2. Nits (no change proposed, style only):
   - exercises.json, fy3-1-L3-03 text: "se näyttää kilogrammoina voiman jaettuna luvulla 9,81 N/kg" is grammatical but heavy; the sentence could be "se näyttää kilogrammoina voiman ja luvun 9,81 N/kg osamäärän".
   - solutions.md L3-01 "Paino pienenee suhteessa 3,71 / 9,81" could be "Paino on 3,71 / 9,81 ≈ 0,38-kertainen Maahan verrattuna".
   - lesson.md uses "Jupiterilla" (surface sentence) and "Jupiterissa" (exercises, solutions); both are correct.
   - Normal spaces rather than thin spaces before units, same as content/_gold.

Unified diff (not applied; copies in /tmp/claude-0/-home-user-hellsla-github-io/1d51c594-3563-5c38-9136-caaa788c1662/scratchpad/proofread-fy31b/):

```diff
--- content/FY3/fy3-1/solutions.md	2026-10-25 04:24:30.772439356 +0000
+++ content/FY3/fy3-1/solutions.md	2026-10-25 04:24:30.790038521 +0000
@@ -44,7 +44,7 @@
 **Kaava:** G = m g, joten m = G / g
 **Sijoitus:** m = 49 N / 9,81 N/kg = 4,995 kg
 **Vastaus:** 5,0 kg
-**Järkevyys:** Noin 10 N painaa yhtä kilogrammaa, joten 49 N vastaa noin 5 kg.
+**Järkevyys:** Yksi kilogramma painaa noin 10 N, joten 49 N vastaa noin 5 kg.
 
 ## fy3-1-L2-02
 **Annettu:** m = 60 g = 0,060 kg, g = 9,81 N/kg
```
