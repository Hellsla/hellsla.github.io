VERDICT: PASS
CONTENT-HASH: 37ee21db139040ce

Pedagogy review of the Selkeä suomi translation of fy9-voimat (NOTES.md §12) against the reviewed Finnish source.
The lesson structure, task counts (6 Ennusta, 1 Tutki, 8 Sovella, 3 Tarkista, 2 exit ticket, 6 long tasks, 95
points), skills, chapter links (named, never ids), rubrics and the 75-minute plan are the source's; no step,
criterion or hint is dropped (formula and number comparison of every string, check_i18n 0 errors).

**Selkeä suomi.** The language is clearly simpler and still natural: long clauses are split into short connected
sentences ("Kiekko hidastuu. Siksi kokonaisvoima osoittaa taaksepäin."), participle and -essa/-ttaessa forms are
opened ("kun pallo nousee", "ennen kuin kaappi alkaa liukua"), and difficult words are explained inside the sentence
the first time (kohdistuu eli osuu, mukautuu eli muuttuu, yläraja eli suurin mahdollinen arvo, supistuu eli häviää,
lomitse eli niiden välistä, tamppautunut eli tiiviiksi painettu, peilijää, vinssi, vaijeri, veneluiska, keula,
systeemi, diagnostinen testi). Physics terms (tukivoima, lepokitka, liikekitka, jännitysvoima, komponentti,
rajanopeus, verrannollinen) are kept. Instructions are explicit and ordered: the *Ydinajatus* method is now a
numbered 1–5 list, and the long-task intro says what to do in which order. The tone is adult and not padded.

**Key concepts.** `unit.json` has five: voimakuvio, voima ja vastavoima, tukivoima, lepokitka, rajanopeus — the
central ideas of the unit, all from the glossary candidates, each one or two plain sentences under 25 words, and
correct (lepokitka "vain niin suuri kuin tilanne vaatii, enintään $\mu_0 N$"; tukivoima "ei ole aina yhtä suuri
kuin paino"). They target exactly the misconceptions the Ennusta test diagnoses. Rendered after the opening with the
fixed lead and the *Vapaaehtoinen* tag, no note field (checked in the preview).

**Feedback and options.** Every misconception feedback still names the error and the right reasoning; answer
options were kept identical to the source where they were already plain, so option lengths stay balanced and no
option gives itself away by wording.

## Blocking
None.

## Polish
1. `inquiry.json` activities.11 choice 1 feedback: "Tämä kuvaa nopeuden kasvua väärin." (as in the source) is an
   unclear opening for an S2 reader — the option is about acceleration. Suggest: "Tämä vaihtoehto sekoittaa
   kiihtyvyyden ja nopeuden."
2. `sovella/tasks.json` fy9-voimat-s5 text: the quoted group report keeps the source's long sentences ("Luimme
   kulman kulmamittarista, jonka vieressä kuvasimme mittauksen puhelimella."). Keeping an authentic report voice is
   defensible, but one split ("Kuvasimme mittauksen puhelimella. Kulmamittari näkyi videossa.") would help without
   changing the task.
3. `unit.md` *Kaava: Paino, kitka ja rinne*: "Joskus pintaa vastaan kohtisuorassa vaikuttavat vain …" — "Joskus"
   reads as chance rather than a condition to check; see science review Polish 2.
4. `teacher.md` is fully translated and keeps every time slot and the 0,12 kg extension; fine as is.
