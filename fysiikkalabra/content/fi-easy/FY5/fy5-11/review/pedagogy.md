VERDICT: PASS
CONTENT-HASH: ca7df1baa03e1065

## Blocking
(none)

## Polish
- Six strings stay as in the Finnish (experiment 4 intro, conclusion prompt, Palaa ennusteisiisi, check tasks 1-2 prompts): already short sentences and plain words, judged acceptable.

## Checked
- Sentences split, every step, hint, feedback, model answer and seven-stage solution present (counts equal to the Finnish).
- Fixed here: conclusion model answer fragment 'Esimerkiksi alpha = 30 ja beta = 30 sekä ...' -> 'Esimerkiksi kun alpha = 30, niin beta = 30, ...'; worked example 'Ajatellaan, että kumpaakin suoraa käännetään'; 'Oletetaan, että rintamat ovat'.
- Figure descriptions (figures.json) were the standard-Finnish ones: rewritten in short plain sentences (same data, no answer added) and written into lesson.md with scripts/figures.py --lang fi-easy; the SVG labels stay the lesson's terms.
- Captures opened: contact-1 (top-390, sim, figures 1-6, example, Pohdinta, Ennusta); check_layout fy5-11 at 345 px OK for preview/fi-easy/fy5-11.
