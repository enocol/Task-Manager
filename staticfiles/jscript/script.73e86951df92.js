console.log('script.js loaded')

const mobileMenu = document.getElementById('mobile-menu')
const navBar = document.querySelector('.nav-bar')
const navLinks = document.querySelector('.nav-items')
console.log(navLinks)

mobileMenu.addEventListener('click', () => {
  navBar.classList.toggle('show-hide-menu')
  navLinks.style.display = 'block'
})