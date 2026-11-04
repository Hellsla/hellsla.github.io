VERDICT: FAIL
CONTENT-HASH: 219c197fec2ce7b3

## Blocking
- solutions.md fy4-3-L3-04, the new ```voimakuvio two-body spec — the model diagram is drawn wrongly. The two bodies are 480 N against 30 N, so fbdspec.py scales the arrows up (small force at least 44 px, up to 300 px) and the long arrows run out of their half of the figure: the horse's T (pointing left) is drawn across the cart and ends inside it, so the cart looks to have T pointing backwards (the text says forwards), the cart's forward T and the horse's F_t are cut off or unlabelled, and the label of F_v (rolling resistance) is not visible. A student who compares text and picture would learn a wrong diagram, the exact error the chapter teaches against. Fix: write two separate ```voimakuvio blocks, one per body (cart: pinta 0 / T 450 oikea / F_v 410 vasen / F_k 40 vasen / a 0; horse: pinta 0 / F_t 480 oikea kitka / T 450 vasen / F_h 30 vasen / a 0), each on its own scale, with a sentence before each saying which body it is; check the captures after the rebuild.

## Polish
- solutions.md L1-08 Periaate — "Valitaan kappaleeksi lapsi, joka piirretään suorakulmiona" now announces a drawing that never comes (no Voimakuvio step); say instead "Lapsen kuvioon kuuluisi vain köyden voima…" or keep it as a thought step. Wording only, not blocking.

## Checked
- L1-08: the sentence moved into Periaate unchanged in meaning; no equation of motion is written, so no Voimakuvio step is needed; numbers and answer untouched.
- Opened the L3-04 capture at 1280 px (fi, en, fi-easy): same defect in all three; the capture of L1-08 is text only.
- Solution order in L3-04 stays principle, diagram text, diagram, formula; forces and numbers unchanged (450 N, 480 N).
- Hash unchanged at the end of the review.
