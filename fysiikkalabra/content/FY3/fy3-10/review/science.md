VERDICT: PASS
CONTENT-HASH: 3bcebf10ec3465fe

## Blocking

## Polish
- solutions.md:L1-03 — "18 g, mikä on tavallisen patruunan koko": adult automatic life jackets mostly use 33 g cartridges — say "pienen patruunan koko" or drop the claim (carried from round before).
- sim.js:131 — right after "Nollaa mittaus" or "Aseta alkutila" the readout shows a short-window value (the 1280 capture: 1,04 "keskiarvo 0,3 s:n ajalta"); the intros say to wait about 2 s, so nothing is wrong, but "–" until tAvg ≥ 0,5 s would remove the temptation.

## Checked
- LaTeX pass in sim.js: physics untouched (step, impulse per perimeter, P_REF = NkT/A, thermalize, √T rescale, averaging window); only label strings changed. The 1280 capture renders p/p_ref, osumia/s, V = 100 %, axis ticks and slider labels correctly with decimal commas.
- Test diff (tests/sims/fy3-10.json): no physics assertion lost. Readout/label tests now match the TeX via simText with the same values (N, T, V, p/p_ref with two decimals, tAvg, hits/s = simState.hitRate); the removed Lisätietoja test is replaced by a stronger physics one (N = 20: |measured/predicted − 1| < 0,2 over 20 two-second samples, which backs the "±10 %" claim); the old 11 px subscript check became a 13 px whole-label check (layout only). Ratio, hit-rate, Maxwell-median and speed assertions unchanged.
- Every sentence of the old Lisätietoja box is now in inquiry.json kokeile model/calc/howto; the earlier polish on T staying constant under a volume change is resolved.
- One python call recomputed all 12 exercise answers from the task text: all match answers.py and exercises.json within 0,5 % (L1-05 9,659 → 9,7; L3-02 10,96 → 11; L2-03 555,3 °C).
- Inquiry: m/M 0,2075/0,2064/0,2076/0,2068, R from mean 8,32; laske-r 8,302 with mistakes 121,7/8302/0,0083; siirto 91 200 mol, 2645 kg, mistakes 9869 and 2,64, outside air 3,37 t; virhe 1,22 → 0,083 mol; check-2 3,00 (2,25, 1,69); exp-2 N = 50; table pV/(NT) 1,05/1,00/0,98/0,98/0,99 and p/p_ref close to the model 1/2/4/1/5,14.
- Correct options of kertaus, pred-n, punnitus-vertailu, pred-1, taulukko, virhe, check-1 are right; exp-1/exp-2 lock T and V and vary only N, and simState carries pMeasured and hitRate.
- Worked example 0,2073 mol, 0,83 g, air 6,0 g, 24,1 l/mol, symbolic first; exit ticket 0,601 mol.
- Figures unchanged and to scale (arrows √(29/4), bars 4 : 29 : 44).
- Scope: FY3 "kaasujen tilanmuutokset ja ideaalikaasun tilanyhtälö".
- Hash 3bcebf10ec3465fe at start and end.
