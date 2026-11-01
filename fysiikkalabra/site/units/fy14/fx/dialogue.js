/* A dialogue to read, hear and then perform (data-fx="dialogue"): three steps of support. 1 "Read": the French
   lines with their meaning. 2 "Practise": French only. 3 "Perform": only the English cues, so the pair speaks
   from memory or improvises. Each line can be heard with the browser's French voice. Data: {title?, roles:
   {A: name, B: name}, lines: [{role, fr, en, cue?}], task?: text for the pair}. */
window.FX.dialogue = (el, d, A) => {
  const { h, md, speech } = A;
  const lines = h('ol', { class: 'fx-dlg' });
  const steps = [['read', '1 Read'], ['practise', '2 Practise'], ['perform', '3 Perform']];
  let mode = 'read';
  const draw = () => {
    lines.textContent = '';
    d.lines.forEach((l) => {
      const plain = l.fr.replace(/\*|\{\/?fr\}/g, '');
      const say = speech.ok && mode !== 'perform' ? h('button', { type: 'button', class: 'fx-btn fx-small fx-quiet', 'aria-label': 'Listen: ' + plain, onclick: () => speech.say(plain, 'fr-FR', 0.85) }, '▶') : null;
      const fr = mode === 'perform' ? h('span', { class: 'fx-cue', html: md(l.cue || l.en) }) : h('span', { class: 'fx-fr', lang: 'fr', html: md(l.fr) });
      const en = mode === 'read' ? h('span', { class: 'fx-en', html: md(l.en) }) : null;
      lines.append(h('li', { class: 'fx-dlg-line', 'data-role': l.role }, h('span', { class: 'fx-role' }, d.roles[l.role] || l.role), h('span', { class: 'fx-dlg-text' }, fr, en), say));
    });
  };
  const bar = h('div', { class: 'fx-steps', role: 'group', 'aria-label': 'Support level' }, steps.map(([k, label]) => {
    const b = h('button', { type: 'button', class: 'fx-step', 'aria-pressed': String(k === mode) }, label);
    b.addEventListener('click', () => { mode = k; bar.querySelectorAll('button').forEach((x) => x.setAttribute('aria-pressed', String(x === b))); draw(); });
    return b;
  }));
  draw();
  el.append(...(d.title ? [h('p', { class: 'fx-prompt', html: md(d.title) })] : []), bar, lines, ...(d.task ? [h('p', { class: 'fx-note', html: md(d.task) })] : []));
};
