VERDICT: PASS
CONTENT-HASH: cc1b6258a152ff14

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
