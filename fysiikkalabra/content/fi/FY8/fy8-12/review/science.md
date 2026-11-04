VERDICT: PASS
CONTENT-HASH: 4706a24b50cab984

## Blocking

## Polish
- lesson.md:456 — carried over: "lääketieteessä käytetty ... röntgen- ja elektronisäteily ... energia ei riitä muuttamaan ytimiä" holds for sterilisation (≤ 10 MeV electrons, ≤ 5 MeV X-rays) and diagnostics; 15–18 MV radiotherapy linacs make some photoneutrons and slight activation in the head. C at this level, "lähinnä neutronisäteily" softens it. — If wanted, "Steriloinnissa ja diagnostiikassa käytetty ...".

## Checked
- Only change since the last PASS: lessons/FY8/fy8-12/figures.py:208 `tuntematon` d-axis label filter `v % 4` → `v % 6`. Grid unchanged: xticks 2..48 step 2 (24 vertical lines), yticks 50..850 step 50; curve still R0 = 800, d½ = 12 mm from lesson-answers.py:138.
- Rendered the SVG: d labels 6, 12, 18, 24, 30, 36, 42, 48 (plus 0 at the origin) at x = 147, 194, …, 476 = X(d); y labels 200/400/600/800 at the right grid lines.
- Reading d½ still works and is easier: the curve passes (12 mm, 400 /min) = (194, 192.5) exactly on the crossing of two labelled grid lines. The solution's check points 24 mm → 200 /min and 48 mm → 50 /min also sit on labelled d values.
- Alt text (aria-label) "paksuus nollasta 48 millimetriin, ruudukon väli 2 millimetriä ja 50 pulssia minuutissa ... 800 pulssia minuutissa" is still true; it says nothing about label spacing.
- inquiry.json:390–411 (Tarkista 2): answer 12, tolerance 0,06, mistakes 24 and 400, hints and solution ("ruudukon väli 2 mm ja 50 pulssia minuutissa") need no change; nothing in lesson or inquiry refers to the old 4 mm labels.
- Screenshot review/shots/fy8-12-fig-14-390.png shows the new labels, no overlap.
- Content hash 4706a24b50cab984 at start and end, equal to the packet.
- Earlier physics checks (sim values 586/328/171, Ennuste 2 0,284, Siirto 5,57 %, 60 keV / 0,12 mm) untouched by this change and stand.
