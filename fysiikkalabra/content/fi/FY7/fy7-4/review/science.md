VERDICT: PASS
CONTENT-HASH: 6ffc43175c5150d4

## Blocking

## Polish
- inquiry.json check-1, third option ("muuttaa tasavirran vaihtovirraksi") — the commutator really does make the loop's own current alternate, so a careful student can read this distractor as half right. The feedback says so ("vaihtaa virran suuntaa vain silmukassa"), but the option text hinges on the odd phrase "ennen kuin virta tulee virtalähteeseen" — make it clearly wrong, e.g. "syöttää vaihtovirtaa takaisin sähköverkkoon".
- lesson.md Kaiutin / inquiry.json tarkistus-3 model — the radial field is presented as giving the largest, same-direction forces. The stronger reason is missing: in a uniform field the forces on a closed circular coil cancel (net force zero), so without the radial field there would be no push at all. Consider one clause.
- inquiry.json siirto prompt — "Auton akkua ladataan … Kun moottori käynnistetään" mixes charging and jump-starting; 150 A belongs to cranking. Wording only, the physics is fine.

## Checked
- Recomputed in one script (my formulas): worked example l = 4,90 m, F = 6,98 N → 7,0 N; balance Δm 2,45 / 1,22 / 1,22 / 2,12 g, readings 247,75 / 242,85 g, B = 0,080 T; siirto 0,60 N and mistakes 0,006 / 3,77 / 0,30 N; virhe 0,15 vs 0,26 N; tarkistus-2 0,20 N (cos 0,35, ⊥ 0,40); exit ticket 0,30 N. All agree.
- Directions by cross product: swing (F left, right-hand-rule panel), motor (forces down/up, counter-clockwise torque, forces radial-outward at the perpendicular position), speaker (both gaps F toward the cone), angle figure (B sin α component perpendicular to wire, F into page), wires (CCW field, attract/repel). Exit ticket 2 (east × north = up) correct.
- sim.js: F = I l B sin α, sign convention consistent between top view (N right, B left) and side view (I > 0 into page → F up → reading up); side projection l |cos α|; slider steps reach 3, 6 A and 30°, 60°; simState carries `lukema` for both experiments; the locks isolate I and α.
- Predictions: exactly one correct option each; distractor feedback numbers match the model.
- Ampere definition (2·10⁻⁷ N/m, until 2019), tesla unit, μ0 value, B = μ0I/(2πr) conditions (long straight wire; 2 m ≫ 1,5 cm).
- Scope: inside FY7 contents; no self-induction or para/diamagnetism; the copper is "not ferromagnetic" statement is a fair C.
- Sim model box states its simplifications (uniform field in gap, rigid wire, model values, not measurements).
