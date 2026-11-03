VERDICT: PASS
CONTENT-HASH: d141c14dfc9f5692

## Blocking

## Polish
- inquiry.json:381 (tarkistus-3 model) — the new perceived-loudness sentence is correct (2^(−0,6) ≈ 0,66, so about a third quieter), but it adds a second idea to a model answer whose criteria do not ask for it. Optional: shorten it to one clause, or add a criterion if it is meant to be assessed.

## Checked
- Round 1 blocking fixed: inquiry.json:94 now says a billion times the 90 dB speaker and thousands of times a nearby jet (true for a jet at 140–150 dB); inquiry.json:280 now says about three million times I₀ (10^6,5 = 3,16 · 10⁶).
- Round 1 polish fixed: ennuste-1 states even radiation and no reflections; siirto says "yhdestä … toisesta".
- New option wordings (ennuste-1 84 dB, ennuste-2 93 dB): each is still the only correct option, and its reason is right.
- tarkistus-1 is now set in an anechoic room: the 0 dB = I₀ physics is unchanged and correct.
- lesson.md calculator line: lg 3 = 0,4771 and 10^0,477 = 3,00 are correct.
- Fig-4's new 90,0 label matches L(1 m) = 90,0 dB at P = 12,6 mW. The other points (84,0 / 78,0 / 71,9 dB) were re-verified.
- The worked example's unit-step layout changed, not its values (9,6; 3,98 · 10⁻³ W/m²; 5,0 W).
- Re-ran the round 1 script: koe-1/koe-2 model values, the sums, virhe, siirto 0,969 dB, tarkistus-2 and the exit ticket all agree.
- sim.js and the experiments' setups are unchanged since round 1: same model, and each experiment locks P/N or P/r correctly.
