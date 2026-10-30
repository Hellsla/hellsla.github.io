VERDICT: PASS
CONTENT-HASH: f885cf951601f6aa

## Blocking

## Polish
- check-1 (inquiry.json): the Finnish says "pallo ammutaan" (a ball shot from a bow); this version says "nuoli", which is physically right. The Finnish wording is the odd one and should be fixed there; left as is.

## Checked
- Compared lesson.md, figures.json, inquiry.json (all activities, feedback, model answers, numbers), exit-ticket.json, meta.json and the sims.fy4-7 labels with the Finnish: complete, no number or justification lost, nothing added after the fix.
- Terms as in the Finnish glossary; chapter names, not ids; decimal comma {,} everywhere, LaTeX symbols, \overline{v}, \cdot.
- Opening illustration at 360, 768 and 1280 px: language-neutral LaTeX labels, no overflow; aria-label in short sentences.
- check_i18n, check_latex (541 fragments) and figures.py --check --lang fi-easy are clean.
- Fixed: removed an added sentence from the Ydinajatus ("Sisäenergia on pienten hiukkasten liike-energiaa ..."; not in the Finnish and imprecise); the sim howto named the option *Nopeus* while the label is *Animaation nopeus*, now matched; the sim label "vähän kitkaa" is now "pieni kitka", as in the Finnish and the experiment tables.
