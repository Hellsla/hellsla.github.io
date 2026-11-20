VERDICT: PASS
CONTENT-HASH: da144a33e701c6ed

## Blocking
(none)

## Polish
(none)

## Checked
- Delta review, round 4 (the confirmation round): only the third self-assessment criterion of `johtopaatos` (inquiry.json:262) changed from round 3.
- The new criterion is "efficiency of the incandescent lamp is about $5\,\%$, so only a small part of the energy taken is useful". It is about the koe-2 lamp the prompt asks about, the student's own table gives it, and the model answer shows it ($20\,\text{J} : 400\,\text{J} = 5\,\%$, with the remaining $95\,\%$ as losses). Round 3's finding (A, a criterion asking about the petrol engine from optional koe-1) is fixed.
- I recomputed it for the locked koe-2 setup ($P_\text{o} = 40\,\text{W}$, $\eta = 0.05$): $t = 10$ and $20\,\text{s}$ give $E_\text{o} = 400$ and $800\,\text{J}$, $E_\text{a} = 20$ and $40\,\text{J}$, $\eta = 5\,\%$ on both rows, and $P_\text{a} = 2.0\,\text{W}$. These agree with the model answer and the criterion.
- All three criteria now ask only for what the prompt and the koe-2 data give. No core item depends on optional koe-1 or ennuste-1.
- The Finnish source has the same fix (content/fi/FY2/fy2-4/inquiry.json:262, "hehkulampun hyötysuhde on noin $5\,\%$ …"), so the language versions agree.
- Hash (`--lang en`) run at the start and at the end: unchanged, da144a33e701c6ed.
