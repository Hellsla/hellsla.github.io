VERDICT: PASS
CONTENT-HASH: 307c0dfc144588a5

Scope: preview/fy3-1.html, Chromium at 1280/390/360/320. Screenshots in review/ (fy3-1-390.png, fy3-1-1280.png, fy3-1-sim-{390,360,320}.png, fy3-1-table-320.png).

1. Text column: paragraph width 608 px at 17 px font = about 67 characters per line at 1280 (target 60-75). OK.
2. Horizontal overflow: documentElement scrollWidth equals clientWidth at 1280, 390, 360 and 320. No page overflow. Only KaTeX display math is wider than the viewport (up to 410 px) and it sits inside scrollable display blocks. OK.
3. Maths: no .katex-error elements. G = mg, the worked example and "9,81 m/s²" render readably.
4. g table: header "Taivaankappale | g pinnalla (m/s²)" renders with the unit. Row height 45 px, header 34 px. At 1280, 390 and 360 the table fits, apart from 305 px content in 328 px at 360. At 320 the table (305 px) is wider than its box (286 px) and scrolls inside itself (overflow-x auto), so the last ")" of the header sits at the edge. Minor, not breakage. Numbers are left-aligned, not decimal-aligned. Optional improvement: right-align the numeric column or shorten the header to "g (m/s²)".
5. Sim controls: select 40 px high, range input 40 px high, labels 24 px; width follows the container (324/294/254 px at 390/360/320). Tap targets below 40 px: 0 (links, summaries, controls all >= 40 px).
6. Sim readout (DOM text, 16 px): "g = 9,81 m/s² (Maa)" fits on one line at every width (readout box 72 px high, no overlap or clipping at 320). OK.
7. Sim canvas labels at 320 (canvas scaled to 254 px, about 0.42x): the title "Sama massa, paino eri paikoissa", "asteikko 0 – 2480 N", bar values (16,2 N / 37,1 N / 98,1 N / 248 N) and names (Kuu/Mars/Maa/Jupiter) are all inside the canvas, nothing clipped. Text is small (about 9-10 px effective) but legible. Fine at 390 and 360.
8. Inline SVG figure (spring scale): label text effective size is 20.3 px at 1280, 11.9 px at 390, 10.9 px at 360 and 9.6 px at 320. This is a little small at 320 and acceptable.
9. Exercises: 3 collapsible <details class="level"> (Taso 1/2/3, with counts), each answer in its own <details>. A "Siirry lähtölippuun" skip link is present. OK.
10. Exit ticket: section #exit follows the exercises and is reachable by the skip link and by scrolling; 3 questions with collapsible answers. OK.
11. Contrast: body text is dark on light cream. The canvas grey 60 text on a light background is above 7:1 and the green title (26,77,46) is above 8:1. No low-contrast text noticed in the screenshots.
