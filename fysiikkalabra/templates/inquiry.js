/* Inquiry lesson behaviour (pages built from inquiry.json; see docs/inquiry.md). Runs after lesson.js, which
   already handles every form.check (numeric answers), the section nav and the staged example.
   Everything stays in the browser. Answers are kept in memory, and copied to localStorage only so that a
   reload on the same device does not lose a prediction; every access is wrapped, and the page works without it.
   1. Predictions (fieldset.choice with data-reveal): the student commits before any feedback; the feedback
      appears only after the linked experiment has recorded data-reveal-min measurements.
   2. Plain choices: feedback for the selected option after "Vastaa"; the student may change and re-check.
   3. Experiments (.experiment): drive window.simAdapter — set the initial conditions, lock the controlled
      parameters, record the varied parameter and the measured quantities into a table, reset.
   4. Numeric tasks: common-mistake feedback (data-mistakes) on top of lesson.js, progressive hints.
   5. Explanations: model answer and self-assessment criteria once the student has written an answer of their own; a
      conclusion (data-after) also waits for the measurements of its experiments and copies tables and text for notes.
   6. Reflection: shows the student's own predictions next to the evidence and asks whether to revise.
   7. The Ennusta box (details.fold, closed at first): its summary counts the answers; closing it keeps them. */
