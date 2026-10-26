'use strict';
(() => {
  const fi = {
    'The agent office · Fysiikkalabra':'Agenttitoimisto · Fysiikkalabra',
    'HASH UNAVAILABLE':'TIIVISTETTÄ EI OLE','STALE':'VANHENTUNUT','INVALID':'VIRHEELLINEN',
    "A pixel office replay of Fysiikkalabra's recorded development history.":'Pikselitoimisto havainnollistaa Fysiikkalabran tallennettua kehityshistoriaa.',
    'An illustrated office with development, review, publication and coffee rooms.':'Havainnollistettu toimisto, jossa on kehitys-, tarkistus-, julkaisu- ja kahvihuoneet.',
    'Speech bubbles':'Puhekuplat','Office controls':'Toimiston painikkeet',
    'A little window into the work':'Pieni ikkuna työn kulisseihin',
    'LESSON WALKTHROUGH':'OPPITUNNIN MATKA','DAY HISTORY':'PÄIVÄN HISTORIA',
    'About this office':'Tietoa toimistosta','Office only':'Vain toimisto','Show controls':'Näytä painikkeet',
    'Switch between Finnish and English':'Vaihda suomen ja englannin välillä',
    'BEHIND THE LESSONS':'OPPITUNTIEN KULISSEISSA','Every lesson has a journey.':'Jokaisella oppitunnilla on matkansa.',
    'Follow the people, the checks and the decisions behind the classroom.':'Seuraa ihmisiä, tarkistuksia ja päätöksiä oppituntien taustalla.',
    'A DAY IN THE OFFICE':'PÄIVÄ TOIMISTOSSA','Choose a recorded day':'Valitse tallennettu päivä',
    'Office replay':'Toimiston tapahtumat','THE AGENT OFFICE':'AGENTTITOIMISTO',
    'Play':'Toista','Pause':'Tauko','Next handoff':'Seuraava luovutus','Next commit':'Seuraava commit',
    'Step through the illustrated lesson journey':'Etene oppitunnin havainnollistetulla matkalla',
    'Jump to next recorded commit':'Siirry seuraavaan tallennettuun commitiin',
    'Playback mode':'Toistotapa','Lesson journey':'Oppitunnin matka','Day history':'Päivän historia',
    'Speed':'Nopeus','Playback speed':'Toistonopeus','Office zoom':'Toimiston zoomaus','Still scene':'Pysäytä liike',
    'Toggle full screen':'Vaihda koko näytön tilaan','Exit full screen':'Poistu koko näytöstä','Enter full screen':'Siirry koko näyttöön',
    'Full screen':'Koko näyttö','Unavailable':'Ei käytettävissä',
    'Play lesson journey':'Toista oppitunnin matka','Pause lesson journey':'Keskeytä oppitunnin matka',
    'Play day history':'Toista päivän historia','Pause day history':'Keskeytä päivän historia',
    'Follow a lesson':'Seuraa oppituntia','Choose a lesson to follow':'Valitse seurattava oppitunti',
    'Follow recorded activity':'Seuraa tallennettuja tapahtumia',
    'BRIEF · DEVELOP · CHECK · REVIEW · DECIDE':'TOIMEKSIANTO · KEHITYS · TESTIT · ARVIOINTI · PÄÄTÖS',
    'WORKFLOW MODEL · RECORDED REVIEW EVIDENCE':'TYÖNKULUN HAVAINNOLLISTUS · TALLENNETUT TARKISTUKSET',
    'DAY TIMELINE':'PÄIVÄN AIKAJANA','Scrub to explore':'Tutki liukusäätimellä','Replay time':'Toistoaika',
    'Choose a lesson to follow its journey.':'Valitse oppitunti ja seuraa sen matkaa.',
    'Inspect an office role':'Tutustu toimiston rooliin','RECORDED SNAPSHOT':'TALLENNETTU TILANNE',
    'Evidence for this lesson version':'Tämän oppituntiversion tarkistukset',
    'Choose an event to inspect its lesson.':'Valitse tapahtuma nähdäksesi oppitunnin.',
    'Lesson workflow':'Oppitunnin työnkulku','1. Develop':'1. Kehitä','Text, exercises & simulation':'Teksti, tehtävät ja simulaatio',
    '2. Run checks':'2. Aja testit','No results observed':'Tuloksia ei havaittu',
    '3. Independent reviews':'3. Riippumattomat arviot','Science and pedagogy, in parallel':'Fysiikka ja pedagogiikka rinnakkain',
    '4. Review gate':'4. Tarkistusportti','Both PASS on the same version':'Molemmilta PASS samalle versiolle',
    '5. Teacher & publication':'5. Opettaja ja julkaisu','Merge decision, then deployment':'Yhdistämispäätös, sitten julkaisu',
    'Science reviewer':'Fysiikan tarkistaja','Pedagogy reviewer':'Pedagogiikan tarkistaja','Not observed':'Ei havaittu',
    'No lesson snapshot selected.':'Oppitunnin tilannetta ei ole valittu.',
    'What is actually recorded?':'Mitä on oikeasti tallennettu?',
    'Checks are saved reports without a content hash; their freshness and CI result are not established. A merge records integration, not the identity of the approving person or a successful deployment.':'Testiraporteissa ei ole sisältötiivistettä, joten niiden ajantasaisuutta tai CI-tulosta ei ole varmistettu. Yhdistäminen kertoo muutosten liittämisestä, ei hyväksyjän henkilöllisyydestä tai onnistuneesta julkaisusta.',
    'People carrying lesson packets illustrate the workflow. Review badges come from files in the selected commit; they are not live agent messages.':'Oppituntipaketteja kantavat hahmot havainnollistavat työnkulkua. Tarkistustiedot tulevat valitun commitin tiedostoista, eivät reaaliaikaisista agenttiviesteistä.',
    'Based on committed Git history. Desk activity is inferred from changed files; the animation is illustrative, not live agent monitoring.':'Perustuu Git-historiaan. Työpisteiden toiminta päätellään muuttuneista tiedostoista. Animaatio havainnollistaa työnkulkua, ei seuraa agentteja reaaliajassa.',
    'ON THIS DAY':'TÄNÄ PÄIVÄNÄ','Small steps. Better lessons.':'Pieniä askelia. Parempia oppitunteja.',
    'commits recorded':'tallennettua commitia','lesson changes':'oppituntimuutosta','science review changes':'fysiikan arvion muutosta','pedagogy review changes':'pedagogiikan arvion muutosta',
    'Counts cover the selected day, including events ahead of the replay clock. Review changes do not imply a pass.':'Luvut kattavat koko valitun päivän, myös toistokellon edellä olevat tapahtumat. Arvion muuttuminen ei tarkoita hyväksyntää.',
    'At this moment':'Juuri nyt','REPLAY':'TOISTO','The office is quiet.':'Toimistossa on hiljaista.',
    "The day's story":'Päivän tapahtumat','Choose a commit to jump to that moment.':'Siirry hetkeen valitsemalla commit.',
    'No recorded events for this day.':'Tältä päivältä ei ole tallennettuja tapahtumia.',
    'Made of curiosity, careful checks & a little pixel dust.':'Uteliaisuutta, tarkkoja tarkistuksia ja ripaus pikselipölyä.',
    'Close role details':'Sulje roolin tiedot','Close about dialog':'Sulje toimiston tiedot','Close':'Sulje',
    'A READ-ONLY WINDOW':'IKKUNA TYÖNKULKUUN','A team, in miniature.':'Tiimi pienoiskoossa.',
    "This office represents Fysiikkalabra's developer and its independent science and pedagogy reviewers. Their roles come from the repository's existing agent definitions.":'Toimisto kuvaa Fysiikkalabran kehittäjää ja riippumattomia fysiikan ja pedagogiikan tarkistajia. Roolit perustuvat projektin nykyisiin agenttimäärittelyihin.',
    "The replay uses the latest 200 reachable commits, including branch commits so separate review rounds are visible. Times are commit times in Europe/Helsinki. Each lesson panel describes that commit's own snapshot; a later timestamp on a different branch does not necessarily supersede an earlier version.":'Toisto käyttää 200 uusinta saatavilla olevaa commitia, myös haarojen committeja, jotta erilliset tarkistuskierrokset näkyvät. Ajat ovat commitien aikoja Suomen aikavyöhykkeellä. Jokainen tilanne kuuluu omaan commitiinsa; myöhempi aika toisessa haarassa ei välttämättä korvaa aiempaa versiota.',
    "A lesson goes to independent science and pedagogy review. Both must say PASS with the current content hash to clear the review gate. A content edit invalidates earlier approvals, and a FAIL returns the work for revision. Automated checks and the teacher's merge decision are separate requirements; this office does not infer successful CI or deployment from commits. A current legacy marker is a grandfathered prototype exception, not a cleared two-review gate.":'Oppitunnin fysiikka ja pedagogiikka arvioidaan riippumattomasti. Molempien on annettava PASS nykyiselle sisältötiivisteelle. Sisältömuutos vanhentaa aiemmat hyväksynnät, ja FAIL palauttaa työn korjattavaksi. Automaattiset testit ja opettajan yhdistämispäätös ovat erillisiä vaatimuksia. Commit ei yksin todista onnistunutta CI-ajoa tai julkaisua. Voimassa oleva legacy-merkintä on aiemman prototyypin poikkeus, ei kahden tarkistuksen hyväksyntä.',
    'The office does not run agents, inspect private session transcripts, edit lessons, trigger reviews, or publish anything. Office colleagues and carried lesson packets explain the workflow, not actual timed transfers between people.':'Toimisto ei käynnistä agentteja, lue yksityisiä istuntoja, muokkaa oppitunteja, käynnistä arviointeja eikä julkaise mitään. Hahmot ja niiden kantamat paketit havainnollistavat työnkulkua, eivät ihmisten todellisia liikkeitä.',
    "Inspired by Fysiklabbet's agent office. This implementation uses its own drawing and scripts, without the original site's analytics or dependencies.":'Innoittajana on Fysiklabbetin agenttitoimisto. Piirrokset ja ohjelmakoodi ovat omia; alkuperäisen sivun analytiikkaa tai riippuvuuksia ei käytetä.',
    'Speech and coffee breaks are playful workflow illustrations, not quotations or recorded agent activity. Commit messages and lesson titles stay in their original language.':'Puhekuplat ja kahvitauot ovat leikillisiä havainnollistuksia, eivät lainauksia tai tallennettuja agenttitapahtumia. Commitviestit ja oppituntien nimet näytetään alkuperäisellä kielellään.',
    'Enable JavaScript to explore the office replay. Your lessons and simulations are unaffected.':'Ota JavaScript käyttöön tutkiaksesi toimistoa. Oppitunteihin ja simulaatioihin ei tehdä muutoksia.',
    'Developer':'Kehittäjä','Teacher':'Opettaja','Review coordinator':'Tarkistuskoordinaattori','Publication decision':'Julkaisupäätös','Automatic checks':'Automaattiset testit','Website courier':'Verkkokuriiri','Coffee lounge':'Kahvihuone',
    'THE MAKER':'TEKIJÄ','THE PHYSICS CHECK':'FYSIIKAN TARKISTUS','THE LEARNER’S VIEW':'OPISKELIJAN NÄKÖKULMA','THE HUMAN DECISION':'IHMISEN PÄÄTÖS','THE REVIEW DESK':'TARKISTUSPÖYTÄ','THE HUMAN COORDINATOR':'OPETTAJAN ROOLI','THE CHECK RUNNER':'TESTIEN AJAJA','AFTER THE PUBLICATION DECISION':'JULKAISUPÄÄTÖKSEN JÄLKEEN','A WELL-EARNED PAUSE':'PIENI HENGÄHDYSTAUKO',
    'Git history · not an agent definition':'Git-historia · ei erillinen agenttimäärittely','Human role · not an additional AI agent':'Ihmisen rooli · ei uusi tekoälyagentti','Illustrated break · no real agent is paused':'Havainnollistettu tauko · oikeita agentteja ei pysäytetä',
    'PASS · current version':'PASS · nykyinen versio','FAIL · revision needed':'FAIL · korjattava','STALE · content changed':'VANHENTUNUT · sisältö muuttui','Waiting for review':'Odottaa tarkistusta','Invalid report · blocked':'Virheellinen raportti · estetty',
    'Report: {hash} · no longer matches':'Raportti: {hash} · ei enää vastaa versiota','Report: {hash}':'Raportti: {hash}',
    'No valid matching report in this snapshot.':'Tässä tilanteessa ei ole kelvollista nykyistä raporttia.',
    '{n} saved failures · freshness unknown':'{n} tallennettua hylkäystä · ajantasaisuus ei tiedossa','{n} saved passes · freshness unknown':'{n} tallennettua hyväksyntää · ajantasaisuus ei tiedossa',
    'No check results observed':'Testituloksia ei havaittu','No lesson selected':'Oppituntia ei ole valittu',
    'OPEN · both PASS on current hash':'AVOIN · molemmilta PASS nykyiselle versiolle','CLOSED · both current approvals required':'SULJETTU · molemmat nykyiset hyväksynnät tarvitaan',
    'Select an event or a different lesson to inspect the gate.':'Valitse tapahtuma tai toinen oppitunti tutkiaksesi hyväksyntää.',
    'Review gate cleared. Automated checks and the teacher’s publication decision remain separate.':'Tarkistusvaatimus täyttyy. Automaattiset testit ja opettajan julkaisupäätös ovat erillisiä.',
    'Return to developer: a reviewer found a blocking issue. Fix it, run checks and request independent review again.':'Palautus kehittäjälle: tarkistaja löysi estävän puutteen. Korjaa työ, aja testit ja pyydä uudet riippumattomat arviot.',
    'Return to review: the lesson changed after approval. Earlier PASS reports cannot open this gate.':'Uusi tarkistus tarvitaan: oppitunti muuttui hyväksynnän jälkeen. Aiemmat PASS-raportit eivät enää riitä.',
    'Waiting for both independent reviewers. A missing or invalid approval keeps the gate closed.':'Odotetaan molempia riippumattomia arvioita. Puuttuva tai virheellinen hyväksyntä estää etenemisen.',
    'No commit at the current replay time.':'Nykyisellä toistohetkellä ei ole commitia.',
    'Lesson content hash: {hash}.':'Oppitunnin sisältötiiviste: {hash}.',
    'Commit {sha} · {time}. {detail}This is the selected commit’s snapshot, including its branch context.':'Commit {sha} · {time}. {detail}Tämä on valitun commitin tilanne omassa haarassaan.',
    'Lesson packet: {files}. Reviewers return separate reports; they do not take ownership of or edit the lesson.':'Oppituntipaketti: {files}. Tarkistajat palauttavat erilliset raportit; he eivät ota oppituntia haltuunsa eivätkä muokkaa sitä.',
    'This lesson has an HTML page in this commit’s site/ snapshot. That does not establish a fresh build or successful deployment.':'Oppitunnilla on HTML-sivu tämän commitin site/-hakemistossa. Se ei todista tuoretta rakennusta tai onnistunutta julkaisua.',
    'This lesson has no HTML page in this commit’s site/ snapshot.':'Oppitunnilla ei ole HTML-sivua tämän commitin site/-hakemistossa.',
    'A current legacy marker allows the earlier prototype exception; it does not clear the two-review gate.':'Voimassa oleva legacy-merkintä sallii aiemman prototyypin poikkeuksen; se ei täytä kahden tarkistuksen vaatimusta.',
    'No lesson snapshot at this point in the recorded history.':'Tässä historian kohdassa ei ole oppitunnin tilannetta.',
    '{id}: science {science}; pedagogy {pedagogy}. Recorded review eligibility {eligibility}.':'{id}: fysiikka {science}; pedagogiikka {pedagogy}. Tallennettu tarkistuskelpoisuus: {eligibility}.',
    'cleared':'kunnossa','blocked':'estetty','stale':'vanhentunut','missing':'puuttuu','invalid':'virheellinen',
    'The walkthrough desk separately waits for both report deliveries. Passing review clears only the review requirement; automated checks and the teacher’s publication decision are separate.':'Havainnollistuksessa pöytä odottaa molempien raporttien saapumista. Hyväksytyt arviot täyttävät vain tarkistusvaatimuksen; automaattiset testit ja opettajan julkaisupäätös ovat erillisiä.',
    'Room activity comes from recorded file changes. Couriers and handoffs illustrate the workflow; they are not records of running agents, actual conversations or human approvals.':'Huoneiden toiminta perustuu tallennettuihin tiedostomuutoksiin. Kuriirit ja luovutukset havainnollistavat työnkulkua, eivät käynnissä olevia agentteja, todellisia keskusteluja tai ihmisten hyväksyntöjä.',
    'The office is quiet between recorded changes.':'Toimistossa on hiljaista tallennettujen muutosten välillä.',
    '{roles} — changes recorded near {time}.':'{roles} — muutoksia tallennettu noin klo {time}.',
    '{sha} · {n} changed files · {roles}':'{sha} · {n} muuttunutta tiedostoa · {roles}',
    '{n} commits':'{n} committia','Git history · {n} commits · Europe/Helsinki':'Git-historia · {n} committia · Suomen aika',
    'Repository changes':'Muut projektimuutokset','No history available':'Historiaa ei ole saatavilla','{time} Helsinki time':'{time} Suomen aikaa',
    'Workflow illustration: {caption}':'Työnkulun havainnollistus: {caption}',
    'DEVELOPMENT WORKSHOP':'KEHITYSPAJA','Text · exercises · simulations':'Teksti · tehtävät · simulaatiot',
    'SCIENCE REVIEW':'FYSIIKAN TARKISTUS','Independent physics & mathematics':'Riippumaton fysiikan ja matematiikan arvio',
    'PEDAGOGY REVIEW':'PEDAGOGINEN TARKISTUS','Independent learning & usability':'Riippumaton oppimisen ja käytettävyyden arvio',
    'THE TEACHER':'OPETTAJA','A question worth exploring':'Tutkimisen arvoinen kysymys',
    'AUTOMATIC CHECKS':'AUTOMAATTISET TESTIT','Build · tests · layout':'Rakennus · testit · ulkoasu',
    'PUBLICATION DECISION':'JULKAISUPÄÄTÖS','The teacher decides':'Opettaja päättää','THE WEBSITE':'VERKKOSIVUSTO','A separate deployment':'Erillinen julkaisu',
    'TEACHER':'OPETTAJA','DEVELOPER':'KEHITTÄJÄ','SCIENCE':'FYSIIKKA','PEDAGOGY':'PEDAGOGIIKKA','COORDINATOR':'KOORDINAATTORI','WEB COURIER':'VERKKOKURIIRI',
    'BRIEF':'TOIMEKSIANTO','LESSON':'OPPITUNTI','COPY':'KOPIO','REPORT':'RAPORTTI','REVIEWED':'TARKISTETTU','REVISE':'KORJATTAVA','APPROVED':'HYVÄKSYTTY','WAITING':'ODOTTAA','READY':'VALMIS',
    'PASS REPORT':'PASS-RAPORTTI','FAIL REPORT':'FAIL-RAPORTTI','STALE REPORT':'VANHENTUNUT RAPORTTI','INVALID REPORT':'VIRHEELLINEN RAPORTTI',
    'COLLECTING COPY':'HAKEE KOPIOTA','RETURNING TO DESK':'PALAA TYÖPÖYDÄLLE','DELIVERING REPORT':'VIE RAPORTTIA','WAITING FOR COPY':'ODOTTAA KOPIOTA','REPORT NOT RECORDED':'RAPORTTIA EI TALLENNETTU','REVIEWING COPY':'ARVIOI OPPITUNTIA','REPORT DELIVERED':'RAPORTTI TOIMITETTU',
    'CHECK RUNNER':'TESTIEN AJAJA','BUILD':'RAKENNUS','SIM TESTS':'SIMULAATIOTESTIT','LAYOUT':'ULKOASU',
    '{n} SAVED FAILURES':'{n} TALLENNETTUA HYLKÄYSTÄ','{n} SAVED PASSES':'{n} TALLENNETTUA HYVÄKSYNTÄÄ','NO SAVED RESULTS':'EI TALLENNETTUJA TULOKSIA','Freshness / CI unknown':'Ajantasaisuus / CI ei tiedossa',
    'REVIEW DESK':'TARKISTUSPÖYTÄ','{n}/2 REPORTS':'{n}/2 RAPORTTIA','Recorded: {n}/2 PASS':'Tallennettu: {n}/2 PASS',
    'HTML IN COMMIT':'HTML COMMITISSA','NO HTML IN SNAPSHOT':'EI HTML-SIVUA','Deployment unverified':'Julkaisua ei varmistettu',
    '1 · DEVELOP':'1 · KEHITÄ','RECORDED {status}':'TALLENNETTU {status}','NO SNAPSHOT':'EI TILANNETIETOA','NO REPORT RECORDED':'RAPORTTIA EI OLE','WAITING FOR LESSON':'ODOTTAA OPPITUNTIA',
    'BRIEF & ASSIGN':'SUUNNITTELE JA ANNA TEHTÄVÄ','MERGE RECORDED':'YHDISTÄMINEN TALLENNETTU','DECISION UNKNOWN':'PÄÄTÖS EI TIEDOSSA','Approver unverified':'Hyväksyjää ei varmistettu',
    '2 · CHECK':'2 · TESTAA','3 · INDEPENDENT REVIEWS':'3 · RIIPPUMATTOMAT ARVIOT','5 · HUMAN DECISION':'5 · IHMISEN PÄÄTÖS','4 · MATCH BOTH APPROVALS':'4 · MOLEMMAT HYVÄKSYNNÄT',
    'ONE LESSON. TWO INDEPENDENT REVIEWS.':'YKSI OPPITUNTI. KAKSI RIIPPUMATONTA ARVIOTA.','SELECT A RECORDED LESSON':'VALITSE TALLENNETTU OPPITUNTI',
    'WORKFLOW ILLUSTRATION · COURIER MOVEMENT IS NOT A SESSION LOG':'TYÖNKULUN HAVAINNOLLISTUS · HAHMOJEN LIIKKEET EIVÄT OLE ISTUNTOLOKI',
    'Choose a recorded lesson to explore its route through the office.':'Valitse tallennettu oppitunti ja tutki sen matkaa toimistossa.',
    'The teacher brings a brief to the developer.':'Opettaja tuo toimeksiannon kehittäjälle.',
    'The developer brings the lesson packet to automatic checks.':'Kehittäjä tuo oppituntipaketin automaattisiin testeihin.',
    'The reviewers collect separate copies at different times and review independently, in parallel.':'Tarkistajat hakevat omat kopionsa eri aikaan ja arvioivat niitä riippumattomasti rinnakkain.',
    'A failed, stale or invalid review blocks approval. The lesson must return for revision or renewed review.':'Hylätty, vanhentunut tai virheellinen arvio estää hyväksynnän. Oppitunti palautetaan korjattavaksi tai uuteen arviointiin.',
    'Both independent reports have arrived and PASS the current version. The review desk is ready.':'Molemmat riippumattomat raportit ovat saapuneet ja antavat PASSin nykyiselle versiolle. Tarkistuspöytä on valmis.',
    '{role} report received. Waiting for {other} to finish independently.':'{role} raportti saapui. Odotetaan, että {other} saa oman työnsä valmiiksi.',
    'Science':'Fysiikan','Pedagogy':'Pedagogiikan','science':'fysiikan tarkistaja','pedagogy':'pedagogiikan tarkistaja','science and pedagogy':'fysiikan ja pedagogiikan tarkistajia',
    'No review reports are recorded for this version. The desk keeps waiting.':'Tälle versiolle ei ole tallennettu arvioita. Pöytä jatkaa odottamista.',
    'The reviewers work independently and return reports at different times.':'Tarkistajat työskentelevät itsenäisesti ja palauttavat raporttinsa eri aikaan.',
    'The review coordinator delivers the reviewed lesson to the publication decision-maker, then returns to the review desk.':'Koordinaattori vie tarkistetun oppitunnin julkaisupäätöksen tekijälle ja palaa tarkistuspöydälle.',
    'Approval is blocked. The developer takes a REVISE packet back to development.':'Hyväksyntä on estetty. Kehittäjä vie KORJATTAVA-paketin takaisin kehitykseen.',
    'Still waiting for {roles} review. Nothing proceeds to the publication desk.':'Odotetaan vielä: {roles}. Julkaisupöydälle ei toimiteta mitään.',
    'After fixing the work, the developer must rerun checks and request new reviews of the changed version.':'Korjausten jälkeen kehittäjän on ajettava testit uudelleen ja pyydettävä uudet arviot muuttuneesta versiosta.',
    'The review desk keeps waiting for {roles}. No publication handoff is made.':'Tarkistuspöytä odottaa edelleen: {roles}. Julkaisuun ei luovuteta mitään.',
    'The website courier comes to the publication desk to collect approved material.':'Verkkokuriiri saapuu julkaisupöydälle hakemaan hyväksyttyä aineistoa.',
    'Approval is recorded for this version. The website courier can collect the approved lesson.':'Tälle versiolle on tallennettu hyväksyntä. Verkkokuriiri voi noutaa hyväksytyn oppitunnin.',
    'The website courier waits: publication approval is not recorded for this version.':'Verkkokuriiri odottaa: tälle versiolle ei ole tallennettu julkaisuhyväksyntää.',
    'The website courier carries approved material to the website. Deployment itself remains unverified.':'Verkkokuriiri vie hyväksytyn aineiston sivustolle. Varsinaista julkaisua ei silti ole varmistettu.',
    'No publication approval is recorded. The website courier returns without collecting material.':'Julkaisuhyväksyntää ei ole tallennettu. Verkkokuriiri palaa ilman aineistoa.',
    'COFFEE LOUNGE':'KAHVIHUONE','COFFEE':'KAHVI','A little pause, not a skipped check.':'Pieni tauko, ei oikotietä tarkistuksiin.',
    'COFFEE BREAK':'KAHVITAUOLLA','TODAY’S LESSON':'PÄIVÄN OPPITUNTI',
    "Let's turn ‘why?’ into a lesson.":'Tehdään miksi-kysymyksestä oppitunti.',
    'It worked in my head. Now for the tests.':'Päässäni se toimi. Sitten testit.',
    'Coffee in. Bugs out.':'Kahvia sisään. Bugeja ulos.',
    'The universe would like one small correction.':'Maailmankaikkeus pyytää pientä korjausta.',
    'New version? My old PASS just expired.':'Uusi versio? Vanha PASS meni vanhaksi.',
    'SI units. Not vibes.':'SI-yksiköitä. Ei mututuntumaa.',
    'Would a student understand this before coffee?':'Ymmärtäisikö opiskelija tämän ennen kahvia?',
    'One PASS is not a quorum.':'Yksi PASS ei vielä riitä.',
    'Two matching passes. My favourite duet.':'Kaksi saman version PASSia. Lempiduettoni.',
    'Back to the drawing board. Literally.':'Takaisin taululle. Ihan kirjaimellisesti.',
    'Coffee is approved. Publication is still pending.':'Kahvi hyväksytty. Julkaisu odottaa.',
    'I deliver pages, not assumptions.':'Kuljetan sivuja, en oletuksia.',
    'Approved cargo. Still not a deployment receipt.':'Hyväksytty lasti. Ei vielä julkaisukuittia.',
    'Same lesson. A fresh pair of eyes.':'Sama oppitunti. Tuoreet silmät.',
    'Refactoring my caffeine levels.':'Refaktoroin kofeiinitasoani.',
    'A peer review of this coffee is now in progress.':'Tämän kahvin vertaisarviointi on käynnissä.',
    'A brief pause. The universe can wait.':'Lyhyt tauko. Maailmankaikkeus voi odottaa.',
    '{role} is taking a short coffee break after their handoff.':'{role} pitää pienen kahvitauon luovutuksen jälkeen.'
  };
  const descriptions = {
    developer:'Kirjoittaa ja korjaa oppitunnin tekstiä, tehtäviä, kuvia ja simulaatioita. Nykyinen kehittäjän työnkulku tarkistaa oppitunnin ennen riippumatonta arviointia.',
    science:'Tarkistaa riippumattomasti fysiikan, matematiikan, yksiköt, laskutulokset ja simulaation toiminnan. Arvioi työn muokkaamatta itse oppituntia.',
    pedagogy:'Arvioi riippumattomasti oppimispolun, selitykset, toiminnalliset tehtävät ja käytettävyyden puhelimella ja tietokoneella. Ei muokkaa oppituntia.',
    repository:'Tämän pöydän hahmo kuvaa opettajan julkaisupäätöstä. Opettaja päättää, mitä yhdistetään. Rakennus hyväksyy oppitunnit, joilla on molemmat voimassa olevat PASS-arviot tai legacy-poikkeus. CI tarkistaa sivuston erikseen. Yhdistäminen ei todista hyväksyjää tai onnistunutta julkaisua.',
    gatekeeper:'Tavallinen toimistohahmo kuvaa arvioiden hyväksyntätarkistusta. Molempien riippumattomien raporttien on annettava PASS nykyiselle sisältötiivisteelle. Koordinaattori vie tarkistetun paketin päätöksentekijälle ja palaa omalle pöydälleen. Puuttuva, hylätty, virheellinen tai vanhentunut raportti ei riitä. Hahmo havainnollistaa automaattista sääntöä, ei uutta käynnissä olevaa agenttia.',
    teacher:'Asettaa oppitunnin tavoitteet ja antaa kehitystehtävän. Opettajan julkaisupäätös kuvataan erillisellä pöydällä. Hahmojen liikkuminen havainnollistaa työnkulkua; Git-historia ei tallenna opettajan todellisia liikkeitä tai yksityisiä ohjeita.',
    checks:'Oppitunnin työnkulku rakentaa esikatselun ja tarkistaa sisällön, matematiikan, simulaatiot ja ulkoasun. Tallennetut checks.txt-tulokset näkyvät tässä, mutta niissä ei ole sisältötiivistettä: niiden ajantasaisuus ja CI-tulos ovat tuntemattomia. Kone kuvaa automaatiota, ei uutta agenttia.',
    site:'Kuvaa julkaisuprosessia, ei uutta tekoälyagenttia. Kuriiri saapuu julkaisupöydälle, odottaa tälle versiolle tallennettua hyväksyntää ja ottaa mukaansa vain hyväksytyn aineiston. Yhdistäminen tai HTML-tiedosto ei yksin todista päätöstä. Julkaisua ei ole varmistettu.',
    lounge:'Kahvikone, sohva ja pieni hengähdystauko. Vapaana oleva hahmo käy välillä kahvilla ja palaa ajoissa seuraavaan luovutukseen. Tauot ja puhekuplat ovat havainnollistuksia; oikeita agentteja ei pysäytetä eikä oppitunteja muuteta.'
  };
  const escape=s=>s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  const patterns=Object.keys(fi).filter(key=>key.includes('{')).sort((a,b)=>b.length-a.length).map(key=>{
    const names=[];let source='',last=0;
    for(const match of key.matchAll(/\{(\w+)\}/g)){source+=escape(key.slice(last,match.index))+'([\\s\\S]*?)';names.push(match[1]);last=match.index+match[0].length;}
    return {regex:new RegExp('^'+source+escape(key.slice(last))+'$'),names,value:fi[key]};
  });
  let language='fi';
  try{language=new URLSearchParams(location.search).get('lang') || localStorage.getItem('agent-office-language') || 'fi';}catch{}
  if(!['fi','en'].includes(language))language='fi';
  const cache=new Map();
  function t(value,parameters,depth=0){
    const source=String(value ?? '');
    const fill=(template,values)=>template.replace(/\{(\w+)\}/g,(_,name)=>String(values[name] ?? ''));
    if(parameters){const localized=Object.fromEntries(Object.entries(parameters).map(([k,v])=>[k,t(v,undefined,depth+1)]));return fill(language==='fi'?(fi[source] || source):source,localized);}
    if(language==='en' || depth>5 || !source)return source;
    if(cache.has(source))return cache.get(source);
    let result=fi[source];
    if(result===undefined){
      for(const pattern of patterns){const match=source.match(pattern.regex);if(match){result=fill(pattern.value,Object.fromEntries(pattern.names.map((name,i)=>[name,t(match[i+1],undefined,depth+1)])));break;}}
    }
    if(result===undefined){
      const parts=source.split(/(\s+·\s+|\s+—\s+|\n|(?<=\.)\s+(?=[A-Z]))/);
      result=parts.length>1?parts.map(part=>/^[\s·—]*$/.test(part)?part:t(part.trim(),undefined,depth+1)).join(''):source;
    }
    if(cache.size>2000)cache.clear();cache.set(source,result);return result;
  }
  const textMemory=new WeakMap(),attributeMemory=new WeakMap();
  function apply(root=document){
    const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);
    for(let node=walker.nextNode();node;node=walker.nextNode()){
      if(!node.parentElement || node.parentElement.closest('script,style,[data-no-i18n]'))continue;
      const current=node.data,record=textMemory.get(node);
      const original=record && record.translated===current?record.original:current;
      const leading=original.match(/^\s*/)[0],trailing=original.match(/\s*$/)[0];
      const translated=original.trim()?leading+t(original.trim())+trailing:original;
      textMemory.set(node,{original,translated});if(current!==translated)node.data=translated;
    }
    for(const element of (root.querySelectorAll?.('[aria-label],[title],meta[name="description"]') || [])){
      if(element.closest('[data-no-i18n]'))continue;
      const records=attributeMemory.get(element) || {};
      for(const name of ['aria-label','title',...(element.matches('meta[name="description"]')?['content']:[])]){
        if(!element.hasAttribute(name))continue;
        const current=element.getAttribute(name),record=records[name],original=record && record.translated===current?record.original:current,translated=t(original);
        records[name]={original,translated};if(current!==translated)element.setAttribute(name,translated);
      }
      attributeMemory.set(element,records);
    }
  }
  let observer;
  function start(){
    document.documentElement.lang=language;apply();
    observer=new MutationObserver(()=>apply());observer.observe(document.documentElement,{subtree:true,childList:true,characterData:true,attributes:true,attributeFilter:['aria-label','title']});
  }
  function setLanguage(next){
    language=next==='en'?'en':'fi';cache.clear();document.documentElement.lang=language;
    try{localStorage.setItem('agent-office-language',language);const url=new URL(location.href);url.searchParams.set('lang',language);history.replaceState(null,'',url);}catch{}
    apply();window.dispatchEvent(new CustomEvent('office-language-change'));
  }
  window.OfficeI18n={t,start,apply,setLanguage,get language(){return language;},roleDescription:(id,fallback)=>language==='fi'?(descriptions[id] || fallback):fallback,dateLabel:day=>new Intl.DateTimeFormat(language==='fi'?'fi-FI':'en-GB',{weekday:'short',day:'numeric',month:'long',year:'numeric',timeZone:'Europe/Helsinki'}).format(new Date(day+'T12:00:00+02:00'))};
})();
