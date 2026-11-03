VERDICT: PASS
CONTENT-HASH: 3ca89352c3f28244

## Blocking
(none)

## Polish
- Open doubt 'Turn' (the Väännä button) next to 'turning effect' (vääntövaikutus): not confusing, no change. The button is an imperative for one attempt, the term names a concept in the theory stage, and the Finnish pair Väännä/vääntövaikutus has the same echo. If the teacher prefers sharper wording, 'Pull' (the hand pulls the handle) would avoid the echo and fits the oblique-force story; it would need the lang/en.json label and the five 'press *Turn*' sentences in inquiry.json changed together. Optional.
- For the developer, not a translation fault: scripts/check_i18n.py reports ERROR on activities[15].practice because 'practice' is not in its TEXT_KEYS although the page shows it after a wrong check. The English text 'Practise the net moment in the level 2 tasks.' is kept (Finnish left in the English page otherwise); adding 'practice' to TEXT_KEYS in check_i18n.py/translate_kit.py clears the error.

## Checked
- All activities in inquiry.json against the Finnish: same ids, stages, options, correct flags, hints, mistakes, criteria, model answers, solutions (seven-step) and reveal rules; no step dropped.
- Fixed here: the experiment table and status line showed Finnish ('mutteri: tiukassa', column 'mutteri', value 'aukesi') -> nut / tight / rusted / came loose in both experiments; the check-2 'practice' hint was Finnish -> English; 'long wrench' in the reflect prompt -> spanner.
- Fixed in lang/en.json sims.fy5-1.selite: the 16-word legend was folded by the shared sim-embed rule (notes over 15 words) into the 'Assumptions of the model and explanation' box and so invisible; now 15 words and visible under the sim, like the Finnish.
- Captures opened: contact sheets 1-2, sim-390, exp-1-390-1/-2, exp-2-390-2, open-exercises-1280-1; check_layout fy5-1 --lang en --width 345 OK.
