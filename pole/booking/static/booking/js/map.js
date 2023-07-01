let center = [41.32145360231076,69.26054294711807];
function init() {
	let map = new ymaps.Map('map-test', {
		center: center,
		zoom: 13
	}, {
        // Зададим ограниченную область прямоугольником, 
        // примерно описывающим Санкт-Петербург.
        restrictMapArea: [
            [41.21995919178839,68.98802733956808],
			[41.42054917876853,69.51537108956808]
        ]
    }),
	objectManager = new ymaps.ObjectManager({
            // Чтобы метки начали кластеризоваться, выставляем опцию.
            clusterize: true,
            // ObjectManager принимает те же опции, что и кластеризатор.
            gridSize: 32,
            clusterDisableClickZoom: true
        });

    // Чтобы задать опции одиночным объектам и кластерам,
    // обратимся к дочерним коллекциям ObjectManager.
    objectManager.objects.options.set('iconColor', '#6B49FF');
    objectManager.objects.options.set('icons', [[50, 50]]);
    objectManager.clusters.options.set('iconColor', '#6B49FF');
    map.geoObjects.add(objectManager);


	data = {
				"type": "FeatureCollection",
				"features": [
					{% for field in fields %}
					    {"type": "Feature", "id": 0, "geometry": {"type": "Point", "coordinates": [41.32145360231076,69.26054294711807]}, "properties": {"balloonContentHeader": "<h5 class='map__cluster__title'>Теннесный корт<h5><p class='map__cluster__free'>Свободен<p>", "balloonContentBody": "<div class='map__cluster__block'><p class='map__cluster__price'>100 000 UZS / <span>час<span><p><a href='#' class='map__cluster__btn'>Подробнее</a><div>", "balloonContentFooter": "", "clusterCaption": "<strong><s>Еще</s> одна</strong> метка", "hintContent": "<strong>Текст  <s>подсказки</s></strong>"}}
				    {% endfor %}
				]
			}

    objectManager.add(data);

	map.controls.remove('geolocationControl'); // удаляем геолокацию
	map.controls.remove('searchControl'); // удаляем поиск
	map.controls.remove('trafficControl'); // удаляем контроль трафика
	map.controls.remove('typeSelector'); // удаляем тип
	map.controls.remove('fullscreenControl'); // удаляем кнопку перехода в полноэкранный режим
	map.controls.remove('zoomControl'); // удаляем контрол зуммирования
	map.controls.remove('rulerControl'); // удаляем контрол правил
}

ymaps.ready(init);