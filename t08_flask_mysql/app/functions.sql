DELIMITER //
CREATE FUNCTION getAverageReviewRating()
RETURNS DECIMAL(10,2)
READS SQL DATA
BEGIN
    DECLARE avg_rating DECIMAL(10,2);
    SELECT AVG(rating) INTO avg_rating
    FROM reviews;
    RETURN avg_rating;
END //
DELIMITER ;
SELECT getAverageReviewRating() AS average_review_rating;
