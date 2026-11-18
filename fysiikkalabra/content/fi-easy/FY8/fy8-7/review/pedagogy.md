VERDICT: FAIL
CONTENT-HASH: d6a1f284318a9815

## Blocking
- content/fi-easy/FY8/fy8-7/inquiry.json:33 — the prompt of "kertaus" now says 633 nm (He-Ne), but the correct option's feedback still says "Aallonpituutta $650\,\text{nm}$ vastaa energia ... $1{,}91\,\text{eV}$" — the student reads feedback about a different wavelength than the one in the task — change to $633\,\text{nm}$ and $\approx 1{,}96\,\text{eV}$ (answers.py "kert-633-eV" already holds 1,96 eV).
- content/fi-easy/FY8/fy8-7/inquiry.json:37 — same stale values in the distractor "Fotonin energia on ylemmän tason $E_2$ energia." — change to $633\,\text{nm}$ and $1{,}96\,\text{eV}$.

## Polish
- none

## Checked
- Prompt change (He-Ne laser, 633 nm) is physically right and suits the laser topic; the third distractor's feedback rewording ("atomien itsestään lähettämä valo leviää kaikkialle") is correct and no longer refers to a lamp that is not in the task.
- 633 nm gives 1,96 eV, so the old 1,91 eV figure is wrong for this task.
- answers.py key renamed to kert-633-eV with 1,96 eV; consistent with the prompt, but not with the feedback in inquiry.json.
- Hash at start and end: d6a1f284318a9815 (fi-easy).
