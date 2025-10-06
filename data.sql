USE lab5;


INSERT INTO route_types (type_name) VALUES
('cruise'),
('hiking'),
('bus'),
('hotelstay'),
('adventure'),
('cultural'),
('historical'),
('wildlife'),
('luxury'),
('budget');


INSERT INTO routes (route_type_id, name, description, duration_days, price_per_person, next_departure_date) VALUES
(1, 'Чорноморський круїз', 'Круїз по Чорному морю з відвідуванням кількох портів.', 7, 1500.00, '2024-12-01'),
(1, 'Середземноморський круїз', 'Розкішний круїз по Середземному морю з зупинками у відомих містах.', 10, 1800.00, '2024-11-20'),
(2, 'Карпатський пішохідний тур', 'Пішохідний тур у горах Карпат з досвідченими гідами.', 5, 800.00, NULL),
(2, 'Поліський пішохідний маршрут', 'Відкрийте красоти Полісся під час нашого пішохідного туру.', 6, 900.00, NULL),
(3, 'Автобусний тур по Києву', 'Оглядова екскурсія по головним визначним пам\'яткам Києва.', 3, 300.00, '2024-11-15'),
(3, 'Автобусний тур по Львову', 'Детальний тур по історичному центру Львова з гідом.', 2, 250.00, '2024-11-30'),
(4, 'Відпочинок у готелі "Сонячний"', 'Комфортний відпочинок у готелі з усіма зручностями.', 10, 2000.00, '2024-12-20'),
(4, 'Відпочинок у готелі "Зоряний"', 'Розкішний відпочинок у готелі з видом на море.', 8, 1700.00, '2024-12-10'),
(4, 'Відпочинок у готелі "Морський"', 'Гостинний відпочинок у готелі біля узбережжя.', 7, 1600.00, '2024-12-05'),
(4, 'Відпочинок у готелі "Карпатський"', 'Туристичний відпочинок у серці Карпатських гір.', 9, 1900.00, '2024-11-25');

INSERT INTO stops (name, location) VALUES
('Київ', 'Україна, Київ'),
('Львів', 'Україна, Львів'),
('Одеса', 'Україна, Одеса'),
('Харків', 'Україна, Харків'),
('Дніпро', 'Україна, Дніпро'),
('Запоріжжя', 'Україна, Запоріжжя'),
('Чернівці', 'Україна, Чернівці'),
('Івано-Франківськ', 'Україна, Івано-Франківськ'),
('Ужгород', 'Україна, Ужгород'),
('Полтава', 'Україна, Полтава'),
('Луцьк', 'Україна, Луцьк'),
('Чернігів', 'Україна, Чернігів'),
('Кропивницький', 'Україна, Кропивницький'),
('Рівне', 'Україна, Рівне'),
('Тернопіль', 'Україна, Тернопіль');


INSERT INTO guides (first_name, last_name, contact_info) VALUES
('Іван', 'Петров', 'ivan.petrov@example.com'),
('Марія', 'Іванова', 'maria.ivanova@example.com'),
('Олексій', 'Сидоренко', 'oleksiy.sydorenko@example.com'),
('Світлана', 'Коваленко', 'svitlana.kovalenko@example.com'),
('Дмитро', 'Богданов', 'dmytro.bogdanov@example.com'),
('Олена', 'Мельник', 'olena.melnyk@example.com'),
('Віктор', 'Лисенко', 'viktor.lysenko@example.com'),
('Наталя', 'Гончар', 'nataliya.gonchar@example.com'),
('Юрій', 'Кравченко', 'yuriy.kravchenko@example.com'),
('Тетяна', 'Дмитрук', 'tetiana.dmytruk@example.com');

INSERT INTO route_stops (route_id, stop_id, stop_order) VALUES
(1, 1, 1),
(1, 3, 2),
(1, 5, 3),
(2, 2, 1),
(2, 4, 2),
(2, 6, 3),
(3, 1, 1),
(3, 2, 2),
(4, 7, 1),
(5, 8, 1),
(6, 9, 1),
(7, 10, 1),
(8, 1, 1),
(9, 2, 1),
(10, 3, 1);


INSERT INTO route_guides (route_id, guide_id, work_date) VALUES
(1, 1, '2024-12-01'),
(1, 2, '2024-12-02'),
(2, 3, '2024-11-20'),
(2, 4, '2024-11-21'),
(3, 5, '2024-11-15'),
(4, 6, '2024-12-10'),
(5, 7, '2024-11-30'),
(6, 8, '2024-12-05'),
(7, 9, '2024-12-20'),
(8, 10, '2024-12-10');

