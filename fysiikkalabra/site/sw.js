/* Ruukkilabra service worker (work queue 17a PR 1, teacher 2026-11-15): pages visited once work without a network.
   No interface text, no tracking: it only keeps copies of same-origin files the student has already fetched.
   Written to site/sw.js by scripts/build.py (the build hash below is the hash of the shared scripts, so a new release
   is a new file and the browser replaces the old worker). To remove a broken worker see docs/audits/2026-11-15-kehitys-ilman-kirjautumista.md
   "Hätäkatkaisu": publish templates/sw-kill.js as sw.js (build with FL_SW_KILL=1).
   build: 5bd7d2973680 */
"use strict";
const SCHEMA = "1";
const PREFIX = "fl-sw-";                      // only caches with this prefix are ours: fl-tts-supertonic3-v1 (read aloud) is never touched
const PAGES = PREFIX + SCHEMA + "-pages";
const STATIC = PREFIX + SCHEMA + "-static";
const MAX = {}; MAX[PAGES] = 120; MAX[STATIC] = 1500;   // entries; the oldest go first
const NET_WAIT = 3000;                        // ms a page waits for the network before the cached copy is shown
const SKIP = /(^|\/)(models|audio)\//;        // the read-aloud model has its own cache; the recordings are large and streamed
const SCOPE = new URL(self.registration.scope);

function relPath(url) { return url.pathname.slice(SCOPE.pathname.length); }
function ours(url) {
  return url.origin === SCOPE.origin && url.pathname.startsWith(SCOPE.pathname) && !SKIP.test(relPath(url)) && relPath(url) !== "sw.js";
}
function isPage(req, url) {
  return req.mode === "navigate" || /\.html$/.test(url.pathname) || url.pathname.endsWith("/");
}
function pageKey(url) { const u = new URL(url); u.search = ""; u.hash = ""; return u.href; }

async function trim(name) {
  const c = await caches.open(name), keys = await c.keys();
  let drop = keys.length - MAX[name];
  try {
    const e = await navigator.storage.estimate();
    if (e.quota && e.usage / e.quota > 0.8) drop = Math.max(drop, 20);   // nearly full: make room
  } catch (_) {}
  for (let i = 0; i < drop; i++) await c.delete(keys[i]);
}
async function keep(name, key, res) {
  if (!res || res.status !== 200 || res.type !== "basic" || res.redirected) return;
  const c = await caches.open(name);
  await c.delete(key); await c.put(key, res.clone());   // delete first: a refreshed copy counts as the newest
  await trim(name);
}

self.addEventListener("install", e => { e.waitUntil(self.skipWaiting()); });
self.addEventListener("activate", e => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (k.startsWith(PREFIX) && k !== PAGES && k !== STATIC) await caches.delete(k);
    await self.clients.claim();
  })());
});

async function page(req, event) {
  const url = new URL(req.url), key = pageKey(url);
  const cache = await caches.open(PAGES);
  const net = fetch(req).then(async res => { await keep(PAGES, key, res); return res; });
  const cached = await cache.match(key) || (url.pathname.endsWith("/") ? await cache.match(key + "index.html") : undefined);
  if (!cached) return net;                                   // never visited: the network decides, offline it is the browser's own error page
  const timer = new Promise(r => setTimeout(() => r(cached), NET_WAIT));
  event.waitUntil(net.catch(() => {}));                      // a slow answer still refreshes the copy
  return Promise.race([net.catch(() => cached), timer]);
}
async function versioned(req) {                              // ?v=<hash> files never change: cache first
  const cache = await caches.open(STATIC), hit = await cache.match(req.url);
  if (hit) return hit;
  const res = await fetch(req); await keep(STATIC, req.url, res); return res;
}
async function revalidate(req, event) {                      // everything else: the copy at once, a fresh one fetched behind it
  const cache = await caches.open(STATIC), hit = await cache.match(req.url);
  const net = fetch(req).then(async res => { await keep(STATIC, req.url, res); return res; });
  if (hit) { event.waitUntil(net.catch(() => {})); return hit; }
  return net;
}

self.addEventListener("fetch", event => {
  const req = event.request, url = new URL(req.url);
  if (req.method !== "GET" || req.headers.has("range") || !ours(url)) return;
  event.respondWith(isPage(req, url) ? page(req, event) : url.searchParams.has("v") ? versioned(req) : revalidate(req, event));
});

// A page that loaded before this worker took over sends the addresses it already used (offline.js), so the first
// visit works offline too.
self.addEventListener("message", event => {
  const d = event.data;
  if (!d || d.type !== "fl-cache" || !Array.isArray(d.urls)) return;
  event.waitUntil(Promise.all(d.urls.slice(0, 400).map(async u => {
    try {
      const url = new URL(u, SCOPE);
      if (!ours(url)) return;
      const page_ = isPage({ mode: "no-cors" }, url);
      const res = await fetch(url.href, { cache: "reload" });
      await keep(page_ ? PAGES : STATIC, page_ ? pageKey(url) : url.href, res);
    } catch (_) {}
  })));
});
