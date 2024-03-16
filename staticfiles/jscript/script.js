

const mobileMenu = document.getElementById('mobile-menu');
const navBar = document.querySelector('.nav-bar');
const navLinks = document.querySelector('.nav-items');



mobileMenu.addEventListener('click', () => {
  navBar.classList.toggle('show-hide-menu');
  navLinks.style.display = 'block';
})



const deletebutton = document.getElementById('deletebtn');
console.log('deletebutton', deletebutton);

deletebutton.addEventListener('click', () => {
  
  console.log('delete button clicked');
  const divContainer = document.createElement('div');
  divContainer.className = 'container1'
  divContainer.innerHTML = `<h4>Are you sure you want to delete</h4>`
  document.body.appendChild(divContainer);

})

 