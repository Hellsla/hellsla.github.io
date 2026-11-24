VERDICT: PASS
CONTENT-HASH: 143de208888628e3
SCOPE: delta caption-label,md-paragraphs,numbers,paragraphs,reflow,teacher-figure,typography from 52fabbb87f61e010 base 98218de
Delta (queue 8g): nine solutions now give the Kaava step as aligned rows that start from the basic equations ($W = qEd = qU$, $F = qE$, $F = G$, $\Sigma F = ma$, $\Sigma \overline{F} = \overline{0}$). Several solution paragraphs were split with the words unchanged, captions lost their marker, and the four teacher-approved pick figures were re-rendered. No data, substitution or answer changed.

## Blocking
- none

## Polish
- solutions.md:106 (L2 levitating drop, $U_2$) and :213 (L3-04), Kaava: the first row $F = G$ compares the electric force with the weight. The lesson writes the weight as $mg$ and never names it $G$; the Periaate states "sähköinen voima ja paino ovat yhtä suuret". Fix (optional): either open with $qE = mg$ directly, or keep $F = G$ and write "paino $G = mg$" in the Periaate.
- solutions.md:215 (L3-04): $e \approx S : N$ now stands as a loose paragraph after the Kaava block, before Muunnokset. Fix: join it to the Kaava line, or move it into Sijoitus b).

## Checked
- Every new Kaava chain is algebraically right and ends in the formula that its unchanged substitution uses: $E = U : d$; $F = qU : d$; $U = Fd : q$; $F : G = qU : (mgd)$; $F_2 = F_1 d_1 : d_2$; $U_2 = U_1 q_1 : q_2$; $v = \sqrt{2eU : m}$; $q = mg\tan\alpha : E$; $q = mgd : U$.
- Electron task: $\Sigma F = ma$ with $eE$ as the only force matches the Periaate, which says the plates are in a vacuum and the weight is negligible.
- Hanging ball: $T\sin\alpha = qE$ and $T\cos\alpha = mg$ come from $\Sigma \overline{F} = \overline{0}$, a correct force balance.
- One script recomputed the substitutions: 15 000 V/m; 2,0 mN; 15 kV; 20,4; 0,45 mN; 337,5 V; 4,19·10⁶ m/s; 23 nC. All agree with the solutions.
- L2-07, L2-08, L3-04 and L3-05: the paragraph splits leave every number and sentence unchanged, and the physics passed earlier still holds.
- Notation follows the lesson: $E = U : d$, $F = qE$, $a = qE : m$; vectors are written with an overline only in the vector balance.
- The pick figures were approved by the teacher, and the diff changed no number in them.
- Content hash checked at the start and the end.
