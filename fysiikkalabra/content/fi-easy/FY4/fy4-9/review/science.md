VERDICT: PASS
CONTENT-HASH: 8d7e2803f598ca5f

## Blocking

## Polish

## Checked
Delta review against the Finnish diff since a6af45ae. Compared every changed passage in fi-easy: the F_x graph text (figures.json, aria-label, axis and curve labels), sim texts (inquiry.json text/model/calc, lang sims.fy4-9.selite), hook, check-3 option and model answer (oletetaan, kokonaisvoima, alustan voima painon verran suurempi), rebound passages (-2mv, suuruus 2mv, summary bullet, misconceptions), the mat paragraph and the kokonaisvoiman impulssi wording. All agree with the Finnish; decimal comma and the same $...$ mentions; nothing added or dropped. No change needed.
Ran: check_i18n (0 errors), build.py fy4-9, figures.py fy4-9 --lang fi-easy --check (up to date), check_layout fy4-9 --lang fi-easy at 360 and 1280 (OK).
