window.addEventListener('scroll', function() {
    var scrollButton = document.getElementById("scroll-to-top");
    if (window.innerWidth <= 768 && window.scrollY > 100) {
        scrollButton.style.display = "block";
    } else {
        scrollButton.style.display = "none";
    }
});

if (window.location.href.includes('movies') || window.location.href.includes('advisory')) {
    document.getElementById("scroll-to-top").addEventListener("click", function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/public/js/service-worker.js').then(function(registration) {
            //console.log('ServiceWorker registration successful with scope: ', registration.scope);
        }, function(err) {
            //console.log('ServiceWorker registration failed: ', err);
        });
    });
}
