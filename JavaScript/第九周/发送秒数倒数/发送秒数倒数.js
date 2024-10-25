var btn = document.querySelector('button');
var time = 60;
btn.addEventListener('click', function () {
    btn.disabled = true;
    var timer = setInterval(function () {
        if (time == 0) {
            clearInterval(timer);
            btn.disabled = false;
            btn.innerHTML = '发送';
        } else {
            btn.innerHTML = '还剩下' + time + '秒';
            time--;
        }
    }, 1000);
})