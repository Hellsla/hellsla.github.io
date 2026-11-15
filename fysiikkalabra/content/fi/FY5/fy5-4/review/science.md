VERDICT: PASS
CONTENT-HASH: 29869917bd624813

## Blocking

## Polish
- lesson.md:564 (Tiivistelmä) — "Kaarteessa keskeisvoiman antaa tien kitka" leaves out the condition the theory states (level road, no air resistance) — add "vaakasuoralla tiellä".
- lesson.md:555 (Järkevyys) — on wet asphalt $\mu_0 \approx 0{,}5$ is just under the $0{,}51$ needed, so "pito on rajoilla" undersells it — say "ei aivan riitä" or "pettää juuri ja juuri".
- inquiry.json pred-2, the "vauhti hidastuu" feedback — "se ei hidasta autoa" holds while the grip holds and in the model; a real skid does slow the car (the sim's Mallin oletukset says so) — add "mallissa" or "niin kauan kuin pito riittää".
- inquiry.json check-3 — $T$ is used for the cord's tension, while the lesson and its prior knowledge use $T$ for the period ($v = 2\pi r/T$) — consider $\overline{T}$ written as $\overline{F}_\text{j}$ or a note, to avoid a clash in the lesson where both appear.
- lesson-answers.py:1110 — `siirto-G` (a 55 kg passenger) is a number the siirto task does not give or use — remove it or tie it to the text.

## Checked
- I recomputed every number in lesson-answers.py in one script with my own formulas (graph, worked example 6000 N and $\mu_0 \ge 0{,}510$ → 0,51 rounded up, Koe 1 3,0/6,75/12 kN against 11,8 kN, $v_\text{max} = 19{,}81\,\text{m/s}$ (19,8 rounded down for an "at most" value) with both mistakes, Koe 2 ratio 0,920, siirto 15,34 m/s with both mistakes, check-2 148 N with both mistakes, check-3 0,765 N). All of them match.
- Figures: in *muutos* the tangents point counter-clockwise and $\Delta\overline{v}$ points to the centre. In *kaarre* and *esimerkki*, $F_\mu/G$ is about 0,5 and N equals G. In *nyppyla*, N is 0,6 G and 1,4 G (the same $a_n$ in both). The graph has the stated scale and its points read 2, 8, 4 and 9.
- Force diagrams: *virhe* (N + F_kp = G, so the only error is the invented force) and *valitse* a–d (exactly one correct, each wrong option has one error, every feedback is right). *malli-kiekko* has G, N and T only, with T about 0,46 G.
- Sim: the code computes $a_n = v^2/r$, $N = mg$ and the grip condition $m v^2/r \le \mu_0 mg$. When the car slides, it turns at the rate $\mu_0 g/v$, on a circle of radius $v^2/(\mu_0 g)$ (51 m at 20 m/s, so it stays on the asphalt; 79,6 m and 114,7 m at 25 and 30 m/s, so it leaves). The headings and normals are correct, and the inward direction in the rear view matches anticlockwise motion. The model's limits are stated in Mallin oletukset.
- Experiments: exp-1 varies v with r, m and the surface locked. exp-2 varies m with r, v and the surface locked. The keys an, Ftarve, Fmax and pito are all in simState.
- Predictions, kertaus, check-1, the exit ticket (a factor of 9 and $N = m(g - v^2/r)$) and every explain model answer agree with the theory.
- Centrifugal force is presented correctly: no real outward force in the ground frame, and a fictitious force only in the rotating frame. The friction terms (lepokitka, lähtökitka) follow the guardrails.
- Scope: normal acceleration and Newton's second law in circular motion, with no angular quantities, as FY5 requires.
- Hash at start 29869917bd624813. A concurrent edit briefly changed it to 10405e6603ece95c during the review; the file was restored and the hash at the end is 29869917bd624813 again.
