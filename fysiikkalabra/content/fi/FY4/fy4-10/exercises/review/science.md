VERDICT: PASS
CONTENT-HASH: f73c86410af7bc40

## Blocking

## Polish
- exercises.json:258 (L2-08, row 4 feedback) — "kimpoamisen etumerkki kuuluu nopeuteen v_A' rivillä 3" names the wrong row on a wrong pick, so a retry becomes trivial — end it after "…jaetaan massalla m_B" and give a hint only ("tarkista, mitä riviltä 2 sijoitettiin").
- exercises.json:252 (L2-08) — the correct label "Rivi 3: vaunun A nopeus törmäyksen jälkeen" is the longest option, by a few characters. This is marginal, but you could shorten it, for example to "Rivi 3: A:n nopeus jälkeen".

## Checked
- New task L2-08 (Virheen löytäminen), recomputed: v_B' = (0,24 + 0,060)/0,50 = 0,60 m/s; the student's version gives 0,36 m/s. Exactly one row is wrong (row 3, the sign). Row 4 is algebraically right given row 3.
- The data are self-consistent: the kinetic energy is 0,096 J before and 0,006 + 0,090 J after, so the collision is exactly elastic, which fits the formula (m_A − m_B)/(m_A + m_B) · v = −0,20 m/s. The rebound is physically possible.
- The "ei virhettä" feedback check is right: B's momentum must exceed 0,24, and 0,50 · 0,36 = 0,18 does not.
- The distractor feedback carries the chapter's warned ideas: sign forgetting is the key, the kinetic-energy-instead-of-momentum idea sits on row 2, and a body at rest having momentum sits on row 1.
- Conditions are stated: friction is neglected, and weight and normal force cancel. Momentum is conserved across the collision. The notation (v, v′, m_A v_A) matches the brief.
- solutions.md:185–202 complete, symbolic before numbers, with a real check.
- Inline formulas checked from the text only, with no render. The longest, the full conservation law in Periaate, is about 200 px.
- answers.py comment agrees; the rest of the set is unchanged since the PASS. Hash is the same at the start and at the end.
