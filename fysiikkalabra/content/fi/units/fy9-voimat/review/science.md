VERDICT: FAIL
CONTENT-HASH: 187e87e7e825313c

Delta review: only the new `hints` in `sovella/tasks.json` (diff against origin/main; 150 lines, nothing else changed). Each hint was checked against its part's text, rubric, `sovella/solutions.md` and answer. Every number a hint relies on was recomputed with my own formulas (s1 b $1331\,\text{N}$, $\tan 14^\circ = 0{,}249 < 0{,}35$, $\alpha_0 = 19{,}3^\circ$; s2 $T_2 = 118{,}5\,\text{N}$, $T_1 = 296{,}2\,\text{N}$, ratio $0{,}40$; s3 $\mu = 0{,}0285$, $1/m' = 0{,}740\,\tfrac{1}{\text{kg}}$, intercept $0{,}38\,\text{N}$; s5 $\tan 22{,}5^\circ = 0{,}414$, $\tan 21^\circ$, $\tan 24^\circ$; s6 $10{,}09\,\text{m/s}$, $64{,}8\,\text{m}$; s7 $623\,\text{N}$, $48{,}3\,\text{m/s}$, $\sqrt{100/75}$; s8 $-1{,}143$ and $0{,}857\,\text{m/s}^2$, $12{,}23\,\text{m}$). They agree with the solutions.

## Blocking

1. **s3 d, hint 3 (A, an error).** "Laske $N$ vaunun massasta (b-kohta) ja jaa kitkavoimalla" says to divide $N$ by the friction force, which gives $N/F_\mu \approx 35$, the inverse of the coefficient. It contradicts hint 2, the task text and the solution ($\mu = F_\mu/N$). The en hint has it right ("divide the friction force by it"). Replacement: "Laske $N$ vaunun massasta (b-kohta) ja jaa kitkavoima sillä. Lisäpunnuksen jälkeen massa on $m + 0{,}500\,\text{kg}$: laske uusi $\tfrac{1}{m'}$ ja uusi leikkauskohta $\mu m' g$ ja vertaa vanhoihin."

## Polish

2. **s4 c, hint 2.** Hint 1 asks which bodies interact with the car, but hint 2 names only the road and the air. The weight, from the Earth, is left out, while the solution's Periaate lists it first. Replacement start: "Maa antaa painon; tie antaa tukivoiman, lepokitkan vetäviin pyöriin ja vierimisvastuksen; ilma antaa ilmanvastuksen. …"
3. **s6 c, hint 3.** "ilmanvastus pysyy suunnilleen samana" is a bit stronger than the solution, which says the father's air resistance is "vähän suurempi". Suggest: "…kun massa kasvaa paljon mutta ilmanvastus vain vähän?"

## Checked
- Same model, symbols and sign conventions as the solutions: $x$ up the ramp (s1), $\Sigma F = m a$ per sledge with the light rope (s2), $F - F_\mu = ma$ with the F-axis intercept (s3), lepokitka at most $\mu_0 N$ as the external driving force (s4), $\mu_0 = \tan\alpha_0$ with measurement 5 treated with a reason (s5), down positive $mg - F_\text{v} = ma$ and $v_\text{r}$ (s7), up positive $N - mg = ma$ (s8).
- Friction terms follow the house rule (liukukitka, lepokitka). No "lämmöksi".
- The two equal rope-2 forces (s2 a) are attributed to the light rope and not called a third-law pair: correct.
- No hint states a final answer. Hint 3 always leaves the substitution or the conclusion to the student. s2 d and s7 d give the ratio to compute, not its value.
- Numbers with units are LaTeX with decimal commas.
- Hashes are the same at the start and the end.
