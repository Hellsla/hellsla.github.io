VERDICT: PASS
CONTENT-HASH: c33ef8000459c4d0

## Blocking

## Polish
- exercises.json:347 and solutions.md:359 (L2-08) — "lähes kaksikymmenkertaisia": the differences are 20,6 and 19,2 times $\Delta x$, so one of them is over twenty. Write "noin kaksikymmenkertaisia".

## Checked
- Scope: only the new task L2-08 (measurement data, type 10). The rest of the set was PASS before and is unchanged. Checked from the text only, no renders.
- Model: $x = h/\mu$ (the brief's "Miksi pulkat pysähtyvät yhtä kauas", the mass cancels). The data give $h/x$ = 0,102; 0,0985; 0,0995; 0,101, so μ ≈ 0,10 for a sled on snow, which is realistic. Same slope, start at rest and a horizontal distance from the start are all stated in the task.
- Uncertainty logic follows the guardrails. The mass differences are 0,7 m < Δx and the intervals overlap, so a difference cannot be shown, which does not prove there is none (option 3 feedback). The height effect is 20,6 and 19,2 m ≫ Δx, so "todennäköisesti todellista". The extrapolation to 8 m (twice the measured range) is called an estimate, with its assumption (same μ) named.
- Distractors: overlap ignored, "no difference proven", and an extrapolation stated as certain. Option 1 catches the intuition that a heavier sled goes further, which the lesson refutes. The correct option is not the longest and not the hedged one.
- "Lukeman epävarmuus Δx" is phrased as in the FY3 data tasks. The data caption is short.
- solutions.md L2-08: Kysytty · Periaate · Mallivastaus. Every option is argued from the data, and the reasonableness check (h : x ≈ 0,10) is real.
- answers.py: no line is needed. All 18 numeric answers in the set were recomputed in one call and match.
