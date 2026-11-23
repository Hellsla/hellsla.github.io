VERDICT: PASS
CONTENT-HASH: bcf5e6261c14c7a4
SCOPE: full (fi-easy); the three new ```pysahdy boxes judged first against content/fi/units/fy9-voimat/unit.md.

## Blocking
- (none)

## Polish
- kalteva.webp (C, not a physics error): at the centre of the free-body diagram the G_x and G_y dashed components start together at the top of the solid G line and form a small "^". It can read as an upward arrowhead on G. The old SVG had the same junction. Visual reviewer: a small gap or a dot at the centre would remove it.
- s8 c: "0,02 m/s on pyöristysero". With unrounded values v(8,7 s) = +0,026 m/s, so the lift stops at about 8,67 s. That is inside the precision of a value read from the graph and is not wrong; "lukematarkkuuden rajoissa" would be more exact. The same wording is in the Finnish version.
- s7: the task text gives 75 kg, but the solutions and rubric use 75,0 kg. This does not affect the answers to two significant figures. It is the same in the Finnish version.

## Checked
- Pysähdy 1 (third law): the forces act on different bodies, and only the forces on the trailer decide its motion. This has the same physics as fi and matches the Ydinajatus paragraph and the hook.
- Pysähdy 2 (braking on a straight road): the net force points along the acceleration, against the motion. Same as fi. "Suoralla" excludes a centripetal component. It matches the paragraph above it and lt-3.
- Pysähdy 3 (slope): N = mg cos α under the stated condition (only weight and the normal force act perpendicular to the surface). N cancels G_y and is smaller than mg. Same as fi. It matches the theory text and the rubrics of s1, s6 and virhe-rinne.
- kalteva.webp, measured from the pixels: G_y ≈ 338 px ≈ N 327 px, G = 367 px, G_x = 155 px = G sin 25°, G_y ≈ G cos 25°. The α between G and G_y is correct. Friction is at the upper corner and points up the slope. v and a point down the slope at 25°. This agrees with the aria-label. The hero picture is decorative and has no physics claims.
- One script recomputed every number from the task data. Results: s1 664,5/666,3/1330,8 N, 932,8 N, 19,29°; s2 118,48 and 296,2 N, ratio 0,40; s3 least squares k = 1,175 1/kg, intercept 0,239 N, readings 0,851 kg and 0,238 N, μ = 0,0285, k' = 0,740, F0' = 0,378 N; s5 tan 22,5° = 0,414, 0,384–0,445, atan 0,54 = 28,4°; s6 1,272 m/s², 10,09 m/s, 7,9 s, 64,83 m; s7 623,25 N, 48,35 m/s, k = 0,3147, 55,8 m/s, ratio 1,155; s8 −1,1433 m/s², −2,287 m/s, 0,8567 m/s², 12,234 m. Inquiry: 23,0/8,39 N, 6766,5 N, μ = 0,3596, 3,306 and 12,03 m/s², P = 48,0 N, T = 23,54 N, plus every mistake value. teacher.md m_p = 0,124 kg. All agree with tasks.json, solutions.md, answers.py and inquiry.json.
- The rubric points add up. The criteria ask only what the tasks give, and correct alternative methods are listed under Hyväksytään myös. Every choice item has exactly one correct option, and the feedback on each distractor is right. The scope stays within FY4 plus FY1 graphing. Friction terms follow the house rules, and no data is falsely presented as measured.
