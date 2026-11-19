VERDICT: PASS
CONTENT-HASH: 338baa44a2d54eaa

## Blocking

## Polish
- exit-ticket.json:2 — "Ilmakivääri on levossa": if a shooter holds it, the hand is an external force. The answer's "ulkoisten voimien impulssi on merkityksettömän pieni" covers this (C), but the reasoning would be cleaner with "vapaasti riippuva" or "kevyesti kädessä pidetty" kivääri.
- lesson.md "Törmäysten lajit" — "liike-energia pienenee eniten: suurin mahdollinen osa" is true for the given initial velocities (momentum fixed). "samoilla alkunopeuksilla" would make the comparison explicit (C, optional).

## Checked
- One script recomputed every number in lesson.md and inquiry.json with my own formulas and compared them with lesson-answers.py. Kertaus 0,30 / 12 000; pred-1 0,30 m/s and the distractor 0,424 m/s (E_k conserved); kaava 0,072 → 0,036 J; worked example 1,14 → 1,1 m/s, 38,3 → 32,5 kJ, 15 %; virhe 0,025 and 0,475; siirto 1,0 m/s with mistakes 2,4, 0,706 (velocity relative to the boat) and 5,76; check-2 0,15 m/s with 0,60 and 0,20. All agree.
- model.js run in Node at every experiment setting. Tarra gives 0,40/0,30/0,24 m/s with E_k' 0,048/0,036/0,029 J. Kimmoisa gives (0,20; 0,80), (0; 0,60), (−0,12; 0,48). Räjähdys with m₂ = 0,20 kg gives −0,632 and 1,265 m/s, p = ∓0,253, 0,24 J = ½·300·0,04². These match my closed-form results and every feedback number. E_k + E_p + E_sis = E₀ in every case, kimmoton included.
- The sim gets momentum conservation from equal and opposite bumper forces (RK4), not by imposing it. When the velcro sticks, the remaining E_p is moved to E_sis, as the Mallin oletukset box says. simState holds u1, u2, pJ and EkJ at the "after" moment, and tx removes negative zero.
- Experiments: m₁, v₁, v₂ and tyyppi are locked and only m₂ varies; exp-3 needs no velocities because the sliders are disabled.
- Exactly one correct option in each of kertaus, pred-1–3, the exp-1 and exp-2 questions, virhe and check-1. Every distractor's feedback names the real error. The "lämmöksi" distractor is deliberately wrong, and its feedback correctly says sisäenergia.
- The conservation condition (external impulse negligible) is stated in the theory, the glossary, the Tiivistelmä, the worked example, siirto, check-3 and the exit ticket.
- The derivation from Newton's third law covers both constant and varying force. The equal-mass elastic derivation (2v₁'v₂' = 0, and the cue ball cannot pass through) is correct.
- Figures: in tarra the v arrow after is half as long (132 → 66) and the p arrow keeps its length. In tyypit the elastic and perfectly inelastic p arrows are equal and the explosion arrows are equal and opposite, so the "mittakaavassa" claim holds. Vuorovaikutus has equal F and Δp arrows.
- Scope: only 1D, within the FY4 central content. The formula section is named after its law (Liikemäärän säilymislaki).
- Significant figures: 1,1 m/s from 1,5 and 0,50; 1,0 m/s from 2,4; 0,15 m/s.
