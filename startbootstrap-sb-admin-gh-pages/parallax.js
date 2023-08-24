var image = document.querySelector('.parallax');
var zoomFactor = parseFloat(image.getAttribute('data-zoom'));
var scrollFactor = 0.001;

window.addEventListener('scroll', function() {
    var scrollY = window.scrollY || window.pageYOffset;
    var zoomedScale = 1 + (scrollY * scrollFactor * zoomFactor);

    // Limit the zoom effect
    if (zoomedScale > 1 + zoomFactor) {
        zoomedScale = 1 + zoomFactor;
    }

    image.style.transform = `scale(${zoomedScale})`;
});
