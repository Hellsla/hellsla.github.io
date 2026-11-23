VERDICT: PASS
CONTENT-HASH: 5bb4e6ce076f9a5c
SCOPE: delta md-paragraphs,numbers,paragraphs,reflow,typography from 0c746c938ac9ccb7 base e238aa9

## Blocking

## Polish
- solutions.md (L2-09 Järkevyys) — the earlier item still applies: "kuvan paneelin suurinta tehoa ($0{,}92\,\text{W}$)" points to the lesson's figure, not the task's figure.
- solutions.md:104 (maximum-power task, Kaava) — $U = RI$ is the load's Ohm's law. The earlier words "kuormalle" are gone from the Kaava row, though Periaate still says it.

## Checked
- Every changed Kaava line is now an `aligned` block. Each opens with Kirchhoff's voltage law in the lesson's form $U = U_R + U_\text{D}$ (with $2U_\text{D}$ or $3U_\text{D}$ for series LEDs) and Ohm's law $U_R = RI$, then solves for $R$ or $I$. This is the notation the brief teaches; the lesson does not use $\Sigma\Delta V = 0$.
- Efficiency rows start from $\eta = P_\text{hyöty}/P_\text{otettu}$ with $P_\text{otettu} = GA$, which is right. For the year task, $\eta = E/(HA)$ gives $E_\text{vuosi} = \eta A\sum H$, which is right with $H$ as energy per m².
- Reverse-bias row: $I = 0$ gives $U_\text{D} = U - RI = U$, which is right.
- LED-strip share: $(U - 3U_\text{D})/U$, with the current cancelling, is right.
- One script recomputed every number in the diff's context: 95 Ω; 8,3 mA; 250 Ω; 20,3 %; 0,36; 5,86 Ω; 25 %; 16,7 %; 207 Ω; 387 Ω; 4683 kWh; 87,7 %. All agree. The L3-05 work point (2,02 V; 13,8 mA) is unchanged and was checked last round.
- The paragraph splits (L3-04 Sijoitus a/b/c, L3-05 Sijoitus c and Järkevyys) and the exercises.json reflow only cut the text: the same numbers, signs and units in the same order.
- Hash read at start and end: unchanged.
