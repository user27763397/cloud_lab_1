USE lab5;

DROP TRIGGER IF EXISTS insert_foreign_key;
DROP TRIGGER IF EXISTS update_foreign_key;
DROP TRIGGER IF EXISTS delete_foreign_key;
DROP PROCEDURE IF EXISTS insert_route_type;
DROP PROCEDURE IF EXISTS insert_route_stops;
DROP PROCEDURE IF EXISTS insert_noname;
DROP FUNCTION IF EXISTS calculate_distance;
DROP PROCEDURE IF EXISTS get_calculate_distance;
DROP TRIGGER IF EXISTS forbid_deletion;
DROP TRIGGER IF EXISTS insert_validate_form;
DROP TRIGGER IF EXISTS update_validate_form;
DROP TRIGGER IF EXISTS insert_allowed_port_of_arrival;
DROP TRIGGER IF EXISTS update_allowed_port_of_arrival;

DELIMITER //

CREATE TRIGGER insert_foreign_key
BEFORE INSERT ON hotel_owner
FOR EACH ROW
BEGIN
    DECLARE hotel_exists INT;
    SELECT COUNT(*) INTO hotel_exists FROM hotel_info WHERE id = NEW.hotel_id;
    IF hotel_exists = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Hote; does not exist';
    END IF;
END //

CREATE TRIGGER update_foreign_key
BEFORE UPDATE ON hotel_owner
FOR EACH ROW
BEGIN
    DECLARE hotel_exists INT;
    SELECT COUNT(*) INTO hotel_exists FROM hotel_info WHERE id = NEW.hotel_id;
    IF hotel_exists = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Hotel does not exist.';
    END IF;
END //

CREATE TRIGGER delete_foreign_key
BEFORE DELETE ON hotel_info
FOR EACH ROW
BEGIN
    DECLARE hotel_count INT;
    SELECT COUNT(*) INTO hotel_count FROM hotel_owner WHERE hotel_id = OLD.id;
    IF hotel_count > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete hotel_owner.';
    END IF;
END //

CREATE PROCEDURE insert_route_type(
	IN type_name VARCHAR(150)
    )
BEGIN
	INSERT INTO route_types (type_name)
    VALUES (type_name);
END //

CREATE PROCEDURE insert_route_stops(
	IN route_id INT,
    IN stop_id INT,
    IN stop_order INT
    )
BEGIN
	INSERT INTO route_stops (route_id, stop_id, stop_order)
    VALUES (route_id, stop_id, stop_order);
END //

CREATE PROCEDURE insert_noname()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 10 DO
        INSERT INTO route_types (type_name)
        VALUE (CONCAT('Noname', i));
        SET i = i + 1;
    END WHILE;
END //

CREATE FUNCTION calculate_distance(type VARCHAR(10))
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    DECLARE result DECIMAL(10, 2);

    IF type = 'max' THEN
        SELECT MAX(distance_km) INTO result FROM hiking_info;
    ELSEIF type = 'min' THEN
        SELECT MIN(distance_km) INTO result FROM hiking_info;
    ELSEIF type = 'sum' THEN
        SELECT SUM(distance_km) INTO result FROM hiking_info;
    ELSEIF type = 'avg' THEN
        SELECT AVG(distance_km) INTO result FROM hiking_info;
	ELSE
        SET result = NULL;
    END IF;

    RETURN result;
END //

CREATE PROCEDURE get_calculate_distance(type VARCHAR(10))
BEGIN
    SELECT calculate_distance(type) AS result;
END //

CREATE TRIGGER forbid_deletion
BEFORE DELETE ON hiking_info
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'You cannot delete from this table.';
END //

CREATE TRIGGER insert_validate_form
BEFORE INSERT ON bus_info
FOR EACH ROW
BEGIN
    IF NEW.vehicle_type NOT REGEXP '^[A-LN-Z]{2}-[0-9]{3}-[0-9]{2}$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid format.';
    END IF;
END //

CREATE TRIGGER update_validate_form
BEFORE UPDATE ON bus_info
FOR EACH ROW
BEGIN
    IF NEW.vehicle_type NOT REGEXP '^[A-LN-Z]{2}-[0-9]{3}-[0-9]{2}$' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid format.';
    END IF;
END //

CREATE TRIGGER insert_allowed_port_of_arrival
BEFORE INSERT ON cruise_info
FOR EACH ROW
BEGIN
    IF NEW.port_of_arrival NOT IN ("Ізмаїл", "Бердянськ", "Очаків") THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Only Ізмаїл, Бердянськ, and Очаків are allowed.';
    END IF;
END //

CREATE TRIGGER update_allowed_port_of_arrival
BEFORE UPDATE ON cruise_info
FOR EACH ROW
BEGIN
    IF NEW.port_of_arrival NOT IN ("Ізмаїл", "Бердянськ", "Очаків") THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Only Ізмаїл, Бердянськ, and Очаків are allowed.';
    END IF;
END //

DELIMITER //

CREATE DATABASE cur;
USE cur;

DROP PROCEDURE IF EXISTS create_stops_tables;

DELIMITER //

CREATE PROCEDURE create_stops_tables()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE stop_id INT;
    DECLARE cur CURSOR FOR SELECT id FROM lab5.stops;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO stop_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SET @current_timestamp = DATE_FORMAT(NOW(), '%Y%m%d%H%i%s');
        SET @table_name = CONCAT('stop_', stop_id, '_', @current_timestamp);
        SET @num_columns = FLOOR(1 + (RAND() * 9));
        SET @columns = '';

        SET @i = 1;
        WHILE @i <= @num_columns DO
            SET @column_name = CONCAT('col', @i);
            SET @column_type = 'INT';
            SET @columns = CONCAT(@columns, @column_name, ' ', @column_type, IF(@i < @num_columns, ', ', ''));
            SET @i = @i + 1;
        END WHILE;

        SET @create_table_sql = CONCAT('CREATE TABLE ', @table_name, ' (id INT AUTO_INCREMENT PRIMARY KEY, ', @columns, ')');
        PREPARE stmt FROM @create_table_sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;

    END LOOP;

    CLOSE cur;
END //

DELIMITER //

call create_stops_tables();