-- Check if user exists before setting the payment option
DELIMITER //
CREATE TRIGGER payment_options_insert_trigger
BEFORE INSERT ON payment_options
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1 FROM users WHERE id = NEW.user_id) THEN
        SIGNAL SQLSTATE '23000' SET MESSAGE_TEXT = 'Provided non-existent users.id';
    END IF;
END //
DELIMITER ;

-- Check if user exists before updating the payment option
DELIMITER //
CREATE TRIGGER payment_options_update_trigger
BEFORE UPDATE ON payment_options
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1 FROM users WHERE id = NEW.user_id) THEN
        SIGNAL SQLSTATE '23000' SET MESSAGE_TEXT = 'Provided non-existent users.id';
    END IF;
END //

DELIMITER ;

-- Cascade delete payments if the user gets deleted
DELIMITER //
CREATE TRIGGER users_delete_trigger
AFTER DELETE ON users
FOR EACH ROW
BEGIN
    DELETE FROM payment_options WHERE user_id = OLD.id;
END //
DELIMITER ;


-- Block russian places
DELIMITER //
CREATE TRIGGER block_russian_places_insert_update
BEFORE INSERT ON places
FOR EACH ROW
BEGIN
    IF NEW.country = 'Russia' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insertion of places with country as Russia is not allowed';
    END IF;
END //
DELIMITER ;

-- Check rating formatting
DELIMITER //
CREATE TRIGGER check_ratings_range
BEFORE INSERT ON ratings
FOR EACH ROW
BEGIN
    IF NEW.overall_rating < 0 OR NEW.overall_rating > 5
    OR NEW.cleanliness_rating < 0 OR NEW.cleanliness_rating > 5
    OR NEW.service_rating < 0 OR NEW.service_rating > 5
    OR NEW.value_rating < 0 OR NEW.value_rating > 5 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ratings must be between 0 and 5';
    END IF;
END //
DELIMITER ;

-- Check media type
DELIMITER //
CREATE TRIGGER check_media_url_format
BEFORE INSERT ON media
FOR EACH ROW
BEGIN
    IF NEW.url NOT LIKE '%.jpg' AND NEW.url NOT LIKE '%.mp4' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Media URL must be .jpg or .mp4 datatype';
    END IF;
END //
DELIMITER ;