(() => {
  const key = (id) => 'fl:' + location.pathname.split('/').pop() + ':' + id;
  const store = { get(id) { try { return JSON.parse(localStorage.getItem(key(id))); } catch (e) { return null; } },
                  set(id, v) { try { localStorage.setItem(key(id), JSON.stringify(v)); } catch (e) { /* private mode, blocked storage */ } } };
  const fi = (x) => {
    if (typeof x !== 'number' || !Number.isFinite(x)) return String(x);
    const a = Math.abs(x), s = a >= 100 ? x.toFixed(0) : a >= 10 ? x.toFixed(1) : a >= 1 ? x.toFixed(2) : x.toPrecision(3);
    return s.replace('.', ',').replace('-', '−');
  };
  const measured = {};              // experiment id -> number of recorded measurements
  const bus = new EventTarget();

  // 1–2. choices
  document.querySelectorAll('fieldset.choice').forEach((fs) => {
    const id = fs.closest('.activity')?.id || fs.querySelector('input')?.name || '';
    const radios = [...fs.querySelectorAll('input[type=radio]')], out = fs.querySelector('output');
    const btn = fs.querySelector('button.commit'), pending = fs.querySelector('.pending'), justify = fs.querySelector('.justify textarea');
    const reveal = fs.dataset.reveal, min = Number(fs.dataset.revealMin || 1);
    const feedbacks = [...fs.querySelectorAll('.feedback')];
    const show = (i) => {
      feedbacks.forEach((f) => { f.hidden = f.dataset.for !== String(i); });
      const ok = radios[i].dataset.correct === '1';
      out.textContent = ok ? 'Oikein.' : 'Ei aivan.'; out.dataset.state = ok ? 'ok' : 'no';
      fs.dataset.state = ok ? 'ok' : 'no';
    };
    const commit = (i, silent) => {
      fs.dataset.committed = '1';
      store.set(id, { choice: i, text: radios[i].parentElement.textContent.trim(), why: justify ? justify.value : '' });
      if (reveal) {
        radios.forEach((r) => { r.disabled = true; });
        btn.hidden = true;
        if ((measured[reveal] || 0) >= min) { show(i); if (pending) pending.hidden = true; }
        else if (pending) { pending.hidden = false; if (!silent) pending.focus?.(); }
      } else show(i);
      if (!silent) bus.dispatchEvent(new CustomEvent('fl:answered', { detail: { id } }));
    };
    btn.addEventListener('click', () => {
      const i = radios.findIndex((r) => r.checked);
      if (i < 0) { out.textContent = 'Valitse ensin vaihtoehto.'; out.dataset.state = 'hint'; return; }
      commit(i, false);
    });
    radios.forEach((r) => r.addEventListener('change', () => { if (!reveal) { feedbacks.forEach((f) => { f.hidden = true; }); out.textContent = ''; delete out.dataset.state; delete fs.dataset.state; } }));
    if (justify) justify.addEventListener('input', () => { const s = store.get(id); if (s) { s.why = justify.value; store.set(id, s); } });
    if (reveal) bus.addEventListener('fl:measured', (e) => {
      if (e.detail.id !== reveal || e.detail.count < min) return;
      const i = radios.findIndex((r) => r.checked);
      if (fs.dataset.committed && i >= 0) { show(i); if (pending) pending.hidden = true; }
    });
    const saved = store.get(id);
    if (saved && radios[saved.choice]) { radios[saved.choice].checked = true; if (justify && saved.why) justify.value = saved.why; if (reveal) commit(saved.choice, true); }
  });

  // 7. the Ennusta box: "2 kysymystä", then "vastattu 1/2", then "vastattu 2/2 · palaute 2/2"
  document.querySelectorAll('details.fold').forEach((fold) => {
    const status = fold.querySelector('.fold-status'), sets = [...fold.querySelectorAll('fieldset.choice')], n = sets.length;
    if (!status || !n) return;
    const update = () => {
      const done = sets.filter((f) => f.dataset.committed).length, shown = sets.filter((f) => f.dataset.state).length;
      status.textContent = done ? `vastattu ${done}/${n}` + (shown ? ` · palaute ${shown}/${n}` : '') : `${n} ${n === 1 ? 'kysymys' : 'kysymystä'}`;
    };
    bus.addEventListener('fl:answered', update); bus.addEventListener('fl:measured', update); update();
  });

  // 3. experiments: the physics stays in the simulation; this only sets, locks, reads and resets it.
  // p5 runs the sketch's setup (which defines the adapter) after the window load event, so bind lazily.
  const whenAdapter = (cb) => {
    const t0 = Date.now();
    const tick = () => { if (window.simAdapter) cb(window.simAdapter); else if (Date.now() - t0 < 4000) setTimeout(tick, 100); else cb(null); };
    tick();
  };
  // The page has one simulation. On a wide screen it stays in its column beside the experiments (.lab, site.css) and
  // moves down level with the experiment that starts. On a phone an experiment that starts brings it next to its own
  // buttons and table, so the picture, the control being varied and "Kirjaa mittaus" fit one screen; its first place
  // keeps a link. A resize puts it right again.
  const simEl = document.getElementById('sim');
  const simHome = simEl ? document.createElement('p') : null;
  if (simHome) { simHome.className = 'sim-moved'; simHome.hidden = true; simEl.before(simHome); }
  let activeExp = null;
  const besideLab = () => { const lab = simHome && simHome.closest('.lab'); return !!lab && getComputedStyle(lab).getPropertyValue('--wide').trim() === '1'; };
  const placeSim = () => {
    if (!simEl) return;
    if (!activeExp || besideLab()) {
      if (simHome.nextElementSibling !== simEl) simHome.after(simEl);
      simHome.hidden = true; simEl.style.marginTop = '';
      if (activeExp) { const d = activeExp.ex.closest('.activity').getBoundingClientRect().top - simEl.getBoundingClientRect().top; if (d > 0) simEl.style.marginTop = Math.round(d) + 'px'; }
      return;
    }
    simEl.style.marginTop = '';
    const { ex, id } = activeExp;
    if (!ex.contains(simEl)) ex.querySelector('.exp-controls').before(simEl);
    const title = ex.closest('.activity').querySelector('h3')?.textContent || 'kokeeseen';
    simHome.innerHTML = 'Simulaatio on nyt kokeen kohdalla: <a></a>.';
    const link = simHome.querySelector('a'); link.href = '#' + id; link.textContent = title;
    simHome.hidden = false;
  };
  const bringSim = (ex, id) => { activeExp = { ex, id }; placeSim(); };
  let resizing = false;
  window.addEventListener('resize', () => { if (!resizing) { resizing = true; requestAnimationFrame(() => { resizing = false; placeSim(); }); } });
  document.querySelectorAll('.experiment').forEach((ex) => {
    const id = ex.closest('.activity').id;
    const initial = JSON.parse(ex.dataset.initial), locked = JSON.parse(ex.dataset.locked), vary = ex.dataset.vary, measure = JSON.parse(ex.dataset.measure), min = Number(ex.dataset.min || 2);
    const varyName = ex.dataset.varyName || vary, lockedNames = ex.dataset.lockedNames ? JSON.parse(ex.dataset.lockedNames) : locked;
    const start = ex.querySelector('.exp-start'), rec = ex.querySelector('.exp-record'), reset = ex.querySelector('.exp-reset');
    const tbody = ex.querySelector('tbody'), status = ex.querySelector('.exp-status'), question = ex.querySelector('.exp-question');
    let rows = [], armed = false;
    const say = (t) => { status.textContent = t; };
    [start, rec].forEach((b) => { b.disabled = true; });
    if (question) question.hidden = true;
    const announce = () => {
      measured[id] = rows.length;
      bus.dispatchEvent(new CustomEvent('fl:measured', { detail: { id, count: rows.length } }));
      if (question) question.hidden = rows.length < min;
    };
    whenAdapter((A) => {
      const unit = (k) => (A && A.params && A.params[k] && A.params[k].unit ? ' ' + A.params[k].unit : '');
      const render = () => {
        tbody.innerHTML = '';
        rows.forEach((r) => {
          const tr = document.createElement('tr');
          tr.innerHTML = `<td>${fi(r.vary)}${unit(vary)}</td>` + measure.map((k) => `<td>${fi(r[k])}${unit(k)}</td>`).join('');
          tbody.appendChild(tr);
        });
      };
      if (!A) {
        say('Tämä koe tehdään sivun simulaatiolla, jota tämä selain ei voinut käynnistää. Voit lukea kokeen asetelman ja päätellä tuloksen kaavasta.');
        if (question) question.hidden = false;
        measured[id] = Infinity; bus.dispatchEvent(new CustomEvent('fl:measured', { detail: { id, count: Infinity } }));   // nothing to wait for
        return;
      }
      const missing = Object.keys(initial).concat(locked, [vary]).filter((k) => !A.params || !A.params[k]);
      if (missing.length) { say('Simulaatio ei tue tätä koetta (parametri ' + missing.join(', ') + ').'); return; }
      start.disabled = false;
      start.addEventListener('click', () => {
        A.set(initial); locked.forEach((k) => A.lock(k, true)); A.lock(vary, false);
        armed = true; rec.disabled = false;
        say(`Alkutila asetettu. ${lockedNames.length ? 'Vakiona: ' + lockedNames.join(', ') + '. ' : ''}Säädä ${varyName}, anna simulaation pyöriä ja paina Kirjaa mittaus.`);
        bringSim(ex, id);
        if (besideLab()) ex.closest('.activity').scrollIntoView({ behavior: 'smooth', block: 'start' });   // the sim is level with it
        else rec.scrollIntoView({ behavior: 'smooth', block: 'end' });
      });
      rec.addEventListener('click', () => {
        if (!armed) { say('Aseta ensin alkutila.'); return; }
        const S = A.get() || {};
        if (!(vary in S) || measure.some((k) => !(k in S))) { say('Simulaatio ei anna mitattavaa arvoa.'); return; }
        const row = { vary: S[vary] };
        measure.forEach((k) => { row[k] = S[k]; });
        if (rows.length && rows[rows.length - 1].vary === row.vary) { say(`Sama ${varyName} kuin edellisessä mittauksessa. Muuta arvoa ennen uutta mittausta.`); return; }
        rows.push(row); render(); announce();
        say(rows.length < min ? `Mittaus ${rows.length} kirjattu. Muuta ${varyName} ja kirjaa vielä ${min - rows.length}.` : `Mittaus ${rows.length} kirjattu. Vertaa tuloksia ennusteeseesi.`);
      });
      reset.addEventListener('click', () => {
        locked.forEach((k) => A.lock(k, false)); A.reset(); rows = []; armed = false; rec.disabled = true; render(); announce();
        say('Simulaatio ja taulukko nollattu.');
      });
    });
  });

  // 4. numeric tasks: common-mistake feedback and progressive hints
  document.querySelectorAll('.act-numeric form.check, .exp-question form.check, .interpret form.check').forEach((form) => {
    let mistakes = [];
    try { mistakes = JSON.parse(form.dataset.mistakes || '[]'); } catch (e) { mistakes = []; }
    if (!mistakes.length) return;
    const input = form.querySelector('input'), out = form.querySelector('output'), tol = Number(form.dataset.tol);
    form.addEventListener('submit', () => {
      const v = Number(input.value.trim().replace(/\s+/g, '').replace(/−/g, '-').replace(',', '.').replace(/[^\d.eE+-]/g, ''));
      if (!Number.isFinite(v) || out.dataset.state === 'ok') return;
      const m = mistakes.find((x) => Math.abs(v - x.value) <= (x.value === 0 ? tol : tol * Math.abs(x.value)));
      if (m) { out.textContent = m.feedback; out.dataset.state = 'no'; }
    });
  });
  document.querySelectorAll('.hints').forEach((h) => {
    const items = [...h.querySelectorAll('details.hint')];
    items.forEach((d, i) => { if (i) d.hidden = true; d.addEventListener('toggle', () => { if (d.open && items[i + 1]) items[i + 1].hidden = false; }); });
  });

  // 5. explanations
  const MIN_CHARS = 15;              // an answer of one's own, however short, before the model answer
  const expMin = (eid) => Number(document.querySelector(`#${CSS.escape(eid)} .experiment`)?.dataset.min || 2);
  const copyText = (text, done) => {
    const fallback = () => { const t = document.createElement('textarea'); t.value = text; t.setAttribute('readonly', ''); t.style.position = 'fixed'; t.style.opacity = '0';
      document.body.appendChild(t); t.select(); let ok = false; try { ok = document.execCommand('copy'); } catch (e) { ok = false; } t.remove(); done(ok); };
    try { navigator.clipboard.writeText(text).then(() => done(true), fallback); } catch (e) { fallback(); }
  };
  const tableText = (eid) => {        // an experiment's recorded rows as tab-separated text, headings in plain words
    const act = document.getElementById(eid), tb = act && act.querySelector('table.exp-table');
    if (!tb) return '';
    let cols = []; try { cols = JSON.parse(tb.dataset.cols || '[]'); } catch (e) { cols = []; }
    const rows = [...tb.querySelectorAll('tbody tr')].map((tr) => [...tr.children].map((td) => td.textContent.trim()).join('\t'));
    const title = act.querySelector('h3')?.textContent.trim() || eid;
    return [title, cols.join('\t'), ...(rows.length ? rows : ['(ei mittauksia)'])].join('\n');
  };
  document.querySelectorAll('.explain').forEach((ex) => {
    const btn = ex.querySelector('.show-model'), model = ex.querySelector('.model'), ta = ex.querySelector('textarea');
    const copy = ex.querySelector('.copy-notes'), status = ex.querySelector('.explain-status');
    const id = ex.closest('.activity')?.id || '';
    let after = []; try { after = JSON.parse(ex.dataset.after || '[]'); } catch (e) { after = []; }
    const saved = store.get(id); if (saved && saved.text) ta.value = saved.text;
    const say = (t) => { if (status) status.textContent = t; };
    const missing = () => after.filter((eid) => (measured[eid] || 0) < expMin(eid));
    ta.addEventListener('input', () => { store.set(id, { text: ta.value }); if (status && status.textContent && ta.value.trim().length >= MIN_CHARS && !missing().length) say(''); });
    btn.addEventListener('click', () => {
      const m = missing();
      if (m.length) { say('Tee ensin mittaukset: ' + m.map((eid) => document.getElementById(eid)?.querySelector('h3')?.textContent.trim() || eid).join(', ') + '. Johtopäätös tehdään omista havainnoista.'); return; }
      if (ta.value.trim().length < MIN_CHARS) { say('Kirjoita ensin oma vastauksesi. Sitten voit verrata sitä mallivastaukseen.'); ta.focus(); return; }
      say(''); model.hidden = false; btn.hidden = true; model.querySelector('h4')?.focus?.();
    });
    if (copy) copy.addEventListener('click', () => {
      const title = ex.closest('.activity')?.querySelector('h3')?.textContent.trim() || 'Johtopäätös';
      const text = [document.title, '', ...after.map(tableText).filter(Boolean).flatMap((t) => [t, '']), title + ':', ta.value.trim() || '(ei vielä kirjoitettu)'].join('\n');
      copyText(text, (ok) => say(ok ? 'Taulukot ja johtopäätöksesi on kopioitu. Liitä ne muistiinpanoihisi.' : 'Kopiointi ei onnistunut tässä selaimessa. Valitse teksti ja kopioi se itse.'));
    });
  });

  // 6. reflection: the student's own predictions beside the evidence
  document.querySelectorAll('.reflect').forEach((r) => {
    const ids = JSON.parse(r.dataset.predictions), list = r.querySelector('.my-predictions');
    const fill = () => {
      list.innerHTML = '';
      ids.forEach((pid) => {
        const act = document.getElementById(pid), fs = act && act.querySelector('fieldset.choice');
        const legend = fs ? fs.querySelector('legend').textContent.trim() : pid;
        const saved = store.get(pid);
        const li = document.createElement('li');
        const q = document.createElement('p'); q.className = 'rq'; q.textContent = legend; li.appendChild(q);
        const a = document.createElement('p');
        if (saved && fs) {
          const ok = fs.querySelectorAll('input[type=radio]')[saved.choice]?.dataset.correct === '1';
          const revealed = fs.dataset.state !== undefined;
          a.innerHTML = `<strong>Ennustit:</strong> ${saved.text}` + (saved.why ? ` <em>(${saved.why})</em>` : '') +
            (revealed ? ` — ${ok ? 'aineisto tukee ennustettasi.' : 'aineisto ei tue ennustettasi.'}` : ' — tee vielä mittaukset, niin näet, pitikö ennuste.');
        } else { a.innerHTML = `Et ole vielä vastannut: <a href="#${pid}">siirry ennusteeseen</a>.`; }
        li.appendChild(a); list.appendChild(li);
      });
    };
    fill(); bus.addEventListener('fl:answered', fill); bus.addEventListener('fl:measured', fill);
    const ta = r.querySelector('textarea'), id = r.closest('.activity').id;
    const saved = store.get(id); if (saved && saved.text) ta.value = saved.text;
    ta.addEventListener('input', () => store.set(id, { text: ta.value }));
  });
})();
