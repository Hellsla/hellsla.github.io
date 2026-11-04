VERDICT: FAIL
CONTENT-HASH: 1d2219da8a5ea8a9

## Blocking
- exercises.json:311 fy5-14-L3-05 — **A, near-duplicate across chapters.** The task gets the speed of sound from the slope of s against t with a constant device delay. That is the idea of fy5-11-L2-05 (echo, constant phone delay, slope from first and last point) and fy5-10-L2-07 (click, slope of d against Δt). It also leaves out the plan's level 3, "perustelu sointivärin synnystä". — Replace it with that plan task. Example: one string plucked at its middle and near the bridge, with spectra given as a table. Students find f1, see that plucking at the middle leaves out the even harmonics (they have a node there), and explain the difference in timbre.
- solutions.md:140 fy5-14-L2-05 Järkevyys — **A, wrong number.** The text says "enintään 1,5 Hz, mikä vastaa noin 0,4 m/s:n vaihtelua". But dv_s/df = v·f0/f² ≈ 0,72 (m/s)/Hz, and the rows give 30,8, 29,3, 31,5 and 30,0 m/s, so the spread is about 1,1 m/s. — Change it to "noin 1 m/s:n vaihtelua (29,3–31,5 m/s)".

## Polish
- solutions.md:128 fy5-14-L1-08 — "kolme merkitsevää numeroa" has no reason, and the limiting datum is the difference of 6 Hz. — Either say that the nominal fork frequencies are taken as exact, or give 0,17 s.
- solutions.md:135,146,168 (L2-05, L2-06, L3-04) — the heading "Kuvaajan lukeminen" is used for reading a table. — Use "Aineiston käsittely".
- solutions.md:156 fy5-14-L2-07 — "Virhe ei ole siinä, että Doppler muuttaisi vain voimakkuutta" refutes a claim the student never made. — Delete the sentence.
- solutions.md:180 fy5-14-L3-05, if the task is kept — the raw points are called points "on the fitted line". The least-squares fit gives 342,9 m/s and t0 = 0,41 ms, so the result stands. — Read the points from the drawn line.

## Checked
- I recomputed all 20 answers in one script, and they all match answers.py: L1-08 0,167 s; L2-05 430,5 Hz → 30,41 m/s; L2-06 262 Hz; L2-07 544,1 (student) and 548,4 Hz; L3-04 vΔf/(2f0+Δf) = 0,4753 m/s; L3-05 fit 342,9 m/s.
- L3-04: the double Doppler shift (moving observer, then moving source) and the rearrangement are right. Flow "suoraan kohti anturia" is stated as an assumption, and 0,48 m/s is plausible.
- L2-07: the tolerance of 0,002 rejects 544 and accepts 548, as intended.
- L1-06 and L1-07: each has exactly one correct option, and every distractor's feedback is right. L1-07 matches the lesson's misconception (f stays constant while the source approaches).
- Scope: beats, Doppler, the harmonic series and timbre are all in FY5. No new task other than L3-05 duplicates fy5-12, fy5-13 or fy5-15.
