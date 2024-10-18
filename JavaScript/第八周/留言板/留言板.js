var btn = document.querySelector('button');
var text = document.querySelector('textarea'); var ul = document.querySelector('ul');
btn.onclick = function () {
     if (text.value == '') {
        alert('您没有输入内容');
         return false;
     } else {
         var li = document.createElement('li');
         li.innerHTML = text.value + '<a name="del" href="javascript:;">删除</a><a name="copy" href=javascript:;>复制</a>';
         ul.insertBefore(li, ul.children[ul.length - 1]);
         var as = document.getElementsByName("del");
         var as2 = document.getElementsByName("copy");
         function setOnClick(){
             for (var i = 0; i < as.length; i++) {
                 as[i].onclick = function () {
                     ul.removeChild(this.parentNode);
                 };
             }
             for (var i = 0; i < as2.length; i++) {
                 as2[i].onclick = function () {
                     ul.insertBefore(this.parentNode.cloneNode(true), ul.children[ul.length - 1]);
                     setOnClick();
                }
             }
        }
         setOnClick();
     }
};