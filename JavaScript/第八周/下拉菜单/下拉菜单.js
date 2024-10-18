// 获取所有带有下拉菜单的导航项
const navItems = document.querySelectorAll('.nav > li');

// 为每个导航项添加鼠标移入和移出事件
navItems.forEach(item => {
  item.addEventListener('mouseover', () => {
    const dropdown = item.querySelector('ul');
    if (dropdown) {
      dropdown.style.display = 'block';
    }
  });

  item.addEventListener('mouseout', () => {
    const dropdown = item.querySelector('ul');
    if (dropdown) {
      dropdown.style.display = 'none';
    }
  });
});
