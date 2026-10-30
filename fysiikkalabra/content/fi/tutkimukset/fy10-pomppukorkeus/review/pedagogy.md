VERDICT: PASS
CONTENT-HASH: 551da66bcc73d7db

## Blocking
None.

## Previous blocking finding, now fixed
1. **Goal 1 is now practised in all modes, and mode I keeps its decisions.**
   - A new section, *Tutkimuskysymyksestä mitattaviksi suureiksi*, comes before the theory. It asks the student to write down which quantities give the energy fraction, with an energy argument; what they vary, measure and keep constant; and which point on the ball they measure to, with a reason.
   - In mode I, the theory now shows only the energy principle. The definitions of $h_0$ and $h_1$, the reference point, the derivation $E_1/E_0 = h_1/h_0$, the model and both figures are in `::: tuki O OO`, which starts "Tarkista kirjauksesi tästä". O and OO students therefore write their own answer first and then check it.
   - A mode I student now has to justify $h_1/h_0$, the reference point and the axes. The all-mode sentence "kuvaaja, josta säilyvän energian osuus saadaan kulmakertoimena" states what must be found without giving the axes away.
   - The Raportoi item on goal 1 can no longer be copied in mode I.
   - teacher.md *Eriyttäminen* now matches the page.

## Polish
- **Ennusta Q2** names the axes ($h_1$ vertical, $h_0$ horizontal) in all modes, which hints at the axis choice in mode I. This is harmless as a prediction, but "Millainen on pomppukorkeuden ja pudotuskorkeuden välinen kuvaaja?" would leave the choice fully open.
- **teacher.md** says that measuring to the top of the ball gives a constant term equal to "pallon halkaisija". The intercept is in fact $d(1-a)$. The page itself says "pieni vakiotermi", which is correct.

## Checked
- **Hero.** The ball now falls directly in front of the scale (x 300–350), and the phone is drawn side-on with its lens towards the ball. The spacing at equal time steps is physically consistent, and the apex is lower than the drop point. The figure matches the research question.
- **Setup figure.** It shows a vertical drop with a dashed fall line before the bounce.
- **Intro.** The energy-loss sentence is removed, so Ennusta Q3 is open again.
- **Raportoi** now says "kaikki osat".
- **Finnish.** "keskenään" and "lukemassa on virhettä" are fixed.
- **Top-of-ball note.** The note "vähennä niistä pallon halkaisija" and the explanation of the small constant term are correct and placed in O/OO.
- **Restitution wording.** The teacher.md wording (restituutiokerroin is the square root of the energy ratio) is correct.
- **Scaffolding.**
  - O keeps the variables, the controls, at least six heights, three repeats, the table, a randomised order, the reading hints, the axes, two methods for $\Delta a$ and a rounding rule.
  - OO leaves the heights, the repeats and the reading method open.
  - Mode I is told that the extension is part of the work.
- **Goals 2 and 3** are met in the core sections. The help links (fy1-3, fy1-4) sit at the steps where they are needed.
- **Preview.** It is rebuilt with the new section and five O/OO blocks.
- Polish diff (9d2d77c8c89ec9d5) checked: Ennusta Q2 no longer names the axes and is a genuine proportionality prediction; teacher.md intercept now $(1 - a)d$. Both fine.
- Layout diff (551da66bcc73d7db) checked: setup figure release and apex moved down; brackets still meet the ball bottoms (104, 210), h1 < h0 kept, "pudotus" label clear of the edge, no text changed. Fine.
