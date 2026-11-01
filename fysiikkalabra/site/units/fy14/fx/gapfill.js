/* Sentence completion (data-fx="gapfill"): a text with gaps written [[right|wrong 1|wrong 2]]; each gap becomes a
   <select> of the choices in a seeded order. "Check" marks the gaps and shows the line's feedback for a wrong one.
   Data: {prompt?, lang?: "fr", lines: [{text, feedback?, en?: translation shown after a right answer}]}. */
window.FX.gapfill = (el, d, A) => {
  const { h, md, shuffle, typeset } = A;
  const gaps = [];
  const lines = d.lines.map((ln, li) => {
    const p = h('p', { class: 'fx-gap-line', lang: d.lang || false });
    String(ln.text).split(/(\[\[[^\]]+\]\])/).forEach((part, k) => {
      const m = part.match(/^\[\[([^\]]+)\]\]$/);
      if (!m) { if (part) p.append(h('span', { html: md(part) })); return; }
      const choices = m[1].split('|'), right = choices[0];
      const sel = h('select', { 'aria-label': 'Gap ' + (gaps.length + 1) }, h('option', { value: '' }, '…'), ...shuffle(choices, el.id + li + '-' + k).map((c) => h('option', { value: c }, c)));
      gaps.push({ sel, right, li }); p.append(sel);
    });
    const out = h('output', { 'aria-live': 'polite', class: 'fx-gap-out' });
    return { p, out, ln };
  });
  const msg = h('p', { class: 'fx-msg', 'aria-live': 'polite' });
  const check = h('button', { type: 'button', class: 'fx-btn' }, 'Check');
  check.addEventListener('click', () => {
    let ok = 0;
    lines.forEach((l, li) => {
      const mine = gaps.filter((g) => g.li === li);
      const good = mine.every((g) => g.sel.value === g.right), blank = mine.some((g) => !g.sel.value);
      mine.forEach((g) => { g.sel.dataset.state = !g.sel.value ? '' : g.sel.value === g.right ? 'ok' : 'no'; });
      l.out.dataset.state = blank ? 'hint' : good ? 'ok' : 'no';
      l.out.innerHTML = blank ? 'Fill every gap.' : good ? 'Right.' + (l.ln.en ? ' <span class="fx-en" lang="en">' + md(l.ln.en) + '</span>' : '') : 'Not yet. ' + md(l.ln.feedback || 'Read the whole sentence again.');
      if (good && !blank) ok++;
    });
    msg.textContent = ok === lines.length ? '✓ Every sentence is right.' : `${ok} of ${lines.length} sentences right.`;
    typeset(el);
  });
  el.append(...(d.prompt ? [h('p', { class: 'fx-prompt', html: md(d.prompt) })] : []),
    h('div', { class: 'fx-gaps' }, lines.map((l) => h('div', { class: 'fx-gap-row' }, l.p, l.out))), h('p', { class: 'fx-actions' }, check), msg);
};
