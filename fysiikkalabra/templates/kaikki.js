/* The whole work in one file (work queue 17b PR 1, teacher 2026-11-15 K3): on Tietosuoja, under "Mitä selaimeesi
   tallentuu?", Tallenna kaikki työni tiedostoon and Avaa kaikki työni tiedostosta. A backup of this browser's own
   storage, made and opened here; nothing is sent anywhere. It is not a submission: the teacher's grading page rejects it.

     { format: "ruukkilabra-kaikki", version: 1, lang, created: ISO time, content_sha256,
       modules: { "FY3": { store: { local: { key: text }, solutions: [padstore record] } }, ... },   (modules with work only)
       progress: padstore readDone() { v: 1, done: { id: ISO }, log: [[id, ISO, 1|0]] } | null,
       site: { "ruukkilabra:kortit": text, "ruukkilabra:kortit-suunta": text, "ruukkilabra:viimeisin": text } }   (keys present only)
   Each module's store is exactly the one of the module's work file ("ruukkilabra-tyo" v1; padstore.js work()), so both
   files read and write a module with the same code and the same merge rule: what this browser lacks is added, and where
   both differ one question: the file replaces them (OK) or this browser's stay (Cancel). content_sha256 = SHA-256 of
   JSON.stringify({ modules, progress, site }). The module's work file gains nothing (it goes to the teacher).
   Texts: lang/<lang>.json js.kaikki_* and the module work file's js.palautus_* (build.py kaikki_block, #fl-kaikki). */
