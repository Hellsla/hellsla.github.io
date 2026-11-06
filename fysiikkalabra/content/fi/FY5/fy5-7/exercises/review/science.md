VERDICT: PASS
CONTENT-HASH: 2c890badbdfaaf11

## Blocking

## Polish

## Checked
- New task L1-09 (type 2, graph choice; exercises.json:126–150, solutions.md:197–210). I checked it from the text, the figure code (lessons/FY5/fy5-7/figures.py pick_graph) and the figure descriptions. I did not render it.
- Physics: f = 2,0 Hz gives T = 0,50 s, the first peak at T/4 = 0,125 s, and 4 oscillations in 0–2 s. The generator draws B with A = 3,0 cm and T = 0,50 s, A with T = 1,0 s, C with A = 1,5 cm, and D with T = 2,0 s. These match the solution, the feedback and the descriptions.
- All four curves start upward from x = 0 on the same axes, so the right option cannot be told apart by phase or form. The option texts are all "Kuvaaja X".
- The three distractors catch the lesson's own warned mistakes: half a period read between crossings of x = 0, A taken as the top-to-bottom distance, and T confused with f.
- The correct option's feedback restates only T = 1/f and the peak height. The rest of the set had no new items to check.
- Inline formula chains in the solution are one short step per line (T = 1/f; 1/(2,0 Hz); 0,50 s). From the text they fit about 300 px.
- The task stays inside this chapter (f = 1/T, amplitude, reading graphs). Notation follows the lesson: x, t, A, T, f.
- answers.py ran once (python3 -I). I compared all 18 numeric answers with exercises.json in one script, and all are within tolerance. L1-09 is MC, so it is not in answers.py, which is correct.
- The hash was the same at the start and at the end.
