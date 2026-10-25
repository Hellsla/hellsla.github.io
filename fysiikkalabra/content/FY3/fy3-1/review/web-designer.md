VERDICT: PASS
CONTENT-HASH: 941320a85db9b4cb

Final check of fy3-1 (preview/fy3-1.html), measured with Playwright (chromium-1243). Hash re-run at end: unchanged.

1. Text column at 1280: paragraphs are 608 px wide, 17 px font, line-height 28 px, about 67 characters per line (target 60-75). OK.
2. Horizontal overflow: documentElement.scrollWidth equals viewport at 1280, 390, 360 and 320. No page overflow. Only off-screen elements are the hidden KaTeX MathML accessibility nodes, which are not visible.
3. Maths: 0 .katex-error nodes; smallest KaTeX font 20.57 px. Readable.
4. g table (Taivaankappale / g pinnalla (m/s²): Kuu 1,62, Mars 3,71, Maa 9,81, Jupiter 24,8): 305 px wide, display:block with overflow-x:auto. Fits at 390 (358) and 360 (328); at 320 (288) it scrolls inside itself, page does not overflow. OK.
5. Simulation: select and range slider are 40 px high at all widths (324/294/254 px wide at 390/360/320). Canvas scales (324x216, 294x196, 254x169). Readout is DOM text (m, g with m/s², G = m · g in N), and it updates (Jupiter, 100 kg: g = 24,80 m/s², G = 2480,0 N; simState matches). Screenshot review/fy3-1-wd-sim-320-jup.png: bar labels (162/371/981/2480 N) and axis labels not clipped.
6. Exercises: three details.level blocks are closed by default, open on click; each answer is its own details/summary. OK.
7. Exit ticket: #exit exists and is visible after scroll at 390, 360 and 320.
8. Tap targets: no a/button/input/select/summary under 40 px in either dimension at any width (small list empty).
9. Contrast: body text rgb(20,23,30) on rgb(247,243,236); lowest ratio among all text elements measured 7.13:1 (table header). Above AA.

Minor (non-blocking): none found.
Screenshots: review/fy3-1-1280.png, fy3-1-390.png, fy3-1-wd-*.png.
