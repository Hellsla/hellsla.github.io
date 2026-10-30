VERDICT: FAIL
CONTENT-HASH: 5976e5a1e11b688e

## Blocking
- inquiry.json (activity `siirto`, prompt and `mistakes` value 0.706) — "hyppää veneestä laiturille vaakasuoralla nopeudella 2,4 m/s" does not say what the speed is measured against. Read as relative to the boat, the correct answer is 0,71 m/s, and the page tells that student they divided by the wrong mass. The solution silently assumes the ground frame — fix: write "2,4 m/s laituriin (maahan) nähden", and make the 0,706 feedback name the relative-speed reading if it stays.

## Polish
- lesson.md, "Vastaus alun kysymykseen" — "Kumpikin ehto täyttyy vain, jos toinen palloista on levossa" is a jump for a 17-year-old, and it answers the lesson's opening question. Add one line: squaring '+v_2'=v$ and subtracting '^2+v_2'^2=v^2$ gives v_1'v_2'=0$.
- inquiry.json `virhe` feedback: "suurempi kuin kummankaan vaunun liikemäärä yksinään sallisi" is muddled. Corrected: "Opiskelijan tulos /bin/bash{,}48\,\text{m/s}$ on suurempi kuin kummankaan vaunun alkunopeus, mikä on mahdotonta, kun vaunut liikkuvat toisiaan kohti."
- Figure 4 (`tyypit`): the carts carry no numbers and the violet arrows no label, so cart 1 versus 2 rests on yellow/grey alone. Add "1", "2" and $\overline{p}$ as in figures 2 and 3.
- Hero illustration: the alt text says the cue ball "on osunut", but the picture shows a gap between the balls. Say the moment just after contact in the alt text, or close the gap.
- Experiments always have  = 0$; the sign error (most common mistake) is practised only in Etsi virhe and the checks. An optional row with <0$ would help; not required.

## Checked
- Opening question is answered after the evidence; no answer shown before commitment (hook gives only the phenomenon).
- Predictions 1–2 are refutable by exp-1/exp-2; every option's feedback repairs its own misconception; model values re-computed (0,030; 0,048/0,029 J; 0,20/0,80; −0,12/0,48 m/s).
- Worked example: seven stages, symbolic first, energy check 38,3 → 32,5 kJ correct.
- Goals match the slot; 2D excluded; workload is one lesson (core path 2 predictions, 2 experiments).
- 390 px: sim, readout and the three closed boxes fit; the experiment captures are legible; figures 2–3 are legible and uncluttered.
- Finnish and glossary terms (kimmoisa, kimmoton, räjähdys, systeemi) correct.
- Hash at end equals hash at start.
