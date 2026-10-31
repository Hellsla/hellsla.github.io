VERDICT: PASS
CONTENT-HASH: cc1b6258a152ff14

## Blocking

None.

## Polish

- Step 3: "Avaa **Data Collection Settings**" does not say where; the verified path is the Mode button (tilapainike) → Data Collection Settings. Add it so the student finds the rate and duration settings; steps 4–5 depend on the same dialog.
- Step 7: say that **Examine** is under **Graph Tools** (as nopeus-datasta does for **Tangent**).
- Mistake "Puhelimen lukemat ovat $g$:n kerrannaisia": "kerrannainen" suggests integer multiples; "Puhelin ilmoittaa lukemat $g$:n yksikköinä" is clearer.
- Valoportti uses $b$ for the flag width, while three other guides use $b$ for the intercept; consider another symbol (e.g. $d$) here and in tvt-nopeus-datasta.
- Checklist does not check goal 2 (reading values, means, areas); add one line, e.g. "Olet rajannut keskiarvon ja pinta-alan oikealle välille."

## Checked

- Read guide.json, guide.md and the figure's labels in full; ran the hash. Menu names (Sensor Data Collection, Discovered Wireless Devices, Connect, Zero, Data Collection Settings, Time Based, End Collection: After Fixed Duration, Manually, On a Triggering Event, Event Based, Events with Entry, Examine, View Statistics, View Integral, Export data as csv, Export graph as png, Photogate Timing, Speed Through Gate, Linear Motion, Pendulum Period) are all in the verified facts.
- Order: connect → zero → rate/duration → trigger → event mode → test run → read values → statistics → integral → save. Each step gives the physical reason (peak between samples, drift, impulse in N·s, Δv in m/s).
- Goals match; mistakes are real ones (not zeroed, rate too low, start missed, clipped range, phone in g units, raw data not saved), each with a fix.
- Sampling figure (dense vs sparse samples missing a peak) supports step 3; no numbers.
- Finnish grammatical around bold names. Cross-links to suoran-sovitus and taulukkolaskenta sensible; investigation titles exist. No Logger Pro / spreadsheet leftovers.
