VERDICT: PASS
CONTENT-HASH: 13bbadfdc5fe3724

## Blocking
(none)

## Polish
- [Minor] fy7-s1 model answer a) — the two lines "- For the ion to travel straight…" and "- The velocity … is not a force" follow the paragraph with no blank line, so they render as plain text starting with a hyphen, not as a list (same in fi and fi-easy). Fix: blank line before the list in all three solutions.md.
- [Minor] points labels — "3 p" / "1 p" beside tasks and criteria is the Finnish abbreviation, while the card header says "16 points". Fix: "3 pts" via the shared template string (not Sovella-specific).
- [Minor] subscripts — $F_\text{s}$, $B_\text{s}$, $U_\text{s}$ keep the Finnish initials (sähkö, valitsin) in the figures and text while other subscripts are translated ($U_\text{mine}$, $P_\text{in}$, $f_\text{w}$, $I_\text{sc}$). Not misleading since each is defined; fix: per-language subscripts (shared with FY5).
- [Minor] 390 px top — the task tab strip's "2 Hub d…" is overlapped by the Listen button, and the banner reads "this lesson" on a task page (shared header, as in fi).
- [Minor] s1 e) model answer — "$m_{10} : m_{11} = 1.6627 : 1.8281 \approx 0.91$" wraps mid-ratio at 390 px; acceptable.

## Checked
Captures made by me (scratchpad/tools/cap_sovella.py, preview/en/FY7-sovella.html, 390 and 1280, every box open).
- top-390; s1 at 390 in full (task text, fig-1, selector fig-3, model answer a)–e), Also accepted, Common mistakes, marking cards).
- All six figures (implanter, selector forces, hub-dynamo graph, spectrum, fibre, grating graph): every label English ("silicon wafer", "analysing magnet", "velocity selector", "cladding n2", "core n1", "air", "relative intensity", "visible"), decimal point on ticks (fi uses comma; a figure may keep either, not a finding).
- s4 c)–e) and s5 task with both tables and graph at 390; s3 e) at 1280.
- No Finnish word in text, alt text or figure labels. The solution headings Hyväksytään myös / Yleisiä virheitä render as "Also accepted" / "Common mistakes".
- check_layout.py FY7-sovella --width 340 and 360: OK for en. scrollWidth equals viewport at 390 and 1280.
- Translation matches the reviewed Finnish structure: same steps, numbers, boxes, figures; s1 d) uses the split mv line.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4
