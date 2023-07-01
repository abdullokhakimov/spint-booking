const navbar = document.querySelector('.navbar');
const navbarNav = document.querySelector('.navbar__nav');
const navbarBurger = document.querySelector('.navbar__burger');

function burgerToggle() {
	navbarBurger.classList.toggle("active");
	navbarNav.classList.toggle("active");
	navbar.classList.toggle("active");
}

navbarBurger.addEventListener("click", burgerToggle);