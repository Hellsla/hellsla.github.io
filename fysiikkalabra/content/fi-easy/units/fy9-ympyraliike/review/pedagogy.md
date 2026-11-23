VERDICT: PASS
CONTENT-HASH: f6825d133f2e7219

## Blocking
None.

## Polish
1. Box 2 (Tasainen ympyräliike): the answer ("Nopeus on radan tangentin suuntainen ...") is repeated word for word in the paragraph directly under the box. The box then retrieves nothing. Fix: drop or reword the paragraph's second and third sentences, or move the box after the paragraph.
2. Box 2: "tangentin suuntainen" is never explained in plain language (unit.md lines 145 and 148). Selkosuomi rule: explain a hard word at first use. Add "eli sivuaa rataa" in the paragraph.
3. Box 1 (Ydinajatus): it sits directly under the bullet that already says "voimien summa osoittaa keskipisteeseen". The student only copies the answer. The "miksi" part still has some retrieval value. Move the box to the figure "kartta" or ask something new, for example "Mikä voima kaartaa rataa, kun auto ajaa nyppylän yli?".
4. Box 3 (gravitaatiolaki): good, since a student can reason it out from $1/r^2$. Say "kaksinkertaistuu eli tulee kaksi kertaa niin suureksi" once, for the S2 reader.
5. All three boxes ask a plain question, so the student can answer in one sentence. None of them asks for a justification except box 1. This is fine for a pause, but a "Miksi?" in box 2 would make it better.

## Checked
- Box wording is at selkosuomi level: short sentences, one idea each, units and symbols in LaTeX. The answers are correct and match the unit's text. The page reveals the answer only behind the `---` line.
- Unit text and Sovella tasks: the diff changes only the pysahdy boxes, the hero, geo and tilanteet illustrations (now `<image>` elements with the same aria-labels, so a reader who cannot see them gets the same data), and a paragraph break in the inquiry model answer. I judged these and the whole set (9 tasks).
- Task set: all tasks (about 14-20 points each) present unfamiliar situations: trailer, weather satellite, turntable, space station, metre-stick experiment, loop-the-loop, ISS with NASA source, car on a bend with a graph (s8, `fy5-4/kuvaaja-a`), sign on a pole. Parts rise in demand. Titles name no formula. Criteria are specific and tied to the shared keys. Sources are marked. Variety is good: graph, data, experiment, source reading and modelling.
- The S2 version keeps the points, answers and criteria of the passed Finnish unit. The deterministic check (`practice.py check`) is OK. The hash at the start and the end was f6825d133f2e7219.
- I did not read every part's solution text line by line. I spot-checked s2, s7 and s8. They show a given, principle, symbolic step and criteria.
