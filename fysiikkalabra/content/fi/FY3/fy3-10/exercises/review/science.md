VERDICT: FAIL
CONTENT-HASH: 6f8f7939dcbb01f5

## Blocking
- exercises/exercises.json (fy3-10-L2-09, text) — A (internal consistency): the task shows the same figure `fy3-10/pt-suorat` as fy3-10-L2-04 and describes the same two identical rigid vessels A and B, but gives $n_A = 0{,}0500\,\text{mol}$, so vessel A comes out $1{,}66\,\textsf{l}$. In fy3-10-L2-04 the same vessels are $2{,}00\,\textsf{l}$ each, so line A ($p/T = 0{,}25\,\text{kPa/K}$) means $n_A = pV/(RT) = 0{,}0602\,\text{mol}$, and the figure generator's docstring says the same (V = 2,00 l, A 0,0602 mol). Within one chapter the same drawn vessel A has two different volumes and amounts of substance. A student who does both tasks sees data that contradict each other. — Fix: give L2-09 its own variant figure from figures.py (other lines or other vessel names, drawn from the L2-09 data with $V = 1{,}66\,\textsf{l}$), or keep the figure and take $n_A$ consistent with $2{,}00\,\textsf{l}$ while asking for something L2-04 does not already give. Then update answers.py and the solution to match.

## Polish
- lessons/FY3/fy3-10/answers.py:60 — the comment "# Added exercises (teacher 2026-11-12 …)" is still there twice (lines 60 and 62) — keep one.

## Checked
- L2-09 on its own: $V = nRT/p = 0{,}0500 \cdot 8{,}31 \cdot 400 / 100\,000 = 1{,}662 \cdot 10^{-3}\,\text{m}^3 = 1{,}66\,\textsf{l}$; the point (200 K; 50 kPa) gives the same value. answers.py gives 1,662.
- L2-09 conditions: a closed rigid vessel (fixed $n$, $V$) and ideal gas, both stated; T already in kelvins; the read point (400 K; 100 kPa) is a grid crossing; conversions kPa→Pa and m³→l shown; three significant figures justified by 0,0500 mol; the molar-volume check (about 33 l/mol at 400 K and 100 kPa) is real.
- The figure description lists A's points (200 K; 50 kPa) and (400 K; 100 kPa), so a reader who cannot see it has the data, and the answer is not given away.
- The previous Polish point (L2-09 repeating L2-04's step for B) is answered by asking for A's volume, but that is what brought in the contradiction above.
- L1-09 unchanged: $n = 500/39{,}95 = 12{,}52\,\text{mol}$, $p = 3{,}047\,\text{MPa} \approx 3{,}05\,\text{MPa}$; answers.py agrees.
- Hash same at start and end.
