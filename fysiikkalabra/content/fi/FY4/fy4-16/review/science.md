VERDICT: PASS
CONTENT-HASH: 6dc6c5354081ac27

## Blocking

## Polish
- inquiry.json:19 (hook) — the round-1 note was applied to the johtopaatos prompt, not here: the hook still says the measured stopping points are "yhtä kaukana", while lesson.md (Miksi pulkat pysähtyvät yhtä kauas) says a real sled on the steep side stops a little earlier. Write "lähes yhtä kaukana".
- inquiry.json:178 (johtopaatos) — the prompt now asks why the sleds stop "lähes yhtä kauas", but the table's model values (and the model answer) give exactly 60,0 m on every row. Add "mallin mukaan yhtä kauas (todellisuudessa lähes)", or keep "yhtä kauas" in the prompt because it asks about the table.

## Checked
- Round-1 Blocking fixed: Tiivistelmä restricts "tukivoima ei tee työtä" to a body sliding on a fixed surface and says the lift floor's normal force does work; siirto Järkevyys says "Jos ilmanvastusta ei olisi".
- Recomputed every lesson and inquiry number in one script: lift 648,6 N / 66,1 kg; 78,48 kJ; Tutki 1 a = 1,023 and −0,643 m/s²; table x1, v, x2 to the printed digits, Σ = 60,0 m, √(2gh) = 10,85 m/s; example 0,1541, 8,694 m/s, 12,95 m/s, a = 1,512 m/s²; siirto 95,65 kJ and its mistakes; check-2 48,27 kg and mistakes; suitcase 149,6 N < 176,6 N.
- Force-plate graph (figures.py): 650 N for 1,0–3,0 s and 550 N for 9,0–12,18 s are consistent with the lift ending at rest.
- Energy principle with W_muut, W_μ = −μmgx with its stated conditions, tan α > μ, losses in the bend named; the table text now states the no-bend-loss assumption.
- Force diagrams (kolme, esimerkki, malli-laukku): right bodies and interactions, relative lengths, v and a not drawn as forces, no third-law pairs.
- All choice items have exactly one correct option, and each distractor's feedback is correct. check-1, check-3 and the exit ticket agree with the theory.
- Scope: FY4 central contents.
