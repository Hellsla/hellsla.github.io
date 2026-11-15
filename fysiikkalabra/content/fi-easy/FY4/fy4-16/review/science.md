VERDICT: PASS
CONTENT-HASH: 45247432a6a7f54a

## Blocking
None.

## Polish
1. lesson.md:407 — "Hississä lattian tukivoima on liikkeen suuntainen, ja se tekee työtä" holds only while the lift moves, and when it moves down the force is opposite to the motion (negative work). — "Kun hissi liikkuu, lattian tukivoima on liikesuoran suuntainen ja tekee työtä (ylös mennessä positiivista, alas negatiivista)."
2. lesson.md:364 — the worked example writes $E_\text{p,1}$, $E_\text{p,2}$, $v_1$, $v_2$, but the Kaava table defines the energy principle with index 0 for the start and no index for the end. — Say once that 1 and 2 mark the start and the end here, or use the table's indices.

## Checked
- Every number recomputed in one script with my own formulas: Ydinajatus 648,6 N → 650 N, 66 kg, 78,5 kJ; force-plate graph 650/589/550 N with $a = 1{,}023$ and $-0{,}643\,\text{m/s}^2$, slowing 3,18 s (9,0 → 12,2 s on the graph); slope table (10,39/9,866/49,61; 16,48/9,240/43,52; 34,03/7,138/25,97 m, sums 60,0 = h/μ; $\sqrt{2gh}$ = 10,85 m/s); worked example 8,694 m/s, 12,95 m/s without friction, $a$ = 1,512 m/s², $v^2$ = 75,6; siirto 95,65 kJ with mistakes 0,975 and 96,62; check-2 48,27 kg with mistakes 61,73 and 473,55; suitcase T = 149,6 N < 176,6 N. All agree with lesson-answers.py and the text.
- Models and conditions: $N = m(g+a)$ with the sign convention stated; the terminal-speed energy argument (drag work $-mgh$, ends as internal energy, P1 wording right); $W_\mu = -\mu mgx$ with its three conditions; $x_1 + x_2 = h/\mu$ with constant μ, no air drag, short bend, $\tan\alpha > \mu$.
- Causality: scale reading follows acceleration, not velocity; on the steep slope both the friction force and the slope length are smaller.
- Force diagrams (Ydinajatus, example, model suitcase; fbd.py): right bodies, forces, directions and relative lengths; friction up the slope; velocity and acceleration apart from the forces; tension < weight for the suitcase.
- Inquiry: exactly one correct option in kertaus, pred-1, pred-2, the table question, check-1 and check-3; every distractor wrong and its feedback right; example data and model values labelled.
- Exit ticket and summary agree with the theory; liukukitka used throughout (P8); scope inside FY4's central contents.
