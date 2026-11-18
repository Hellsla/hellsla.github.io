VERDICT: FAIL
CONTENT-HASH: e9bf2efc3c9791b6
SCOPE: delta: Sovella itsenäisesti tasks s8 (Auto ajaa kaarteessa, figure fy5-4/kuvaaja-a) and s9 (Kyltti seinän tangossa, figure fy5-2/kyltti) with solutions, rubric and answers, and the changed intro sentence ("Yhdeksän ... tehtävää"), en. Tasks s1-s7 not re-judged.

## Blocking
- B s8 d) Mallivastaus and rubric (tasks.json s8 d, solutions.md "### d)", line about 606): the greatest friction is given as `{\approx 7360\,\text{N}}` (three figures) although the data ($\mu_\text{s} = 0{,}50$) has two. Round to the data's precision: $0.50 \cdot 1500\,\text{kg} \cdot 9.81\,\text{m/s}^2 \approx 7400\,\text{N}$ (or $7{,}4\,\text{kN}$). The "4500 N" beside it is right. The 61 % ratio and the 5,9 kN of part c are already two-figure. Language-neutral: the same line in all three languages.

## Polish
- B s9 a) Periaate: one paragraph of about 115 words (hinge choice, centre of mass, torque of $T\sin\theta$, directions of rotation). Split before "Tangon paino vaikuttaa painopisteestä" and again before "Vaijerin voimasta tankoa vastaan ...".
- C s9 d) Mallivastaus: the last chain (H') ends a display block and "Aiemmin $331\,\text{N}$" starts the next sentence with no full stop; s8 d) has "$$ja suurin" with no space after a display block. Both render acceptably at 390 px but the source joins are fragile; end the display with a full stop or move the text into its own sentence.

## Checked
- No English captures exist; read the English tasks.json and solutions.md against the Finnish captures (same cut: paragraphs, chains and the 7360 line sit at the same lines), and ran `check_layout.py fy9-ympyraliike --width 360`: OK for en (1 known clipped formula, all in older tasks, none in s8/s9). Captures not opened per language, so layout verdict rests on that check plus the Finnish captures.
- s8: graph has quantity and unit on both axes, readable ticks, the marked point (15 m/s, 3,0 m/s²) with dashed guides, curve distinct from the marker; alt text uses the task's names (auto, kaarre, normaalikiihtyvyys, ratanopeus). Answer box $r = 75\,\text{m}$, $F \approx 3{,}6\,\text{kN}$, $v_\text{max} \approx 19\,\text{m/s}$ (69 km/h) rounded to two figures; chains aligned at `=`, nothing clipped with solutions open at 390.
- s9: figure alt names kyltti, tanko, vaijeri match the task; hinge, wire angle and length are shown; answers $380\,\text{N}$, $330\,\text{N}$, $29\,\text{kg}$ rounded to two figures; aligned chains and fractions intact at 390 and 1280.
- Task texts do not reveal the structure (no "kolme vaihetta", no "kahdesti"); questions are last. Unit is language-neutral: ids, figures, numbers and answers identical across fi, en, fi-easy.
- Hash at start and end: e9bf2efc3c9791b6 (unchanged).
