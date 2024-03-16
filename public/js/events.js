window.addEventListener('scroll', function() {
    var scrollButton = document.getElementById("scroll-to-top");
    if (window.innerWidth <= 768 && window.scrollY > 100) {
        scrollButton.style.display = "block";
    } else {
        scrollButton.style.display = "none";
    }
});

document.getElementById("scroll-to-top").addEventListener("click", function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});