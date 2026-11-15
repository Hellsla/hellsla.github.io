VERDICT: PASS
CONTENT-HASH: 1042d3c37f4db574
SCOPE: delta round 2 (formula chains split, subscripts renamed, precision wordings)

## Blocking
(none)

## Polish
- solutions.md L3-06 reading the graph / answer — "lähes yhtä suuren energian" ylikorostaa: 3,06 ja 2,27 eV eroavat neljänneksellä; tarkempi: "kun luetut energiat vähennetään toisistaan, johtava numero kumoutuu ja suhteellinen virhe kasvaa".
- L2-09 vastaus 2,84 (3 merkitsevää) vs. epävarmuus ±0,02 eV: kolmas numero on epävarma; lisää "viimeinen numero on epävarma" tai pidä perusteluna vain mittaustarkkuus. Ei estä.

## Checked
- L2-09 chain split into hc, E in J, E in eV: each step one operation, units carried; 1.9865e-25/436e-9 = 4.556e-19 J and /1.602e-19 = 2.844 eV verified.
- L2-09 "energy secure to about ±0.02 eV": ±3 nm at 436 nm gives 0.02 eV; consistent, and answer tolerance 0.03 still covers it.
- L3-06 subscripts (viol/vihr or viol/green; E_a,viol etc.) are consistent across Given, Asked, Formula, Substitution; the g/green clash from round 1 is gone.
- L3-06 numbers verified: 3.0617, 2.2711, 0.7907 eV; 0.794 eV table value; 1240/0.79 = 1570 nm; the split Reasonableness formulas read cleanly.
- Model answer in c) still repairs the sum misconception directly.
- Figure lamp-spectrum and its description unchanged by the diff: no answer disclosed.
