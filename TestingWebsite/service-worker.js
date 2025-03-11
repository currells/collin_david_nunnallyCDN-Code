self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('recipes-cache').then((cache) => {
      return cache.addAll([
        '/recipes/index.html',
        '/recipes/main.js',
        '/recipes/recipes.css'
      ]);
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
