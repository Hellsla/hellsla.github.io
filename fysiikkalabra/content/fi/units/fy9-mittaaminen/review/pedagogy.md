VERDICT: PASS
CONTENT-HASH: 0ca9f52c9bb8edae
SCOPE: delta: round 2, the fixes of round 1 in s7 and s8; older tasks untouched

Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
- (none)

## Polish
- s8 c in the solution still says "kuvaaja, jonka kulmakertoimesta $g$ saadaan" under Kysytty; fine for a solution, no change needed.
- s7 a names the model ("jousivakio", "sovita suora"); acceptable at part-a level (carried over, optional).

## Checked
- Round 1 had no Blocking items. Re-checked its Polish in the fi packet: s8 a now reads "Esitä aineisto kuvaajana, josta putoamiskiihtyvyys voidaan määrittää, ja sovita pisteisiin suora. Perustele kuvaajan valinta." (route no longer given, matches the intro); s8 c uses "Mittakaavan virhe" and "mittakaavan virhe noin 5,5 %", no "pituuskaavan virhe" left (grep).
- Newly broken: nothing; s7 text, points and answers unchanged, packet's practice.py check OK.
- Results rounded to the data (30,0 ± 1,2 N/m; 15,0 ± 0,6 cm; 10,35 ± 0,15 m/s^2), no revealed structure in the task texts, aligned rows, language-neutral units unchanged.
- Hash re-checked: 0ca9f52c9bb8edae.
