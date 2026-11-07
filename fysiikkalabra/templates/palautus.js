/* Submission trial (teacher 2026-11-05, "palautus- ja arviointikokeilu"; FY3 in every language, build.py SUBMISSION_COURSES).
   "Lataa kaikki ratkaisut" writes one file, <chapter>.ratkaisut.json, from the solutions the student wrote in this chapter's
   solution editors (lesson.js part 6, kept on this device by padstore.js). The student returns the file with the
   school's Google Forms form; the teacher's Apps Script (palautus/apps-script/) reads and grades it. Ruukkilabra
   itself sends nothing anywhere: the file is made in this browser and saved on this device.

   File format "ruukkilabra-palautus", version 1 (palautus/TIEDOSTOMUOTO.md is the full description):
     { format, version: 1, chapter, lang, submission_id: 32 hex, exported: ISO time, includes: "solution-editor",
       content_sha256, answers: [ { task, status: "answered" | "empty", content: [item, ...] }, ... ] }
     item = { type: "text", text } | { type: "math", latex, png?, w?, h? } | { type: "image", mime, data, w, h, dw? }
   Every exercise of the chapter is in `answers`, in page order, an unanswered one as "empty" with no content, so the
   teacher can tell an unanswered task from a missing or broken file. Text keeps its line breaks ("\n"); a formula is
   its LaTeX (the formula image is redrawn as a PNG, `png`, for the teacher's view); a picture is PNG or JPEG data
   (base64, no "data:" prefix), pasted into the editor with Ctrl+V (teacher 2026-11-05: no separate image button); `dw`
   is the width in CSS px the student made it in the editor (teacher 2026-11-06), only when smaller than its own pixels.
   Items keep the order of the solution. No name, e-mail or other chapters.
   content_sha256 is the SHA-256 of the answers without the formula PNGs (JSON, UTF-8): the same solutions keep the
   same random submission_id (kept in localStorage ruukkilabra:palautus:<chapter>), any change gives a new one.
   Version 2 (teacher 2026-11-06, guided self-assessment, build.py SELF_ASSESS_COURSES): a page with the self-assessment
   of Tarkista osaamisesi (fieldset.sa-rate, inquiry.js part 8) adds
     selfassessment: { items: [ { id, level: "a" | "b" | "c" | "d" | "x", history: [[level, ISO time], ...] }, ... ] }
   with the assessed items in page order, and content_sha256 is then the SHA-256 of
   JSON.stringify({ answers: <as above>, selfassessment: <items> }), so a changed assessment is a new submission.
   Version 3 (teacher 2026-11-06 evening, "kaikki tehtävävastaukset mukaan"): every task of the chapter with an answer
   control, in page order: the exercises (and FY9 review tasks) as before, and the lesson's own tasks (Ennusta, Tutki,
   Itsearvio …: .activity[id] outside Tehtävät, task "<chapter>:<activity id>"), each { task, status, content: [editor
   items], responses: [item, ...] }
   with responses = { type: "number", value, unit? } (a typed number as typed, its unit) | { type: "choice", question,
   answer, option } (the chosen option's text) | { type: "truefalse", items: [{ text, value: true | false | null }] } |
   { type: "order", items: [{ text, rank: n | null }] } | { type: "text", label, text } (a written answer, a reason) |
   { type: "table", head: [...], rows: [[...], ...] } (an experiment's measurements). A task is "answered" when its
   editor or any of its responses has something, so a number with an empty editor is an answer (before this, the file
   held the editor only and a checked number or choice came out empty). Text keeps LaTeX between $…$.
   The self-assessment of version 3 is the goals' summary only: selfassessment: { goals: [ { id: "tavoite-<n>", text,
   level: "a" | "b" | "c" | "d" | "x" | null } ] }, every goal of the chapter, null = not answered, "x" = "En ole vielä
   harjoitellut". The tasks' own self-assessments and the history of changes stay on this device and are not in the file.
   content_sha256 = SHA-256 of JSON.stringify({ answers: <answers, formula PNGs left out>, selfassessment: <goals> }).
   One work file per module (teacher 2026-11-07; FY1-FY8, build.py course_block): see "Work file" below. On those pages
   the chapter file above is no longer downloaded by a button; it stays for FY9 and as window.flChapterFile (tests).
   The list of tasks is window.flSubmissionTasks (scripts/palautus_tasks.py reads the same list for the grading page). */
