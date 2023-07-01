const showMapListBtn = document.querySelector('.show__cart-list');
const showMapListBtnText = document.querySelector('.show__cart-list span');
const header = document.querySelector('.header');
const myMap = document.querySelector('.map');
const mainContent = document.querySelector('.main-content');
const myHTML = document.querySelector('html');

function showMapListToggle() {
    showMapListBtn.classList.toggle("list");
    header.classList.toggle("list");
	
	if (showMapListBtnText.innerHTML == 'Показать список'){
		showMapListBtnText.innerHTML = 'Показать карту';
	}else if (showMapListBtnText.innerHTML == 'Показать карту'){
		showMapListBtnText.innerHTML = 'Показать список';
	}
}

const screenHeight = screen.height;
const screenWidth = screen.width;
const headerHeight = screenHeight - 280;

if (screenWidth < 576) {
	header.style.height = `${headerHeight}px`;
	myMap.style.height = `${headerHeight}px`;
	mainContent.style.height = `${headerHeight}px`;
	myHTML.style.overflow = "hidden";
}
showMapListBtn.addEventListener("click", showMapListToggle);