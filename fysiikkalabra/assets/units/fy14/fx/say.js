/* Phrases to hear and say (data-fx="say"): a table of French phrases with their meaning and a pronunciation tip,
   each with a "Listen" button that uses the browser's own French voice (speechSynthesis; nothing is downloaded or
   sent), and "Slowly" for a slower rate. Where the browser has no voice the buttons are left out and a note says
   to practise with a partner and the teacher. Data: {lang?: "fr-FR", title?, phrases: [{fr, en, tip?}]}. */
window.FX.say = (el, d, A) => {
  const { h, md, speech } = A;
  const lang = d.lang || 'fr-FR';
  const rows = d.phrases.map((p) => {
    const cells = [h('td', { lang: lang.slice(0, 2), class: 'fx-fr' }, h('strong', { html: md(p.fr) })), h('td', { html: md(p.en) + (p.tip ? '<span class="fx-tip">' + md(p.tip) + '</span>' : '') })];
    if (speech.ok) {
      const plain = p.fr.replace(/\*|\{\/?fr\}/g, '');
      cells.push(h('td', { class: 'fx-say-btns' },
        h('button', { type: 'button', class: 'fx-btn fx-small', 'aria-label': 'Listen: ' + plain, onclick: () => speech.say(plain, lang, 0.9) }, '▶ Listen'),
        h('button', { type: 'button', class: 'fx-btn fx-small fx-quiet', 'aria-label': 'Listen slowly: ' + plain, onclick: () => speech.say(plain, lang, 0.6) }, 'Slowly')));
    }
    return h('tr', {}, cells);
  });
  const head = h('tr', {}, h('th', { scope: 'col' }, 'Français'), h('th', { scope: 'col' }, 'Meaning and tip'), ...(speech.ok ? [h('th', { scope: 'col' }, 'Hear it')] : []));
  el.append(h('div', { class: 'fx-table-wrap' }, h('table', { class: 'fx-say' }, ...(d.title ? [h('caption', { html: md(d.title) })] : []), h('thead', {}, head), h('tbody', {}, rows))),
    h('p', { class: 'fx-note' }, speech.ok ? 'The voice is your browser’s own French voice. It is a model, not a native speaker: listen to your teacher and to the videos too.'
      : 'Your browser has no French voice. Practise the phrases aloud with a partner and listen to your teacher.'));
};