(() => {
  const ME = document.currentScript;
  const CHAPTER = ME && ME.dataset.chapter;
  const HERE = ME ? ME.src : location.href;
  const FORMAT = 'ruukkilabra-palautus';
  const VERSION = 3;
  const SA_LEVEL = /^[abcdx]$/;
  // the chapter's goals (Itsearvio's first card, inquiry.py sa_goals_html) with the student's latest level, or null
  const goals = () => {
    let all = {};
    try { const v = JSON.parse(localStorage.getItem('ruukkilabra:itsearvio:' + CHAPTER)); if (v && v.v === 1 && v.items) all = v.items; } catch (e) { /* none */ }
    const seen = new Set();
    return [...document.querySelectorAll('fieldset.sa-rate')].filter((f) => /^tavoite-\d+$/.test(f.dataset.sa || '') && !seen.has(f.dataset.sa) && seen.add(f.dataset.sa)).map((f) => {
      const it = all[f.dataset.sa];
      return { id: f.dataset.sa, text: (f.dataset.label || '').slice(0, 500), level: it && SA_LEVEL.test(it.level) ? it.level : null };
    });
  };
  // Limits, the same in the teacher's Apps Script (Code.gs RL_LIMITS): Forms takes a file of at most 10 MB when the
  // teacher picks that size; a picture of 2 MB is a full-screen screenshot, and the teacher's view loads one task at a time.
  const LIMITS = { file: 9000000, image: 2000000, side: 5000, images: 40, text: 20000, latex: 4000, items: 400, mathPng: 200000 };
  const STORE_KEY = 'ruukkilabra:palautus:' + CHAPTER;
  const sec = document.getElementById('exercises');
  const ON_CHAPTER = !!(CHAPTER && sec);
  const COURSE = (() => { try { return JSON.parse(document.getElementById('fl-course').textContent); } catch (e) { return null; } })();
  if (!ON_CHAPTER && !COURSE) return;
  // an exercise (li > p.task) and a review task of FY9 (div.practice-task, practice.py; teacher 2026-11-06), the ones
  // lesson.js part 6 gives a solution editor: a task with only choices has none
  const edTasks = !ON_CHAPTER ? [] : [...sec.querySelectorAll('li[id], div.practice-task[id]')].filter((t) => (t.matches('li') ? t.querySelector(':scope > .task')
    : !t.querySelector(':scope > ol.parts') || t.querySelector(':scope > ol.parts > li:not(:has(.choices))')));
  // the answer controls of the page (teacher 2026-11-06 evening: numbers, choices, written answers, also of Itsearvio's
  // tasks). Not answers: the self-assessment scales (sa-rate, rubric points), the "Olen tehnyt ratkaisun" ticks and the
  // criteria an explanation is checked against (self-assessment marks), the solution editor's own fields.
  const CONTROLS = 'form.check, fieldset.choice, fieldset.tf, fieldset.order, textarea, .experiment table.exp-table, .revise';   // an exercise's data table is part of its statement
  const TASK = '#exercises li[id], #exercises div.practice-task[id], .activity[id]';
  const hostOf = (el) => el.closest(TASK);
  const own = (t, sel) => [...t.querySelectorAll(sel)].filter((x) => hostOf(x) === t && !x.closest('.pad, .pad-saved, .rich-text-editor, .sa-rate, .rubric, .palautus') && !(x.matches('textarea') && (x.readOnly || x.closest('.justify'))));
  const lessonTasks = [...document.querySelectorAll('.activity[id]')].filter((a) => !a.closest('#exercises') && !a.matches('.act-exercises, .act-selfgoals') && own(a, CONTROLS).length);
  const isEd = new Set(edTasks);
  const tasks = !ON_CHAPTER ? [] : [...new Set([...edTasks, ...lessonTasks, ...[...sec.querySelectorAll('li[id], div.practice-task[id]')].filter((t) => own(t, CONTROLS).length)])]
    .filter((t) => isEd.has(t) || own(t, CONTROLS).length)
    .sort((a, b) => (a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1));
  // a lesson task's id in the file is "<chapter>:<activity id>" ("fy3-1:reflect"): the activity ids repeat from chapter
  // to chapter, an exercise's id ("fy3-1-L1-02") does not
  const taskId = (t) => (t.closest('#exercises') ? t.id : CHAPTER + ':' + t.id);
  window.flSubmissionTasks = () => tasks.slice();
  window.flSubmissionTaskId = taskId;
  if (!tasks.length && !COURSE) return;
  const numOf = (li) => li.dataset.num || (li.querySelector(':scope > h3, :scope h3') || {}).textContent?.trim() || li.id;
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
  const say = (node, text, state) => { node.textContent = text; if (state) node.dataset.state = state; else delete node.dataset.state; };
  const fail = (text) => { const e = new Error(text); e.user = true; return e; };
  // Texts: lang/<lang>.json js.palautus_<key> (build.py strings_block), Finnish as the fallback.
  const L10N = (() => { try { return JSON.parse(document.getElementById('fl-strings').textContent).js || {}; } catch (e) { return {}; } })();
  const FI = {"download": "Lataa kaikki ratkaisut", "return": "Palauta", "busy": "Tallennetaan ja kootaan ratkaisuja…", "done_link": "Palauta ladattu tiedosto Palauta-napista oman ryhmäsi lomakkeella.", "done_forms": "Palauta ladattu tiedosto opettajan Google Forms -lomakkeella.", "failed": "Tiedostoa ei voitu koota. Lataa sivu uudelleen ja yritä uudelleen.", "task": "Tehtävä {{n}}", "store": "Tallennettuja ratkaisuja ei voitu lukea. Lataa sivu uudelleen.", "flush": "Kaikkia avoimia ratkaisuja ei saatu tallennettua, joten tiedostoa ei ladattu. Katso virheilmoitus ratkaisun alta ja yritä uudelleen.", "corrupt": "{{where}}: tallennettu ratkaisu on vioittunut. Kirjoita ratkaisu uudelleen.", "no_storage": "Tallennettuja ratkaisuja ei voitu lukea (selain ei salli tallennusta). Tiedostoa ei ladattu.", "img_type": "{{where}}: ratkaisussa on kuva, jonka muoto ei kelpaa (vain PNG ja JPEG). Poista se ja liitä kuva uudelleen.", "img_web": "{{where}}: ratkaisussa on verkkosivulta liitetty kuva, jota ei voi palauttaa. Poista se ja liitä kuvakaappaus.", "img_read": "{{where}}: kuvaa ei voitu lukea. Poista kuva ja liitä se uudelleen.", "img_big": "{{where}}: kuva on liian suuri ({{mb}} Mt, enintään {{max}} Mt). Rajaa kuvakaappaus pienemmäksi ja liitä se uudelleen.", "img_broken": "{{where}}: kuva on vioittunut. Poista se ja liitä kuva uudelleen.", "img_side": "{{where}}: kuva on liian suuri (yli {{n}} pikseliä leveä tai korkea).", "latex_long": "{{where}}: kaava on liian pitkä (yli {{n}} merkkiä).", "items": "{{where}}: ratkaisussa on liian monta osaa.", "text_long": "{{where}}: ratkaisun teksti on liian pitkä (yli {{n}} merkkiä).", "images": "Ratkaisuissa on {{n}} kuvaa, enintään {{max}}. Poista osa kuvista.", "file_big": "Tiedostosta tulisi liian suuri ({{mb}} Mt, enintään {{max}} Mt). Rajaa tai poista kuvia.", "progress": "Tiedostossa ovat myös annettujen tehtävien Tehty-merkinnät ja niiden ajat."};
  const S = (k, v) => (typeof L10N['palautus_' + k] === 'string' ? L10N['palautus_' + k] : FI[k] || '').replace(/\{\{(\w+)\}\}/g, (m, n) => (v && n in v ? String(v[n]) : m));
  const LANG = (document.documentElement.lang || 'fi').slice(0, 2);
  const bytesOfB64 = (b64) => Math.floor(b64.length * 3 / 4) - (b64.endsWith('==') ? 2 : b64.endsWith('=') ? 1 : 0);

  const loadStore = () => (window.flPadStore ? Promise.resolve() : new Promise((ok, no) => {
    const s = document.createElement('script'); s.src = new URL('padstore.js', HERE).href; s.onload = ok; s.onerror = () => no(fail(S('store'))); document.head.append(s);
  }));
  const loadImage = (src) => new Promise((ok, no) => { const i = new Image(); i.onload = () => ok(i); i.onerror = () => no(new Error('image')); i.src = src; });
  const readAsDataUrl = (blob) => new Promise((ok, no) => { const r = new FileReader(); r.onload = () => ok(r.result); r.onerror = () => no(r.error); r.readAsDataURL(blob); });
  // A formula image (MathJax SVG) redrawn as a PNG at 3x, so the teacher's view needs no SVG and no fonts.
  const mathPng = (src) => loadImage(src).then((img) => {
    const w = img.naturalWidth, h = img.naturalHeight;
    if (!w || !h) return null;
    const c = document.createElement('canvas'); c.width = Math.ceil(w * 3); c.height = Math.ceil(h * 3);
    const g = c.getContext('2d'); g.scale(3, 3); g.drawImage(img, 0, 0, w, h);
    const png = c.toDataURL('image/png').split(',')[1];
    return png && bytesOfB64(png) <= LIMITS.mathPng ? { png, w, h } : null;
  }).catch(() => null);   // a browser that will not draw it: the formula goes as LaTeX only

  // The editor's HTML (read inertly: DOMParser runs no script and loads no picture) -> items in their order.
  const contentOf = async (html, where) => {
    const doc = new DOMParser().parseFromString('<div>' + html + '</div>', 'text/html');
    const raw = [];
    const text = (t) => { const last = raw[raw.length - 1]; if (last && last.type === 'text') last.text += t; else raw.push({ type: 'text', text: t }); };
    const walk = (node) => node.childNodes.forEach((n) => {
      if (n.nodeType === 3) text(n.nodeValue.replace(/ /g, ' '));
      else if (n.nodeType === 1) {
        const tag = n.tagName.toLowerCase();
        if (tag === 'br') text('\n');
        else if (tag === 'img') raw.push({ img: n });
        else if (tag === 'script' || tag === 'style') { /* never part of an answer */ }
        else { if (/^(div|p|li|h[1-6]|pre|blockquote)$/.test(tag) && raw.length) text('\n'); walk(n); }
      }
    });
    walk(doc.body.firstChild);
    const items = [];
    for (const r of raw) {
      if (r.type === 'text') { items.push(r); continue; }
      const img = r.img, src = img.getAttribute('src') || '', latex = img.getAttribute('data-latex') || img.getAttribute('alt') || '';
      if (/^data:image\/svg\+xml/.test(src) || /\/math\.svg\?latex=/.test(src)) {
        if (!latex.trim()) throw fail(S('img_type', { where }));   // an SVG that is no formula
        if (latex.length > LIMITS.latex) throw fail(S('latex_long', { where, n: LIMITS.latex }));
        const p = /^data:image\/svg\+xml/.test(src) ? await mathPng(src) : null;
        items.push(Object.assign({ type: 'math', latex }, p || {}));
        continue;
      }
      let url = src;
      if (/^blob:/.test(src)) {   // a picture the browser holds only for this page: turned into data in the file
        try { url = await readAsDataUrl(await (await fetch(src)).blob()); } catch (e) { throw fail(S('img_read', { where })); }
      }
      const m = /^data:(image\/(?:png|jpeg));base64,([A-Za-z0-9+/=]+)$/.exec(url);
      if (!m) throw fail(S(/^https?:/i.test(src) ? 'img_web' : 'img_type', { where }));
      const bytes = bytesOfB64(m[2]);
      if (bytes > LIMITS.image) throw fail(S('img_big', { where, mb: (bytes / 1e6).toFixed(1).replace('.', ','), max: LIMITS.image / 1e6 }));
      let size;
      try { size = await loadImage(url); } catch (e) { throw fail(S('img_broken', { where })); }
      if (size.naturalWidth > LIMITS.side || size.naturalHeight > LIMITS.side) throw fail(S('img_side', { where, n: LIMITS.side }));
      const item = { type: 'image', mime: m[1], data: m[2], w: size.naturalWidth, h: size.naturalHeight };
      // the size the student gave the picture in the editor (lesson.js imageSizer, teacher 2026-11-06): its width in CSS px
      const dw = Number(img.getAttribute('width'));
      if (Number.isInteger(dw) && dw >= 1 && dw < size.naturalWidth) item.dw = dw;
      items.push(item);
    }
    // trim the whitespace at both ends; a solution of only spaces and line breaks is empty
    const first = items[0], last = items[items.length - 1];
    if (first && first.type === 'text') first.text = first.text.replace(/^\s+/, '');
    if (last && last.type === 'text') last.text = last.text.replace(/\s+$/, '');
    const out = items.filter((i) => i.type !== 'text' || i.text !== '');
    if (out.length > LIMITS.items) throw fail(S('items', { where }));
    if (out.filter((i) => i.type === 'text').reduce((n, i) => n + i.text.length, 0) > LIMITS.text) throw fail(S('text_long', { where, n: LIMITS.text }));
    return out;
  };
  // A piece of the page as plain text with its formulas as $LaTeX$ (KaTeX's annotation, or the source still unrendered
  // in a closed box), without its controls and feedback.
  const plainOf = (node) => {
    if (!node) return '';
    const c = node.cloneNode(true);
    c.querySelectorAll('.katex').forEach((k) => { const a = k.querySelector('annotation'); k.replaceWith('$' + (a ? a.textContent : k.textContent) + '$'); });
    c.querySelectorAll('input, select, textarea, button, output, .feedback, .ord-right, .sa-rate, script, style, svg, .visually-hidden').forEach((x) => x.remove());
    return c.textContent.replace(/\s+/g, ' ').trim().slice(0, 2000);
  };
  const cellText = (td) => String(td.dataset.value ?? td.dataset.plain ?? plainOf(td)).trim().slice(0, 200);
  const responsesOf = (t) => {
    const out = [];
    own(t, CONTROLS).forEach((x) => {
      if (x.matches('form.check')) {
        const v = (x.querySelector('input') || {}).value || '';
        if (v.trim()) out.push(Object.assign({ type: 'number', value: v.trim().slice(0, 100) }, x.querySelector('.unit') ? { unit: plainOf(x.querySelector('.unit')).slice(0, 60) } : {}));
      } else if (x.matches('fieldset.choice')) {
        const r = x.querySelector('input[type=radio]:checked');
        if (r) out.push({ type: 'choice', question: plainOf(x.querySelector('legend')), answer: plainOf(r.closest('label')), option: Number(r.value) || 0 });
        const j = x.querySelector('.justify textarea');
        if (j && j.value.trim()) out.push({ type: 'text', label: plainOf(j.closest('label')), text: j.value.trim().slice(0, LIMITS.text) });
      } else if (x.matches('fieldset.tf')) {
        const items = [...x.querySelectorAll('.tf-list > li')].map((li) => { const c = li.querySelector('input:checked'); return { text: plainOf(li.querySelector('.tf-text')), value: c ? c.value === '1' : null }; });
        if (items.some((i) => i.value !== null)) out.push({ type: 'truefalse', items });
      } else if (x.matches('fieldset.order')) {
        const items = [...x.querySelectorAll('.order-list > li')].map((li) => { const v = li.querySelector('select').value; return { text: plainOf(li.querySelector('.ord-text')), rank: v ? Number(v) : null }; });
        if (items.some((i) => i.rank !== null)) out.push({ type: 'order', items });
      } else if (x.matches('.revise')) {
        const r = x.querySelector('input[type=radio]:checked');
        if (r) out.push({ type: 'choice', question: plainOf(x.querySelector('strong')), answer: plainOf(r.closest('label')), option: [...x.querySelectorAll('input[type=radio]')].indexOf(r) });
      } else if (x.matches('textarea')) {
        if (x.value.trim()) out.push({ type: 'text', label: (x.getAttribute('aria-label') || x.getAttribute('placeholder') || '').slice(0, 200), text: x.value.trim().slice(0, LIMITS.text) });
      } else if (x.matches('.experiment table.exp-table')) {
        const rows = [...x.querySelectorAll('tbody tr')].map((tr) => [...tr.children].map(cellText)).slice(0, 200);
        if (rows.length) out.push({ type: 'table', head: [...x.querySelectorAll('thead th')].map((th) => String(th.dataset.plain || plainOf(th)).slice(0, 200)), rows });
      }
    });
    return out;
  };
  const canonical = (answers) => JSON.stringify(answers.map((a) => ({ task: a.task, status: a.status,
    content: a.content.map((i) => (i.type === 'math' ? { type: 'math', latex: i.latex } : i)), responses: a.responses })));
  const sha256 = async (s) => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)))].map((b) => b.toString(16).padStart(2, '0')).join('');
  const newId = () => [...crypto.getRandomValues(new Uint8Array(16))].map((b) => b.toString(16).padStart(2, '0')).join('');
  const remembered = () => { try { return JSON.parse(localStorage.getItem(STORE_KEY) || 'null'); } catch (e) { return null; } };
  const remember = (v) => { try { localStorage.setItem(STORE_KEY, JSON.stringify(v)); } catch (e) { /* the next download gets a new id */ } };

  const build = async () => {
    if (window.flPads) {
      try { await window.flPads.flush(); } catch (e) { throw fail(S('flush')); }
    }
    await loadStore();
    const answers = [];
    for (const li of tasks) {
      const where = S('task', { n: numOf(li) });
      let html = null;
      if (isEd.has(li)) {
        try { html = await window.flPadStore.get(li.id); } catch (e) {
          throw fail(e && e.code === 'corrupt' ? S('corrupt', { where }) : S('no_storage'));
        }
      }
      const content = html ? await contentOf(html, where) : [];
      const responses = responsesOf(li);
      if (responses.filter((r) => r.type === 'text').reduce((n, r) => n + r.text.length, 0) + content.filter((i) => i.type === 'text').reduce((n, i) => n + i.text.length, 0) > LIMITS.text) throw fail(S('text_long', { where, n: LIMITS.text }));
      answers.push({ task: taskId(li), status: content.length || responses.length ? 'answered' : 'empty', content, responses });
    }
    const images = answers.reduce((n, a) => n + a.content.filter((i) => i.type === 'image').length, 0);
    if (images > LIMITS.images) throw fail(S('images', { n: images, max: LIMITS.images }));
    const self = goals();
    const sha = await sha256(JSON.stringify({ answers: JSON.parse(canonical(answers)), selfassessment: self }));
    const prev = remembered();
    const same = !!(prev && prev.sha === sha && /^[0-9a-f]{32}$/.test(prev.id || ''));
    const id = same ? prev.id : newId();
    const file = { format: FORMAT, version: VERSION, chapter: CHAPTER, lang: LANG, submission_id: id, exported: new Date().toISOString(),
      includes: 'answers', content_sha256: sha, answers, selfassessment: { goals: self } };
    const text = JSON.stringify(file);
    const size = new TextEncoder().encode(text).length;
    if (size > LIMITS.file) throw fail(S('file_big', { mb: (size / 1e6).toFixed(1).replace('.', ','), max: LIMITS.file / 1e6 }));
    return { text, id, same, sha, answers };
  };

  window.flChapterFile = ON_CHAPTER && tasks.length ? () => build().then((r) => { remember({ sha: r.sha, id: r.id }); return r.text; }) : null;
  const RETURN = ME && ME.dataset.return;
  if (COURSE) { courseWork(); return; }

  // Only the button at the top of Tehtävät (teacher 2026-11-05: "eikä pitkää ohjetta, pelkästään Lataa kaikki ratkaisut"),
  // in the heading row before "Avaa tehtävät teorian viereen" (teacher 2026-11-05); a short line under the row after the
  // download, or the reason when it could not be made.
  const box = el('div', 'palautus');
  const btn = el('button', 'pad-btn palautus-btn', S('download')); btn.type = 'button';
  const status = el('p', 'pad-status palautus-status'); status.setAttribute('aria-live', 'polite');
  box.append(status);
  const head = sec.querySelector(':scope > .split-head') || sec.querySelector(':scope > h2');   // lesson.js part 9 wraps the heading
  // "Palauta" (teacher 2026-11-06): to the page of the groups' Forms links, when build.py palautukset.json names them
  const go = RETURN ? el('a', 'pad-btn palautus-btn palautus-link', S('return')) : null;
  if (go) go.href = RETURN;
  const btns = go ? [btn, go] : [btn];
  if (head && head.matches('.split-head')) { const t = head.querySelector(':scope > .split-toggle'); if (t) t.before(...btns); else head.append(...btns); }
  else box.prepend(...btns);
  if (head) head.after(box); else sec.prepend(box);

  let busy = false;
  btn.addEventListener('click', async () => {
    if (busy) return;
    busy = true; btn.disabled = true; say(status, S('busy'));
    try {
      const r = await build();
      const a = document.createElement('a');
      a.href = URL.createObjectURL(new Blob([r.text], { type: 'application/json' }));
      a.download = `${CHAPTER}.ratkaisut.json`; document.body.append(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(a.href), 4000);
      remember({ sha: r.sha, id: r.id });
      say(status, S(go ? 'done_link' : 'done_forms'), 'ok');
    } catch (e) {
      say(status, e && e.user ? e.message : S('failed'), 'no');
    } finally { busy = false; btn.disabled = false; }
  });


  /* Work file (teacher 2026-11-07, "yksi työ opintojaksoa kohti"): the whole module in one file, the same from every
     chapter's Tehtävät (Tallenna työ tiedostoon, Palauta) and from the module page (Tallenna työ tiedostoon, Avaa
     tallennettu työ). Nothing leaves this browser until the student attaches the file to the group's form.
       { format: "ruukkilabra-tyo", version: 1, course, lang, created: ISO time, submission_id: 32 hex, content_sha256,
         chapters: [ { chapter, answers: [ { task, status: "answered", content: [item], responses: [{ type: "number", value }] } ],
                       selfassessment: { goals: [ { id: "tavoite-<n>", text: "", level } ] } } ],   (chapters with work only)
         progress: tehty.js progress (course, assigned, done [[id, ISO]], history [[id, ISO, 1|0]]) | null,
         store: { local: { key: value }, solutions: [padstore record] } }
     `store` is what this browser keeps of the module (padstore.js records whose id starts "fy3-", localStorage keys of
     the module's pages: answers, choices, explanations, tables, self-assessment), so "Avaa tallennettu työ" brings back
     exactly that. `chapters` is the teacher's view (palautus/apps-script): the editor's solutions as items (a picture's
     data stays in store.solutions, the item has its place `ref`; a formula is its LaTeX and PNG), the typed numbers and the goals'
     levels. content_sha256 = SHA-256 of JSON.stringify({ chapters, progress, store }). The name is
     Ruukkilabra_<COURSE>_<date>_<time>.json, a new time every save; the ticks keep their own times. */
  function courseWork() {
    const WFORMAT = 'ruukkilabra-tyo', WVERSION = 1, CODE = COURSE.course, PRE = CODE.toLowerCase() + '-';
    const KEY_RE = new RegExp('(^|[:/])' + CODE.toLowerCase() + '-[a-z0-9]', 'i');
    const ownKey = (k) => /^(fl:|ruukkilabra:)/.test(k) && k !== 'ruukkilabra:tehty' && !k.startsWith('ruukkilabra:palautus:') && KEY_RE.test(k);
    const ownRec = (r) => r && typeof r.id === 'string' && r.id.toLowerCase().startsWith(PRE);
    const WKEY = 'ruukkilabra:palautus:' + CODE;
    const readLocal = () => {
      const out = {};
      try { for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (ownKey(k)) out[k] = localStorage.getItem(k); } } catch (e) { /* no storage */ }
      const sorted = {}; Object.keys(out).sort().forEach((k) => { sorted[k] = out[k]; });
      return sorted;
    };
    const pad2 = (n) => String(n).padStart(2, '0');
    const fileName = (d) => `Ruukkilabra_${CODE}_${d.getFullYear()}-${pad2(d.getMonth() + 1)}-${pad2(d.getDate())}_${pad2(d.getHours())}${pad2(d.getMinutes())}${pad2(d.getSeconds())}.json`;
    const make = async () => {
      if (window.flPads) { try { await window.flPads.flush(); } catch (e) { throw fail(S('flush')); } }
      try { await loadStore(); } catch (e) { throw fail(S('store')); }
      let all;
      try { all = await window.flPadStore.all(); } catch (e) { throw fail(S('no_storage')); }
      const sols = all.solutions.filter(ownRec).sort((a, b) => (a.id < b.id ? -1 : a.id > b.id ? 1 : 0));
      const byId = new Map(sols.map((r) => [r.id, r]));
      const local = readLocal();
      const numbers = {};
      Object.keys(local).filter((k) => k.startsWith('ruukkilabra:vastaukset:')).forEach((k) => {
        try { const v = JSON.parse(local[k]); Object.keys((v && v.items) || {}).forEach((ik) => { const m = /^(.+):num\d+$/.exec(ik), val = v.items[ik];
          if (m && typeof val === 'string' && val.trim()) (numbers[m[1]] = numbers[m[1]] || []).push(val.trim().slice(0, 100)); }); } catch (e) { /* damaged: left out */ }
      });
      const chapters = [];
      let images = 0;
      for (const ch of COURSE.chapters) {
        const answers = [];
        for (let i = 0; i < ch.tasks.length; i++) {
          const id = ch.tasks[i], r = byId.get(id), where = S('task', { n: ch.n + '-' + (i + 1) });
          const content = r ? await contentOf(r.html, where) : [];
          // a picture and a MathJax formula are in the file once, in store.solutions; here only their place (ref, sref).
          // A formula drawn on Abitti's server (/math.svg?latex=) has no SVG in the file: its PNG stays.
          const own = r ? [...new DOMParser().parseFromString('<div>' + r.html + '</div>', 'text/html').querySelectorAll('img')].map((m) => m.getAttribute('src') || '')
            .filter((s) => /^data:image\/svg\+xml/.test(s) || /\/math\.svg\?latex=/.test(s)).map((s) => /^data:image\/svg\+xml;base64,/.test(s)) : [];
          let k = 0, f = 0, svgs = 0;
          content.forEach((it) => {
            if (it.type === 'image') { delete it.data; it.ref = k++; images++; }
            else if (it.type === 'math' && own[f++]) { delete it.png; it.sref = svgs++; }
          });
          const responses = (numbers[id] || []).map((value) => ({ type: 'number', value }));
          if (content.length || responses.length) answers.push({ task: id, status: 'answered', content, responses });
        }
        let goals = [];
        try { const v = JSON.parse(local['ruukkilabra:itsearvio:' + ch.id] || 'null');
          if (v && v.items) goals = Object.keys(v.items).filter((g) => /^tavoite-\d+$/.test(g) && v.items[g] && SA_LEVEL.test(v.items[g].level))
            .sort((a, b) => parseInt(a.slice(8), 10) - parseInt(b.slice(8), 10)).map((g) => ({ id: g, text: '', level: v.items[g].level })); } catch (e) { /* none */ }
        if (answers.length || goals.length) chapters.push({ chapter: ch.id, answers, selfassessment: { goals } });
      }
      if (images > LIMITS.images * 8) throw fail(S('images', { n: images, max: LIMITS.images * 8 }));
      const progress = window.flDone ? window.flDone.progress() : null;
      const body = { chapters, progress, store: { local, solutions: sols } };
      const sha = await sha256(JSON.stringify(body));
      let prev = null; try { prev = JSON.parse(localStorage.getItem(WKEY) || 'null'); } catch (e) { /* a new id */ }
      const id = prev && prev.sha === sha && /^[0-9a-f]{32}$/.test(prev.id || '') ? prev.id : newId();
      const now = new Date();
      const text = JSON.stringify(Object.assign({ format: WFORMAT, version: WVERSION, course: CODE, lang: LANG, created: now.toISOString(), submission_id: id, content_sha256: sha }, body));
      const size = new TextEncoder().encode(text).length;
      if (size > LIMITS.file) throw fail(S('file_big', { mb: (size / 1e6).toFixed(1).replace('.', ','), max: LIMITS.file / 1e6 }));
      try { localStorage.setItem(WKEY, JSON.stringify({ sha, id })); } catch (e) { /* the next save gets a new id */ }
      return { text, name: fileName(now), mb: Math.max(0.1, size / 1e6).toFixed(1).replace('.', LANG === 'en' ? '.' : ',') };
    };
    const save = async () => {
      const r = await make();
      const a = document.createElement('a');
      a.href = URL.createObjectURL(new Blob([r.text], { type: 'application/json' }));
      a.download = r.name; document.body.append(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(a.href), 4000);
      return r;
    };
    // Avaa tallennettu työ: the file is checked whole (format, version, module, checksum, every record) before anything
    // is written. What this browser does not have is added; where both differ, one question: the file replaces them
    // (OK) or this browser's stay and only the missing come from the file (Cancel). Then the page is reloaded.
    const open = async (text) => {
      let d;
      try { d = JSON.parse(text); } catch (e) { throw fail(S('broken')); }
      if (!d || d.format !== WFORMAT || typeof d.version !== 'number') throw fail(S('broken'));
      if (d.version > WVERSION) throw fail(S('newer'));
      if (d.course !== CODE) throw fail(S('wrong_course', { c: String(d.course).slice(0, 10) }));
      const st = d.store;
      if (!st || typeof st !== 'object' || !Array.isArray(st.solutions) || !st.local || typeof st.local !== 'object' || Array.isArray(st.local)) throw fail(S('broken'));
      if (await sha256(JSON.stringify({ chapters: d.chapters, progress: d.progress, store: d.store })) !== d.content_sha256) throw fail(S('broken'));
      const sols = st.solutions.filter((r) => ownRec(r) && typeof r.html === 'string');
      const local = Object.keys(st.local).filter((k) => ownKey(k) && typeof st.local[k] === 'string');
      if (sols.length !== st.solutions.length || local.length !== Object.keys(st.local).length) throw fail(S('broken'));
      try { await loadStore(); } catch (e) { throw fail(S('open_failed')); }
      let mine;
      try { mine = new Map((await window.flPadStore.all()).solutions.map((r) => [r.id, r])); } catch (e) { throw fail(S('open_failed')); }
      let have = {};
      try { localStorage.length; have = readLocal(); } catch (e) { throw fail(S('open_failed')); }
      const diffS = sols.filter((r) => mine.has(r.id) && mine.get(r.id).html !== r.html);
      const diffL = local.filter((k) => k in have && have[k] !== st.local[k]);
      const newer = diffS.filter((r) => (mine.get(r.id).updated || '') > (r.updated || '')).length;
      const replace = diffS.length + diffL.length > 0 && window.confirm(S('conflict', { n: diffS.length + diffL.length, newer }));
      const putS = sols.filter((r) => !mine.has(r.id) || (replace && mine.get(r.id).html !== r.html));
      const putL = local.filter((k) => !(k in have) || (replace && have[k] !== st.local[k]));
      try { if (putS.length) await window.flPadStore.putAll(putS); } catch (e) { throw fail(S('open_failed')); }
      try { putL.forEach((k) => localStorage.setItem(k, st.local[k])); } catch (e) { throw fail(S('open_failed')); }
      const p = d.progress;
      if (p && Array.isArray(p.done) && Array.isArray(p.history)) window.flPadStore.mergeDone({ v: 1, done: Object.fromEntries(p.done.filter((x) => Array.isArray(x) && x.length === 2)), log: p.history }, replace);
      return { n: putS.length, m: putL.length };
    };
    window.flWork = { make, save, open };

    const saveBtn = el('button', 'pad-btn palautus-btn', S('save')); saveBtn.type = 'button';
    const status = el('p', 'pad-status palautus-status'); status.setAttribute('aria-live', 'polite');
    let busy = false;
    const run = async (b, work) => {
      if (busy) return; busy = true; b.disabled = true; say(status, S('busy'));
      try { await work(); } catch (e) { say(status, e && e.user ? e.message : S('failed'), 'no'); } finally { busy = false; b.disabled = false; }
    };
    saveBtn.addEventListener('click', () => run(saveBtn, async () => { const r = await save(); say(status, S('saved', { name: r.name, mb: r.mb }), 'ok'); }));
    // a message carried over the reload after Avaa tallennettu työ
    try { const m = sessionStorage.getItem('ruukkilabra:avattu'); if (m) { sessionStorage.removeItem('ruukkilabra:avattu'); setTimeout(() => say(status, m, 'ok'), 0); } } catch (e) { /* none */ }
    if (ON_CHAPTER) {
      // Tehtävät's heading row: Tallenna työ tiedostoon, Palauta (the file first, then the group's form), Avaa tehtävät teorian viereen
      const box = el('div', 'palautus'); box.append(status);
      const btns = [saveBtn];
      if (RETURN) {
        const go = el('button', 'pad-btn palautus-btn palautus-link', S('return')); go.type = 'button';
        go.addEventListener('click', () => run(go, async () => { await save(); say(status, S('done_link'), 'ok'); setTimeout(() => { location.href = RETURN; }, 700); }));
        btns.push(go);
      }
      const head = sec.querySelector(':scope > .split-head') || sec.querySelector(':scope > h2');
      if (head && head.matches('.split-head')) { const t = head.querySelector(':scope > .split-toggle'); if (t) t.before(...btns); else head.append(...btns); }
      else box.prepend(...btns);
      if (head) head.after(box); else sec.prepend(box);
    } else {
      const host = document.getElementById('oma-tyo');
      if (!host) return;
      const openBtn = el('button', 'pad-btn palautus-btn', S('open')); openBtn.type = 'button';
      const file = el('input'); file.type = 'file'; file.accept = 'application/json,.json'; file.hidden = true;
      openBtn.addEventListener('click', () => file.click());
      file.addEventListener('change', () => {
        const f = file.files && file.files[0]; file.value = '';
        if (!f) return;
        run(openBtn, async () => {
          const r = await open(await f.text());
          const m = r.n || r.m ? S('opened', { n: r.n, m: r.m }) : S('nothing');
          try { sessionStorage.setItem('ruukkilabra:avattu', m); } catch (e) { /* the page says nothing after the reload */ }
          location.reload();
        });
      });
      const row = el('div', 'work-row'); row.append(saveBtn, openBtn, file);
      host.append(row, status); host.hidden = false;
    }
  }
})();
