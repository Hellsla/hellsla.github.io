VERDICT: FAIL
CONTENT-HASH: d996ffa7f72afcaa

First science review of fy14-global-fusion-explorer, 2026-11-01. It covers the unit, `assets/units/fy14/data/facilities.json` as committed in 04ac2449, and the year rule in `fx/map.js`.

## Blocking
1. **(A) Fusion research before 1958 was not limited to three countries.** The first Summary bullet in `unit.md` says "Until 1958 fusion research was secret and limited to the United States, the Soviet Union and the United Kingdom". The unit's own source, *Timeline of nuclear fusion*, says that Japan, France and Sweden started programmes in 1955–56. West Germany's Wendelstein 1-A and 1-B ran from 1960, and 2-A from 1968, according to the *List of fusion experiments*. Fix: "Until 1958 the large fusion programmes of the United States, the Soviet Union and the United Kingdom were secret; the 1958 Geneva conference made them open."
2. **(A) "During the Cold War" covers too long a period.** The `check-write` model says "During the Cold War, fusion machines in the explorer stood only in the United States, the United Kingdom and the Soviet Union", and the `check-write-help` starter is "During the Cold War, fusion machines stood only in …". The Cold War lasted until 1991. The explorer itself shows TFR and Pulsator (1973), JT-60 (1985) and others. Fix: write "Before 1970" (or "In the 1950s and 1960s"), for example "Before 1970, fusion machines in the explorer stood only in …".

## Polish
1. In `unit.md` Story, after "machines that started before 1970 stand in exactly these three countries", add "(the selection leaves out, for example, West Germany's first Wendelstein stellarators of 1960)". This keeps a gap in the data from reading as history. The pred-cold feedback already says "the explorer is a selection".
2. The Common difficulties in `teacher.md` say TEXTOR "shows only *Germany*". It now shows "West Germany until 1990 (today Germany)". Update the line.

## Checked
- **Counts:** I recomputed them from facilities.json with the year rule in map.js (start ≤ y ≤ end; a retired machine with end null counts to last_seen, or else to start + 10; planned and construction never count). All of them match the unit:
  - 63 facilities in 14 countries.
  - Before 1970: the US, the UK and Russia/USSR.
  - 1958: 6 facilities in 3 countries (Model A, Model B, Perhapsatron, Scylla I, ZETA, T-1).
  - 1965: 4 (Scylla I and T-3 are counted by the rule).
  - 1985: 8 in 6 countries (JET, TFR, ASDEX, TEXTOR, TFTR, JT-60, PLT, T-10).
  - 2026: 24 operating facilities in 12 countries on 3 continents.
  - Model A and the Perhapsatron are counted until 1963. TFR and Pulsator start in 1973.
- **Data checked against sources:**
  - The List of fusion experiments gives T-1 1958–59, T-3 1962–?, Model B 1954–59, Model C 1961–69, ST 1970–74, Pulsator 1973–79 (also on IPP's page), JT-60 1985–89, T-15 1988–95, PDX 1978–83, ASDEX 1980–90, START 1990–98 and HL-2A 2002–18.
  - The TFR end year of 1986 has a note about the difference between sources.
  - NIFS confirms that LHD ended on 25 Dec 2025.
  - The notes on T-10's and FTU's last_seen, the two COMPASS records, and the uncertain status of LM26 and Norman are honest and sourced.
- **History:** declassification in Geneva in September 1958; T-3 at about 10 million K, confirmed in 1969 by laser Thomson scattering (UKAEA); the JET Joint Undertaking, 30 May 1978; the Geneva summit, 19–21 Nov 1985; the ITER Agreement, 21 Nov 2006 in Paris, with seven members; HL-2A from ASDEX; JT-60SA.
- **JET label:** 16 MW in 1997 and 69 MJ in 2023.
- **Choices:** every choice has exactly one correct option, and its feedback is right. Company results are marked as company-reported, and planned dates as plans.

## Shared issues
None. The data file and map.js are consistent with the unit.
