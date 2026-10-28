VERDICT: PASS
CONTENT-HASH: b75319bc1ce1db3b

## Blocking

## Polish
- inquiry.json:96 (kayra; pred-1 prompt) — pred-1 has "1,0 kg jääpussi ja juomia", while the kayra graph and text model only 1,0 kg ice (the post-melt rise uses C = 4190 J/K for 1,0 kg water). Either drop "ja juomia" from pred-1 or say in kayra that the drinks are left out of the model.
- lesson.md:203 (Esimerkki) — "0,80 m²" is plain text in a sentence whose other values are inline LaTeX.
- lesson.md Kaava, step 4 — the list names "not enough" and "just enough" but not "more than enough (all melts, temperature rises above the melting point)"; one clause would complete the guardrail's three cases (C-level, step 3 implies it).

## Checked
- Recomputed in one script: worked example (41 900 J, 33,6 W, 8,69·10³ s = 2,4 h; 2,8 h without drinks; 19 K/h initial rise), sauna paragraph (67 kJ / 452 kJ), misconception (126 kJ < 334 kJ), kylmälaukku bars (334 / 42 / 335 kJ).
- Lesson graph to scale: t₀ = 2,41 h, exponential approach τ = C/UA = 1,45 h, 25,6 °C at 6 h; kayra graph: t₀ = 3,68 h (UA = 0,90 W/K, 25,2 W), τ = 1,29 h, 27,0 °C at 8 h.
- Inquiry numerics: kayra 333 kJ (mistakes 92,5 and 5,55 right), taulukko rows P = 0,90ΔT and t = sm/P all right (8,59…2,86 h), pred-2 4,30 h → 2,86 h, löyly 85,7 % (mistakes 14,3 % and 6,0), virhe 10,7 °C / 62,9 kJ / 267 kJ / 0,19 and 0,61 kg, siirto 64,9 s (mistakes 8,4 and 56,5 s), check-2 213 kJ (mistakes 200 and 12,6), check-3 13 %, exit ticket 175,5 kJ and 335 kJ.
- Exactly one correct option in pr-teho, pred-1, pred-2, taulukko, virhe, check-1; distractor feedback right; "kylmä ei virtaa" uses the guardrail net-transfer wording.
- Plateau explained causally (energy goes to melting, temperature constant), rise slows because UAΔT falls; model values labelled as model, not measurements (source "model").
- Boundary case for mixing stated with its condition (ice initially at 0 °C) in the summary.
- lesson-answers.py reproduces the inquiry numbers; scope inside FY3.
