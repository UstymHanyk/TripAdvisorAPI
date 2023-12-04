DELIMITER //

CREATE PROCEDURE InsertIntoMedia(
    IN media_review_id INT,
    IN media_type VARCHAR(45),
    IN media_url VARCHAR(255),
    IN media_upload_date DATE
)
BEGIN
    INSERT INTO media (review_id, type, url, upload_date)
    VALUES (media_review_id, media_type, media_url, media_upload_date);
END //
DELIMITER ;
CALL InsertIntoMedia(1, 'Image', 'http://example.com/image.jpg', '2023-12-05');


DELIMITER //
CREATE PROCEDURE InsertIntoPlaceOwner(IN place_id INT, IN owner_id INT)
BEGIN
    DECLARE place_name VARCHAR(255);
    DECLARE owner_email VARCHAR(255);

    SELECT name INTO place_name FROM places WHERE id = place_id;
    SELECT email INTO owner_email FROM owners WHERE id = owner_id;
    IF (place_name IS NOT NULL AND owner_email IS NOT NULL) THEN
        INSERT INTO place_owners (place_id, owner_id, place_name, owner_email)
        VALUES (place_id, owner_id, place_name, owner_email);
        SELECT 'Inserted successfully' AS Message;
    ELSE
        SELECT 'Provided non-existent ids' AS Message;
    END IF;
END //
DELIMITER ;
CALL InsertIntoPlaceOwner(2, 4);


DELIMITER //

CREATE PROCEDURE Insert10NewMedia()
BEGIN
    DECLARE i INT DEFAULT 0;
    WHILE i < 10 DO
        INSERT INTO media (review_id, type, url, upload_date)
        VALUES (
			1,
            'Image',
            CONCAT('https://imgur.com/Noname#', i, '.jpg'),
            CURDATE()
        );
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;
CALL Insert10NewMedia();