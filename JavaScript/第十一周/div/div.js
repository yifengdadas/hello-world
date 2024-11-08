$("button").eq(0).click(function () {
    $("div").show(1000, function () {
        alert("以显示");
    });
});
$("button").eq(1).click(function () {
    $("div").hide(1000, function () {
        alert("已隐藏");
    });
});
$("button").eq(2).click(function () {
    $("div").toggle(1000);
});