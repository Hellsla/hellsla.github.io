VERDICT: PASS
CONTENT-HASH: 7eb29709fe3b4f87

## Blocking

## Polish
- content/fi/FY4/fy4-3/exercises/solutions.md:301 (L2-08) — the "Tarkistus" only restates the third law (circular) — replace it with a real check, e.g. "Yhtä suuri voima muuttaa kevyemmän henkilöauton liikettä paljon enemmän kuin kuorma-auton, mikä näkyy törmäyksissä: henkilöauto sinkoutuu, kuorma-auto tuskin hidastuu."
- content/fi/FY4/fy4-3/exercises/exercises.json:275 (L2-08) — "Esimerkkiarvot:" at the start of the text reads as if the masses were placeholders — drop the prefix.
- lessons/FY4/fy4-3/answers.py:23 — the comment lists L1-06, L1-07, L2-07 as multiple choice; add L2-08.

## Checked
- New task fy4-3-L2-08 (two-stage, type 1): F_HK = F_KH by Newton III regardless of masses or which car moved; exactly one correct choice and one correct reason.
- Notation: F_{KH} = force by K on H, F_{HK} = by H on K, as the lesson's F_{AB} = −F_{BA}; vectors with \overline, magnitudes plain.
- Choices catch the warned/classic mistakes: 1/10 (heavier pushes harder), 0 (only a moving body pushes). Reasons: mass ∝ force, "kumoavat toisensa" (this chapter's warned mistake: true premise, wrong conclusion), "vain liikkuva työntää", and the correct pair reason. Each feedback says why.
- Form: the correct reason is not the longest (86 vs 92/82/78 characters), not the only hedged one, and the "kumoavat" distractor also says "yhtä suuret ja vastakkaiset", so equality alone does not pick it. The correct choice's feedback states equal and opposite forces but not the voima–vastavoima reason, so it does not give the reason stage away.
- Scope: only the first and third law; no ΣF = ma needed.
- Solution complete, principle right, wrong options and the wrong reason explained.
- All 21 answers: answers.py run once and compared: 17 numeric within tolerance; L1-06, L1-07, L2-07, L2-08 each have exactly one correct choice (and reason).
- Inline formulas (text only): all short (F_{HK} = ⅒ F_{KH} the longest, ≈ 100 px).
- Hash identical at start and end.
