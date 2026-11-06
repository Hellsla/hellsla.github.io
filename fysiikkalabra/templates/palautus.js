/* Submission trial (teacher 2026-11-05, "palautus- ja arviointikokeilu"; Finnish FY3-1 only, build.py SUBMISSION_PAGES).
   "Lataa kaikki ratkaisut" writes one file, <chapter>.ratkaisut.json, from the solutions the student wrote in this chapter's
   solution editors (lesson.js part 6, kept on this device by padstore.js). The student returns the file with the
   school's Google Forms form; the teacher's Apps Script (palautus/apps-script/) reads and grades it. Ruukkilabra
   itself sends nothing anywhere: the file is made in this browser and saved on this device.

   File format "ruukkilabra-palautus", version 1 (palautus/TIEDOSTOMUOTO.md is the full description):
     { format, version: 1, chapter, lang, submission_id: 32 hex, exported: ISO time, includes: "solution-editor",
       content_sha256, answers: [ { task, status: "answered" | "empty", content: [item, ...] }, ... ] }
     item = { type: "text", text } | { type: "math", latex, png?, w?, h? } | { type: "image", mime, data, w, h }
   Every exercise of the chapter is in `answers`, in page order, an unanswered one as "empty" with no content, so the
   teacher can tell an unanswered task from a missing or broken file. Text keeps its line breaks ("\n"); a formula is
   its LaTeX (the formula image is redrawn as a PNG, `png`, for the teacher's view); a picture is PNG or JPEG data
   (base64, no "data:" prefix), pasted into the editor with Ctrl+V (teacher 2026-11-05: no separate image button).
   Items keep the order of the solution. No name, e-mail or other chapters.
   content_sha256 is the SHA-256 of the answers without the formula PNGs (JSON, UTF-8): the same solutions keep the
   same random submission_id (kept in localStorage ruukkilabra:palautus:<chapter>), any change gives a new one. */