(() => {
  const host = document.getElementById('kaikki-tyo');
  const T = (() => { try { return JSON.parse(document.getElementById('fl-kaikki').textContent); } catch (e) { return {}; } })();
  if (!host || !window.flPadStore) return;
  const ps = window.flPadStore;
  const FORMAT = 'ruukkilabra-kaikki', VERSION = 1;
  const SITE_KEYS = ['ruukkilabra:kortit', 'ruukkilabra:kortit-suunta', 'ruukkilabra:viimeisin'];
  const MODULE_ID = /(?:^|[:/])(fy\d+)-[a-z0-9]/i;
  const S = (k, v) => String(T[k] || '').replace(/\{\{(\w+)\}\}/g, (m, n) => (v && n in v ? String(v[n]) : m));
  const fail = (key) => { const e = new Error(S(key)); e.user = true; return e; };
  const sha256 = async (s) => [...new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s)))].map((b) => b.toString(16).padStart(2, '0')).join('');
  const pad2 = (n) => String(n).padStart(2, '0');
  const fileName = (d) => `Ruukkilabra_kaikki_${d.getFullYear()}-${pad2(d.getMonth() + 1)}-${pad2(d.getDate())}_${pad2(d.getHours())}${pad2(d.getMinutes())}${pad2(d.getSeconds())}.json`;
  const getItem = (k) => { try { return localStorage.getItem(k); } catch (e) { return null; } };

  const make = async () => {
    let all;
    try { all = (await ps.all()).solutions; } catch (e) { throw fail('palautus_no_storage'); }
    const codes = new Set();
    const note = (id) => { const m = MODULE_ID.exec(id); if (m) codes.add(m[1].toUpperCase()); };
    all.forEach((r) => note(r.id));
    try {
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (/^(fl:|ruukkilabra:)/.test(k) && k !== 'ruukkilabra:tehty' && !k.startsWith('ruukkilabra:palautus:')) note(k);
      }
      ['ruukkilabra:ratkaistu', 'ruukkilabra:tarkistettu'].forEach((k) => { try { Object.keys(JSON.parse(localStorage.getItem(k) || '{}') || {}).forEach(note); } catch (e) { /* damaged: left out */ } });
    } catch (e) { throw fail('palautus_no_storage'); }
    const modules = {};
    [...codes].sort().forEach((code) => {
      const W = ps.work(code), local = W.readLocal(), solutions = all.filter(W.ownRec).sort((a, b) => (a.id < b.id ? -1 : a.id > b.id ? 1 : 0));
      if (solutions.length || Object.keys(local).length) modules[code] = { store: { local, solutions } };
    });
    const site = {};
    SITE_KEYS.forEach((k) => { const v = getItem(k); if (typeof v === 'string') site[k] = v; });
    const body = { modules, progress: ps.readDone(), site };
    const now = new Date();
    const text = JSON.stringify(Object.assign({ format: FORMAT, version: VERSION, lang: (document.documentElement.lang || 'fi').slice(0, 2), created: now.toISOString(), content_sha256: await sha256(JSON.stringify(body)) }, body));
    return { text, name: fileName(now) };
  };
  const save = async () => {
    const r = await make();
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([r.text], { type: 'application/json' }));
    a.download = r.name; document.body.append(a); a.click(); a.remove();
    setTimeout(() => URL.revokeObjectURL(a.href), 4000);
  };

  // the file is checked whole before anything is written; then one question for every module and the site keys together
  const open = async (text) => {
    let d;
    try { d = JSON.parse(text); } catch (e) { throw fail('palautus_broken'); }
    if (d && (d.format === 'ruukkilabra-tyo' || d.format === 'ruukkilabra-palautus')) throw fail('kaikki_wrong');
    if (!d || d.format !== FORMAT || typeof d.version !== 'number') throw fail('palautus_broken');
    if (d.version > VERSION) throw fail('palautus_newer');
    const isObj = (x) => x && typeof x === 'object' && !Array.isArray(x);
    if (!isObj(d.modules) || !isObj(d.site) || (d.progress !== null && !isObj(d.progress))) throw fail('palautus_broken');
    if (await sha256(JSON.stringify({ modules: d.modules, progress: d.progress, site: d.site })) !== d.content_sha256) throw fail('palautus_broken');
    const parts = [];
    for (const code of Object.keys(d.modules)) {
      const st = d.modules[code] && d.modules[code].store, W = /^FY\d+$/.test(code) ? ps.work(code) : null;
      if (!W || !isObj(st) || !Array.isArray(st.solutions) || !isObj(st.local)) throw fail('palautus_broken');
      const keys = Object.keys(st.local);
      if (st.solutions.some((r) => !W.ownRec(r) || typeof r.html !== 'string') || keys.some((k) => !W.ownKey(k) || typeof st.local[k] !== 'string')) throw fail('palautus_broken');
      parts.push({ W, sols: st.solutions, local: st.local });
    }
    const siteKeys = Object.keys(d.site);
    const json = (t) => { try { return isObj(JSON.parse(t)); } catch (e) { return false; } };
    // the deck and the last chapter are JSON objects; the card direction is one short word (kortit.js)
    const okSite = (k, v) => typeof v === 'string' && (k === 'ruukkilabra:kortit-suunta' ? /^[\w-]{1,40}$/.test(v) : json(v));
    if (siteKeys.some((k) => !SITE_KEYS.includes(k) || !okSite(k, d.site[k]))) throw fail('palautus_broken');
    try {
      for (const p of parts) p.plan = await p.W.plan(p.sols, p.local);
      const diffSite = siteKeys.filter((k) => getItem(k) !== null && getItem(k) !== d.site[k]);
      const differs = parts.reduce((n, p) => n + p.plan.differs, 0) + diffSite.length;
      const newer = parts.reduce((n, p) => n + p.plan.newer, 0);
      const replace = differs > 0 && window.confirm(S('palautus_conflict', { n: differs, newer }));
      let n = 0, m = 0;
      for (const p of parts) { const r = await p.W.apply(p.plan, replace); n += r.n; m += r.m; }
      siteKeys.filter((k) => getItem(k) === null || (replace && getItem(k) !== d.site[k])).forEach((k) => { localStorage.setItem(k, d.site[k]); m++; });
      const p = d.progress;
      if (p && isObj(p.done) && Array.isArray(p.log)) ps.mergeDone(p, replace);
      return { n, m };
    } catch (e) { throw fail('palautus_open_failed'); }
  };

  const status = document.createElement('p'); status.className = 'pad-status palautus-status'; status.setAttribute('aria-live', 'polite');
  const say = (t, state) => { status.textContent = t; if (state) status.dataset.state = state; else delete status.dataset.state; };
  let busy = false;
  const run = async (b, work) => {
    if (busy) return; busy = true; b.disabled = true; say(S('palautus_busy'));
    try { await work(); } catch (e) { say(e && e.user ? e.message : S('palautus_failed'), 'no'); } finally { busy = false; b.disabled = false; }
  };
  const btn = (label) => { const b = document.createElement('button'); b.type = 'button'; b.className = 'pad-btn palautus-btn'; b.textContent = label; return b; };
  const saveBtn = btn(S('kaikki_save')), openBtn = btn(S('kaikki_open'));
  const file = document.createElement('input'); file.type = 'file'; file.accept = 'application/json,.json'; file.hidden = true;
  saveBtn.addEventListener('click', () => run(saveBtn, async () => { await save(); say(''); }));
  openBtn.addEventListener('click', () => file.click());
  file.addEventListener('change', () => {
    const f = file.files && file.files[0]; file.value = '';
    if (!f) return;
    run(openBtn, async () => {
      const r = await open(await f.text());
      const m = r.n || r.m ? S('palautus_opened', { n: r.n, m: r.m }) : S('palautus_nothing');
      try { sessionStorage.setItem('ruukkilabra:avattu', m); } catch (e) { /* the page says nothing after the reload */ }
      location.reload();
    });
  });
  try { const m = sessionStorage.getItem('ruukkilabra:avattu'); if (m) { sessionStorage.removeItem('ruukkilabra:avattu'); setTimeout(() => say(m, 'ok'), 0); } } catch (e) { /* none */ }
  const row = document.createElement('div'); row.className = 'work-row'; row.append(saveBtn, openBtn, file);
  host.append(row, status); host.hidden = false;
})();
