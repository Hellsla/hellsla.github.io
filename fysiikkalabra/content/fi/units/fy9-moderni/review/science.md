VERDICT: PASS
CONTENT-HASH: cd634be9954c2f85
SCOPE: full; this change is three new ```pysahdy boxes in unit.md (git e3fe8089ea); the rest since the passed hash 876c08f6ee47b4ec is carried md-paragraphs, caption-label and teacher-figure (hero WebP) changes

## Blocking
None.

## Polish
- s8 Yleisiä virheitä, a-kohta (still open from round 2): "$\mu = 16 / 20\,\text{cm} = 0{,}80$" comes from the old reading point. With the current points (0; 80) and (10; 20) the quotient error is $4 / 10\,\text{cm} = 0{,}40\,\text{1/cm}$. The text contradicts itself, but no physics is wrong.
- Pysähdy 1 (Ydinajatus): "Yksi fotoni luovuttaa energiansa yhdelle elektronille" holds for absorption and the photoelectric effect, and the sentence above the box says the same, so it is type C at this level. The answer gives no reason; it only repeats that sentence. That is a pedagogy question, not physics.

## Checked
- The three pysahdy boxes. 1: the answer matches the Ydinajatus and s3 d. 2: no electrons are freed when $hf < W$, matching the condition under the formulas ("vain, kun $hf \geq W$") and s3 d. 3: after $2T_{1/2}$ one quarter is left, matching $N = N_0(\tfrac12)^{t/T_{1/2}}$, the "puolitus" figure and the misconceptions list ("neljäsosa"). The text already says the law describes a large group of nuclei. Each box has exactly one correct answer and fits FY8 scope.
- Diff since 876c08f6ee47b4ec: the solutions.md and inquiry.json changes only split paragraphs, with the same words and numbers. The hero image is now a WebP; the teacher approved it and it is in carry.tsv.
- One script (scratchpad rc.py) recomputed every number from the task data. Every value matches the text:
  - intro: 1,88 eV; ratio 3,2·10⁴
  - s1: 1,873 pm; 1047,6 Bq/kg; 0,0681 mSv (1,15 %); 1,436·10¹²; 0,327 ng
  - s2: 656,5 nm; z = 0,02362; 7080 km/s; 101 Mpc; 497,58 nm; Hβ 486,3 nm
  - s3: the five frequencies; h = 6,608·10⁻³⁴; f₀ = 5,43·10¹⁴ Hz; 590 nm gives 5,08·10¹⁴ Hz and 2,10 eV; λ₀ = 552 nm
  - s4: 0,0042
  - s5: least-squares fit of ln(N−5) gives 153,1 s, line ends 5,993 and 4,635 (157 s without the background); two-point value 151 s; √212 ≈ 7 %; 1/√5 = 45 %; 1/√300 = 6 %
  - s6: 37,2 %; 1,342·10²⁰ 1/s; 1653 kg; 1,51 kg; 0,09 %; 58 581 kg/s; 5,26·10⁹ kg; ratio 3·10⁶; 14 000 t/d
  - s7: 1,537; 9,40 kg; 1,05 %; 0,7 %; 0,35 %; 3,5·10⁻¹¹ kg
  - s8: μ = 0,1386 1/cm; d½ = 5,0 cm; 6,6 µSv/h; 2180 µSv; 3,03 µSv/h; 23,6 cm, so 24 cm is right (23 cm gives 3,3, 24 cm gives 2,87)
  - s9: 72; 116,7 Mpc; 8640 km/s; 2,333·10⁻¹⁸ 1/s; 1,358·10¹⁰ a
  - inquiry: lead d½ = 5,79 mm
- Significant figures and rounding reasons are sound. s8 d rounds a minimum thickness up, which is the safe side. Every model and its conditions are stated: v = cz for small z; d½ only for photon radiation; H = Ḣt at constant dose rate, marked as not in the MAFY tables; the inverse-square derivation assumes a point source and no absorption in air.
- The hash was the same at the start and at the end.
