VERDICT: PASS
CONTENT-HASH: 339ff2bfdf81959e

## Blocking

## Polish
- The sim readout shows `ΔV = 0,001 l` with a decimal comma in the English page (platform convention, as in other FY3 sims).

## Checked
- Previous blocking item resolved: in the built page (Playwright, 1280 px) no visible text contains "sama paine" or "jäähdytys ensin"; both experiments' "Initial state" lines read "piston return = at the same pressure", and "Kept constant"/"Varied" name the parameter. The remaining occurrences in the HTML are data attributes and sim configuration, not shown.
- The table row's varied value goes through `shown()` / `window.__v` ("sama paine" returns "at the same pressure"; lang/en.json sims.fy3-11.values has both entries); I did not drive the table row itself.
- Same activity order, predictions, experiments, hints, mistakes, feedback, solutions and exit ticket as the Finnish; nothing added or dropped.
- Learning path: retrieval, two predictions each tested by an experiment, conclusion, staged worked example, transfer task; the opening question is answered in the efficiency section; slot goals met.
- Natural English; terms (efficiency, coefficient of performance, heat engine) consistent; units and symbols as in the Finnish.
- Workload fits one lesson; optional items marked.
