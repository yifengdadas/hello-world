console.log(location.search);
var params = location.search.substr(1);
console.log(params);
var arr = params.split('=');
console.log(arr);
var div = document.querySelector('div');
div.innerHTML = arr[1] + '欢迎您';