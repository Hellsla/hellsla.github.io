VERDICT: PASS
CONTENT-HASH: 2e3710706cf4d933

## Blocking
- None.

## Polish
- Step 3: ga-facts.md says Data Collection Settings opens from the Mode button; "Avaa **Data Collection Settings**" could add "tila-painikkeesta (Mode)" so the student finds it.
- Photogate: "**Linear Motion** useiden katkosten liikkeelle" — in Vernier software this mode is for a flag/picket fence or several gates; acceptable, optionally "usean katkoksen (esimerkiksi aitaliuskan) liikkeelle".
- Motion detector: the sign convention (positive away from the sensor) is the default and can be reversed in the app; "yleensä" already hedges it.

## Checked
- UI names all in ga-facts.md: Sensor Data Collection, Discovered Wireless Devices > Connect, sensor meter > Zero, Data Collection Settings, Time Based, End Collection: After Fixed Duration / Manually, On a Triggering Event, Event Based > Events with Entry, Examine, region drag, View Statistics, View Integral, Photogate Timing (Speed Through Gate, Linear Motion, Pendulum Period), Export data as csv / graph as png, .gambl.
- Physics: zeroing unloaded and zero drift, offset accumulating in an integral; sampling rate vs short peaks (figure shows sparse samples straddling the peak, consistent with the text); range clipping; v = b/Δt is the mean speed through the gate; area of F–t is impulse in N·s, of a–t is Δv in m/s; phone g-units and whether g is included.
- Figure matches figures.py; legend clear of the curve; labels LaTeX; schematic without numbers.
- LaTeX: units $\text{N} \cdot \text{s}$, $9{,}81\,\text{m/s}^2$, $1{,}00$.

## Delta 1 (2026-10-31, Finnish UI and screenshots)

- Bold Finnish UI names checked against Lauri's GA v6.2.1 screenshots (cropped assets/pics/tvt/*.png and the uncropped originals in /mnt/project-files/ga-pro-kuvat/); English names in brackets checked against ga-facts.md. No invented Finnish names found.
- Verified: **Mittaa antureilla** (ga-aloitus.png), **Tilastotiedot**, **Integraali** (ga-kuvaajatyokalut.png). The status-bar strings "Tila: Ajan funktiona" and "Nopeus: 2 mittauspistettä/s" and the blue selection with a menu beside it (Sulje valikko, Tilastotiedot, Integraali, Käyrän sovitus…) are not in the cropped pictures but are in Lauri's uncropped originals (alkun_kym_.png, k_yr_n_sovitus2.png), so they are confirmed. English: Discovered Wireless Devices, Connect, Zero, Data Collection Settings, Time Based, End Collection: After Fixed Duration, Manually, On a Triggering Event, Event Based, Events with Entry, Examine, Export data as csv, Export graph as png, Photogate Timing, Speed Through Gate, Linear Motion, Pendulum Period (all in ga-facts).
- Physics unchanged and correct: F–t area = impulse in N·s, a–t area = change of velocity in m/s.
