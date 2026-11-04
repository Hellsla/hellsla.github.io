VERDICT: PASS
CONTENT-HASH: ecedd7bc074658dc

Follow-up review of the fix commit 2c31ff041 (delta from e3d3c48d800417d8, whose full review is kept below). Change: the paragraph after $P = UA\Delta T$ in `## Kaava: Energiatase`.

## Blocking

None.

## Polish

1. inquiry.json pred-1 correct option (Cem), :126 (kayra solution), :135 (taulukko), :167 (model answer): "sisällä pysyy $0\,{}^\circ\text{C}$" is right inside the stated model ("laskettu mallilla"; the example's "Oletetaan"); "mallissa" would make the link explicit (C).
2. lesson.md Ydinajatus "Olomuodon muutoksen aikana lämpötila ei muutu": optional "puhtaan aineen … normaalipaineessa" (C).

## Checked

- Earlier blocking item resolved: "Mallissa oletetaan, että laukun sisälämpötila on $0\,{}^\circ\text{C}$ niin kauan kuin jäätä on, jolloin $\Delta T$ on ulkolämpötila celsiusasteina. Silloin kaikki seinän läpi tuleva energia sulattaa jäätä" — now a stated model assumption, so $t = sm/(UA\Delta T)$ carries its condition and agrees with the Ydinajatus (only the ice–water mixture is at about $0\,{}^\circ\text{C}$).
- Consistency: grep of "$0\,{}^\circ\text{C}$" in lesson.md and inquiry.json finds no remaining unqualified claim outside the model contexts listed under Polish.
- Boundary cases: mixing misconception and virhe (ice remains, mixture at $0\,{}^\circ\text{C}$) and Tiivistelmä — right.
- Recomputed: $s = 334\,\text{kJ} \approx c\cdot80\,\text{K}$; sauna $67/452\,\text{kJ}$; example $41\,900\,\text{J}$, $33{,}6\,\text{W}$, $8{,}69\cdot10^3\,\text{s} = 2{,}4\,\text{h}$, without drinks $2{,}8\,\text{h}$, $19\,\text{K/h}$ afterwards; mixing $126\,\text{kJ} < 334\,\text{kJ}$; virhe $63\,\text{kJ}$, $0{,}19\,\text{kg}$; siirto $64{,}9\,\text{s}$ (mistakes $8{,}4$, $56{,}5$); check-2 $213 \to 210\,\text{kJ}$; pred-2 $2{,}9\,\text{h}$; exit $175{,}5\,\text{kJ}$. All agree with lesson-answers.py.
- Coolant $P = c\,(m/t)\,\Delta T$, glycol $c \approx 3500$ — right.
- Each choice has exactly one correct option with right feedback.
- Hash same at start and end.
