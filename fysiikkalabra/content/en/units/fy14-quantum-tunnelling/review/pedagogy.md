VERDICT: PASS
CONTENT-HASH: d2a9fd877ad07dac

Pedagogy review of fy14-quantum-tunnelling (2026-11-01). Read unit.md, inquiry.json, teacher.md, developer.md and the hero capture. Page rebuilt and tested in Playwright at 390 px.

Browser check: both predictions lock on commit with no feedback. `pred-slits` opens at *Key idea*, after the slit panels, `slits-talk` and the tunnelling table. `pred-tunnel` opens at *Tunnelling and the Sun*. The model answers of the two explain tasks stay closed until the student writes. There are no console errors.

The lesson works well:
- The hook-talk ("impossible or only unlikely?") is a good way into probability.
- The factor task on the table makes exponential decrease something the student finds, not something they are told; `check-2` then tests it.
- `check-explain` ("explain to a younger student") brings the chapter back to fusion.
- Word banks and starters sit with both written tasks, there is a vocabulary match, and the French corner is tied to de Broglie.
- The selita sections run to about 410 words.

## Blocking
None.

## Polish
1. `inquiry.json` `pred-tunnel` prompt: "What does quantum physics say happens?" asks for knowledge that the student does not have yet. The Why line, the hook and the learning goal ("how quantum tunnelling makes fusion possible") already show that barriers can be crossed. So the part still open to argument is the role of the width. Fix: ask "What do you predict?", and put the width in the stem: "… The barrier is then made twice as wide. What do you predict?"
2. `inquiry.json` `pred-tunnel`: the correct option joins two claims ("Sometimes it passes; a wider wall makes it rarer."), so the choice is forced for a student who agrees only with the first. This is fine once Polish 1 puts the width in the stem.
3. `inquiry.json` `proton-wave` asks the student to compare the result with the classical turning distance of about $1000\ \text{fm}$, but only the number is checked. Fix: end the solution's Reasonableness step with that comparison ("$779\ \text{fm}$ is about the same size as $1000\ \text{fm}$, so the wave reaches into the barrier").
4. `unit.md` *Tunnelling and the Sun*: "An average proton … waits about 9 billion years …: this is why the Sun shines steadily" reads as if tunnelling alone caused the slowness. Teacher.md rightly names the weak force. Fix: add half a sentence to the page, "(partly because the first step also needs the weak force; chapter *The Energy of the Stars*)".
5. `check-3`: the correct option ties for longest (63 characters). Fix: shorten it to "Protons tunnel, rarely, and there are huge numbers of them."

## Shared issues
- As for fy14-classical-limits: in `templates/inquiry.js` a section that is merely touched by the viewport counts as seen.