INSERT INTO departures (route_id, departure_date) VALUES
(1, '2024-12-01'),
(2, '2024-11-20'),
(3, '2024-11-15'),
(4, '2024-12-10'),
(5, '2024-11-30'),
(6, '2024-12-05'),
(7, '2024-12-20'),
(8, '2024-12-10'),
(9, '2024-11-25'),
(10, '2024-12-15');

-- Вставка CruiseInfo
INSERT INTO cruise_info (route_id, ship_name, port_of_departure, port_of_arrival) VALUES
(1, 'Морська Зірка', 'Одеса', 'Севастополь'),
(2, 'Сонце Середземномор\'я', 'Іспанія, Барселона', 'Італія, Рим'),
(3, 'Вітрильник Світла', 'Київ', 'Одеса'),
(4, 'Океанічний Бриз', 'Харків', 'Запоріжжя'),
(5, 'Піратський Флот', 'Дніпро', 'Київ'),
(6, 'Галактика', 'Чернівці', 'Львів'),
(7, 'Південний Шлях', 'Івано-Франківськ', 'Ужгород'),
(8, 'Північний Вітер', 'Полтава', 'Харків'),
(9, 'Тропічний Рай', 'Львів', 'Одеса'),
(10, 'Західний Потік', 'Київ', 'Чернівці');


INSERT INTO hiking_info (route_id, difficulty_level, distance_km, elevation_gain_m) VALUES
(3, 'Середній', 20.5, 800),
(4, 'Важкий', 35.0, 1200),
(5, 'Легкий', 15.0, 300),
(6, 'Середній', 25.0, 700),
(7, 'Важкий', 40.0, 1500),
(8, 'Середній', 30.0, 900),
(9, 'Легкий', 10.0, 200),
(10, 'Середній', 22.0, 600),
(2, 'Важкий', 50.0, 2000),
(1, 'Середній', 18.0, 500);


INSERT INTO bus_info (route_id, bus_company, vehicle_type) VALUES
(1, 'Українські Авто', 'Міський автобус'),
(2, 'Зоряний Тур', 'Туристичний автобус'),
(3, 'Мандрівка+', 'Експрес автобус'),
(4, 'Комфорт Транс', 'Привітний автобус'),
(5, 'Швидкісний Транспорт', 'Автобус з кондиціонером'),
(6, 'АвтоСонце', 'Міський автобус'),
(7, 'Турбо Транс', 'Туристичний автобус'),
(8, 'Надійний Авто', 'Експрес автобус'),
(9, 'Комфорт Лайн', 'Привітний автобус'),
(10, 'Магістраль Транс', 'Автобус з кондиціонером');


INSERT INTO hotel_info (route_id, hotel_name, address, amenities) VALUES
(7, 'Готель "Сонячний"', 'вул. Сонячна, Київ, Україна', 'Wi-Fi, Ресторан, Басейн'),
(8, 'Готель "Зоряний"', 'пр. Зоряний, Львів, Україна', 'Wi-Fi, SPA, Фітнес-центр'),
(9, 'Готель "Морський"', 'вул. Морська, Одеса, Україна', 'Wi-Fi, Басейн, Бар'),
(10, 'Готель "Карпатський"', 'вул. Гірська, Івано-Франківськ, Україна', 'Wi-Fi, Ресторан, Трансфер до гір'),
(1, 'Готель "Бриз"', 'вул. Прибережна, Севастополь, Україна', 'Wi-Fi, СПА, Басейн'),
(2, 'Готель "Середземномор\'я"', 'вул. Венеціанська, Рим, Італія', 'Wi-Fi, Ресторан, Тераса'),
(3, 'Готель "Експрес"', 'вул. Центральна, Київ, Україна', 'Wi-Fi, Паркінг, Фітнес-центр'),
(4, 'Готель "Комфорт"', 'пр. Комфорт, Запоріжжя, Україна', 'Wi-Fi, Ресторан, Басейн'),
(5, 'Готель "Турбо"', 'вул. Турбова, Дніпро, Україна', 'Wi-Fi, SPA, Фітнес-центр'),
(6, 'Готель "АвтоСонце"', 'вул. Автомобільна, Чернівці, Україна', 'Wi-Fi, Ресторан, Бар');


DROP PROCEDURE IF EXISTS get_routes_after_route_type;
DROP PROCEDURE IF EXISTS get_cruises_after_route;
DROP PROCEDURE IF EXISTS get_departures_after_route;
DROP PROCEDURE IF EXISTS get_hotels_after_route;
DROP PROCEDURE IF EXISTS get_hiking_after_route;
DROP PROCEDURE IF EXISTS get_busses_after_route;
DROP PROCEDURE IF EXISTS get_routes_in_rs;
DROP PROCEDURE IF EXISTS get_stops_in_rs;
DROP PROCEDURE IF EXISTS get_routes_in_rg;
DROP PROCEDURE IF EXISTS get_guides_in_rg;

