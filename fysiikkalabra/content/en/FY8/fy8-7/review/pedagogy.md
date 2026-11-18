VERDICT: FAIL
CONTENT-HASH: 6762f2ae91326a1a
## Blocking
- content/en/FY8/fy8-7/inquiry.json:33 — the retrieval item's prompt now says 633 nm (helium-neon), but the correct option's feedback still says "wavelength 650 nm ... approx. 1.91 eV" — the feedback contradicts the question and the new answers.py value (hc/633 nm = 1.96 eV) — change to $633\,\text{nm}$ and $\approx 1.96\,\text{eV}$.
- content/en/FY8/fy8-7/inquiry.json:37 — same in the "energy of the upper level" distractor's feedback (650 nm, 1.91 eV) — change to $633\,\text{nm}$ and $1.96\,\text{eV}$.

## Polish
- The lesson-answers.py key is renamed kert-633-eV; confirm the inquiry/answers check no longer refers to kert-650-eV.
- The reworded direction distractor ("light that atoms emit by themselves spreads in all directions") is fine and no longer mentions a lamp.

## Checked
- Prompt change to the helium-neon laser, 633 nm: fits the lesson's pics (helium-neon-laser) and the physics.
- Direction-distractor feedback: still repairs the misconception.
- Other 650 nm mentions (line 480, exercise solution about graph points) are a separate exercise and unaffected.
- Hash at start and end: 6762f2ae91326a1a (en); no further edits during review.
