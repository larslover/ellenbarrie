const CACHE_NAME = "ellenbarrie-v5";

const FILES_TO_CACHE = [
    "/static/manifest.json"
];

self.addEventListener("install", event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                return cache.addAll(FILES_TO_CACHE);
            })
    );

    self.skipWaiting();
});


self.addEventListener("activate", event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(name => name !== CACHE_NAME)
                    .map(name => caches.delete(name))
            );
        })
    );

    self.clients.claim();
});


self.addEventListener("fetch", event => {

    // Always get Django pages from the server.
    if (event.request.mode === "navigate") {
        event.respondWith(
            fetch(event.request)
        );
        return;
    }

    // Use cache for other resources when available.
    event.respondWith(
        caches.match(event.request)
            .then(cachedResponse => {
                if (cachedResponse) {
                    return cachedResponse;
                }

                return fetch(event.request);
            })
    );
});