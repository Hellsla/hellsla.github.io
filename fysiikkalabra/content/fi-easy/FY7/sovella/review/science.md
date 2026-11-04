VERDICT: PASS
CONTENT-HASH: 698712979e3823c0

## Blocking
None.

## Polish
- fy7-s2 d Johtopäätös: the fi text says "Jarrutus on silloin … paljon pienempi …, **koska** rautasydän tehdään ohuista eristetyistä levyistä". The split leaves "Rautasydän tehdään ohuista eristetyistä levyistä, joissa pyörrevirrat jäävät pieniksi." as a separate sentence, so the reason link is now only implied. "Syy on se, että rautasydän …" would keep the justification explicit, as the S2 rule asks.
- The fi round 2 polish points carry over unchanged: s3 e gives the time-averaged force, and s4 e's 500 nm reflection equals bare glass.

## Checked
- I compared fi-easy with the reviewed fi (af9c16707d86ff5d):
  - tasks.json: every string.
  - solutions.md: every line. It has 343 lines like fi, with the same sections and no line added or dropped.
  - figures.json: every alt text.
- Answers, units, tolerances, points (83) and links are identical. practice.py check reports OK.
- A script compared every formula and every number in the prose, section by section. All of them are identical, including the s1 d `mv = …` split and its decimal commas.
- Every step, reason and condition survives the sentence splitting:
  - s1: F_m points up, so the upper plate is + and the field points from + to −. "Massa ja varaus eivät vaikuta" to the selector. The distance is two significant figures because it is a difference.
  - s2: e₀ ∝ f ∝ v. The no-load assumption becomes "Oleta …". Lenz's law and energy conservation. Eddy currents with the light off.
  - s3: the 2·25 km circuit. The loss falls with I². The AC currents are opposite at all times. l ≫ r is now its own sentence.
  - s4: the slab is assumed to be a black body. The grey-body case is rewritten as "Oletetaan, että …", which is still correct. Both reflections invert. The soap-film error.
  - s5: kλ on the horizontal axis. The ±3 nm and ±1 nm uncertainties and the "vain niukasti" second order. Interference against refraction.
- No definition is new or wrong. The added sentence "Laitetta, joka tekee tämän, sanotaan ioni-istuttimeksi" is correct.
- Rendered page (Playwright, 390 and 1280 px, every solution open):
  - The figures match fi.
  - The headings are the standard fi ones.
  - check_layout FY7-sovella --width 340 reports OK.
- The hash was 698712979e3823c0 at the start and at the end.
