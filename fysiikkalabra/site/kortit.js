/* Käsitetakomo concept cards (teacher 2026-11-03, scripts/concept_cards.py): one card component everywhere.
   A card flips with its button (Enter or Space, aria-expanded) to show the definition and the formula; after the flip
   "Osasin" and "Kertaa myöhemmin". The marks stay on this device only, in localStorage "ruukkilabra:kortit":
   { [card id]: { tila: "osasin" | "kertaa", osasinPutki: n, muokattu: ms } }. "Kertaa myöhemmin" (or "Lisää
   kertauspakkaan") puts a card in the student's review deck (tila "kertaa"); three "Osasin" in a row take it out.
   Nothing is sent anywhere. Each .kc-data element (written by the build) holds the cards and the texts of one place:
     .kc-section   a lesson, the end of Harjoittele: the chapter's cards two at a time (row()), and in
                   Teoriatiivistelmä the popovers of bold terms (strong[data-kortti]) and the chips after the summary list
     .kc-deck      a module page: "Kertauspakkasi", the deck's count and chapters, "Kertaa nyt"
     .kc-practice  Sovella itsenäisesti: the deck's cards of the module (the section stays hidden when there are none)
     .kc-app       site/kasitteet.html: modules, topics (combined), the own deck, one chapter; reads site/kortit/*.json
   Without JavaScript the build's definition lists stay and no popover is made. */
