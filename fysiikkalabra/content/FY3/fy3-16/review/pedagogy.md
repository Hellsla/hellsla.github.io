VERDICT: PASS
CONTENT-HASH: 824a4d20f0370c33

## Blocking
(none)

## Polish
- solutions.md fy3-16-L3-01 and L3-03 — Sijoitus still packs several calculations into one run of text (carried from round 2). Fix: split into one labelled line per calculation, as now done in L3-02 and the inquiry siirto task.
- solutions.md L3-02 Järkevyys, last sentence — "1,51 kg eli kahdella numerolla pienin sopiva massa 1,5 kg" is clumsy (carried). Fix: "1,51 kg, pyöristettynä 1,5 kg".

## Checked
- Siirto task (inquiry.json) Sijoitus: the bracket is first evaluated on its own (335 200 + 2 260 000 = 2 595 200 J/kg), then t is shown as three short aligned lines. Each step is one operation a student can follow; units are carried throughout.
- Arithmetic recomputed: 4190·80 = 335 200; 0,15·2 595 200 = 389 280 J; /6000 = 64,88 s, which matches the Vastaus (65 s).
- L3-02 Sijoitus: numerator (251 400 − 167 000 = 84 400 J) and denominator (4190·2,50 = 10 475 J/K) are named separately, then the final quotient is shown on its own line. 84 400/10 475 = 8,057 matches the Vastaus and Järkevyys.
- The two-significant-figure justification in L3-02 is unchanged and still names the subtraction as the limiting step.
- The split makes each displayed line shorter, which is the aim for 360 px; the layout 360 px check is green.
- No new term, no change to the Annettu, Periaate, Kaava or Muunnokset stages. Only wording and layout changed, so the earlier pass stands.
- Hash differs from round 2 only by this diff and was the same at the start and the end.
