VERDICT: PASS
CONTENT-HASH: 2a315176056af704

Round 3 (delta): L3-04 Sijoitus split into display `aligned` rows for 360 px (commits bf75c929d, 6018cf733); the rest of the set unchanged since the round-2 PASS.

## Blocking

## Polish
- exercises.json L2-07, fourth option feedback — "Virhe syntyy siitä, että jään massa tai lämpötila poikkeaa oletetusta": in this task only the mass explains a too-small s (colder ice makes it too large, as the first option's feedback says). Write "jään massa poikkeaa oletetusta".
- exercises.json L1-06 / solutions.md L1-06 — "Täsmälleen 0 °C" holds at normal pressure; the lesson's Tiivistelmä says "normaalipaineessa". Optional to add (level-1 simplification, C).
- docs/exercise-bank/FY3.md fy3-14 Taso 2 — the planned "lämpötila-aikakuvaaja, jossa kaikki jää ei sula (figure)" has no task; L2-06 (error analysis, table-free) covers "kaikki jää ei sula". Update the plan line or note the substitution.

## Checked
- solutions.md:186-200 L3-04 recomputed: 0,200·21,8 − 0,0500·8,2 = 3,95; 0,200·23,8 − 0,0500·6,2 = 4,45; 4190·3,95/0,0500 = 331 010 → 331 000 J/kg = 331 kJ/kg; 4190·4,45/0,0500 = 372 910 → 372 900 J/kg = 373 kJ/kg.
- c): 2100·0,0500·18,0 J = 1890 J; (18 645,5 J − 1890 J)/0,0500 kg = 335 110 → 335 100 J/kg. Every value identical to the previous single-line chain; Vastaus (331/373/335 kJ/kg) and answers.py untouched.
- The bracket is still m_v(T_v − T) − m_j T with c_v factored out, consistent with the Kaava line; units J and kg on the display rows as before.
- Hash unchanged at start and end.