(() => {
  'use strict';
  const KEY = 'ruukkilabra:kortit', MODE_KEY = 'ruukkilabra:kortit-suunta', STREAK = 3;
  let storeOk = true;
  const SELF = (document.currentScript && document.currentScript.src) || '';
  const BASE = SELF.replace(/kortit\.js(?:\?.*)?$/, '');   // site/: the data files and pictures, from any language folder

  /* ---------------------------------------------------------------- state */
  const load = () => {
    try { const v = JSON.parse(localStorage.getItem(KEY) || '{}'); return v && typeof v === 'object' && !Array.isArray(v) ? v : {}; }
    catch (e) { storeOk = false; return {}; }
  };
  const save = (s) => { try { localStorage.setItem(KEY, JSON.stringify(s)); storeOk = true; } catch (e) { storeOk = false; } };
  const memory = {};               // when the browser refuses storage, the marks last while the page is open
  const state = () => Object.assign({}, memory, load());
  const put = (id, e) => { e.muokattu = Date.now(); memory[id] = e; const s = load(); s[id] = e; save(s); };
  const inDeck = (id) => (state()[id] || {}).tila === 'kertaa';
  /** "Osasin" (true) or "Kertaa myöhemmin" (false); returns what happened: 'good' (n left), 'done', 'removed', 'again' */
  const mark = (id, knew) => {
    const old = state()[id] || { tila: null, osasinPutki: 0 };
    if (!knew) { put(id, { tila: 'kertaa', osasinPutki: 0 }); return { what: 'again' }; }
    const n = (old.osasinPutki || 0) + 1;
    if (old.tila === 'kertaa' && n < STREAK) { put(id, { tila: 'kertaa', osasinPutki: n }); return { what: 'good', left: STREAK - n }; }
    put(id, { tila: 'osasin', osasinPutki: n });
    return { what: old.tila === 'kertaa' ? 'removed' : 'done' };
  };
  const addToDeck = (id) => { const old = state()[id] || {}; if (old.tila !== 'kertaa') put(id, { tila: 'kertaa', osasinPutki: 0 }); };
  const listeners = new Set();
  const changed = () => listeners.forEach((f) => f());
  window.addEventListener('storage', (e) => { if (e.key === KEY) changed(); });

  /* ---------------------------------------------------------------- texts and maths */
  const S = {};
  const t = (k, v) => {
    let s = S[k];
    if (s && typeof s === 'object') s = s[v && v.n === 1 ? 'one' : 'other'];
    if (typeof s !== 'string') return k;
    return s.replace(/\{\{(\w+)\}\}/g, (m, n) => (v && n in v ? String(v[n]) : m));
  };
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
  const maths = (node) => {
    if (window.renderMathInElement) {
      try { window.renderMathInElement(node, { delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }], throwOnError: false }); } catch (e) { /* plain text stays */ }
      if (window.flGlueMath) window.flGlueMath(node);
    }
    return node;
  };
  const formula = (c) => {
    const f = el('div', 'kc-formula');
    if (!c.kaava) return null;
    if (c.kaava_puhe) { f.setAttribute('role', 'img'); f.setAttribute('aria-label', c.kaava_puhe); }
    if (window.katex) { try { window.katex.render(c.kaava, f, { displayMode: true, throwOnError: false }); return f; } catch (e) { /* below */ } }
    f.textContent = c.kaava_puhe || c.kaava;
    return f;
  };
  let uid = 0;

  /* ---------------------------------------------------------------- the card */
  /** opts: {reverse: definition first, onAnswer(card, knew), base: url prefix of pictures} */
  const card = (c, opts = {}) => {
    // both faces sit in one grid cell, so a card keeps its height when it turns (no empty space beside it in a row)
    const id = 'kc-' + (++uid), root = el('div', 'kc-card'), inner = el('div', 'kc-inner');
    root.dataset.id = c.id;
    const term = !opts.reverse;
    const face = el('button', 'kc-face'); face.type = 'button';
    face.setAttribute('aria-expanded', 'false'); face.setAttribute('aria-controls', id);
    const main = el('span', 'kc-front ' + (term ? 'is-term' : 'is-def'), term ? c.kasite : c.maaritelma);
    const hint = el('span', 'kc-hint', t('flip_hint'));
    face.append(el('span', 'kc-kind', t(term ? 'term' : 'definition')), main, hint);
    const back = el('div', 'kc-back'); back.id = id; back.tabIndex = -1;
    back.setAttribute('role', 'group'); back.setAttribute('aria-label', c.kasite);
    const top = el('div', 'kc-back-top');
    top.append(el('span', 'kc-kind', t(term ? 'definition' : 'term')));
    const turn = el('button', 'kc-turn', '↺'); turn.type = 'button';
    turn.setAttribute('aria-expanded', 'true'); turn.setAttribute('aria-controls', id); turn.setAttribute('aria-label', t('flip_back'));
    top.append(turn); back.append(top);
    if (term) { back.append(el('p', 'kc-back-term', c.kasite), el('p', 'kc-def', c.maaritelma)); const f = formula(c); if (f) back.append(f); }
    else { back.append(el('p', 'kc-def kc-def-term', c.kasite)); const f = formula(c); if (f) back.append(f); }
    if (c.kuva) { const img = el('img', 'kc-img'); img.src = (opts.base || '') + c.kuva; img.alt = ''; img.loading = 'lazy'; img.onerror = () => img.remove(); back.append(img); }
    const acts = el('div', 'kc-actions');
    const good = el('button', 'kc-good', t('good')), again = el('button', 'kc-again', t('again'));
    good.type = again.type = 'button';
    acts.append(good, again);
    const status = el('p', 'kc-status'); status.setAttribute('aria-live', 'polite');
    back.append(acts, status);
    inner.append(face, back); root.append(inner);
    maths(main); maths(back);
    const deckMark = () => root.classList.toggle('in-deck', inDeck(c.id));
    deckMark();
    let flipped = false;
    const flip = (on, focus) => {
      flipped = on;
      root.classList.toggle('is-flipped', on);
      face.setAttribute('aria-expanded', String(on));
      face.inert = on; back.inert = !on;
      if (focus) (on ? back : face).focus({ preventScroll: true });
    };
    flip(false);
    face.addEventListener('click', () => flip(true, true));
    turn.addEventListener('click', () => flip(false, true));
    const answer = (knew) => {
      const r = mark(c.id, knew);
      status.textContent = !storeOk ? t('status_nostore')
        : r.what === 'good' ? t('status_good', { n: r.left }) : t('status_' + r.what);
      deckMark(); changed();
      if (opts.onAnswer) opts.onAnswer(c, knew);
    };
    good.addEventListener('click', () => answer(true));
    again.addEventListener('click', () => answer(false));
    return root;
  };

  /* ---------------------------------------------------------------- the popover */
  let open = null;
  const closePop = (focus) => {
    if (!open) return;
    const { pop, trigger } = open; open = null;
    pop.remove(); trigger.setAttribute('aria-expanded', 'false');
    if (focus) trigger.focus();
  };
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && open) { e.preventDefault(); closePop(true); } });
  document.addEventListener('click', (e) => { if (open && !open.pop.contains(e.target) && !open.trigger.contains(e.target)) closePop(false); });
  window.addEventListener('resize', () => closePop(false));
  const popover = (trigger, c) => {
    if (open && open.trigger === trigger) { closePop(true); return; }
    closePop(false);
    const pop = el('div', 'kc-pop'), id = 'kc-pop-' + (++uid);
    pop.id = id; pop.setAttribute('role', 'dialog'); pop.setAttribute('aria-label', c.kasite);
    const head = el('p', 'kc-pop-term', c.kasite);
    const x = el('button', 'kc-pop-close'); x.type = 'button'; x.setAttribute('aria-label', t('close')); x.textContent = '×';
    x.addEventListener('click', () => closePop(true));
    const def = el('p', 'kc-def', c.maaritelma);
    pop.append(x, head, def);
    const f = formula(c); if (f) pop.append(f);
    const add = el('button', 'kc-add'); add.type = 'button';
    const sync = () => { const on = inDeck(c.id); add.textContent = on ? t('added') : t('add'); add.setAttribute('aria-pressed', String(on)); };
    add.addEventListener('click', () => { addToDeck(c.id); sync(); changed(); if (!storeOk) note.textContent = t('status_nostore'); });
    const note = el('p', 'kc-status'); note.setAttribute('aria-live', 'polite');
    sync(); pop.append(add, note);
    maths(head); maths(def);
    document.body.append(pop);
    trigger.setAttribute('aria-expanded', 'true'); trigger.setAttribute('aria-controls', id);
    const r = trigger.getBoundingClientRect(), w = Math.min(352, document.documentElement.clientWidth - 32);
    pop.style.width = w + 'px';
    const left = Math.max(16, Math.min(r.left + window.scrollX, window.scrollX + document.documentElement.clientWidth - w - 16));
    pop.style.left = left + 'px';
    pop.style.top = (r.bottom + window.scrollY + 8) + 'px';
    const pr = pop.getBoundingClientRect();
    if (pr.bottom > window.innerHeight - 8 && r.top - pr.height - 8 > 0) pop.style.top = (r.top + window.scrollY - pr.height - 8) + 'px';
    open = { pop, trigger };
    add.focus({ preventScroll: true });
  };
  const termButton = (label, c, cls) => {
    const b = el('button', cls); b.type = 'button';
    b.setAttribute('aria-expanded', 'false'); b.setAttribute('aria-haspopup', 'dialog');
    b.addEventListener('click', (e) => { e.stopPropagation(); popover(b, c); });
    if (typeof label === 'string') b.textContent = label; else b.append(...label);
    return b;
  };

  /* ---------------------------------------------------------------- places */
  /** Two cards side by side (teacher 2026-11-04, "kaksi aina näkyy ja kun sen kääntää tulee uusi"): the rest wait in
      order; an answered card (Osasin or Kertaa myöhemmin) gives its place to the next one after a moment, so its
      status can be read. When none are left, "Aloita alusta" starts the same cards again. Never scrolls sideways. */
  const SLOTS = 2, NEXT_MS = 1400;
  const row = (cards, opts) => {
    const box = el('div', 'kc-pair'), r = el('div', 'kc-row'), foot = el('div', 'kc-pair-foot');
    const left = el('p', 'kc-left'); left.setAttribute('aria-live', 'polite');
    const again = el('button', 'kc-restart', t('row_restart')); again.type = 'button'; again.hidden = true;
    foot.append(left, again); box.append(r, foot);
    let queue = [];
    const sync = () => {
      left.textContent = queue.length ? t('row_left', { n: queue.length }) : r.children.length ? '' : t('row_done');
      again.hidden = !!(queue.length || r.children.length);
    };
    const make = (c) => {
      const node = card(c, Object.assign({}, opts, { onAnswer: () => {
        node.querySelectorAll('.kc-actions button').forEach((b) => { b.disabled = true; });
        setTimeout(() => {
          const had = node.contains(document.activeElement);
          let to = null;
          if (queue.length) { const n = make(queue.shift()); n.classList.add('is-new'); node.replaceWith(n); to = n.querySelector('.kc-face'); }
          else { node.remove(); to = r.querySelector('.kc-face:not([inert])') || (r.children.length ? null : again); }
          sync();
          if (had && to) { if (to === again) again.hidden = false; to.focus({ preventScroll: true }); }
        }, NEXT_MS);
      } }));
      return node;
    };
    const start = () => {
      queue = cards.slice(); r.textContent = '';
      queue.splice(0, SLOTS).forEach((c) => r.append(make(c)));
      sync();
    };
    again.addEventListener('click', () => { start(); const f = r.querySelector('.kc-face'); if (f) f.focus({ preventScroll: true }); });
    start();
    return box;
  };

  const lesson = (sec, d) => {
    const byId = Object.fromEntries(d.cards.map((c) => [c.id, c]));
    const mine = d.cards.filter((c) => c.luku === d.luku);
    // Teoriatiivistelmä: a bold term that names a card opens its popover
    document.querySelectorAll('#selita strong.kc-mark[data-kortti]').forEach((s) => {
      const c = byId[s.dataset.kortti]; if (!c) return;
      const b = termButton([...s.childNodes], c, 'kc-term-btn');
      s.append(b);
      s.classList.add('kc-ready');
    });
    // the chips after the summary list
    document.querySelectorAll('.kc-chips[data-luku]').forEach((box) => {
      if (!mine.length) return;
      box.append(el('p', 'kc-chips-label', t('chips', { n: mine.length })));
      const ul = el('ul', 'kc-chip-list');
      mine.forEach((c) => { const li = el('li'); li.append(termButton(c.kasite, c, 'kc-chip')); ul.append(li); });
      box.append(ul); maths(box); box.hidden = false;
    });
    // the section: the chapter's cards two at a time, an answered one replaced by the next
    const list = sec.querySelector('dl.kc-dl');
    const r = row(mine, { base: d.base });
    if (list) list.replaceWith(r); else sec.append(r);
  };

  const deck = (sec, d) => {
    const body = sec.querySelector('.kc-deck-body');
    const draw = () => {
      const s = state(), ids = d.cards.filter((c) => (s[c.id] || {}).tila === 'kertaa');
      body.textContent = '';
      if (!ids.length) { body.append(el('p', null, d.empty)); return; }
      const order = Object.keys(d.chapters || {});
      const chs = [...new Set(ids.map((c) => c.luku).filter(Boolean))].sort((a, b) => order.indexOf(a) - order.indexOf(b));
      const names = chs.map((l) => (d.chapters || {})[l]).filter(Boolean);
      const list = names.length < 2 ? names.join('') : names.slice(0, -1).join(', ') + ' ' + t('deck_and') + ' ' + names[names.length - 1];
      const p = el('p', 'kc-deck-count');
      p.textContent = t('deck_count', { n: ids.length }) + ' ' + (names.length ? t(names.length === 1 ? 'deck_from_one' : 'deck_from_many', { list }) : t('deck_from_other'));
      const a = el('a', 'kc-button', t('review_now'));
      a.href = `${d.app}?moduuli=${encodeURIComponent(d.moduuli)}&pakka=oma`;
      body.append(p, a); maths(p);
    };
    draw(); listeners.add(draw);
  };

  const practice = (sec, d) => {
    const s = state(), mine = d.cards.filter((c) => (s[c.id] || {}).tila === 'kertaa');
    if (!mine.length) return;
    sec.querySelector('.kc-row').replaceWith(row(mine, { base: d.base }));
    sec.hidden = false;
  };

  /* ---------------------------------------------------------------- Käsitetakomo (site/kasitteet.html) */
  const app = async (box, d) => {
    let files = {};
    try { files = JSON.parse(box.dataset.files || '{}'); } catch (e) { /* none */ }
    const base = BASE;
    const mods = {};
    try {
      const got = await Promise.all(Object.entries(files).map(async ([code, f]) => {
        const r = await fetch(base + f); if (!r.ok) throw new Error(f);
        return [code, await r.json()];
      }));
      got.forEach(([code, m]) => { mods[code] = m; });   // in the curriculum's order
    } catch (e) {
      const p = el('p', 'notice', t('load_failed')); p.setAttribute('role', 'note'); box.before(p); return;
    }
    document.querySelector('.kc-static')?.setAttribute('hidden', '');
    box.hidden = false;
    let mode = 'kasite';
    try { mode = localStorage.getItem(MODE_KEY) || localStorage.getItem('kasitetakomo-mode') || 'kasite'; } catch (e) { /* default */ }
    const names = d.names || {};
    const q = (() => { try { return new URLSearchParams(location.search); } catch (e) { return new URLSearchParams(); } })();
    const setUrl = (params) => {
      try { history.replaceState(null, '', location.pathname + (params ? '?' + new URLSearchParams(params).toString() : '') + location.hash); } catch (e) { /* file:// */ }
    };
    const screen = el('div', 'kc-screen');
    box.append(screen);
    const clear = () => { closePop(false); screen.textContent = ''; window.scrollTo({ top: Math.max(0, box.offsetTop - 80) }); };
    const backBtn = (label, fn) => { const b = el('button', 'kc-back-btn', label); b.type = 'button'; b.addEventListener('click', fn); return b; };

    const modulesView = () => {
      clear(); setUrl(null);
      screen.append(el('h2', null, t('modules')));
      const grid = el('div', 'kc-grid');
      Object.entries(mods).forEach(([code, m]) => {
        const b = el('button', 'kc-tile'); b.type = 'button';
        b.append(el('span', 'kc-tile-code', code), el('span', 'kc-tile-name', names[code] || m.nimi),
                 el('span', 'kc-tile-count', m.kesken ? t('coming') : t('n_cards', { n: m.kortit.length })));
        if (m.kesken) b.disabled = true; else b.addEventListener('click', () => topicsView(code));
        grid.append(b);
      });
      screen.append(grid); maths(grid);
    };

    const modeGroup = () => {
      const g = el('div', 'kc-mode'); g.setAttribute('role', 'group'); g.setAttribute('aria-label', t('mode'));
      [['kasite', 'mode_term'], ['maaritelma', 'mode_def']].forEach(([m, k]) => {
        const b = el('button', null, t(k)); b.type = 'button'; b.setAttribute('aria-pressed', String(mode === m));
        b.addEventListener('click', () => { mode = m; try { localStorage.setItem(MODE_KEY, m); } catch (e) { /* this visit only */ }
          g.querySelectorAll('button').forEach((x, i) => x.setAttribute('aria-pressed', String((i === 0) === (m === 'kasite')))); });
        g.append(b);
      });
      return g;
    };

    const topicsView = (code) => {
      const m = mods[code]; clear(); setUrl({ moduuli: code });
      screen.append(backBtn(t('back_modules'), modulesView));
      const h = el('h2', null, `${code} · ${names[code] || m.nimi}`); screen.append(h);
      const list = el('div', 'kc-topics');
      const own = m.kortit.filter((c) => inDeck(c.id));
      const line = (label, n, fn, pick) => {
        const r = el('div', 'kc-topic' + (pick ? '' : ' kc-topic-all'));
        if (pick) r.append(pick);
        const b = el('button', 'kc-topic-main'); b.type = 'button';
        b.append(el('span', 'kc-topic-label', label), el('span', 'kc-topic-n', String(n)), el('span', 'kc-go', '→'));
        b.addEventListener('click', fn); r.append(b); list.append(r); return r;
      };
      line(t('own_deck'), own.length, () => study(code, own, t('own_deck'), { moduuli: code, pakka: 'oma' }));
      line(t('all_topics'), m.kortit.length, () => study(code, m.kortit, t('all_topics'), { moduuli: code }));
      const chosen = new Set();
      const bar = el('div', 'kc-startbar'); bar.hidden = true;
      const start = el('button', 'kc-start'); start.type = 'button';
      const clr = el('button', 'kc-clear', t('clear')); clr.type = 'button';
      bar.append(start, clr);
      const tip = el('p', 'kc-tip', t('combine_hint'));
      const sync = () => { bar.hidden = !chosen.size; tip.hidden = !!chosen.size; start.textContent = t('start', { n: chosen.size }); };
      m.aiheet.forEach((a) => {
        const cs = m.kortit.filter((c) => c.aihe === a.id); if (!cs.length) return;
        const pick = el('button', 'kc-pick'); pick.type = 'button'; pick.setAttribute('aria-pressed', 'false');
        pick.setAttribute('aria-label', t('pick', { name: a.nimi })); pick.append(el('span', null, '✓'));
        const r = line(a.nimi, cs.length, () => study(code, cs, a.nimi, { moduuli: code, aihe: a.id }), pick);
        pick.addEventListener('click', () => { chosen.has(a.id) ? chosen.delete(a.id) : chosen.add(a.id);
          pick.setAttribute('aria-pressed', String(chosen.has(a.id))); r.classList.toggle('is-chosen', chosen.has(a.id)); sync(); });
        r.dataset.aihe = a.id;
      });
      start.addEventListener('click', () => {
        const ids = m.aiheet.map((a) => a.id).filter((x) => chosen.has(x));
        const cs = m.kortit.filter((c) => chosen.has(c.aihe));
        study(code, cs, ids.length === 1 ? m.aiheet.find((a) => a.id === ids[0]).nimi : t('topics_n', { n: ids.length }), { moduuli: code, aihe: ids.join(',') });
      });
      clr.addEventListener('click', () => { chosen.clear(); list.querySelectorAll('.kc-pick').forEach((p) => p.setAttribute('aria-pressed', 'false'));
        list.querySelectorAll('.is-chosen').forEach((r) => r.classList.remove('is-chosen')); sync(); });
      screen.append(list, bar, tip, modeGroup()); maths(list); sync();
      return { chosen, list, start, sync };
    };

    const shuffle = (a) => { const x = a.slice(); for (let i = x.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [x[i], x[j]] = [x[j], x[i]]; } return x; };

    const study = (code, cards, label, params) => {
      clear(); setUrl(params);
      screen.append(backBtn(t('back_topics'), () => topicsView(code)));
      const head = el('div', 'kc-studybar');
      head.append(el('h2', 'kc-crumb', `${code} · ${label}`));
      const tally = el('span', 'kc-tally'); head.append(tally);
      const track = el('div', 'kc-track'), fill = el('div', 'kc-fill'); track.append(fill);
      screen.append(head, track); maths(head);
      if (!cards.length) {
        const p = el('p', 'kc-empty', t('empty_deck')), a = el('a', null, t('empty_deck_link'));
        a.href = '?moduuli=' + encodeURIComponent(code);
        a.addEventListener('click', (e) => { e.preventDefault(); study(code, mods[code].kortit, t('all_topics'), { moduuli: code }); });
        screen.append(p, a); tally.textContent = ''; return;
      }
      let queue = shuffle(cards), done = 0, again = 0;
      const total = cards.length, slot = el('div', 'kc-study');
      screen.append(slot);
      const show = () => {
        tally.textContent = t('progress', { done, total }); fill.style.width = (done / total) * 100 + '%';
        slot.textContent = '';
        if (!queue.length) return finish();
        const c = queue[0];
        const node = card(c, { reverse: mode === 'maaritelma', base, onAnswer: (k, knew) => {
          queue.shift();
          if (knew) done++; else { again++; queue.splice(Math.min(queue.length, 3 + Math.floor(Math.random() * 3)), 0, k); }
          setTimeout(show, 650);
          node.querySelectorAll('.kc-actions button').forEach((b) => { b.disabled = true; });
        } });
        slot.append(node);
        node.querySelector('.kc-face').focus({ preventScroll: true });
      };
      const finish = () => {
        tally.textContent = t('progress', { done: total, total }); fill.style.width = '100%';
        const box2 = el('div', 'kc-done');
        box2.append(el('h3', null, t('done_title')), el('p', null, again ? t('done_stats', { total, n: again }) : t('done_none', { total })));
        const acts = el('div', 'kc-done-actions');
        [['same_again', () => study(code, cards, label, params)], ['other_topic', () => topicsView(code)], ['other_module', modulesView]].forEach(([k, fn], i) => {
          const b = el('button', i ? null : 'kc-primary', t(k)); b.type = 'button'; b.addEventListener('click', fn); acts.append(b);
        });
        box2.append(acts); slot.append(box2); acts.firstChild.focus({ preventScroll: true });
      };
      show();
    };

    // ?moduuli=FY4 (old ?kurssi=), &aihe=a[,b] starts those topics, &pakka=oma the own deck, &luku=fy4-4 one chapter;
    // an unknown or bad value opens the module menu and cleans the address
    const code = (q.get('moduuli') || q.get('kurssi') || '').trim().toUpperCase();
    const aiheet = (q.get('aihe') || '').split(',').map((x) => x.trim().toLowerCase()).filter(Boolean);
    const luku = (q.get('luku') || '').trim().toLowerCase(), oma = q.get('pakka') === 'oma';
    const m = mods[code] || (aiheet.length ? Object.values(mods).find((x) => x.aiheet.some((a) => a.id === aiheet[0])) : null);
    if (!m || m.kesken) return modulesView();
    const mc = m.moduuli;
    if (oma) return study(mc, m.kortit.filter((c) => inDeck(c.id)), t('own_deck'), { moduuli: mc, pakka: 'oma' });
    if (luku) {
      const cs = m.kortit.filter((c) => c.luku === luku);
      if (!cs.length) return topicsView(mc);
      return study(mc, cs, t('chapter', { title: (d.chapters || {})[luku] || luku }), { moduuli: mc, luku });
    }
    if (!aiheet.length) return topicsView(mc);
    if (aiheet.some((a) => !m.aiheet.some((x) => x.id === a)) || new Set(aiheet).size !== aiheet.length) return topicsView(mc);
    const v = topicsView(mc);
    aiheet.forEach((a) => { v.chosen.add(a); const r = v.list.querySelector(`[data-aihe="${a}"]`); if (r) { r.classList.add('is-chosen'); r.querySelector('.kc-pick').setAttribute('aria-pressed', 'true'); } });
    v.sync(); v.start.click();
  };

  /* ---------------------------------------------------------------- start */
  const init = () => {
    document.querySelectorAll('script.kc-data').forEach((s) => {
      if (s.dataset.done) return; s.dataset.done = '1';
      let d; try { d = JSON.parse(s.textContent); } catch (e) { return; }
      Object.assign(S, d.strings || {});
      const host = s.parentElement;
      d.base = BASE;
      if (host.classList.contains('kc-section')) lesson(host, d);
      else if (host.classList.contains('kc-deck')) { d.empty = (host.querySelector('.kc-deck-body p') || {}).textContent || ''; deck(host, d); }
      else if (host.classList.contains('kc-practice')) practice(host, d);
      else { const box = document.querySelector('.kc-app'); if (box) app(box, d); }
    });
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
