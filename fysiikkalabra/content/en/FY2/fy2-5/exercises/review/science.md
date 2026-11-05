VERDICT: PASS
CONTENT-HASH: 9b65aff5f585da33
Round: 3

## Blocking
(none)

## Polish
- Finnish source (not editable here): L2-08 solution says petrol has "lähes 40 MJ/kg" but H = 43; "yli 40" is accurate. Fixed in this translation only.

## Checked
- New task fy2-5-L2-08 (order, YO form) compared with the reviewed Finnish: data (43/1500 g, 15/5.0 kg, 26/0.0040 t, 10/12 kg), order items, answer string, unit "", tolerance 0.02, kind equal.
- Recomputed: 43*1.5=64.5, 15*5.0=75, 26*4.0=104, 10*12=120 MJ; order petrol < firewood < coal < milled peat is correct; 1500 g=1.5 kg, 0.0040 t=4.0 kg.
- Mass-order remark (petrol 1.5, coal 4.0, firewood 5.0, peat 12 kg) correct; firewood and coal swap.
- No formula, number or unit lost; L2-08 solution numbers equal the Finnish.
- Language: natural English, decimal point (5.0, 0.0040), no Finnish left.
- check_i18n.py: nothing for fy2-5; build.py fy2-5 succeeds. Earlier 16 tasks unchanged since round 2.
