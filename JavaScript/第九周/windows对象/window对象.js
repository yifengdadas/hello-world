window.addEventListener('load', function () {
    var div = this.document.querySelector('div');
    window.addEventListener('resize', function () {
        if (window.innerWidth <= 800) {
            div.style.display = 'none';
        } else {
            div.style.display = 'block';
        }
    });
});