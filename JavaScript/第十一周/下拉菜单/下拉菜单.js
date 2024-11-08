$(".nav>li").mouseover(function () {
    $(this).children("ul").slideDown(200);
});
$(".nav>li").mouseout(function () {
    $(this).children("ul").slideUp(200);
});