/* Local, anonymous topic search. No student data is collected. */
(() => {
  const input = document.getElementById('lesson-search');
  const results = document.getElementById('search-results');
  const status = document.getElementById('search-status');
  if (!input || !results || !status) return;
  const normal = (s) => String(s).toLocaleLowerCase('fi-FI')
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '').trim();
  let records = [], ready = false;
  const render = () => {
    const q = normal(input.value);
    results.replaceChildren();
    if (q.length < 2) {
      results.hidden = true;
      status.textContent = q ? 'Kirjoita vähintään kaksi merkkiä.' : '';
      return;
    }
    if (!ready) { status.textContent = 'Ladataan hakemistoa…'; return; }
    const parts = q.split(/\s+/);
    const matching = records.filter((r) => parts.every((w) =>
      normal(r.course + ' ' + r.module + ' ' + r.title).includes(w)));
    for (const r of matching.slice(0, 24)) {
      const li = document.createElement('li');
      const node = document.createElement(r.published ? 'a' : 'span');
      if (r.published) node.href = r.id + '.html';
      else node.className = 'planned';
      node.textContent = r.course + ' · ' + r.title;
      const state = document.createElement('small');
      state.textContent = r.published ? 'Avaa' : 'Tulossa';
      li.append(node, state);
      results.appendChild(li);
    }
    results.hidden = matching.length === 0;
    status.textContent = matching.length
      ? matching.length + ' osumaa' + (matching.length > 24 ? ' · näytetään 24 ensimmäistä' : '')
      : 'Aihetta ei löytynyt. Kokeile toista hakusanaa.';
  };
  input.addEventListener('input', render);
  fetch('catalogue.json').then((r) => {
    if (!r.ok) throw Error('Catalogue not found');
    return r.json();
  }).then((data) => { records = data; ready = true; render(); })
    .catch(() => { ready = true; status.textContent = 'Haku ei ole käytettävissä. Selaa moduuleita alta.'; });
})();
