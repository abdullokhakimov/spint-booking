const showMapListBtn = document.querySelector('.show__cart-list');
const showMapListBtnText = document.querySelector('.show__cart-list span');
const myMap = document.querySelector('.map');
const mainContent = document.querySelector('.main-content');

function showMapListToggle() {
    showMapListBtn.classList.toggle("list");
    header.classList.toggle("list");
	
	if (showMapListBtnText.innerHTML == 'Показать список'){
		showMapListBtnText.innerHTML = 'Показать карту';
	}else if (showMapListBtnText.innerHTML == 'Показать карту'){
		showMapListBtnText.innerHTML = 'Показать список';
	}
}

if (screenWidth < 576) {
	header.style.height = `${headerHeight}px`;
	myMap.style.height = `${headerHeight}px`;
	mainContent.style.height = `${headerHeight}px`;
	myHTML.style.overflow = "hidden";
}
showMapListBtn.addEventListener("click", showMapListToggle);