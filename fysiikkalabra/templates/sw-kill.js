/* Emergency switch (work queue 17a PR 1): published as sw.js it replaces a broken worker, deletes the worker's caches
   and unregisters itself. fl-tts-supertonic3-v1 (the read-aloud model) is not touched. */
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", e => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (k.startsWith("fl-sw-")) await caches.delete(k);
    await self.registration.unregister();
    for (const c of await self.clients.matchAll({ type: "window" })) c.navigate(c.url).catch(() => {});
  })());
});
