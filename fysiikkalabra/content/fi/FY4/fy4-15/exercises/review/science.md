VERDICT: PASS
CONTENT-HASH: bc698d30f1bc8ada

## Blocking

## Polish
- exercises/solutions.md:204 fy4-15-L3-05 — "kolme merkitsevää numeroa kuten korkeudessa 85,0 m ja hyötysuhteessa 0,800": the hourly powers (40, 52 … MW) have two significant figures and limit the result — give 1,0·10⁶ m³ or say the powers are taken as exact hourly means.
- exercises/exercises.json:74 fy4-15-L1-07 — P_o = ρQgh is L1-01 without η; close to a duplicate. Consider asking for the energy in one hour, or for Q from a given power, to vary the skill.
- exercises/exercises.json:300 fy4-15-L3-05 — "alaaltaasta" → "ala-altaasta" (language).
- exercises/solutions.md:194 fy4-15-L3-04 — "teoreettisen ylärajan 59 %" is not in the lesson brief (it is already used in L2-02); add "(Betzin raja)" or drop it, for consistency with what is taught.
- exercises/exercises.json:170 fy4-15-L2-06 — 120 m³/s and 9 MW stretch "pienvesivoimala" (Finnish limit ≈ 10 MW); fine, but "voimala" alone avoids the question.

## Checked
- Recomputed all 8 new answers in one script: L1-07 2,918 MW; L1-08 180 kJ; L2-05 ΣPt = 5,478 GWh (stored 5,5, within 2 %); L2-06 18,80 GWh (stored 19), May/Aug 120 : 28 = 4,3, 9,0 / 2,1 MW; L2-07 242,5 kW (stored 240), 49 × 4948 W, unit argument kg/(m·s) correct; L3-04 P/v³ = 1,250…1,241, mean 1,252 kW s³/m³, η = 39,9 %, model at 13 m/s 2,75 MW > 2,0 MW; L3-05 E = 300 MWh, V = 1,036·10⁶ m³, 86 % full, 6,00 h — all match solutions and answers.py; every rounded stored answer accepts the exact value.
- L1-06: one correct option (mgh per kilogram ∝ h); distractors wrong with correct feedback.
- Model conditions stated: constant η, below rated power, whole flow through turbine, constant power per row/hour, turbine losses ignored in L3-05 c.
- Rated-power limit of P ∝ v³ explained as in the lesson (L3-04 c); power vs energy kept apart (E = Pt, MWh/GWh).
- Efficiency ≤ 100 % and energy conversion, not production (guardrails).
- Notation as in the lesson (η, ρ, Q, A = πr², P_o).
- Scope: FY4 energy, power, efficiency; no later-course physics.
- Levels 8/7/5; L2 data and error-analysis tasks, L3 modelling (v³ from data) and pumped-storage reasoning as in the plan; no duplicate except the L1-07 note.
- Hash identical at start and end.
