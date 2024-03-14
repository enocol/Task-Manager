console.log('script.js loaded')

const mobileMenu = document.getElementById('mobile-menu')
const navBar = document.querySelector('.nav-bar')

mobileMenu.addEventListener('click', () => {
  navBar.classList.toggle('show-hide-menu')
})