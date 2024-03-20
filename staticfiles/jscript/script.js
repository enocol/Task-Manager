const mobileMenu = document.getElementById('mobile-menu');
const navBar = document.querySelector('.nav-bar');
const navLinks = document.querySelector('.nav-items');



mobileMenu.addEventListener('click', () => {
  navBar.classList.toggle('show-hide-menu');
  navLinks.style.display = 'block';
})


document.addEventListener('click', (e) => {
  if (e.target !== mobileMenu && e.target !== navLinks) {
    navBar.classList.remove('show-hide-menu');
    navLinks.style.display = 'none';
  }
})