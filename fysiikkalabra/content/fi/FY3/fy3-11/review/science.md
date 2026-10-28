VERDICT: PASS
CONTENT-HASH: 52aa6a2eb19695e1

## Blocking

## Polish
- lesson.md:70 — "lämpötilaero kuuman lähteen lämpötilaan nähden" is the Carnot ratio, which holds only for absolute temperatures — add "(kelvineinä)" or "absoluuttisiin lämpötiloihin".
- lesson.md:221 — "500 MW … kolmen numeron arvo" is a choice, not a fact (a trailing zero is ambiguous) — say the powers are read as three-digit values, or write 5,00 · 10² MW.
- lessons/FY3/fy3-11/answers.py:12,14,34 — the comments end "-> 37 %", "-> 22 %", "-> 12 kW", but the answers are 37,2 %, 21,7 % and 12,0 kW — match the comments to exercises.json.
- exercises/solutions.md:98 — typo "polttoatehon" — "polttoainetehon".

## Checked
- Recomputed in one script: every exercise answer, exp-1 (ΔV = 2Q/(5p₁): 1,00/1,50/2,00 l, W_k 200/300/400 J, ΔU 600 J), the cycle B values Q₁ = 650 J, Q₂ = 550 J, W = 100 J, η ≈ 15 %, cycle A W = 0 with Q₂ = 500 J, suunnittele (2000/1250/800 MW, distractors 941 and 667), siirto 22,5 MW, check-2 450 J, exit ticket 100 J and 18/42 kW.
- sim.js phaseAt matches the stated monatomic model; Q₁ − Q₂ = W holds in every phase; the η key appears only after the cycle is done.
- Sign convention: ΔU = Q − W_k is tied to fy3-5's ΔU = Q + W with W = −W_k, the same in the theory, kertaus, virhe, the solutions and answers.py.
- Efficiency guardrails: the CHP total efficiency is kept apart from the electrical efficiency (85–90 %, example 88 %); the heat pump's lämpökerroin is said not to be an efficiency; the resistance heater is "käytännössä" 100 %; the heat engine limit is stated with no false "unavoidable friction" cause.
- Exactly one correct option in kertaus, pred-1, pred-2, exp-2 question, virhe and check-1; each distractor's feedback gives the right reason.
- Flow-figure widths: 24/60 = 40 %; heat pump 20 + 40 = 60, COP 3.
- Example: η₁ = 0,380, η₂ = 0,880, losses 310/60 MW; the balances close.
- The sim's numbers are called model values in the feedback and the conclusion's model answer.
