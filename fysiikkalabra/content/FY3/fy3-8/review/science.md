VERDICT: PASS
CONTENT-HASH: 27015f4ef5f3ac24

## Blocking

## Polish
- content/FY3/fy3-8/inquiry.json pred-3 (Aino feedback) — "mikromalli olettaa, että hiukkaset ovat samankokoisia … ja silti hila laajenee" cites the sim's own assumption as if it were evidence; the spacing is set from the formula — lean on the theory instead ("Teoriatiivistelmän mikromallissa hiukkaset pysyvät samankokoisina; kasvaa vain niiden keskimääräinen etäisyys").
- content/FY3/fy3-8/lesson.md figure "particles" — the amplitude arrows are drawn symmetric about each particle while the paragraph above explains the asymmetry; consider a longer outward than inward arrowhead on the warm row, or a caption "keskimääräinen etäisyys kasvaa".
- content/FY3/fy3-8/sim.js readout — axis range still "−20–30 mm" (en dash after a negative number) — write "−20 mm … 30 mm".
- content/FY3/fy3-8/sim.js — `fi` unused — delete it.
- content/FY3/fy3-8/sim-spec.md — still lists α beside each material in the select and omits `rel` from simState — "α näkyy lukemissa", add rel.

## Checked
- answers.py and all 12 exercises recomputed independently (2,88; −51,75; 0,85; 0,84; 0,3375; 52,08; 3,024; 36; 23; 120; 20; 457): all match within 2 %; solutions symbolic first, signs and units right.
- Worked example 0,0864 m ≈ 86 mm, 0,072 %; exit ticket 0,021 m.
- inquiry numbers: pred-1/pred-2 6,00 / 12,0 mm, 0,0600 %; olomuodot 0,36 / 2,1 / 11 / 34 cm³; virhe 27,9 vs 1,84 mm (×15); siirto 44 mm, mistakes 0,044 and 110, with glass 42,9 mm, ratio ≈ 41; check-2 α = 23, mistakes 46 and 15,3; air/steel γ ≈ 94.
- Round-2 change: pred-3 now revealed after theory, whose Ydinajatus gives the asymmetric-interaction argument its feedback relies on ("Teoriatiivistelmä perustelee sen"); correct option (Bea) and the Cem/Daniel/Aino repairs are sound physics.
- exp-1 now tests only pred-1: locks material and L₀, varies T (70, 120, −30 °C inside −40…120), measures dT, dL — both in simState; exp-2 locks material and T, varies L₀, measures dL, rel — in simState.
- Sim model box states the limits honestly: constant α, symmetric drawn vibration, spacing set from ΔL/L₀ = αΔT, ×100 exaggeration; it shows *that*, not *why*. Physics lines unchanged; amplitude ∝ √T correct for classical vibration; max real change 0,23 % < 0,3 %.
- KaTeX readout strings: `sgn` gives 3 s.f. (6,00 mm, +0,0600 %), ΔT line and "20 °C:ssa" render as math; values match the feedback numbers.
- Coefficient tables realistic; water 4 °C anomaly, L1-04 γ(T) remark (true value ≈ 0,90 l) correct.
- Scope: ΔL = αL₀ΔT, ΔV = γV₀ΔT, γ ≈ 3α with small-change condition, inside FY3 "lämpölaajeneminen".
- Hash identical at start and end.
