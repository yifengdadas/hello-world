var modal = document.querySelector('.modal');
var close = document.querySelector('.close');
var login = document.querySelector('.login-header');
var bg = document.querySelector('.login-bg');

login.addEventListener('click', function () {
    modal.style.display = 'block';
    bg.style.display = 'block';
    modal.style.backgroundColor = 'white';
});

close.addEventListener('click', function () {
    modal.style.display = 'none';
    bg.style.display = 'none';
});

modal.addEventListener('mousedown', function (e) {
    var x = e.pageX - modal.offsetLeft;
    var y = e.pageY - modal.offsetTop;
    var move = function (e) {
        modal.style.left = e.pageX - x + 'px';
        modal.style.top = e.pageY - y + 'px';
    };
    document.addEventListener('mousemove', move);
    document.addEventListener('mouseup', function (e) {
        document.removeEventListener('mousemove', move);
    });
});