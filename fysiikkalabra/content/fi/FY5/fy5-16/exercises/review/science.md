VERDICT: FAIL
CONTENT-HASH: 21a7e8ebe0232319

## Blocking
- content/fi/FY5/fy5-16/exercises/solutions.md:295 (L2-10, Vastaus c) — B (a condition missing) and an internal contradiction: "Taso 94 dB on 7 dB raja-arvon 87 dB(A) yläpuolella, joten kuulonsuojainten on vaimennettava vähintään sen verran". The limit value and the action values are 8-hour daily exposure levels. This holds only if 94 dB lasts the whole 8-hour day, and the same answer then shows that 1,0 h at 94 dB gives the same dose as 8 h at 85 dB, which is below 87 dB(A). — Add the condition ("jos altistus kestää koko kahdeksan tunnin työpäivän"). Also say that for a shorter exposure the 8-hour equivalent level is what is compared. The task's question in c) can get the same words.
- content/fi/FY5/fy5-16/exercises/solutions.md:296 (L2-10, Järkevyys) — A (a claim about the source with no basis): "iskumelua, jossa aineiston mukaan yksikin riittävän voimakas huippu voi olla vaarallinen". The fetched page only names impulsive noise and the peak values 135/137/140 dB(C). It does not say this. — Write "Malli ei kata iskumelua, jolle aineistossa on omat huippuarvonsa (dB(C))", or delete "aineiston mukaan".

## Polish
- solutions.md:295 (c) — "alueet merkittävä" at 85 dB: the page mentions warning signs but does not tie them to the upper action value in the notes. Check this or say it without "aineiston mukaan".
- solutions.md:295 (d) — "tiedottamisen" as the obligation at 80 dB(A) is not in the source notes (only "alempi toiminta-arvo"). Write "työnantajan ensimmäiset velvoitteet".

## Checked
- The hash was the same at the start and at the end. I judged only the added exercise L2-10.
- Recomputed: 10^0,3 = 1,995 and 10^1 = 10. 10^0,9 = 7,943, so t₂ = 8 h/7,943 = 1,007 h, which is 1,0 h (tolerance 3 %). The 3-dB rule gives 1 h exactly, and the solution explains the difference.
- The dose model I₁t₁ = I₂t₂ follows from "energia-annos … kahdeksan tunnin laskennalliselle työpäivälle", which the page says. The solution does not claim that the page states the 3-dB rule or a time for 94 dB.
- The source values (80, 85, 87 dB(A); the limit assessed with protectors; protectors compulsory and a noise-control programme at 85) agree with the fetched notes.
- In a), the level is proportional to lg I, and 10¹² fits into 0–120 dB. In d), the claim is refuted with numbers. "1 dB ≈ +26 %" is right.
- The time is called a reference value and not a safe time, as the guardrails and the brief require.
