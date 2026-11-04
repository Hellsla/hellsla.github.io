VERDICT: PASS
CONTENT-HASH: 4208bb67071dc3d5

Science review of the English translation of fy9-kokeellisuus (source content/fi/units/fy9-kokeellisuus/, passed).
Method: field-by-field comparison of every LaTeX expression and number in inquiry.json, exit-ticket.json and
sovella/tasks.json against the Finnish (only the decimal sign differs, plus the subscript v_sovellus -> v_app);
JSON data (answers, units, tolerances, correct flags, points, criteria keys, links, skills) identical;
check_i18n.py: en 0 errors. All numbers recomputed in one Python call: 2.29 %, k = 24.67 N/m (T = 0.894 s at
0.50 kg), theta_0 = -275.1 C (p0 = 101.33 kPa), s_min = 14 m, rho 8.18/7.70 g/cm3 and Delta rho = 0.24, t = 160 s,
g = 9.695 and Delta g = 0.872 m/s2, pendulum T^2 values and least-squares slope 4.020 s2/m (g = 9.82, d = 5.1 cm),
stone 2677 kg/m3 and Delta rho = 78 kg/m3, bicycle slope 0.1205 s2/m (a = 4.15 m/s2), mu_0 >= 0.425, 1.05^2 = 1.1025,
3.78 m/s2. All agree with the text. Figure texts and descriptions (figures.json) carry the same numbers with the
decimal point.

## Blocking
None.

## Polish
1. "Swing" for *heilahdus* (unit.md "Formula" section "measured, for example, from ten swings"; exit-ticket.json
   q2; sovella/tasks.json s4 text "the time t_10 of ten swings"; solutions.md s4 "Yleisiä virheitä" item 2). In
   English a "swing" is often read as half an oscillation, which would halve T. The text does say T = t_10 : 10, so
   nothing is wrong, but "ten oscillations" (or "ten full swings") removes the ambiguity.
2. solutions.md s6 a) Principle: "the motion is uniformly changing" -> "the motion is uniformly decelerated".
3. solutions.md s6 "Yleisiä virheitä" item 3: "the two of the factor 1/2 is forgotten" is unclear -> "the factor 2 in
   k = 1/(2a) is forgotten".
