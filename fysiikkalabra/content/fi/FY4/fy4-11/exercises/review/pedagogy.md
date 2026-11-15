VERDICT: FAIL
CONTENT-HASH: 92b3863b2eaf9805
## Blocking
- content/fi/FY4/fy4-11/exercises/solutions.md:345 (fy4-11-L2-10, **Vastaus**) — the model answers of all five parts are one unbroken paragraph of about 270 words, in the order c, a, b, d, e (capture fy4-11-open-exercises-L2-1280-15.png: twenty lines without a break). The whole answers to d (the force explanation) and e (the ABS claim), which the task asks for as parts of their own, are buried in it, so a student who could not solve the task cannot find or follow them; CLAUDE.md Readability allows about 120 words and one thing per paragraph. — Give each part its own paragraph separated by an empty line, as fy4-8-L2-10 does: first the boxed result of c with its significant figures, then a), b), c) (the 80 km/h margin), d) and e) in order; no sentence needs to change.
## Polish
- exercises.json fy4-11-L2-10 c — the collision speed is the one step of level-3 demand (reaction distance, remaining distance, a relation $v^2 = v_0^2 - 2as$ the chapter does not state, a conversion) and it is the answer-box value — add a hint, e.g. `"hints": ["Laske ensin, kuinka pitkä matka jarrutukseen jää reaktiomatkan jälkeen.", "Nopeudesta $v$ pysähtyminen vaatisi vielä matkan $\\tfrac{v^2}{2a}$."]`.
- exercises.json fy4-11-L2-10 b and e — both end in "jarrutusmatka kasvaa nopeuden neliössä"; to cut the overlap let b only compare with the calculator ("… vertaa tuloksia laskurin arvoihin.") and keep the proportionality argument for e.
- solutions.md fy4-11-L2-10 (**Kaava**) — the sentence about part d ($\mu = a/g$) stands between the derivation of $v^2 = v_0^2 - 2as$ and its final form; move "Törmäysnopeus on $v = \sqrt{\ldots}$" directly after the derivation.
- exercises.json and solutions.md fy4-11-L2-10 — "luettu 16. marraskuuta 2026" is a day after this review round (15.11.2026); write the date the calculator was actually read.
## Checked
- Round 1, full (ids changed): compared with the version passed on main, only fy4-11-L2-10 is new; four small solution fixes (significant-figure wording in L2-05, L3-05 18 kN, L3-06 11 kN) read and fine.
- Counts 9 + 10 + 6 = 25; levels otherwise fit the rubric.
- L2-10 is applied and the source is necessary: the student reads the calculator's values and its stated reaction time and decelerations, then tests the model behind it.
- Progression read (a) → recompute and compare (b) → use on a new situation (c) → explain with forces (d) → judge a claim and the model's limits (e); five parts.
- Only FY4 knowledge: this chapter's formulas, Newton II and friction; the solution derives the collision speed from the chapter's own $s_\text{j}$ formula.
- Part c at 80 km/h reuses the worked example's numbers (9 m/s², about 50 m) but as a step towards the 0,3 m margin and the 100 km/h collision speed, not as a repeat.
- Dated example solution with the instruction to use one's own readings: present and clear.
- Situation first, question last; "kitka" only; case endings correct.
