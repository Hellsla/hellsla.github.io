VERDICT: DONE

Round-1 fixes for fy7-12.
- science Blocking (lesson-answers.py dia-inc1): set to 38.0 and the comment to 38° (facet atan(98,5 : 126)); 38° > 24,4° diamond reflects totally, 38° < 41,8° glass leaks. Matches the figure, aria-label and figures.py.
- science Polish (figures.py water_rays): hit points now computed from the drawn lamp height (ly − 10), so the rays meet the surface at 30°, 48,8° and 65° and the arcs lie on the rays; lesson.md water SVG regenerated with `scripts/figures.py fy7-12`.
- pedagogy/visual Polish (term): "kokonaisheijastus" → "kokonaisheijastuminen" in the water figure label and aria-label, lesson.md ("Kokonaisheijastumisessa valoa ei katoa", "kokonaisheijastuminen on parempi peili") and the inquiry.json Etsi virhe option and feedback.
- No numbers changed in the text; other Polish items not taken.
check_lesson.py fy7-12: all ok.
