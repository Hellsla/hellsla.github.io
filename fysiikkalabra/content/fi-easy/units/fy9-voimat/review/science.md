VERDICT: FAIL
CONTENT-HASH: 7d9f47e38af3bb24

Delta review: only the new `hints` in `sovella/tasks.json` (diff against origin/main). I checked each hint against the part, its rubric, `sovella/solutions.md`, the answer and the Finnish hints. The numbers were recomputed in one script (same values as in the fi report: s1 $1331\,\text{N}$ and $19{,}3^\circ$; s2 $118{,}5\,\text{N}$, $296{,}2\,\text{N}$ and $0{,}40$; s3 $\mu = 0{,}0285$; s5 $0{,}414$; s6 $10{,}09\,\text{m/s}$ and $64{,}8\,\text{m}$; s7 $623\,\text{N}$ and $48{,}3\,\text{m/s}$; s8 $-1{,}143\,\text{m/s}^2$, $0{,}857\,\text{m/s}^2$ and $12{,}23\,\text{m}$). They agree with the solutions. The physics is the same as in fi: each sentence was split, and nothing was dropped.

## Blocking

1. **s3 d, hint 3 (A, an error).** "Laske $N$ vaunun massasta (b-kohta) ja jaa kitkavoimalla" divides $N$ by the friction force ($N/F_\mu \approx 35$). This is the inverse of $\mu = F_\mu/N$ in hint 2, the task and the solution. The fi hint has the same error; en is right. Replacement: "Laske $N$ vaunun massasta (b-kohta). Jaa kitkavoima tällä tukivoimalla. Lisäpunnuksen jälkeen massa on $m + 0{,}500\,\text{kg}$. Laske uusi $\tfrac{1}{m'}$ ja uusi leikkauskohta $\mu m' g$. Vertaa vanhoihin."

## Polish

2. **s4 c, hint 2.** The weight (from the Earth) is missing from the list of the bodies that act on the car. The solution names it first. Start: "Maa antaa painon. Tie antaa tukivoiman, …"
3. **s6 c, hint 3.** "ilmanvastus pysyy suunnilleen samana": the solution says the father's air resistance is a little larger. Suggest: "…kun massa kasvaa paljon mutta ilmanvastus vain vähän?"
4. **s1 a, hint 3; s1 b, hint 2.** In fi the word is "komponentti" and here it is "painon osa". That is acceptable. Saying once "painon osa eli komponentti" would tie the hint to the term the solution uses.

## Checked
- Models, symbols ($T$, $T_1$, $T_2$, $F_\mu$, $F_\text{v}$, $v_\text{r}$, $k$) and sign conventions (down positive in s7, up positive in s8) are the same as in the solutions.
- Lepokitka is described as "enintään $\mu_0 N$", following the house rule.
- No hint gives a final answer.
- Numbers with units are LaTeX with decimal commas.
- Hashes are the same at the start and the end.
