/* A video (data-fx="video"): a card with the title, channel, year and length, and a button that loads the YouTube
   player only when the student chooses to (youtube-nocookie.com, so nothing is loaded or stored before the click),
   plus a link to watch it on YouTube. Data: {id, title, channel, year, length, start?: seconds, note?, lang?}. */
window.FX.video = (el, d, A) => {
  const { h, md } = A;
  const src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(d.id) + '?rel=0' + (d.start ? '&start=' + Number(d.start) : '');
  const frame = h('div', { class: 'fx-video-frame' });
  const play = h('button', { type: 'button', class: 'fx-btn' }, '▶ Load the video');
  play.addEventListener('click', () => {
    frame.append(h('iframe', { src, title: d.title, allow: 'accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen', allowfullscreen: true, loading: 'lazy', referrerpolicy: 'strict-origin-when-cross-origin' }));
    play.remove(); frame.classList.add('on'); frame.querySelector('iframe').focus();
  });
  el.append(h('div', { class: 'fx-video-card' },
    h('p', { class: 'fx-video-title', lang: d.lang || false }, h('strong', { html: md(d.title) })),
    h('p', { class: 'fx-video-meta' }, [d.channel, d.year, d.length].filter(Boolean).join(' · ')),
    ...(d.note ? [h('p', { class: 'fx-note', html: md(d.note) })] : []),
    h('p', { class: 'fx-actions' }, play, ' ', h('a', { href: 'https://www.youtube.com/watch?v=' + encodeURIComponent(d.id) + (d.start ? '&t=' + Number(d.start) + 's' : ''), class: 'fx-link' }, 'Watch on YouTube')),
    h('p', { class: 'fx-note' }, 'The player is loaded from YouTube only when you press the button.')), frame);
};
