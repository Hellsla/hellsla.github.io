VERDICT: PASS
CONTENT-HASH: b81b215185d2bb31

## Blocking

## Polish
- solutions.md fy8-15-L1-10 Periaate — the earlier note still applies: "jokaisella rivillä on sama varaus" holds only for the generation rows. This is not part of this diff.

## Checked
- The hash was b81b215185d2bb31 at the start and the end. Scope: delta on solutions.md since the version I passed (commit 1f881c20d9).
- Two Kaava steps changed, in L1-04 and L2-03. Apart from blank lines, everything else is two Periaate paragraphs split in L3-01 and L3-02. A script collapsed whitespace and confirmed their text is unchanged. exercises.json and answers.py are unchanged.
- L1-04 now starts from energy conservation. $E_\text{alku} = 2m_ec^2$ and $E_\text{loppu} = 2E_\gamma$ give $E_\gamma = m_ec^2$. This is correct for a pair at rest, and Periaate's momentum argument justifies the two equal photons. The answer is $511{,}0\,\text{keV}$, unchanged.
- L2-03 now starts from $E = hf$ and $c = \lambda f$. The rows $f = c/\lambda$, $E = hc/\lambda$ and $\lambda = hc/E$ are correct. The phrase "$E = hf$ ja $c = \lambda f$, joten" names both basic laws, so the derivation is sound. Recomputed: $\lambda = 1{,}2133\,\text{pm}$, which matches answers.py, so $1{,}21\,\text{pm}$.
- Both steps end in the symbolic form substituted in Sijoitus. Notation is as in the brief.
