VERDICT: PASS
CONTENT-HASH: 88cc39fef4d4cd2a

## Blocking

## Polish
- exercises/exercises.json (fy8-13-L2-09 a) — "kolme suurinta lähdettä" depends on how the sources are split. If the student splits "muu luonnon säteily" (external 0,45, internal 0,30, cosmic 0,33 mSv), the three largest become radon, medical use and external gamma. Solution line 281 says "Valitset itse"; say also that both groupings are accepted.
- exercises/solutions.md:278 — "aika $t = 8760\,\text{h}$, jonka vuoden tuntimäärä antaa tarkasti" reads awkwardly. Write "$t = 8760\,\text{h}$ (vuoden tuntimäärä, tarkka)".

## Checked
- Hash 88cc39fef4d4cd2a at the start and the end. The diff was judged: the new L2-09, and four captions that lost "(esimerkkiaineisto)".
- The captions follow main's site-wide change c063afe973 (work queue 8l). The four task texts still say "esimerkkiaineisto", so example data is not presented as measured.
- Recomputed: $H = 0{,}10\,\mu\text{Sv/h} \cdot 8760\,\text{h} = 876\,\mu\text{Sv} = 0{,}876\,\text{mSv}$, so the box value is 0,88 mSv. answers.py also gives 0,876. Tolerance 0,02 (relative) accepts 0,862–0,898. Two significant figures come from the dose rate, and the hours are exact (house rule 2026-11-16).
- b): $4/5{,}9 = 67{,}8\,\%$ ≈ $68\,\%$, consistent with "kaksi kolmasosaa". d): $0{,}88/5{,}9 = 15\,\%$ and $5{,}9 - 0{,}88 = 5{,}0\,\text{mSv}$ are correct.
- Every number attributed to the reports is in the verified lines: 5,9, 4, 1,1, 0,76, "kaksi kolmasosaa", 0,45 and 0,33 mSv. Their sum of 0,78 mSv matches the meter estimate in magnitude.
- The physics of d) is right. Radon decay products irradiate the lungs internally and an external meter does not see them. K-40 (the solution's own reasoning, not attributed), medical use, indoor time and place-to-place variation are also correct. $H = \dot{H}t$ is used under its stated constant-rate assumption.
