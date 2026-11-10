VERDICT: FAIL
CONTENT-HASH: f811235b68f65c28

## Blocking
- content/fi/FY6/fy6-15/lesson.md:408 — (B, 6 consistency) The theory still says "molemmat jalat ovat samassa potentiaalissa: jalkojen välillä ei ole jännitettä, eikä linnun kautta kulje virtaa". That is exact only for a resistance-free conductor. The revised prediction (inquiry.json:91–104) now says the potential difference is very small and only a very small current flows, and its correct feedback opens "Teoria tukee tätä", so theory and feedback now contradict each other. Luku *Kirchhoffin lait ja potentiaali virtapiirissä* also gives millivolts and a tiny current. — Fix: "jalat ovat samalla johtimella lähes samassa potentiaalissa: jalkojen välinen potentiaaliero on hyvin pieni, joten linnun kautta kulkee vain erittäin pieni virta", keeping the danger sentence.
- content/fi/FY6/fy6-15/lesson.md:570 — (B, 6) The misconception paragraph says the bird is safe "koska sen jalkojen välillä ei ole jännitettä". This is the same contradiction. — Fix: "koska sen jalkojen välinen potentiaaliero on hyvin pieni".

## Polish

## Checked
- inquiry.json Ennuste 2: exactly one correct option, and its physics is right. Feet a few cm apart on one conductor give a tiny potential difference (millivolts at hundreds of amperes), so the current through the bird is negligible. A wing touching another conductor or an earthed pole makes a large potential difference and a large current.
- The three distractors are still wrong, and their feedback is right:
  - Legs conduct.
  - Current splits between parallel paths; it does not take only the least-resistance path, and the bird carries a very small share.
  - Bare overhead conductors are insulated only by air.
- The four feedbacks agree with each other.
- The rest of the lesson is unchanged since the last PASS (a362da4bacf76398). No numbers changed in the diff.
- Hash identical at start and end.
