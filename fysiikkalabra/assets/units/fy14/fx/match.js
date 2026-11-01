/* Matching and sorting (data-fx="match"): each item gets a <select> of the options (a category, a translation, a
   definition); "Check" marks every item right or wrong in words and shows the item's own feedback for a wrong
   choice; after two checks "Show answers" appears. Data: {prompt?, options: [text], items: [{text, answer, feedback?}],
   lang_items?: "fr", lang_options?: "fr", done?: text shown when all are right}. Options may be shared by several items. */
window.FX.match = (el, d, A) => {
  const { h, md, shuffle, store, typeset } = A;
  const items = shuffle(d.items.map((x, i) => ({ ...x, i })), el.id + 'i');
  const opts = d.options;
  const saved = store.get(el.id) || {};
  let tries = 0;
  const rows = items.map((it) => {
    const sel = h('select', { 'aria-label': 'Answer for: ' + it.text.replace(/[*{}\/]|fr/g, '') },
      h('option', { value: '' }, 'Choose…'), ...opts.map((o, k) => h('option', { value: String(k), lang: d.lang_options || false }, o)));
    if (saved[it.i] != null) sel.value = saved[it.i];
    const out = h('output', { 'aria-live': 'polite' });
    sel.addEventListener('change', () => { saved[it.i] = sel.value; store.set(el.id, saved); out.textContent = ''; out.removeAttribute('data-state'); li.removeAttribute('data-state'); });
    const li = h('li', { class: 'fx-match-row' }, h('span', { class: 'fx-match-item', html: md(it.text), lang: d.lang_items || false }), sel, out);
    return { it, sel, out, li };
  });
  const msg = h('p', { class: 'fx-msg', 'aria-live': 'polite' });
  const show = h('button', { type: 'button', class: 'fx-btn fx-quiet', hidden: true }, 'Show answers');
  const check = h('button', { type: 'button', class: 'fx-btn' }, 'Check');
  check.addEventListener('click', () => {
    tries++; let ok = 0, blank = 0;
    rows.forEach((r) => {
      if (r.sel.value === '') { blank++; r.out.dataset.state = 'hint'; r.out.textContent = 'Choose an answer.'; return; }
      const good = opts[Number(r.sel.value)] === r.it.answer;
      r.li.dataset.state = good ? 'ok' : 'no'; r.out.dataset.state = good ? 'ok' : 'no';
      r.out.innerHTML = good ? 'Right.' : 'Not yet. ' + md(r.it.feedback || 'Look again at the clue in the text.');
      if (good) ok++;
    });
    msg.innerHTML = blank ? `${ok} of ${rows.length} right. Answer every item, then check again.`
      : ok === rows.length ? '<strong>All right!</strong> ' + md(d.done || '') : `${ok} of ${rows.length} right. Change the ones marked ✗ and check again.`;
    if (tries >= 2 && ok < rows.length) show.hidden = false;
    typeset(el);
  });
  show.addEventListener('click', () => {
    rows.forEach((r) => { r.sel.value = String(opts.indexOf(r.it.answer)); r.li.dataset.state = 'shown'; r.out.dataset.state = 'hint'; r.out.innerHTML = 'Answer: ' + md(r.it.answer) + (r.it.feedback ? ' — ' + md(r.it.feedback) : ''); });
    msg.textContent = 'The answers are shown. Read why each one fits.'; typeset(el);
  });
  el.append(...(d.prompt ? [h('p', { class: 'fx-prompt', html: md(d.prompt) })] : []), h('ol', { class: 'fx-match' }, rows.map((r) => r.li)),
    h('p', { class: 'fx-actions' }, check, ' ', show), msg);
};
