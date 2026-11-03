VERDICT: PASS
CONTENT-HASH: e28dcd59bc448907

## Blocking

## Polish
- solutions.md:59 (L2-01): the Vastaus line is muddled ("rajoittaisi … 170 km; annetaan 168 km välituloksen kanssa"). Either answer 170 km with two significant figures, or say plainly that 168 km is shown and 170 km is accepted.
- solutions.md:111 (L3-02): "Todellinen syvyys on näiden alapuolella" reads as "deeper". Write "pienempi kuin kumpikin", since the true depth is 5,96 cm against 6,16 and 6,32 cm.

## Checked
- One script recomputed all twelve answers. The changed ones are L2-01 168 km (t_P 24 s, t_S 42 s, recording started 12 s after the quake), L3-01 7,06 m and L3-02 5,962 cm. All match answers.py and exercises.json.
- L3-01 now separates the models: the stationary-bat answer 6,86 m is 2,8 % off and rejected at tolerance 0,02, while the two-figure answer 7,1 m is accepted (0,6 %).
- L3-02 now separates the models: the one-speed 1540 m/s answer 6,16 cm (3,4 %) and the all-muscle answer 6,32 cm (6,0 %) are rejected, while the two-figure answer 6,0 cm is accepted (0,7 %).
- L2-01: 7,0/4,0 km/s is realistic crustal data, the same figure (P 12 s, S 30 s) still serves, and 170 km is accepted (1,2 %).
- L3-01 model: sound travels d + (d − v_b t) = vt. L3-02 model: the fat layer is crossed there and back, and the remaining time is spent in muscle. Both correct and stated in the tasks.
- L2-03 rewording ("suurin pulssien lähetystaajuus", s⁻¹): correct.
- L2-02: the 2λ criterion is now explicitly tied to the lesson's "muutama aallonpituus". Consistent.
- Unchanged tasks L1-01–L1-05, L2-02, L2-04 and L3-03 were recomputed: correct, with sound rounding and real reasonableness checks.
- answers.py:10 comment now says 0,205 mm.
