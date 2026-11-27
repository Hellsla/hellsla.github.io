VERDICT: PASS
CONTENT-HASH: dfb3675133290f7c

## Blocking
None.

## Polish
None.

## Checked (delta 2026-11-27, round 1)
- Prerequisite "Lähdejännite ja sisäinen resistanssi" now `target: fy6-8`. FY6 fy6-8 defines $E$ as energy per unit charge (1,5 V = 1,5 J/C) and $R_\text{s}$ as the resistance of electrolyte and electrodes, models the cell as an ideal source $E$ in series with $R_\text{s}$, and gives $U = E - R_\text{s} I$ (with $E$, $R_\text{s}$ assumed constant), $I_\text{k} = E/R_\text{s}$ and the $(I,U)$ line: intercept $E$, slope $-R_\text{s}$, extrapolation to $I_\text{k}$ assuming constant $R_\text{s}$. This matches the investigation's Teoriaa lyhyesti and its questions 2-3 in definitions, symbols and model conditions; no contradiction (the investigation's note that $U = E - RI$ also appears with $R$ as internal resistance does not conflict).
- The "why" text ("Tutkimuksessa määritettävät suureet; lyhyt selitys on tällä sivulla kohdassa Teoriaa lyhyesti") stays true; level `essential` is right, as $E$, $R_\text{s}$ and $I_\text{k}$ are the quantities the investigation determines. FY6 precedes FY10, so no scope issue.
- investigations.py: 27 ok; hash dfb3675133290f7c at start and end.

## Checked (earlier) (delta 2026-10-31)
- `topic` "sahko" fits the physics area.
- New sentence: in a holder, contact resistance between holder and cell adds to the apparent $R_\text{s}$ unless the voltmeter is at the cell's terminals; correct.
- Report names Koejärjestely ja menetelmä, Tulos match the template.
- TVT `guides` (kuvaaja, suoran sovitus, kulmakerroin, epävarmuus) match the prerequisite: a linear fit whose slope and its uncertainty give the result; inline links agree.

## Delta 2 (2026-10-31)
- Raportoi: the tvt-tyoselostus link moved to its own sentence; wording only, no physics changed.

## Delta 4 (2026-10-31)

- Tool wording now names Graphical Analysis Pro (teacher 2026-10-31) and the tvt-taulukkolaskenta link reads *Taulukko ja lasketut sarakkeet*; no physics changed; grammar checked.
