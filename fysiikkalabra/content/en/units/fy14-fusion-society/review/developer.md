VERDICT: DONE

Unit fy14-fusion-society, "Fusion in the energy system" (FY14 chapter 8, order 1). Developer report 2026-11-01.
Content hash at hand-over: f86c35be7cb1d95d.

## Files
- `unit.json` (21 sources checked 2026-11-01), `unit.md` (Why, hero, Energy, Claims, Uncertain, Key idea, Fuel with the fuel-cycle figure, Compare, staged worked example, Common misconception, Summary), `inquiry.json` (28 activities), `teacher.md`; `lessons/units/fy14-fusion-society/figures.py` (hero: wind, solar, coal, fission, town and a fusion building under construction, no text; `cycle`: D–T fuel cycle with the lithium blanket, labels 28 units in a 600-wide figure).
- Core path: review of Q; pair discussion; predictions (JET's fuel mass; main fusion waste) revealed by the theory summary; Ember 2025 electricity table (statistics) with a question; pair discussion on firm vs variable power; the balanced evaluation task: 9 dated statements sorted into established result / institutional plan / corporate claim (`match`), with a written justification; theory summary (476 words); vocabulary match; worked example (energy per kg of D–T vs petrol); numeric task (tritium burned per GW-year, complete solution, two mistake feedbacks); optional NIF error-spotting; three checks (safety, tritium decay, waste claim) and a headline evaluation; French corner with `say`.
- No prediction of when fusion electricity arrives; every changing fact dated; "as of November 2026" for the absence of fusion electricity.

## Numbers (Python, CODATA/AME constants)
- Q(D–T) from masses 17.589 MeV; e_DT = 17.6 MeV / 5.030 u = 3.375e14 J/kg (exact masses 3.3739e14; Wikipedia 3.3739e14); ratio to petrol 46.4 MJ/kg 7.27e6.
- Tritium: 1 GW · 3.156e7 s / 2.820e-12 J = 1.119e28 reactions → 56.1 kg (exact 56.05 kg); mistakes 93.5 kg (D+T mass), 1.78e-6 kg (per second).
- Decay: (1/2)^(10/12.3) = 0.570, 25 kg → 14.2 kg; 5.47 %/a.
- JET: 69.26 MJ / 0.21 mg = 3.30e14 J/kg; 69.26 MJ ≈ 1.49 kg petrol. Deuterium per litre of water: 0.0348 g.
- Ember 2025 table: wind + solar 8.5 + 8.7 = 17.2 % (Ember 17.3 %); "other" row 5.1 % = remainder.

## Facts verified (2026-11-01; sources in unit.json)
Ember Global Electricity Review 2026 and world page; Energy Institute data via Wikipedia (fossil ~80 %, ~590 EJ summed); IPCC SR1.5 (8 Oct 2018); tritium half-life 12.32 a, Li-6 + n (+4.8 MeV); civilian stock ~25 kg, CANDU ~2 kg/a, ~55 kg per GW-year (Kleinman Center, 6 Mar 2025); ITER pages *Tritium breeding*, *Advantages of fusion*, *Safety and environment*; JET 69.26 MJ / 0.21 mg (EUROfusion 8 Feb 2024); NIF 3.15/2.05 MJ, ~300 MJ electricity, 8.6 MJ 2025; WEST 1337 s (12 Feb 2025); ITER 2024 baseline and costs; STEP 2040 (GOV.UK 12 Jun 2025); Helion–Microsoft 50 MWe from 2028 (2023), 2024 goal not met; SPARC 2027; FIA 2026 survey (WNN 14 Jul 2026); deuterium abundance; masses (NIST).

## Checks
units.py check OK; check_layout 360/1280 OK (long inline formulas split); screenshots looked at (table header fixed, cycle figure redrawn larger); Playwright: predictions locked until the theory, 8 choices answered, model answers only after writing, worked example and solution opened and inspected, no console errors, no raw `$`, no katex errors.

## Open questions
- ITER's website says fusion releases "nearly four million times" the energy of burning coal, oil or gas; the computed ratio to petrol is 7.3 million. The worked example's reasonableness step explains why such comparisons differ.

## Shared issues
None found in the components used (match, say). See fy14-global-fusion-explorer for facilities.json.
