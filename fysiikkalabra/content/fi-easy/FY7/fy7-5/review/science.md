VERDICT: PASS
CONTENT-HASH: f57e6d152f7efa45

## Blocking

## Polish
- lesson.md:199 — "napadynamossa magneetti pyörii käämien keskellä": in a real hub dynamo the magnet ring turns round a fixed central coil. The Finnish source says the same, and the induction point is unaffected — optionally "magneetti pyörii käämin ympärillä", in fi too.

## Checked
- Translation against the Finnish lesson: every number, correct option, numeric answer, mistake value and experiment initial/locked set is identical (compared by script).
- Φ = BA with its condition (homogeneous field perpendicular to the plane); the weber; e = −N ΔΦ/Δt with ΔΦ per turn, turns in series, the minus sign only giving the direction (Lenz deferred to fy7-6).
- e = vBl derivation: F_m = evB along the rod, charge separation, eE = evB, U = El; the condition (v, rod and B mutually perpendicular) is stated. Rod figure: for v to the right and B into the page, the force on electrons points down, the lower end is negative and E points down. All correct.
- Kaava graph: N = 10, B = 0,20 T, l = v·1 s: Φmax 2,0 mWb, entry 0,5–1,5 s, exit 2,5–3,5 s, e = −20/+20 mV. Correct signs and timing.
- Worked example 0,20 V (one turn 0,80 mV), symbolic first, sig-fig reason sound.
- inquiry: the predictions (0 mV inside; voltage doubles with v, entry time halves) and all feedback numbers; koe-1/koe-2 isolate v and N, and simState e_tulo/t_tulo/e_sisalla at the default run give −20,0 mV, 1,00 s and 0 mV; e·Δt = −20 mV·s = −N ΔΦ.
- virhe (0,72 V; 72 V; 0,36 V), siirto 4,8 V with mistakes 0,008 / 0,0048 / 4800, tarkistus-2 0,50 V with mistakes 50 / 1,0: all recomputed.
- Exit ticket: 20 mWb; e = 0 at a flux maximum.
- sim.js: overlap model, e = ∓NBlv while entering and leaving, readouts taken at mid-entry and mid-inside, no current/braking (stated in the model box).
- Scope: no self-induction; Lenz only named.
