VERDICT: PASS
CONTENT-HASH: 7bec1da5aa5477b3

## Blocking

## Polish
- exercises/solutions.md (fy3-13-L2-10, Kaava) — "$\theta = T - 273{,}15\,\text{K}$ (celsiusasteina)" still mixes units; $T = \theta + T_0$ solved for $\theta$ is cleaner (carried over).

## Checked
- L2-10 Periaate: "Pisteet ovat lähes suoralla" now follows the fits guardrail and L2-09 (my previous polish point); the five points (75; 82; 89; 96; 102,5 kPa) are indeed nearly, not exactly, linear.
- No number, answer or symbol changed; L2-10 still $p = 75 + 0{,}275\cdot(-73{,}15) = 54{,}9\,\text{kPa}$.
- Every answers.py value lies inside its tolerance.
- Hash same at start and end.
