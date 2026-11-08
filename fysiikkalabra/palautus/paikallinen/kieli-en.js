/* The local grading page in English (teacher 2026-11-08, "tools should also be in english").
   The page is written in Finnish; this script shows it in English when the teacher has chosen EN (button at the top,
   remembered in this browser; Finnish by default). Every text the page writes (texts, titles, aria-labels, alts,
   confirmations, the CSV's header row) passes tr(): known Finnish pieces -> English, the rest (names, numbers, dates)
   as they are. The task statements, model answers, the students' answers and the chapters' goals are not touched:
   they are the course's own Finnish texts (the chapters' and themes' English names come from RL_COURSES title_en).
   Changing the language reloads the page; the points and imports are kept in the browser. */
(function () {
  'use strict';
  var KEY = 'ruukkilabra:arviointi:kieli';
  var lang = 'fi';
  try { if (localStorage.getItem(KEY) === 'en') lang = 'en'; } catch (e) {}
  window.RL_LANG = lang;
  function setLang(l) { try { localStorage.setItem(KEY, l); } catch (e) {} location.reload(); }
  // the language button beside Päivitä, in both languages
  document.addEventListener('DOMContentLoaded', function () {
    var b = document.createElement('button'); b.type = 'button'; b.id = 'langBtn';
    b.textContent = lang === 'en' ? 'FI' : 'EN'; b.title = lang === 'en' ? 'Suomeksi' : 'In English';
    b.setAttribute('lang', lang === 'en' ? 'fi' : 'en');
    b.addEventListener('click', function () { setLang(lang === 'en' ? 'fi' : 'en'); });
    var r = document.getElementById('refresh'); if (r) r.after(b);
  });
  if (lang !== 'en') return;

  // Finnish pieces of the page's texts -> English, longest first. A piece that starts or ends with a letter matches
  // only a whole word there.
  var EN = {
    // Review.html: static
    'RuukkiLabra · arviointi': 'RuukkiLabra · grading', 'Päivitä': 'Refresh', 'Ladataan…': 'Loading…', 'Luvut': 'Chapters',
    'Ensimmäinen luku': 'First chapter', 'Viimeinen luku': 'Last chapter', 'Kooste': 'Summary', 'Piilota nimet': 'Hide names',
    'Näytä nimet': 'Show names', 'Ei palautuksia.': 'No submissions.', 'Ryhmä yhteensä': 'Group in total',
    'Osaamisen sormenjälki': 'Skills fingerprint', 'Tehtävät': 'Tasks', 'Vain arvioimattomat': 'Ungraded only',
    'Tarkistettavat ja hylätyt palautukset': 'Submissions to check and rejected submissions', 'Tila': 'Status', 'Luku': 'Chapter',
    'Opiskelija': 'Student', 'Palautusaika': 'Submitted', 'Tunniste': 'ID', 'Syy': 'Reason', 'Päätös': 'Decision',
    '← Tehtävälista': '← Task list', 'Palautusversio': 'Submission version', 'Tehtävänanto': 'Task',
    'Lyhyt mallivastaus': 'Short model answer', 'Opiskelijan vastaus': "Student's answer",
    'Näytä kaavat LaTeX-muotoisina': 'Show formulas as LaTeX', 'Pisteet': 'Points', '↑ Edellinen': '↑ Previous', '↓ Seuraava': '↓ Next',
    '↓ seuraava · ↑ edellinen · → +1 p · ← −1 p · 0,5: kirjoita kenttään + Enter': '↓ next · ↑ previous · → +1 p · ← −1 p · 0,5: type in the field + Enter',
    'Suurennettu kuva': 'Enlarged picture',
    // Review.html: script
    'tuntematon virhe': 'unknown error', ' · ryhmä ': ' · group ', ' · arviointi': ' · grading',
    'Hyväksyttyjä palauttajia ': 'Accepted submitters: ',
    'Tuo ryhmän palautukset (zip) ylhäältä: Tuo tiedosto.': "Import the group's submissions (zip) at the top: Import file.",
    'Ei palautuksia. RuukkiLabra → Tuo palautukset, sitten Päivitä.': 'No submissions. RuukkiLabra → Import submissions, then Refresh.',
    ' · peru': ' · undo', 'Päätöstä ei tallennettu: ': 'The decision was not saved: ', 'Tietoja ei voitu ladata: ': 'Could not load the data: ',
    '· palautuksia ': '· submissions ', ' · arvioitu ': ' · graded ', ' · arvioimatta ': ' · ungraded ',
    'Tehtävä': 'Task', 'Taso': 'Level', 'Ratkaisuja': 'Solutions', 'Arvioitu': 'Graded', 'Arvioimatta': 'Ungraded', 'Oppitunti': 'Lesson',
    'Kaikki ratkaisut on arvioitu.': 'All solutions are graded.', 'Tehty': 'Done', 'Tarkistamatta': 'Unchecked', 'Itsearvio': 'Self-assessment',
    'Annetut': 'Assigned', 'Ei itsearviota': 'No self-assessment', 'Itsearvion keskiarvo ': 'Self-assessment mean ',
    '); valinnaiset ja Ei vielä eivät mukana': '); optional items and Not yet are not included',
    'Ei Tehty-merkintöjä (vanha palautus tai moduulissa ei annettuja tehtäviä)': 'No Done marks (an old submission, or the module has no assigned tasks)',
    'Ei palautusta tästä luvusta': 'No submission for this chapter',
    'Ryhmä: tehty ': 'Group: done ', 'Ryhmä: pisteet ': 'Group: points ',
    'Osaan niin hyvin, että voisin opettaa kaverille': 'I know this so well that I could teach it to a friend',
    'Koen oivaltaneeni': 'I feel I have grasped this', 'Osaan osittain, epävarmuutta on vielä': 'I partly know this, but I am still unsure',
    'Tarvitsen vielä harjoitusta': 'I still need practice', 'En ole vielä harjoitellut': 'I have not practised this yet',
    'osaan niin hyvin, että voisin opettaa kaverille': 'I know this so well that I could teach it to a friend',
    'tarvitsen vielä harjoitusta': 'I still need practice', 'Annetut tehty': 'Assigned done',
    // the kinds of a lesson's tasks in their names (lang/en.json inquiry); the rest of a name is the chapter's own text
    'Pohdinta': 'Think about it', 'Ennusta': 'Predict', 'Tutki': 'Investigate', 'Käsitetehtävä': 'Concept task',
    'Laskutehtävä': 'Calculation task', 'Selitystehtävä': 'Explanation task', 'Ennuste': 'Prediction', 'Johtopäätös': 'Conclusion',
    'Koe': 'Experiment', 'Lisätutkimus': 'Further investigation', 'Teoria': 'Theory', 'Esimerkit': 'Examples', 'Esimerkki': 'Example',
    'Koko ryhmän osaamisen sormenjälki': "The whole group's skills fingerprint", 'Koko ryhmä': 'Whole group', 'Väitteittäin': 'By statement',
    ', väite ': ', statement ',
    'Ei vastattu': 'Not answered', 'Väittämä': 'Statement', 'Ei vielä': 'Not yet',
    'oppitunnin tehtävä, ei pisteitä': "lesson's task, no points", 'Vain arvioimattomat (': 'Ungraded only (', ' ratkaisua)': ' solutions)',
    'Kaikki tämän tehtävän ratkaisut on arvioitu.': 'All solutions to this task are graded.',
    'Tähän tehtävään ei ole ratkaisuja (tyhjiä ei näytetä).': 'This task has no solutions (empty ones are not shown).',
    'Jonoa ei voitu ladata: ': 'Could not load the queue: ', 'Palautettu ': 'Submitted ', ' · versio ': ' · version ',
    ' (uusin)': ' (newest)', ' (vanhempi)': ' (older)', ' · tunniste ': ' · ID ', 'Pisteet versiosta ': 'Points from version ',
    ' ✓ (sama ratkaisu)': ' ✓ (same solution)', 'Tallennettu ✓ (arvioimaton)': 'Saved ✓ (ungraded)', 'Tallennettu ✓': 'Saved ✓',
    'Tallennettu ✓ · tehtävän viimeinen palautus': "Saved ✓ · the task's last submission", 'Arvioimaton': 'Ungraded',
    'Ladataan vastausta…': 'Loading the answer…', 'Vastausta ei voitu näyttää: ': 'Could not show the answer: ',
    'Numerovastaus: ': 'Numeric answer: ', 'Valinta: ': 'Choice: ', 'Vastaus': 'Answer', 'Tosi vai epätosi:': 'True or false:',
    '(ei valittu)': '(not chosen)', 'Tosi': 'True', 'Epätosi': 'False', 'Järjestys:': 'Order:', '(ei sijaa) ': '(no place) ', 'Mittaukset:': 'Measurements:',
    'Opiskelija jätti tehtävän tyhjäksi.': 'The student left the task empty.', 'Ei ratkaisua editorissa.': 'No solution in the editor.',
    'Opiskelijan kuva (': "Student's picture (", '), suurenna napsauttamalla': '), click to enlarge',
    'Opiskelijan kuva täysikokoisena': "Student's picture at full size", ' (esim. 0,5) tai tyhjä. Ei tallennettu.': ' (e.g. 0,5) or empty. Not saved.',
    'Tallennetaan…': 'Saving…', 'Tallennus epäonnistui: ': 'Saving failed: ', ' Pisteitä ei tallennettu.': ' The points were not saved.',
    // local-backend.js
    'Tuo tiedosto': 'Import file', 'Peru viimeisin tuonti': 'Undo the last import', 'Ryhmä: ': 'Group: ', 'Muut toiminnot': 'More actions',
    'Vie pisteet (CSV)': 'Export points (CSV)', 'Varmuuskopio': 'Backup', 'Palauta varmuuskopio': 'Restore a backup', 'Poista ryhmä': 'Delete the group',
    'Tuonti klo ': 'Import at ', ' palautusta': ' submissions',
    'Lataa Drivesta ryhmän lomakkeen palautuskansio (zip) ja tuo se tähän: Tuo tiedosto.': "Download the group form's response folder (zip) from Drive and import it here: Import file.",
    'Ryhmä ': 'Group ', ' Tuo ryhmän zip uudelleen, niin vastaukset näkyvät.': " Import the group's zip again to see the answers.",
    'Luetaan…': 'Reading…', ': kurssia ': ': the course ', ' ei ole tällä arviointisivulla, ei luettu.': ' is not on this grading page, not read.',
    'Selain ei salli tallentamista (localStorage).': 'The browser does not allow saving (localStorage).',
    'Selain ei salli tallentamista (localStorage). Pisteitä ei tallennettu.': 'The browser does not allow saving (localStorage). The points were not saved.',
    'Zip on lomakkeelta "': 'The zip is from the form "', '", mutta ryhmän ': '", but the submissions of group ',
    ' palautukset on luettu lomakkeelta "': ' were read from the form "', '". Mitään ei luettu.': '". Nothing was read.',
    ': luettu ': ': read ', ' tiedostoa. Uusia palautuksia ': ' files. New submissions ', ' (hyväksyttyjä ': ' (accepted ',
    ', kaksoiskappaleita ': ', duplicates ', ', tarkistettavia ': ', to check ', ', virheellisiä ': ', invalid ',
    'Ryhmää ei tunnistettu: "': 'The group was not recognised: "',
    '". Lomakkeen nimen pitää alkaa ryhmällä, esim. FY3.2 lv 2026-27 Palauta ratkaisut.': '". The form\'s name must start with the group, e.g. FY3.2 lv 2026-27 Palauta ratkaisut.',
    ' Selain ei salli palautusten tallentamista (IndexedDB): vastaukset näkyvät vain, kunnes sivu suljetaan.': ' The browser does not allow storing the submissions (IndexedDB): the answers are shown only until the page is closed.',
    'Tiedostoja ei voitu lukea: ': 'Could not read the files: ',
    'Perutaanko tuonti klo ': 'Undo the import at ', '? Siinä tuodut ': '? The ', ' palautusta poistetaan, ja ryhmän ': ' submissions it imported are removed, and the grading of group ',
    ' arviointi palaa tuontia edeltävään tilaan. Tuonnin jälkeen annetut pisteet poistuvat.': ' returns to its state before the import. Points given after the import are removed.',
    'Tuonti peruttu: ': 'Import undone: ', ' palautusta poistettu.': ' submissions removed.', ' Tuo ryhmän zip-tiedosto.': " Import the group's zip file.",
    'Pisteet viety tiedostoon ': 'Points exported to the file ', '. Avaa se Sheetsissä (Tiedosto → Tuo).': '. Open it in Sheets (File → Import).',
    'Varmuuskopio ladattu. Säilytä se koulun Drivessa, ei julkisesti.': "Backup downloaded. Keep it in the school's Drive, not publicly.",
    'Varmuuskopio on ryhmältä ': 'The backup is from group ', '. Korvataanko ryhmän ': '. Replace the grading of group ', ' arviointi sillä?': ' with it?',
    'Tiedosto ei ole tämän kurssin arvioinnin varmuuskopio.': "The file is not a backup of this course's grading.",
    'Varmuuskopio palautettu ryhmään ': 'Backup restored to group ', 'Tiedostoa ei voitu lukea.': 'Could not read the file.',
    'Poistetaanko ryhmä ': 'Delete group ', ' sekä sen tuonnit ja pisteet tästä selaimesta? Ota ensin varmuuskopio.': ' and its imports and points from this browser? Make a backup first.',
    ' poistettu.': ' deleted.', 'odottamaton virhe': 'unexpected error', 'tuntematon toiminto': 'unknown action', 'tuntematon pakkaus': 'unknown compression',
    'Vastauksia ei ole tässä selaimessa. Tuo ryhmän zip-tiedosto uudelleen ylhäältä (Tuo tiedosto).': "The answers are not in this browser. Import the group's zip file again at the top (Import file).",
    'Tiedosto ei ole zip-tiedosto.': 'The file is not a zip file.', 'Zip-tiedosto on vioittunut.': 'The zip file is damaged.',
    // Code.gs: statuses, decisions, the CSV and the reasons
    'Hyväksytty': 'Accepted', 'Kaksoiskappale': 'Duplicate', 'Tarkistettava': 'To check', 'Virheellinen': 'Invalid', 'Lukuvirhe': 'Read error',
    'Hyväksy': 'Accept', 'Hylkää': 'Reject', 'Yhteensä': 'Total', 'Palautettuja lukuja': 'Chapters submitted', ' klo ': ' at ',
    'Odottamaton virhe. Yritä uudelleen; jos virhe toistuu, tarkista asetukset (KAYTTOONOTTO.md).': 'Unexpected error. Try again; if it happens again, check the settings (KAYTTOONOTTO.md).',
    'Toinen käsittely on juuri käynnissä. Yritä hetken kuluttua uudelleen.': 'Another run is in progress. Try again in a moment.',
    'Tuntematon tehtävä.': 'Unknown task.', 'Virheellinen pyyntö.': 'Invalid request.',
    'Palautusta ei löydy hyväksytyistä palautuksista. Tuo palautukset uudelleen.': 'The submission is not among the accepted submissions. Import the submissions again.',
    'Palautustiedostoa ei voitu avata.': 'Could not open the submission file.',
    'Palautustiedosto ei ole enää palautuskansiossa tai se on muuttunut.': 'The submission file is no longer in the submission folder, or it has changed.',
    'Palautustiedosto ei kelpaa enää: ': 'The submission file is no longer valid: ', 'Palautustiedosto on muuttunut tuonnin jälkeen.': 'The submission file has changed since the import.',
    'Virheellinen tallennuspyyntö.': 'Invalid save request.', 'Oppitunnin tehtävää ei pisteytetä.': "A lesson's task is not scored.",
    'Pisteet ovat luku 0–': 'Points are a number 0–', ' (enintään kaksi desimaalia) tai tyhjä (arvioimaton).': ' (at most two decimals) or empty (ungraded).',
    'Palautusta ei löydy hyväksytyistä palautuksista, joten pisteitä ei tallennettu.': 'The submission is not among the accepted submissions, so the points were not saved.',
    'Virheellinen päätös.': 'Invalid decision.', 'Palautusta ei löydy.': 'Submission not found.',
    'palautusaika puuttuu': 'the submission time is missing', 'palauttajan nimi puuttuu tiedoston nimestä': "the submitter's name is missing from the file name",
    'vahvistettu sähköpostiosoite puuttuu (ota sähköpostien kerääminen käyttöön lomakkeessa)': 'a verified email address is missing (turn on collecting emails in the form)',
    'sähköposti ei ole koulun verkkotunnuksesta': "the email is not from the school's domain", 'palautuksessa ei ole tiedostoa': 'the submission has no file',
    'palautuksessa on useita tiedostoja (sallittu yksi)': 'the submission has several files (one allowed)',
    'tiedostoa ei voitu avata (käyttöoikeus tai poistettu tiedosto)': 'could not open the file (permission or a deleted file)',
    'tiedosto ei ole lomakkeen palautuskansiossa': "the file is not in the form's submission folder", 'tiedosto on liian suuri (': 'the file is too large (',
    ' Mt, enintään ': ' MB, at most ', ' Mt)': ' MB)', 'tiedosto on tyhjä': 'the file is empty', 'tiedostoa ei voitu lukea': 'could not read the file',
    'sama palautustunniste kuin toisella opiskelijalla (': 'the same submission ID as another student (',
    'sama palautus': 'the same submission', 'sama sisältö': 'the same content', ' tuotu jo (': ' already imported (',
    'sama palautustunniste mutta eri sisältö kuin aiemmassa palautuksessa': 'the same submission ID but different content from an earlier submission',
    'tiedosto ei ole JSON-tiedosto': 'the file is not a JSON file', 'tiedoston rakenne on virheellinen': "the file's structure is invalid",
    'tiedosto ei ole RuukkiLabran palautustiedosto': 'the file is not a RuukkiLabra submission file', 'tiedostomuodon versio puuttuu': 'the file format version is missing',
    'tiedostomuodon versio ': 'the file format version ', ' on uudempi kuin tämä skripti tuntee': ' is newer than this script knows',
    'tuntematon tiedostomuodon versio': 'unknown file format version',
    'tiedosto on toiselta opintojaksolta tai tuntemattomasta luvusta (': 'the file is from another course or an unknown chapter (',
    'tiedosto on toiselta opintojaksolta (': 'the file is from another course (', 'palautustunniste puuttuu tai on virheellinen': 'the submission ID is missing or invalid',
    'tarkistussumma puuttuu': 'the checksum is missing', 'vastaukset puuttuvat': 'the answers are missing', 'vastaus ': 'answer ', ' on virheellinen': ' is invalid',
    'tuntematon tehtävä ': 'unknown task ', 'tehtävä ': 'task ', ' on tiedostossa kahdesti': ' is in the file twice', ' puuttuu tiedostosta': ' is missing from the file',
    'kuvia on liikaa (': 'too many pictures (', 'etenemistiedot kuuluvat vain versioon 4': 'progress data belongs only to version 4', 'etenemistiedot: ': 'progress data: ',
    'tarkistussumma ei täsmää: tiedostoa on muutettu tai se on vioittunut': 'the checksum does not match: the file has been changed or damaged',
    'työtiedoston versio ': 'the work file version ', 'työtiedoston rakenne on virheellinen': "the work file's structure is invalid",
    'luku ': 'chapter ', ' on tuntematon': ' is unknown', 'luvun ': 'chapter ', ' rakenne on virheellinen': ': its structure is invalid',
    'tiedostossa ei ole yhtään ratkaisua': 'the file has no solutions', 'itsearvio on virheellinen': 'the self-assessment is invalid',
    'itsearvion kohta ': 'self-assessment item ', 'itsearvion kohdassa ': 'self-assessment item ', ' on tuntematon taso': ' has an unknown level',
    'itsearvion kohdan ': 'self-assessment item ', ' historia on virheellinen': ': its history is invalid',
    'tavoitearvio on virheellinen': 'the goal assessment is invalid', 'tavoitearvion kohta ': 'goal assessment item ',
    ': virheellinen osa': ': invalid part', ': tuntematon kenttä "': ': unknown field "', ': tyhjä tai virheellinen teksti': ': empty or invalid text',
    ': virheellinen kaava': ': invalid formula', ': kaavakuvan koko on virheellinen': ": the formula picture's size is invalid",
    ': kaavakuva ei ole PNG-kuva': ': the formula picture is not a PNG picture', ': kaavakuva ei ole SVG-kuva': ': the formula picture is not an SVG picture',
    ': kaavakuva on liian suuri': ': the formula picture is too large', ': kaavakuva on virheellinen': ': the formula picture is invalid',
    ': kuvan näyttöleveys on virheellinen': ": the picture's display width is invalid",
    ': kuvamuoto ei ole sallittu (vain PNG ja JPEG)': ': the picture format is not allowed (only PNG and JPEG)',
    ': kuvan sisältö ei ole ': ": the picture's content is not a ", '-kuva': ' picture', ': kuvan koko on liian suuri (yli ': ": the picture's size is too large (over ",
    ': kuva on liian suuri': ': the picture is too large', ' (yli ': ' (over ', ': kuvadata ei ole kelvollista base64-dataa': ': the picture data is not valid base64 data',
    ': tuntematon sisältötyyppi': ': unknown content type', ': virheellinen vastaus': ': invalid answer', ': virheellinen valinta': ': invalid choice',
    ': virheellinen väite': ': invalid statement', ': virheellinen järjestys': ': invalid order', ': virheellinen taulukko': ': invalid table',
    ': tuntematon vastaustyyppi': ': unknown answer type', ': virheellinen sisältö': ': invalid content', ': virheelliset vastaukset': ': invalid answers',
    ': tuntematon tila': ': unknown state', ': tila ja sisältö eivät täsmää': ': the state and the content do not match',
    ': teksti on liian pitkä': ': the text is too long', ': kuvaa ei löydy tiedostosta': ': the picture is not in the file',
    ': kaavaa ei löydy tiedostosta': ': the formula is not in the file', ': virheellinen kuva': ': invalid picture'
  };
  var RE = [   // word order that the pieces cannot give
    [/(\d+)\. periodi · lv (\S+)/g, 'period $1 · $2'],
    [/Luku (\S+?)( \(max |$| · |: )/g, 'Chapter $1$2'],
    [/^Opiskelija (\d+)\/(\d+)$/, 'Student $1/$2'],
    [/^Ryhmä (\S+) poistettu\.$/, 'Group $1 deleted.']
  ];
  var esc = function (s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); };
  var keys = Object.keys(EN).sort(function (a, b) { return b.length - a.length; });
  var PIECES = new RegExp(keys.map(function (k) {
    return (/^\p{L}/u.test(k) ? '(?<!\\p{L})' : '') + esc(k) + (/\p{L}$/u.test(k) ? '(?!\\p{L})' : '');
  }).join('|'), 'gu');
  var TITLES = {};   // the chapters' Finnish names -> English (RL_COURSES title_en)
  try {
    Object.keys(window.RL_COURSES || {}).forEach(function (c) {
      (RL_COURSES[c].chapters || []).forEach(function (ch) { if (ch.title_en) TITLES[ch.title] = ch.title_en; });
      (RL_COURSES[c].themes || []).forEach(function (th) { if (th.title_en) TITLES[th.title] = th.title_en; });   // the group fingerprint's themes
    });
  } catch (e) {}
  var TITLE_RE = Object.keys(TITLES).length ? new RegExp(Object.keys(TITLES).sort(function (a, b) { return b.length - a.length; }).map(esc).join('|'), 'g') : null;
  function tr(s) {
    if (typeof s !== 'string' || !/[A-Za-zÄÖäö]/.test(s)) return s;
    if (TITLE_RE) s = s.replace(TITLE_RE, function (m) { return TITLES[m]; });
    RE.forEach(function (r) { s = s.replace(r[0], r[1]); });
    return s.replace(PIECES, function (m) { return EN[m]; });
  }
  window.rlTr = tr;

  // what is not the page's own text: the task statements, model answers, the students' answers and the goals
  var KEEP = '#gStatement, #gModel, .t, code.math, .resp .muted, .resp table, td.lab, script, style';
  var ATTRS = ['title', 'aria-label', 'alt'];
  function text(n) {
    var p = n.parentElement;
    if (!p || p.closest(KEEP)) return;
    var v = tr(n.data); if (v !== n.data) n.data = v;
  }
  function attrs(e) {
    if (e.closest(KEEP) && !e.matches('#gStatement, #gModel')) return;
    ATTRS.forEach(function (a) { var v = e.getAttribute(a); if (v) { var w = tr(v); if (w !== v) e.setAttribute(a, w); } });
  }
  function walk(n) {
    if (n.nodeType === 3) { text(n); return; }
    if (n.nodeType !== 1) return;
    attrs(n);
    if (n.matches(KEEP)) return;
    var w = document.createTreeWalker(n, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT, null);
    while (w.nextNode()) { var x = w.currentNode; if (x.nodeType === 3) text(x); else attrs(x); }
  }
  new MutationObserver(function (list) {
    list.forEach(function (m) {
      if (m.type === 'childList') m.addedNodes.forEach(walk);
      else if (m.type === 'characterData') text(m.target);
      else if (m.type === 'attributes') attrs(m.target);
    });
    if (document.title !== tr(document.title)) document.title = tr(document.title);
  }).observe(document.documentElement, { childList: true, subtree: true, characterData: true, attributes: true, attributeFilter: ATTRS });
  document.documentElement.lang = 'en';
  var ask = window.confirm; window.confirm = function (m) { return ask.call(window, tr(m)); };
  var say = window.alert; window.alert = function (m) { return say.call(window, tr(m)); };
  // the CSV's header row (the rows below are names and numbers)
  if (typeof window.rlScoresCsv === 'function') {
    var csv = window.rlScoresCsv;
    window.rlScoresCsv = function () { var s = csv.apply(this, arguments), i = s.indexOf('\r\n'); return tr(s.slice(0, i)) + s.slice(i); };
  }
})();
