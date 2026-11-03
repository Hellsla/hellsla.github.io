VERDICT: DONE

Draft, round 1 (no simulation; meta.json unchanged, `sim: false`).

- `lesson.md`: Miksi + hero; Ydinajatus (melu, hearing damage and tinnitus, dose = level and time, Valtioneuvoston asetus 85/2006 with the action levels 80/85 dB and the limit 87 dB, A-weighting); `## Kaava: Sallittu altistusaika` ($t_\text{sall} = t_0/2^n$, $n = (L-L_0)/3\,\text{dB}$); Melun torjunta (source, path, ear); Tilan akustiikka (reflection, absorption, reverberation time, qualitative, no Sabine); Vastamelu (destructive interference, low frequencies); Kaiutin ja mikrofoni (energy conversion only); 7-stage example (drummer, needed attenuation 9 dB); misconception "korva tottuu"; summary.
- `figures.py`: hero, decibel ladder, exposure bars, source/path/ear, room rays, decay graph, anti-noise sum, loudspeaker/microphone.
- `inquiry.json`: hook, retrieval (two sources +3 dB), two predictions (94 dB time; anti-noise models, revealed after theory), interpret table (model values) with numeric, phone-app distance data (invented example) with choice, conclusion, transfer (saw + distance), error spotting, three checks, exit.
- Exercises 5/4/3 (two word answers), `solutions.md`, `answers.py`, `lesson-answers.py`, `exit-ticket.json` (2).
- `glossary.json`: melu, jälkikaiunta, kaiutin, mikrofoni.

check_lesson.py: all ok. Doubt: notation assumes *Äänen voimakkuus* uses $L$, $\lg$ and −6 dB per doubling of distance.
