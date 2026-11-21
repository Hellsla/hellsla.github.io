VERDICT: PASS
CONTENT-HASH: 151c9ef890c265ae
## Blocking
(none)
## Polish
1. first box (hyötysuhde 0,85) asks what the paragraph just above already states (80-95 %, "enemmän energiaa kuin akkuun"); the answer is a restatement, so it is recall, not thinking. Fix (optional): ask for a number, e.g. how many kWh must be drawn to store 10 kWh.
2. Box 2 (6,9 kW, 3 phases) says "Kaavasta P = 3UI", but the displayed formula comes only later in "Kaava"; the prose before it does state "kokonaisteho on kolminkertainen", so the student can solve it. Fix (optional): say "kolminkertainen teho" in the answer or move the box after the formula.
3. Box 3 sits between the figure and the P = 3UI paragraph, splitting the formula section; works, but a box right after the t-formula block would read cleaner.
4. OLD: the lesson is long for one lesson (4 sub-sections plus the formula, example and heating); not touched by this PR.
## Checked
- Three boxes only, each after the paragraph that teaches its idea; question, rule line, answer behind a fold; student can act before seeing the answer.
- Task levels: recall (1), one-step rearrangement (2), formula substitution (3); different from the worked example.
- Numbers: 6900/(3*230)=10 A; 20/(0,9*5,0)=4,44 h; units and decimal comma correct.
- Answers give the principle (formula, substitution), not just the result.
- Language reads naturally at the course level; glossary terms (kolmivaihesähkö, vaihejohdin) used correctly.
- Boxes add no new load on the 360/390 px pages (layout checks ok); no old spot stops them working.
- Hash unchanged at the end.
