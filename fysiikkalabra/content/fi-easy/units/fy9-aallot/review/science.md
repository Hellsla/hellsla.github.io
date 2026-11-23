VERDICT: PASS
CONTENT-HASH: b20f769ff7a5fc10
SCOPE: full: the three new "Pysähdy ja mieti" boxes (```pysahdy) judged first against content/fi/units/fy9-aallot/unit.md, then unit.md, unit.json, inquiry.json, teacher.md, sovella tasks.json, solutions.md and answers.py.

## Blocking
(none)

## Polish
- inquiry.json lt-6 and juna write the source speed as $v_\text{s}$. The formula section uses the MAFY symbol $v_\text{L}$. The Finnish version does the same (19 occurrences in each), so a fix belongs in both languages. This is a consistency issue, not an error.
- s7 c: "Täysin hiljainen se ei ole, koska kauempana oleva kaiutin kuuluu hieman heikommin" goes against the task's instruction to ignore the intensity difference. The same sentence is in fi; carried over from the previous report.

## Checked
- Pysähdy boxes: the physics is the same as fi in all three. (1) The source sets the frequency, the speed is higher in water, so by $v = f\lambda$ the wavelength grows. (2) $\Delta s = \tfrac12\lambda$ with in-phase sources is the $(n+\tfrac12)\lambda$, $n = 0$ condition, so the wave is weakened. (3) For a source approaching, the denominator $v - v_\text{L} < v$, so $f > f_0$. Each box agrees with the formula section, the Yleisiä virheitä list and lt-3, lt-4 and lt-6. Only the wording is simpler.
- I recomputed every number in one script from the task text with my own formulas, and compared the results with answers.py and the keys in tasks.json:
  - Pilli: 0,117/0,50 m; the hero's "about four times sparser" is 4,3.
  - Aineisto: B 342,6, A 342,8 m/s; the mistakes 170,4 and 85,2 m/s.
  - Jousitus: 1,472 Hz; the mistakes 0,679, 5,573 and 9,249.
  - Poiju 1,722 m/s; juna 27,46 m/s (mistakes 50,8, 54,9 and 98,9); konsertti 178,3 m (mistakes 1589 and 24,5); seismograph 119,3 km (mistakes 85,2, 49,7 and 35,5); kaikuluotain 17,8 m; tarkistus-1 λ = 1,70 m with Δs = 0,85 m; teacher's Moon pendulum 0,16 m.
  - s1: 142,56 m/s, 3,118 m, 577,2 mm, 70,8 mm and 108,5 Hz.
  - s2: 11,33 mm, 2,04 m and 31,08 kHz.
  - s3: least-squares slope 4,040 s²/m, intercept 0,055 s², l-intercept −1,35 cm, g 9,77 m/s². The points read from the line give 9,778 m/s² and 0,977 m. Forcing the line through the origin gives 9,58 m/s², as the mistakes list says.
  - s4: 80,0 dB and 15 min. s5: 354,2 ± 51,6 m/s and 334 m/s at 5 °C.
  - s6: 18,79 m/s, 39,59 m, 26,17 m/s² and 4,867 s. s7: 6,0, 6,5 and 0,50 m, λ = 1,001 m, 686,8 Hz. s8: 0,600 m, 30 m/s, 37,5 Hz, f₁ = 12,5 Hz and 1,6 loops.
  - All keys are within tolerance.
- Models and their conditions are stated: small swings, harmonic spring, Doppler with only one party moving and speeds below the sound speed, point source without reflections, in-phase sources. The causal mechanisms are right: the weight only moves the equilibrium position; tightening raises the frequency; diffraction is set by wavelength against obstacle size. Everything is within FY5 scope, with FY4 energy in s6.
- Rubric points add up: s1 to s6 are 15/15/20/15/15/15, s7 is 12 and s8 is 13, 120 in total, as teacher.md now says. "Seitsemän muuta tehtävää" matches the eight tasks. Each criterion asks only what its part gives and asks.
- Every choice item has exactly one correct option, and every distractor's feedback is right.
- Paragraph splits in the solutions of aineisto and jousitus change no word.
- The hash was the same at start and end.
