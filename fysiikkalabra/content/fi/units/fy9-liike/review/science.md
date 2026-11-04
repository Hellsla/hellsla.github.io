VERDICT: PASS
CONTENT-HASH: d1021d5831c47cfe

Round 2 (delta review of round 1 fixes; round 1 hash 365135079757531a). Science review of fy9-liike.

## Round 1 Blocking findings, verified
1. **s6 geometry.** Fixed. The task text now reads "Mitta oli jalustalla $3{,}00\,\text{m}$:n päässä kamerasta, ja pallo putosi $0{,}30\,\text{m}$ mitan takana, $3{,}30\,\text{m}$:n päässä kamerasta." The ball is farther than the scale, so its apparent distances are too small by the factor $3{,}00 : 3{,}30$. That matches the data ($a = 8{,}88$), the correction factor $1{,}10$ and the result $9{,}77\,\text{m/s}^2$. Solutions c (Annettu, Periaate) and the c criterion say "metrimitan tasossa". The word "seinä" no longer appears anywhere in the sources or the preview. The frame-rate sentence "joka kolmannesta kuvasta eli $0{,}05\,\text{s}$:n välein" agrees with $60$ kuvaa sekunnissa and with "Taulukossa on joka toinen piste" ($0{,}10\,\text{s}$ steps).
2. **s2 source_note.** Fixed. It now says only "Ilmanvastus jätetään huomiotta."

## Round 1 Polish, verified
3. s1 d says "tasaisesti koko kaistan matkan", and the model answer and the 2 p criterion use that model. 4. unit.md "Kaksi kappaletta" adds "ja kiihtyy". 5. s4 says "suoralle tieosuudelle". 6. The `kuvaajat` tangent is velocity blue.

## Recomputed (one Python call, my own formulas)
- s1: $t = 12{,}0\,\text{s}$, $a = 1{,}25\,\text{m/s}^2$, smallest gap $17{,}5\,\text{m}$ at $6{,}0\,\text{s}$. New s1 d step: $t = 540 : 35 = 15{,}4\,\text{s}$, gain $(22{,}5 - 17{,}5) \cdot 15{,}4 \approx 77\,\text{m} > 40\,\text{m}$, truck at $307\,\text{m}$. All correct.
- s2: $8{,}84\,\text{m}$, $0{,}625\,\text{s}$, $7{,}08\,\text{m}$, $5{,}87$ and $-6{,}13\,\text{m/s}$, Moon $8{,}68\,\text{m}$. New teacher.md extension: the area between the parallel $(t,v)$ lines is $12{,}0 \cdot 0{,}625 = 7{,}5\,\text{m}$, which is the initial separation. Correct.
- s3: fit $k = -2{,}31\,\text{(km/h)/s} = -0{,}642\,\text{m/s}^2$, braking $9{,}8$–$48{,}8\,\text{s}$, $486\,\text{m}$, inside the tolerance of $481\,\text{m} \pm 7\,\%$.
- s4: $81{,}8\,\text{km/h}$, $0{,}59$ and $17{,}8\,\text{km/h}$. s6: $8{,}88 \to 9{,}77\,\text{m/s}^2$, two-point $8{,}92\,\text{m/s}^2$.
- Short items: Tutki $450\,\text{m}$, hirvi $46{,}77\,\text{m}$, koira $8{,}0\,\text{s}$, pesäpallo $-1{,}81\,\text{m/s}$, keskivauhti $30\,\text{km/h}$, hissi $16{,}0\,\text{m}$.
- The new `keskinopeus` options are physically right: the correct option gives $20\,\text{km} : \tfrac{2}{3}\,\text{h}$, and the "keskinopeus on nolla" distractor's feedback correctly separates keskinopeus from keskivauhti.

## New problems from the fixes
None found.

## Polish (not blocking)
- The shared fy4-2 figures are unchanged (see visual.md).

## Checks run
`build.py fy9-liike` OK. `practice.py check` OK (6 tasks, 95 p). `check_layout` OK. In the preview at 390 and 1280: no `.katex-error`, no raw `$`, and no console errors.