(() => {
  const ME = document.currentScript;
  const CHAPTER = ME && ME.dataset.chapter;
  const HERE = ME ? ME.src : location.href;
  const FORMAT = 'ruukkilabra-palautus', VERSION = 1;
  // Limits, the same in the teacher's Apps Script (Code.gs RL_LIMITS): Forms takes a file of at most 10 MB when the
  // teacher picks that size; a picture of 2 MB is a full-screen screenshot, and the teacher's view loads one task at a time.
  const LIMITS = { file: 9000000, image: 2000000, side: 5000, images: 40, text: 20000, latex: 4000, items: 400, mathPng: 200000 };
  const STORE_KEY = 'ruukkilabra:palautus:' + CHAPTER;
  const sec = document.getElementById('exercises');
  if (!CHAPTER || !sec || document.documentElement.lang !== 'fi') return;
  const tasks = [...sec.querySelectorAll('li[id]')].filter((li) => li.querySelector(':scope > .task'));
  if (!tasks.length) return;
  const numOf = (li) => li.dataset.num || li.id;
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
  const say = (node, text, state) => { node.textContent = text; if (state) node.dataset.state = state; else delete node.dataset.state; };
  const fail = (text) => { const e = new Error(text); e.user = true; return e; };
  const bytesOfB64 = (b64) => Math.floor(b64.length * 3 / 4) - (b64.endsWith('==') ? 2 : b64.endsWith('=') ? 1 : 0);

  const loadStore = () => (window.flPadStore ? Promise.resolve() : new Promise((ok, no) => {
    const s = document.createElement('script'); s.src = new URL('padstore.js', HERE).href; s.onload = ok; s.onerror = () => no(fail('Tallennettuja ratkaisuja ei voitu lukea. Lataa sivu uudelleen.')); document.head.append(s);
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
        if (!latex.trim()) throw fail(`${where}: ratkaisussa on kuva, jonka muoto ei kelpaa (vain PNG ja JPEG). Poista se ja liitä kuva uudelleen.`);   // an SVG that is no formula
        if (latex.length > LIMITS.latex) throw fail(`${where}: kaava on liian pitkä (yli ${LIMITS.latex} merkkiä).`);
        const p = /^data:image\/svg\+xml/.test(src) ? await mathPng(src) : null;
        items.push(Object.assign({ type: 'math', latex }, p || {}));
        continue;
      }
      let url = src;
      if (/^blob:/.test(src)) {   // a picture the browser holds only for this page: turned into data in the file
        try { url = await readAsDataUrl(await (await fetch(src)).blob()); } catch (e) { throw fail(`${where}: kuvaa ei voitu lukea. Poista kuva ja liitä se uudelleen.`); }
      }
      const m = /^data:(image\/(?:png|jpeg));base64,([A-Za-z0-9+/=]+)$/.exec(url);
      if (!m) throw fail(/^https?:/i.test(src) ? `${where}: ratkaisussa on verkkosivulta liitetty kuva, jota ei voi palauttaa. Poista se ja liitä kuvakaappaus.`
                                               : `${where}: ratkaisussa on kuva, jonka muoto ei kelpaa (vain PNG ja JPEG). Poista se ja liitä kuva uudelleen.`);
      const bytes = bytesOfB64(m[2]);
      if (bytes > LIMITS.image) throw fail(`${where}: kuva on liian suuri (${(bytes / 1e6).toFixed(1).replace('.', ',')} Mt, enintään ${LIMITS.image / 1e6} Mt). Rajaa kuvakaappaus pienemmäksi ja liitä se uudelleen.`);
      let size;
      try { size = await loadImage(url); } catch (e) { throw fail(`${where}: kuva on vioittunut. Poista se ja liitä kuva uudelleen.`); }
      if (size.naturalWidth > LIMITS.side || size.naturalHeight > LIMITS.side) throw fail(`${where}: kuva on liian suuri (yli ${LIMITS.side} pikseliä leveä tai korkea).`);
      items.push({ type: 'image', mime: m[1], data: m[2], w: size.naturalWidth, h: size.naturalHeight });
    }
    // trim the whitespace at both ends; a solution of only spaces and line breaks is empty
    const first = items[0], last = items[items.length - 1];
    if (first && first.type === 'text') first.text = first.text.replace(/^\s+/, '');
    if (last && last.type === 'text') last.text = last.text.replace(/\s+$/, '');
    const out = items.filter((i) => i.type !== 'text' || i.text !== '');
    if (out.length > LIMITS.items) throw fail(`${where}: ratkaisussa on liian monta osaa.`);
    if (out.filter((i) => i.type === 'text').reduce((n, i) => n + i.text.length, 0) > LIMITS.text) throw fail(`${where}: ratkaisun teksti on liian pitkä (yli ${LIMITS.text} merkkiä).`);
    return out;
  };
  const canonical = (answers) => JSON.stringify(answers.map((a) => ({ task: a.task, status: a.status,
    content: a.content.map((i) => (i.type === 'math' ? { type: 'math', latex: i.latex } : i)) })));
  const sha256 = async (s) => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)))].map((b) => b.toString(16).padStart(2, '0')).join('');
  const newId = () => [...crypto.getRandomValues(new Uint8Array(16))].map((b) => b.toString(16).padStart(2, '0')).join('');
  const remembered = () => { try { return JSON.parse(localStorage.getItem(STORE_KEY) || 'null'); } catch (e) { return null; } };
  const remember = (v) => { try { localStorage.setItem(STORE_KEY, JSON.stringify(v)); } catch (e) { /* the next download gets a new id */ } };

  const build = async () => {
    if (window.flPads) {
      try { await window.flPads.flush(); } catch (e) { throw fail('Kaikkia avoimia ratkaisuja ei saatu tallennettua, joten tiedostoa ei ladattu. Katso virheilmoitus ratkaisun alta ja yritä uudelleen.'); }
    }
    await loadStore();
    const answers = [];
    for (const li of tasks) {
      const where = `Tehtävä ${numOf(li)}`;
      let html;
      try { html = await window.flPadStore.get(li.id); } catch (e) {
        throw fail(e && e.code === 'corrupt' ? `${where}: tallennettu ratkaisu on vioittunut. Kirjoita ratkaisu uudelleen.` : 'Tallennettuja ratkaisuja ei voitu lukea (selain ei salli tallennusta). Tiedostoa ei ladattu.');
      }
      const content = html ? await contentOf(html, where) : [];
      answers.push({ task: li.id, status: content.length ? 'answered' : 'empty', content });
    }
    const images = answers.reduce((n, a) => n + a.content.filter((i) => i.type === 'image').length, 0);
    if (images > LIMITS.images) throw fail(`Ratkaisuissa on ${images} kuvaa, enintään ${LIMITS.images}. Poista osa kuvista.`);
    const sha = await sha256(canonical(answers));
    const prev = remembered();
    const same = !!(prev && prev.sha === sha && /^[0-9a-f]{32}$/.test(prev.id || ''));
    const id = same ? prev.id : newId();
    const file = { format: FORMAT, version: VERSION, chapter: CHAPTER, lang: 'fi', submission_id: id, exported: new Date().toISOString(),
      includes: 'solution-editor', content_sha256: sha, answers };
    const text = JSON.stringify(file);
    const size = new TextEncoder().encode(text).length;
    if (size > LIMITS.file) throw fail(`Tiedostosta tulisi liian suuri (${(size / 1e6).toFixed(1).replace('.', ',')} Mt, enintään ${LIMITS.file / 1e6} Mt). Rajaa tai poista kuvia.`);
    return { text, id, same, sha, answers };
  };

  // Only the button at the top of Tehtävät (teacher 2026-11-05: "eikä pitkää ohjetta, pelkästään Lataa kaikki ratkaisut"),
  // in the heading row before "Avaa tehtävät teorian viereen" (teacher 2026-11-05); a short line under the row after the
  // download, or the reason when it could not be made.
  const box = el('div', 'palautus');
  const btn = el('button', 'pad-btn palautus-btn', 'Lataa kaikki ratkaisut'); btn.type = 'button';
  const status = el('p', 'pad-status palautus-status'); status.setAttribute('aria-live', 'polite');
  box.append(status);
  const head = sec.querySelector(':scope > .split-head') || sec.querySelector(':scope > h2');   // lesson.js part 9 wraps the heading
  // "Palauta" (teacher 2026-11-06): to the page of the groups' Forms links, when build.py palautukset.json names them
  const RETURN = ME && ME.dataset.return;
  const go = RETURN ? el('a', 'pad-btn palautus-btn palautus-link', 'Palauta') : null;
  if (go) go.href = RETURN;
  const btns = go ? [btn, go] : [btn];
  if (head && head.matches('.split-head')) { const t = head.querySelector(':scope > .split-toggle'); if (t) t.before(...btns); else head.append(...btns); }
  else box.prepend(...btns);
  if (head) head.after(box); else sec.prepend(box);

  let busy = false;
  btn.addEventListener('click', async () => {
    if (busy) return;
    busy = true; btn.disabled = true; say(status, 'Tallennetaan ja kootaan ratkaisuja…');
    try {
      const r = await build();
      const a = document.createElement('a');
      a.href = URL.createObjectURL(new Blob([r.text], { type: 'application/json' }));
      a.download = `${CHAPTER}.ratkaisut.json`; document.body.append(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(a.href), 4000);
      remember({ sha: r.sha, id: r.id });
      say(status, go ? 'Palauta ladattu tiedosto Palauta-napista oman ryhmäsi lomakkeella.' : 'Palauta ladattu tiedosto opettajan Google Forms -lomakkeella.', 'ok');
    } catch (e) {
      say(status, e && e.user ? e.message : 'Tiedostoa ei voitu koota. Lataa sivu uudelleen ja yritä uudelleen.', 'no');
    } finally { busy = false; btn.disabled = false; }
  });

})();
