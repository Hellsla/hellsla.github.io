VERDICT: PASS
CONTENT-HASH: 53a1321f7866ba94

## Blocking
(none left; see Fixed)

## Fixed
- lesson.md — worked example (Periaate, Yksikkömuunnokset, Tulos, Järkevyys) and the misconception paragraph were still the dense Finnish original → split into short sentences, significant figures explained in brackets, 'verrannollinen' explained, 'liikuntasauma' explained at first use, 'mikromalli (hiukkasmalli)' explained.
- figures.json — was empty (figures showed the dense Finnish); filled all 15 values (labels kept, 4 descriptions simplified) and redrew with figures.py.
- inquiry.json:pred-1 choice 1 feedback — typo "100 K, Mallin" → "100 K. Mallin".
- inquiry.json — long choice texts (pred-3 Bea and Cem, olomuodot choice 3, check-1 choice 3, kertaus choice 2 feedback) split into short sentences; worked solutions of siirto and check-2 (Periaate, Vastaus, Järkevyys) simplified, formulas unchanged.

## Polish
- None.

## Checked
- Translation review against the reviewed Finnish (teacher's decision 2026-10-28): lesson.md, inquiry.json (all prompts, choices, feedback, hints, mistakes, solutions, experiment intros/names, howto/model), exit-ticket.json, meta.json and figures.json against the Finnish; sim labels sims.fy3-8 resolved in the language. Compared register, term consistency with terms.md and lang labels, and that each question, hint and feedback still matches its option. Checked Selkeä suomi: short sentences, terms kept and explained, no steps or feedback dropped.
- Update 2026-10-28 (physics audit + figures/assessment on main): translated and checked the changed lesson texts (unit formatting, interactions wording, water/liquid caveat), the new check-c2 hole item, the trimmed exit ticket, the new activity titles and the figure description against the new Finnish.
- Update 2026-10-29 (sim LaTeX PR #132): pred-3 is now revealed after the theory section (reveal after theory, min 1) and exp-1 says "Testaa ennuste 1", both matching the Finnish; the waiting note lang/fi-easy.json inquiry.pending_theory ("Ennusteesi on tallessa. Saat palautteen, kun olet lukenut teoriaosan.") is short and plain, in the register of the existing pending note. Sim labels (KaTeX) and the rest of the translation re-compared with the current Finnish: complete, level kept.
