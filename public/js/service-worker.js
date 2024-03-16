self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open('app-cache-v1').then(function(cache) {
      return cache.addAll([
        '/',
        '/public/css/style.css',
        '/public/js/error.js',
        '/public/js/events.js',
        '/public/img/null_image.webp',
        '/public/img/logo.svg',
      ]);
    })
  );
});
  
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});
