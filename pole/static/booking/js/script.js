const showMapListBtn = document.querySelector('.show__cart-list');
const showMapListBtnText = document.querySelector('.show__cart-list span');
const header = document.querySelector('.header');
const navbarNav = document.querySelector('.navbar__nav');
const navbarBurger = document.querySelector('.navbar__burger');


function showMapListToggle() {
    showMapListBtn.classList.toggle("list");
    header.classList.toggle("list");
	
	if (showMapListBtnText.innerHTML == 'Показать список'){
		showMapListBtnText.innerHTML = 'Показать карту';
	}else if (showMapListBtnText.innerHTML == 'Показать карту'){
		showMapListBtnText.innerHTML = 'Показать список';
	}
}

showMapListBtn.addEventListener("click", showMapListToggle);

var screenHeight = window.innerHeight;
var screenWidth = window.innerWidth;
if (screenWidth < 576) {
	headerHeight = screenHeight - 286
	header.style.height = `${headerHeight}px`
	navbarNav.style.height = `${screenHeight}px`
}



function burgerToggle() {
	navbarBurger.classList.toggle("active");
	navbarNav.classList.toggle("active");
	
}

navbarBurger.addEventListener("click", burgerToggle);