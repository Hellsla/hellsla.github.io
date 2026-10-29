VERDICT: PASS
CONTENT-HASH: 7985c5caf17e486c

## Blocking

## Polish
- lessons/FY4/fy4-5/figures.py virhe_liukuva: at 390 px the drawing fills only a third of the frame, so F_μ and the arrows are small. Crop the frame or enlarge the scale.
- lesson.md (suunnat): the helium-balloon panel draws the whole diagram that exercise L3-03 asks for (example H, the challenge). It is kept on purpose. Note that L3-03 is now a calculation, not a drawing challenge.
- lesson.md Yleinen virhekäsitys: the sliding-box sentence gives the answer to Etsi virhe just before the task, so the task tests recall. A different error, such as a reaction force on the wrong body, would test more.
- inquiry.json hook: "painaako pulkka jäätä…" is answered for pulling by pred-1 and exp-1. For pushing it is answered only by the optional exp-2 and one clause in Yleinen virhekäsitys. Name pushing in the johtopäätös model too.

## Checked
- The hissi options have empty text, so the student must read the arrows. The prompt warns that each wrong figure has one error. Each distractor's feedback names its error. Renders cleanly at 390 px.
- The hook question is now answered on the core path (pred-1 → exp-1 → johtopäätös). The reflect prompt matches.
- The fbd plan identify/select/error/draw/equations is fully tagged. check-3 is a real `draw` task: model diagram and criteria appear only behind "Näytä mallikuvio ja arviointi".
- malli-tyonto now shows the box alone, with F starting at the box.
- Etsi virhe has one error. Its description lists the arrows without judging them.
- The worked example is staged one step per stage, with the diagram before the equations. The inquiry solutions follow the same order.
- The predictions can be refuted by Koe 1, and their feedback repairs the misconception.
- Finnish and glossary terms are correct. Nothing is clipped in the 390 px captures.
