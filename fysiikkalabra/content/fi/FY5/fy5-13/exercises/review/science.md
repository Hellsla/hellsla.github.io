VERDICT: PASS
CONTENT-HASH: 24282a4bc568533b

## Blocking

## Polish
- exercises.json fy5-13-L3-04 a): "pysyy mittausepävarmuuden rajoissa vakiona" names an uncertainty that the task never gives. The solution judges by a spread of about 1 % against a steadily falling f1/F, which is sound. Saying "pysyy likimain vakiona" would ask only for what the data gives.
- solutions.md:208 (L1-09): I could not check the MAFY values here (helium 971 m/s, air 331,5 m/s at 0 °C). The ±4 % tolerance covers the usual table differences (965–972 m/s), so this is not blocking. Confirm against the MAFY table.
- exercises.json fy5-13-L2-02: the task does not say that the end correction is ignored (the chapter does, and the solution's check mentions it). L2-06 makes the same phenomenon a topic, so "pääkorjaus jätetään huomiotta" in L2-02 would keep the two consistent.

## Checked
- I recomputed every numeric answer in one script with my own formulas: L1-01 41,0 Hz; L1-02 515 Hz; L1-03 32,7 Hz; L1-04 0,70 m; L1-05 392 Hz; L1-08 100 Hz; L1-09 639,5 Hz; L2-01 5,38 Hz; L2-02 340 m/s; L2-03 33,3 cm; L2-04 60,0 m/s; L2-05 122,8 m/s; L2-06 343,0 m/s; L2-09 31,25 Hz; L3-01 131 Hz; L3-02 110 Hz; L3-03 0,500 m; L3-04 199,0 Hz; L3-05 330,8 m/s. All agree with answers.py and exercises.json.
- The models are right: string and open pipe f_n = nv/(2L), closed pipe n odd. Consecutive closed-pipe resonances differ by 2f1 (L3-03: 510 = 3·170 Hz, 850 = 5·170 Hz). For L2-08, a half-length closed pipe has the same f1.
- Data tasks: L2-05 f/n ≈ 96 Hz. In L2-06, L3 − L1 = λ, so the end correction cancels; e = 0,45 cm, and L2 agrees within 0,1 cm. In L3-04 f1²/F is constant to 1 % while f1/F is not, and the extrapolation beyond 80 N is noted. In L3-05 the ratios 1:2:3 and 1:3:5 identify the pipes, both give about 331 m/s, and that suits 0 °C.
- The task figure (figures.py task_string) shows 1,20 m with four loops and five nodes. It agrees with L2-04 and L2-09, and both state that the ends are nodes.
- Multiple choice (L1-06, L1-07, L2-07, L2-08): each has exactly one correct option, and every distractor's feedback names the actual error.
- Significant figures: L2-01 gives 5,4 Hz from the difference 7,0 m/s, L1-08 gives two figures from 0,60 m, and L1-09 gives two figures from 0,50 m. The stated reasons are right, and the tolerances admit the rounded answers.
- Scope: everything is FY5 standing waves. f ∝ √F is tested only as a data hypothesis, with no formula that lies outside the course.
