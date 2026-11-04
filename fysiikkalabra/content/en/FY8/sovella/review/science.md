VERDICT: FAIL
CONTENT-HASH: 9b8a1649f0d52ce2

## Blocking
- **s3 b figure alt text (A).** The fy8-s3-lin aria-label says "from r = 2 to 22 centimetres". The Finnish source says "r miinus kahdesta 22 senttimetriin", so the axis runs from −2 to 22 cm. It has to: the same text puts the intercept at r = −1.3 cm and its tick at 0. The minus sign was lost in translation. Fix it to "from r = −2 to 22 centimetres" in both places: `content/en/FY8/sovella/figures.json`, then the regenerated aria-label in `solutions.md`.

## Polish
- s5 a Reasonableness reads the Finnish "kolmannes yhdestä" as "about a third more than now" (factor 1.36). That is correct: 2^0.447 = 1.364.
- s2 c "The half-life 4.47·10⁹ a : 87.7 a ≈ 5·10⁷ times longer" is missing "is". This is grammar, not physics.
- The solution headings "Hyväksytään myös" and "Yleisiä virheitä" stay in Finnish. That is fine if the tooling needs them; otherwise it is the editorial reviewer's call.

## Checked
Hash 9b8a1649f0d52ce2 at start and end. The Finnish source hash d656d012098aaf16 is unchanged since its PASS.
- **Numbers.** A script compared every string of tasks.json against content/fi/FY8/sovella/tasks.json, field by field, along with every solutions.md section. After normalising decimal commas to points, every number matches. Every points value, answer value and tolerance is identical. The only extra number in the solutions is the "2" in "r = 2 to 22" (the item above).
- **Independent recompute.** All numbers agree with the solutions:
  - s1: 2.22 / 1.97 eV, 296 nm, 1193, 1107 nm, 0.83 eV.
  - s2: Q 5.594 MeV, A 2.23·10¹⁵ Bq, 3.52 kg of 4.23 kg (83 %), Po 0.16, U factor 5.1·10⁷, 1791 W and 98.5 W, E 2.83·10⁻⁴ J and H_E 0.566 mSv.
  - s3: r 36.2 cm, 0.23 µSv/h, 14 % and 1.8 %.
  - s4: 0.782 MeV/c², 7.16, 135 s; 270.5 s with 1 : 5.
  - s5: 3.67 %, 3.49 a, 82 988 half-lives, 4.7·10¹⁷ J.
- **Physics wording, item by item against the Finnish.** None of these changes a condition, a cause or an assumption:
  - photon energy as the level difference, and intensity as the number of photons;
  - valence and conduction band;
  - collisional de-excitation vs lifetimes;
  - atomic masses and electrons cancelling;
  - A = P/Q and A = λN;
  - the radiation weighting factor of alpha radiation, the tissue weighting factor of lung tissue, and effective dose. All are correctly named, and "a year's effective dose" is kept;
  - the background subtraction and the 1/r² geometry;
  - the d quark changing to a u quark via W⁻;
  - the helium mass-fraction assumptions;
  - the moderator vs coolant, and the multiplication factor "on average at least one";
  - the Oklo vs Onkalo reasoning.
- The rubric criteria still match what each task asks and what each solution shows. The "Hyväksytään myös" alternatives are kept.
