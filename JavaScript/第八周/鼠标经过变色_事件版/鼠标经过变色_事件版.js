var tBody = document.querySelector("tbody")
tBody.addEventListener('mouseover', function (e) {
    e.target.parentNode.style.backgroundColor = 'pink';
})
tBody.addEventListener('mouseout', function (e) {
    e.target.parentNode.style.backgroundColor = '';
})