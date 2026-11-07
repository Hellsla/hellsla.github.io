VERDICT: FAIL
CONTENT-HASH: 630e508758be4e92

## Blocking
- content/fi-easy/FY5/fy5-16/exercises/solutions.md:39 (L1-04 Järkevyys) — A: compares the protected ear level 83 dB with the action values ("jää ylemmän toiminta-arvon 85 dB alle", "yli alemman toiminta-arvon 80 dB"). Under VNA 85/2006 the action values are judged without hearing protectors (106 dB exceeds both, so protectors are obligatory); only the exposure limit 87 dB(A) takes protectors into account — compare 83 dB with the limit 87 dB(A) and say that without protectors 106 dB far exceeds both action values.

## Polish
- content/fi-easy/FY5/fy5-16/exercises/solutions.md:103,204 (L3-01, L3-04) — symbol t_sall,i left beside the renamed t_v — write t_v,i.
- content/fi-easy/FY5/fy5-16/exercises/exercises.json:301 (L2-04 option feedback) — at exactly 85 dB for 8 h the dose equals the reference dose, so "Vaikka annos jää vertailuannosta pienemmäksi" does not fit — write "Vaikka annos ei ylittäisi vertailuannosta".

## Checked
light delta review (teacher 2026-11-07): Mode full in the packet replaced by the teacher's light review of git diff origin/main -- exercises/ answers.py (answers.py unchanged), not a full review: vertailuaika renamed as the time to reach the reference dose; recomputed 2.0 h, 4.0 h, 150 %, 1.875 min, 125 %, 100 dB / 1.60 h / 187-190 % / 47 %, 83 dB, unprotected 3.75 min.
