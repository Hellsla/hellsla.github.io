VERDICT: PASS

Fresh re-check of fy3-2 after the template/CSS/sim revision. Built with `build.py --all`, measured with my own Playwright script (Chromium 1243) at 1280 and 390 px. Screenshots in this folder: `web-designer-1280.png`, `web-designer-390.png`, `web-designer-sim-390.png` (sim at 390), `web-designer-exercises-390.png` (exercises with levels opened). The earlier blockers (canvas-only readout, 40 px targets, no disclosure marker, narrow sliders, small SVG labels) are all resolved. No real breakage. Findings below are polish only.

1. Text column is at the top edge of the 60-75 range (minor). At 1280 the column is 640 px (40rem) at 18 px. Actual characters per rendered line in the first long paragraph: 75, 73, 72, 76, 71 (mean about 73). The font-metric estimate is 67. Lines occasionally reach 76. Proposal: `body{max-width:38rem}` gives about 69 characters per line. This is optional.

2. Horizontal overflow at 390: none. documentElement.scrollWidth = clientWidth = 390 and body.scrollWidth = 390. Display maths is scrollable inside its own box (the three `.katex-display` elements are 358 px wide with scrollWidth 358, so they fit and don't need to scroll). The only elements past the right edge are KaTeX's visually hidden `<math>` MathML nodes, which are clipped and cause no scroll. No change needed.

3. Maths readable: KaTeX renders at 21.8 px against 18 px body text. Display formulas (W = Fs, W = Gh = mgh, P = W/t = Fv) are centred and legible at both widths. No inline formula crosses the right edge at 390. No change needed.

4. Sim layout: no overlap at either width. At 390 the canvas is at y 4090-4329 (358 x 239, scale 0.597), the readout starts at 4337 and the controls at 4417. The readout (W, P, work so far) is DOM text at 16 px. Sliders are 358/358/250 px wide and 40 px tall. The button is 84 x 40, placed beside the third slider with a 24 px gap (slider ends at x 266, button starts at 290). No change needed.

5. In-canvas text at 390: `k` = 1.676 and canvas scale = 0.597, so the 11 px text renders at about 11.0 px, the 12 px text at 12.0 px and the 13 px text at 13.0 px. This meets the 10 px target (screenshot confirms the labels are legible). Decorative tick and dashed lines are grey 150 on 250 (2.83:1). They carry no text, so this is acceptable. If you want them to pass 3:1, use `p.stroke(130)` for the metre ticks and the dashed guide. Margin is thin, so keep the `ts()` scaling when editing the sim.

6. SVG label size: the 600-unit-wide viewBox has 20 px text, which is 21.3 px at 1280 and 11.9 px at 390 (scale 0.597). All six labels pass the 10 px target. No change needed.

7. Exercises collapsible by level with a visible marker: the three `details.level` elements are closed by default. Each shows a blue triangle marker (▸ when closed, ▾ when open) plus a count ("5 tehtävää"). Each answer is a nested `details.answer` with its own ▸ marker. The marker colour #2f6f9f on white is 5.39:1. Note: the underline border on level summaries (#d5dde3, 1.37:1) is decorative only. The marker and bold label are the affordance, so this is fine.

8. Exit ticket reachable: it is the final section, and it is not collapsed. A "Siirry lähtölippuun ↓" skip link at the top of the exercises section (40 px tall) jumps to `#exit`. With levels closed the page is short, so the ticket is about three screens below the sim. No change needed.

9. Contrast (WCAG AA): nav and `.count` #666 on white is 5.74:1. Links #2f6f9f on white is 5.39:1, and 5.0:1 on the blockquote background #f3f7fa. `.note` #555 is 7.46:1. Button border #767676 on white is 4.54:1 (non-text threshold 3:1 met; button text is black on white). Canvas text: grey 90 on 250 is 6.61:1, the blue label is 5.17:1 and the red F label is 5.31:1. All pass. Disabled/focus styling is not overridden, so the browser default focus ring applies.

10. Tap targets (all >= 40 px, measured): nav links "Fysiikkalabra" 101 x 40 and "FY3" 40 x 40; level summaries 41 px tall (358 wide at 390); "Vastaus" summaries 40 px tall (318 wide); range inputs 40 px tall (358/358/250 wide at 390); button 84 x 40; skip link 139 x 40. The "FY3" link is only 40 px wide, which is exactly at the threshold. Optional proposal: `nav a{min-width:40px;justify-content:center}` already holds; to give more room, use `nav a{padding:0 .6rem;margin:0 -.6rem}`. The 40 px figures are at the floor, so do not shrink them.

Summary: PASS. Optional polish is item 1 (38rem column) and item 5 (tick grey 130).
