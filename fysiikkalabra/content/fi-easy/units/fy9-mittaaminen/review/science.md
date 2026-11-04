VERDICT: PASS
CONTENT-HASH: 167a7e1ffcb6d0db

Science review of the fi-easy (Selkeä suomi) translation of fy9-mittaaminen against the reviewed Finnish source.

## Blocking
None.

## Polish
1. [Minor] unit.json key_concepts "mittausepävarmuus": "Kertoo, kuinka paljon tulos voi erota oikeasta arvosta." docs/physics-guardrails.md calls the uncertainty an *estimate* of how large the error may be, not a guaranteed limit. Fix: "Arvio siitä, kuinka paljon tulos voi erota oikeasta arvosta."
2. [Minor] unit.md "Suoran yhtälö ja sen tulkinta": "Malli on osoitettu oikeaksi vain mitatulla alueella" (source: "päteväksi"). "Oikeaksi" is a little stronger than the source. Fix: "Mallin on osoitettu pätevän vain mitatulla alueella" (or "toimivan").
3. [Minor] sovella/solutions.md s3 b) "Seitsemän muun pisteen ja pisteen 20 ml väliin" is the source's own wording, but for S2 readers "Kaikkiin pisteisiin paitsi riviin 60 ml (kahdeksaan pisteeseen)" says the same thing more clearly.

## Checked
- check_i18n.py: fi-easy 0 errors; units.py check ok.
- Every text string of unit.json, inquiry.json, exit-ticket.json and sovella/tasks.json (316 strings): the multiset of numbers is identical to the source in every string. unit.md, teacher.md and solutions.md were compared section by section (8/6/40 sections): no number was lost or added.
- I recomputed the key results myself: 32,46/12 = 2,705 → 2,7 g/cm³; θ₀ = −75,0/0,276 = −271,7 °C; ε = 0,05/1,85 = 2,7 %; k = 15,8 N/0,200 m = 79,0 N/m, L₀ ≈ 0,135 m; a = 2·0,620 = 1,24 m/s²; t = 46/4,6 = 10 min; Δρ = 0,028 g/cm³ → 30 kg/m³; group A (1,8033 ± 0,0005) m, group B (1,803 ± 0,015) m; exit ticket 45,7 ± 1,2 mm; s1 v = 7,294 m/s, Δv = 0,123 m/s; s2 d = 102 ± 2 µm, σ = 79,85 g/m², ρ = 783 kg/m³; s3 k = 0,919, b = 118,6 g, m(1,50 l) = 1,38 kg; s4 factor 1,02, 765/1,02 = 750 g; s5 v = 0,477 ± 0,014 m/s; s6 C = 2,61 J, n = 2,61/(8,314·295,15) = 1,06·10⁻³ mol, p(V+V₀) = 2610/2601 kPa·ml. All agree with the source.
- The correct options, feedback logic, rubric criteria and the model answers keep the source's physics. The simplified sentences change no conditions of a law (Boyle: constant amount and temperature; s = ½at² from rest; extrapolation stated as a model prediction; repetition does not remove systematic error).
- The key concepts are physically correct and match the text.
