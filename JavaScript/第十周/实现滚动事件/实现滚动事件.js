var goBack = document.querySelector('.goBack');
var slider = document.querySelector('.slider-bar');
var banner = document.querySelector('.banner');
var header = document.querySelector('.header');

goBack.onclick = function () {
    window.scrollTo(0, 0);
};

document.onscroll = function () {
    slider.style.top = window.pageYOffset;
    if (window.pageYOffset > (header.scrollHeight + banner.scrollHeight + 30)) {
        goBack.style.display = 'block';
        slider.style.position = 'fixed';
        slider.style.left = '85%';
        slider.style.top = '0px';
    } else {
        slider.style.position = 'absolute';
        slider.style.left = '85%';
        slider.style.top = header.scrollHeight + banner.scrollHeight + 30 + 'px';
        goBack.style.display = 'none';
    }
};