VERDICT: PASS
CONTENT-HASH: 4c569087682acfc2

Mode: translation review (en) against the reviewed Finnish. Round 2, new task fy3-14-L2-08.

## Blocking
- none

## Polish
- none

## Checked
- delta review 2026-11-07 round 3 (fixes to round 2 findings): round 2 Polish (L3-05) resolved. Formula: c_w m_w ΔT_w = Q_i + c_w(m_w+m_i)(T − 0 °C), T_i = 0 °C − ΔT_i, ΔT_w,min = Q_i/(c_w m_w), T_w,min = 0 °C + ΔT_w,min; conversions define ΔT_w = T_w − 0 °C. Recomputed: Q_i = 50 280 − 13 575.6 = 36 704.4 J, ΔT_i = 15.7 K so T_i = −15.7 °C, ΔT_w,min = 36 704.4/1257 = 29.2 K so T_w,min = 29.2 °C; consistent with the Principle and the inquiry. Hashes equal at start and end.
- delta review 2026-11-07 round 2 (follow-up consistency edits): L1-06: shortened correct option (about 0 °C, ice and water coexist in equilibrium only at the melting point) correct, lengths now comparable with the distractors, same form, answer equals option text, teacher's full sentences open its feedback. All Q_w = c_w m_w ΔT_w edits (L2-01, L3-01, L3-03, L2-06, L2-08, L3-05, L1-08 feedback 18 855 J) correct; L3-05 Principle (T_w,min − 0 °C) correct, limit 29.2 °C recomputed (Polish). Hashes equal at start and end.
- delta review 2026-11-07 (teacher's proofread replacement texts): L1-06 correct option, answer key, feedback and model answer: pure water–ice mixture in equilibrium at about 0 °C at normal pressure (melting/freezing point), no net heat transfer so no melting or freezing: correct, conditions stated, exactly one correct option, agrees with the lesson summary. English text carries the same meaning as fi.
- fy3-14-L2-08 recomputed independently: Q_w = 4190*0.25*18 = 18 855 J, Q_i = 334000*0.080 = 26 720 J, melted 56 g, 24 g left, T = 0 C; statements 1 T, 2 F, 3 T, 4 T, 5 F. Equals fi.
- Answer, unit, tolerance, kind, order/statements/choices, correct flags and their order equal fi.
- solutions.md of L2-08: every number, unit and formula equals fi; English decimal point used.
- Physics and scope unchanged; no Finnish-only terms left in en.
- No translation fix needed. check_i18n.py shows nothing for fy3-14; build.py fy3-14 succeeds.