DELIMITER //

CREATE PROCEDURE get_routes_after_route_type(
	IN route_type_id INT
    )
BEGIN
	SELECT rt.id AS route_type_id, r.id AS route_id, r.name, r.description, r.duration_days, r.price_per_person, r.next_departure_date
    FROM route_types rt
    JOIN routes r ON r.route_type_id = rt.id
    WHERE r.route_type_id = route_type_id;
END //

CREATE PROCEDURE get_cruises_after_route(
	IN route_id INT
    )
BEGIN
	SELECT r.id AS route_id, c.id AS cruise_info_id, c.ship_name, c.port_of_departure, c.port_of_arrival
    FROM routes r
    JOIN cruise_info c ON c.route_id = r.id
    WHERE c.route_id = route_id;
END //

CREATE PROCEDURE get_departures_after_route(
	IN route_id INT
    )
BEGIN
	SELECT r.id AS route_id, d.id AS departure_id, d.departure_date
    FROM routes r
    JOIN departures d ON d.route_id = r.id
    WHERE d.route_id = route_id;
END //

CREATE PROCEDURE get_hotels_after_route(
	IN route_id INT
    )
BEGIN
	SELECT r.id AS route_id, h.id AS hotel_info_id, h.hotel_name, h.address, h.amenities
    FROM routes r
    JOIN hotel_info h ON h.route_id = r.id
    WHERE h.route_id = route_id;
END //

CREATE PROCEDURE get_hiking_after_route(
	IN route_id INT
    )
BEGIN
	SELECT r.id AS route_id, h.id AS hiking_info_id, h.difficulty_level, h.distance_km, h.elevation_gain_m
    FROM routes r
    JOIN hiking_info h ON h.route_id = r.id
    WHERE h.route_id = route_id;
END //

CREATE PROCEDURE get_busses_after_route(
	IN route_id INT
    )
BEGIN
	SELECT r.id AS route_id, b.id AS bus_info_id, b.bus_company, b.vehicle_type
    FROM routes r
    JOIN bus_info b ON b.route_id = r.id
    WHERE b.route_id = route_id;
END //

CREATE PROCEDURE get_routes_in_rs(
	IN route_id INT
    )
BEGIN
	SELECT rs.id,  rs.stop_id, rs.route_id, r.name route_name, r.description route_description,
    r.duration_days route_duration_days, r.price_per_person route_price_per_person,
    r.next_departure_date route_next_departure_date, s.name stop_name, s.location stop_location
    FROM routes r
    JOIN route_stops rs ON r.id = rs.route_id
    JOIN stops s ON rs.stop_id = s.id
    WHERE rs.route_id = route_id;
END //

CREATE PROCEDURE get_stops_in_rs(
	IN stop_id INT
    )
BEGIN
	SELECT rs.id,  rs.stop_id, rs.route_id, r.name route_name, r.description route_description,
    r.duration_days route_duration_days, r.price_per_person route_price_per_person,
    r.next_departure_date route_next_departure_date, s.name stop_name, s.location stop_location
    FROM stops s
    JOIN route_stops rs ON s.id = rs.stop_id
    JOIN routes r ON rs.route_id = r.id
    WHERE rs.stop_id = stop_id;
END //

CREATE PROCEDURE get_routes_in_rg(
	IN route_id INT
    )
BEGIN
	SELECT rg.id, rg.guide_id, rg.route_id, r.name route_name, r.description route_description,
    r.duration_days route_duration_days, r.price_per_person route_price_per_person,
    r.next_departure_date route_next_departure_date, g.first_name guide_first_name,
    g.last_name guide_last_name, g.contact_info guide_contact_info
    FROM routes r
    JOIN route_guides rg ON r.id = rg.route_id
    JOIN guides g ON rg.guide_id = g.id
    WHERE rg.route_id = route_id;
END //

CREATE PROCEDURE get_guides_in_rg(
	IN guide_id INT
    )
BEGIN
	SELECT rg.id, rg.guide_id, rg.route_id, r.name route_name, r.description route_description,
    r.duration_days route_duration_days, r.price_per_person route_price_per_person,
    r.next_departure_date route_next_departure_date, g.first_name guide_first_name,
    g.last_name guide_last_name, g.contact_info guide_contact_info
    FROM guides g
    JOIN route_guides rg ON g.id = rg.guide_id
    JOIN routes r ON rg.route_id = r.id
    WHERE rg.guide_id = guide_id;
END //

