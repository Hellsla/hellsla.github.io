VERDICT: PASS
CONTENT-HASH: e63164d38e934673
SCOPE: full: unit.md (the three new "Pysähdy ja mieti" boxes first), inquiry.json, teacher.md, sovella tasks s1-s9, solutions.md, answers.py; physics compared with the fi version. Language: en.

## Blocking
(none)

## Polish
- kone figure (now a webp image under the LaTeX labels): measured arrow widths in the image are Q1 272 px, Q2 178 px (0.654), W 91 px (0.335 instead of 0.35). The caption says "arrow widths to scale". The deviation is small (outgoing arrows 99 % of Q1), but W is 4 % narrow. A 99 px W arrow would match.
- inquiry `pumppu`: the mistake value 100.0 kPa ("gauge pressure substituted into Boyle's law") comes from no obvious wrong calculation path (gauge 0 kPa gives 0). It is the same in fi. This is not an error, but the trigger is probably unreachable.

## Checked
- Pysähdy boxes, against fi line by line: (1) gauge reading vs total pressure, 101 + 230 = 331 kPa. (2) The extension to zero is a model prediction because a real gas condenses first. (3) η < 100 % because Q2 to the colder surroundings cannot be avoided, so W = Q1 − Q2 < Q1. Physics, numbers and conditions are the same as fi. All three agree with the surrounding text, the Common mistakes list, lt-6 and tarkistus-1. No guardrail break (no "turns into heat"; the cyclic engine is stated).
- I recomputed every number in one script (R = 8.31, g = 9.81, 273.15) and set it beside answers.py. Everything agrees. Hook: 285.8 kPa total and 184.8 kPa gauge, −14 % and −20 %. Inquiry: lt-4 1.068, celsius 113.6 kPa, aineisto 0.0602 and 0.0361 mol, luukku 17.66 kN (mistakes 54.0 and 29.4 kN), pumppu 151.5 kPa (40.4), pallo 832 kg (87 942 kg in Celsius, 28 701 mol), manta 750 J, tarkistus-2 58.3 kW, well 10.3 m. Sovella: s1 562.1 kPa, 21.19/25.0/3.81 kJ, 650 kPa, 501 kPa, 0.42 m. s2 2183 mol, 34.92 kg, 485.1 and 174.6 kW, 84 %, 77.6 kW. s3 least squares k 0.1351 ml/°C and −279 °C. The extreme lines (−264.5 and −294.4 °C, ±15) touch the bars at exactly 0.3 ml. s3 also: 1.646 and 1.680 mmol, shift 11 K to −290 °C, −25 °C gives 34 ml. s4 6.0 %. s5 25.45 g/mol, 30 °C gives 26.6, −10 kPa gives 26.7, total-pressure error gives 17.2 (about two thirds). s6 72.0 kg, 11.21, 18.69 and 37.4 kPa, safety factors 5.35, 3.21 and 1.61. s7 37.2 %, 2700 MW, 64.8 GWh = 2.33·10¹⁴ J, 11.3 K (18.0 K from 4300 MW). s8 0.0602 mol, 40 %, 63.3 kPa. s9 750 J, 0.1026 mol, 1173 K.
- Physics: the force balance on the piston uses the pressure difference, and the outside-air work is explained. s1c: flow continues only while tank pressure ≥ cylinder pressure. The heat-pump COP is distinguished from efficiency. In s6 the pressure force is perpendicular to the glass and the upright pane is carried by static friction ≤ μ0N; its FBDs list no invented forces. The first-law sign convention (W done on the gas) is consistent across text, johda, manta and s9d.
- Assessment: each part's criteria add up to its points, and each criterion asks only what its part asks. Every choice item has exactly one correct option, and every distractor's feedback is right. Scope is FY3, with FY1/FY4 links. Significant-figure reasons are stated.
- Hash e63164d38e934673 at start and end.
