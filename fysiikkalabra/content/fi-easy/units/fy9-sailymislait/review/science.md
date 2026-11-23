VERDICT: PASS
CONTENT-HASH: c24d068e46b34b98
SCOPE: full, the new "Pysähdy ja mieti" boxes first. Since 4cb6396da76519c3: three ```pysahdy boxes, the hero and tuuli drawings now raster images (labels kept), inquiry explain model split into two paragraphs (same words), teacher.md task count and points. Language: fi-easy.

## Blocking
- (none)

## Polish
- Box 1 (Ydinajatus) lists only "kitka tai ilmanvastus". The Finnish box and the paragraph above it also name the body's deformation (muodonmuutos). Nothing is wrong, but the list is shorter than the Finnish one; adding "tai muodonmuutos" would make the two equal.
- Boxes 1 and 3 say "hyvin pieni" where the Finnish says "merkityksettömän pieni". The paragraph above defines this as "niin pieni, ettei sillä ole merkitystä", so the condition is stated (C).
- From earlier reviews: s8 b says "13 m/s on noin 47 km/h" while the unrounded value is 45 km/h; s7 d has a closing remark on air resistance that is outside the task's assumption.

## Checked
- Box 1: momentum is conserved when ΣF_ext = 0 or the external impulse is negligible. Mechanical energy becomes internal energy and total energy is conserved. Same physics as fi; no "lämmöksi".
- Box 2: friction does negative work (W < 0) because it acts against the motion, so it lowers mechanical energy and makes internal energy. Same as fi and agrees with the Kaava text.
- Box 3: in a perfectly inelastic collision momentum is conserved (the external impulse is small) and kinetic energy is not, because part of it becomes internal energy. Same as fi.
- Ydinajatus: p = 32 000 · 1,6 = 51 200 kg·m/s; v' = 0,80 m/s; E_k = 41 kJ before and 20 kJ after (40,96 and 20,48).
- Johda blocks (s_p, P = ηρQgh, P = ½ηρAv³) are symbolic and correct, and their conditions are stated.
- tuuli image: a cylinder of base A and length vΔt upstream of the rotor, wind arrows and the bracket match the overlay labels v, A, vΔt and the derivation.
- Task set: own script, independent of answers.py, agrees with answers.py and the solutions: s1 26,6 m/s, −19,7 kJ, 48,1 N, 770 N; s2 μ 0,010, 0,57 m/s, 85 %, 1,6 m; s4 3,375 and 9,5 MW; s5 −11,9/−6,3/−3,7/−2,9 %; s6 3,43 m/s, 2,61 m/s, 4,9 kJ, 916 kN, 7 K; s7 2,04 m, −15 J, 2,5 N, 5,0 m/s; s8 5,4 N s, 12,6 m/s, 33,9 J, 8,04 m, −6,5 J, 1,0 N. Signs and units are correct.
- Points: 15+15+20+15+15+15+15+14 = 124, as teacher.md now says (seven Osa II tasks: six of 15 points and one of 14).
- practice.py check OK. Hash was the same at the start and at the end.
