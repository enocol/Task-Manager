const mobileMenu = document.getElementById('mobile-menu');
const navBar = document.querySelector('.nav-bar');
const navLinks = document.querySelector('.nav-items');



mobileMenu.addEventListener('click', () => {
  navBar.classList.toggle('show-hide-menu');
  navLinks.style.display = 'block';
})


