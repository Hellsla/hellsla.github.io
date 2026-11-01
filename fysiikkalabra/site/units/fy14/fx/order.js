/* Putting things in order (data-fx="order"): the steps of a process, the lines of a dialogue, events in time. The
   list starts scrambled; "Move up" / "Move down" buttons on each line (keyboard and touch, no dragging needed);
   "Check" says how many are in the right place and marks each line. Data: {prompt?, items: [text in the right
   order], lang?: "fr", explain?: text shown when the order is right, hints?: [text by position]}. */
window.FX.order = (el, d, A) => {
  const { h, md, scramble, store, typeset } = A;
  const saved = store.get(el.id);
  let order = Array.isArray(saved) && saved.length === d.items.length ? saved : scramble(d.items.map((_, i) => i), el.id);
  const list = h('ol', { class: 'fx-order' });
  const msg = h('p', { class: 'fx-msg', 'aria-live': 'polite' });
  let tries = 0;
  const draw = (focus) => {
    list.textContent = '';
    order.forEach((k, pos) => {
      const up = h('button', { type: 'button', class: 'fx-move', 'aria-label': 'Move up: ' + d.items[k].replace(/[*{}\/]/g, ''), disabled: pos === 0 }, '↑');
      const dn = h('button', { type: 'button', class: 'fx-move', 'aria-label': 'Move down: ' + d.items[k].replace(/[*{}\/]/g, ''), disabled: pos === order.length - 1 }, '↓');
      up.addEventListener('click', () => move(pos, -1, 'up')); dn.addEventListener('click', () => move(pos, 1, 'down'));
      list.append(h('li', { class: 'fx-order-row', 'data-k': k }, h('span', { class: 'fx-order-text', html: md(d.items[k]), lang: d.lang || false }), h('span', { class: 'fx-order-btns' }, up, dn)));
    });
    if (focus) { const b = list.children[focus.pos] && list.children[focus.pos].querySelectorAll('.fx-move')[focus.dir === 'up' ? 0 : 1]; (b && !b.disabled ? b : list.children[focus.pos].querySelector('.fx-move:not([disabled])')).focus(); }
    typeset(list);
  };
  const move = (pos, step, dir) => {
    const to = pos + step; if (to < 0 || to >= order.length) return;
    [order[pos], order[to]] = [order[to], order[pos]]; store.set(el.id, order); msg.textContent = ''; draw({ pos: to, dir });
  };
  const check = h('button', { type: 'button', class: 'fx-btn' }, 'Check the order');
  check.addEventListener('click', () => {
    tries++; let ok = 0;
    [...list.children].forEach((li, pos) => { const good = Number(li.dataset.k) === pos; li.dataset.state = good ? 'ok' : 'no'; if (good) ok++; });
    if (ok === order.length) msg.innerHTML = '<strong>✓ The order is right.</strong> ' + md(d.explain || '');
    else {
      const wrong = order.findIndex((k, pos) => k !== pos);
      msg.innerHTML = `✗ ${ok} of ${order.length} lines are in the right place (marked ✓).` + (tries >= 2 && d.hints && d.hints[wrong] ? ' Hint: ' + md(d.hints[wrong]) : '');
    }
    typeset(msg);
  });
  draw();
  el.append(...(d.prompt ? [h('p', { class: 'fx-prompt', html: md(d.prompt) })] : []), list, h('p', { class: 'fx-actions' }, check), msg);
};
