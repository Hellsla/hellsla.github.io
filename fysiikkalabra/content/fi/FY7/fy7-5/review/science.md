VERDICT: PASS
CONTENT-HASH: 8e426d6c8acacf91

## Blocking
- none

## Polish
- inquiry.json:18 and :215 (hook, pohdi) — "mitä lujempaa ajat, sitä kirkkaammin se palaa" holds at low speed; a real hub dynamo's lamp brightness levels off at cycling speed (the coil's inductance limits the current, outside FY7 scope). C-level, acceptable; optionally "kun ajat hitaasti, lamppu on himmeä" or "aluksi sitä kirkkaammin".

## Checked
- Hash 8e426d6c8acacf91 at start and end. Every number recomputed in one script with my own formulas: worked example 0,20 V (one turn 0,80 mV); Kaava graph Φ_max 2,0 mWb, ∓20 mV, entry 1,0 s; koe-1 −10/−20/−30/−40 mV with Δt 2,0/1,0/0,67/0,50 s, e·Δt = −20 mV·s = −NΔΦ; koe-2 −2/−10/−20/−40 mV; virhe 72 V wrong, 0,72 V right, 0,36 V without N; siirto 4,8 V and its mistakes 0,008/0,0048/4800 V; tarkistus-2 0,50 V and mistakes 50 V / 1,0 V; exit ticket 20 mWb. All agree with the text, lesson-answers.py and the feedback.
- Definitions: Φ = BA with its perpendicular-field condition, Wb = T·m², ΔΦ per turn, average e_ka vs constant e vs dΦ/dt, magnitude always positive, minus sign deferred to the Lenz chapter (scope note: no self-induction respected).
- e = vBl derivation: evB = eE, U = El in a uniform field, condition all three perpendicular stated; flux-sweep cross-check correct.
- Rod figure (figures.py): v right, B into page → force on electron down, bottom negative, E top→bottom, F_s up: consistent with qv×B.
- Faraday, flux, graph figures: graph drawn from the model (coil_overlap), to scale, matches the sim and lesson-answers.py.
- Photo caption matches the picture (coil and magnet in a clear tube); "lataa energiavaraston" fair.
- Sim: overlap model, e = −NBlv / 0 / +NBlv, e_tulo sampled mid-entry, t_tulo = l/v, e_sisalla mid-inside; coil height (0,10 m) within field height; voltmeter draws no current stated in Mallin oletukset; values called model values.
- Experiments isolate v (B, N locked) and N (v, B locked); simState supplies e_tulo, t_tulo, e_sisalla.
- Each choice item has exactly one correct option; every distractor's feedback names the right reason and right numbers.
- Explain model answers (johtopäätös, tarkistus-3) agree with theory and summary.
