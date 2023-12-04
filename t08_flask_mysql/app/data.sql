


INSERT INTO owneplace_ownersplace_ownersrs (first_name, last_name, email, contact_number) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210'),
('Bob', 'Johnson', 'bob.johnson@example.com', '555-555-5555'),
('Alice', 'Williams', 'alice.williams@example.com', '111-222-3333'),
('David', 'Brown', 'david.brown@example.com', '777-888-9999'),
('Eva', 'Davis', 'eva.davis@example.com', '444-555-6666'),
('Michael', 'Wilson', 'michael.wilson@example.com', '333-222-1111'),
('Sophia', 'Moore', 'sophia.moore@example.com', '666-777-8888'),
('Oliver', 'Jones', 'oliver.jones@example.com', '999-888-7777'),
('Emma', 'Martinez', 'emma.martinez@example.com', '111-999-7777');

INSERT INTO places (name, city, country, latitude, longitude, description, category, working_hours) VALUES
('Restaurant A', 'City A', 'Country A', 123.456, 789.123, 'A great place to dine', 'Restaurant', '9 AM - 9 PM'),
('Hotel B', 'City B', 'Country B', 456.789, 321.654, 'Luxurious hotel', 'Hotel', '24/7'),
('Museum C', 'City C', 'Country C', 789.123, 654.321, 'Explore art and history', 'Museum', '10 AM - 5 PM'),
('Park D', 'City D', 'Country D', 234.567, 876.123, 'Beautiful park for picnics', 'Park', '8 AM - 8 PM'),
('Cafe E', 'City E', 'Country E', 567.890, 432.109, 'Cozy cafe with great coffee', 'Cafe', '7 AM - 7 PM'),
('Beach F', 'City F', 'Country F', 654.321, 321.654, 'Sandy beach for relaxation', 'Beach', 'Open all day'),
('Theater G', 'City G', 'Country G', 987.123, 123.987, 'Live performances and shows', 'Theater', '6 PM - 11 PM'),
('Shop H', 'City H', 'Country H', 321.654, 654.321, 'Retail therapy destination', 'Shop', '10 AM - 6 PM'),
('Zoo I', 'City I', 'Country I', 111.222, 999.888, 'Home to various exotic animals', 'Zoo', '9 AM - 5 PM'),
('Gym J', 'City J', 'Country J', 222.333, 777.888, 'Fitness and workout center', 'Gym', '6 AM - 10 PM');

INSERT INTO place_owners (place_id, owner_id) VALUES
(1, 1),
(2, 2),
(3, 2),
(3, 4),
(5, 3),
(6, 3),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO users (name, email) VALUES
('User 1', 'user1@example.com'),
('User 2', 'user2@example.com'),
('User 3', 'user3@example.com'),
('User 4', 'user4@example.com'),
('User 5', 'user5@example.com'),
('User 6', 'user6@example.com'),
('User 7', 'user7@example.com'),
('User 8', 'user8@example.com'),
('User 9', 'user9@example.com'),
('User 10', 'user10@example.com');

INSERT INTO reviews (user_id, place_id, text, date, rating) VALUES
(1, 1, 'Great restaurant!', '2023-10-24', 4.5),
(2, 2, 'Wonderful hotel experience', '2023-10-25', 5.0),
(3, 3, 'Fascinating museum', '2023-10-26', 4.0),
(4, 4, 'Relaxing day at the park', '2023-10-27', 4.2),
(5, 5, 'Delicious coffee at the cafe', '2023-10-28', 4.8),
(6, 6, 'Sunbathing on the beach', '2023-10-29', 4.7),
(7, 7, 'Impressive theater show', '2023-10-30', 4.6),
(8, 8, 'Shopping spree at the store', '2023-10-31', 4.9),
(9, 9, 'Zoo adventure with the family', '2023-11-01', 4.4),
(10, 10, 'Intense workout at the gym', '2023-11-02', 4.3);


INSERT INTO media (review_id, type, url, upload_date) VALUES
(1, 'Image', 'http://example.com/image1.jpg', '2023-10-24'),
(2, 'Video', 'http://example.com/video1.mp4', '2023-10-25'),
(3, 'Image', 'http://example.com/image2.jpg', '2023-10-26'),
(4, 'Video', 'http://example.com/video2.mp4', '2023-10-27'),
(5, 'Image', 'http://example.com/image3.jpg', '2023-10-28'),
(6, 'Video', 'http://example.com/video3.mp4', '2023-10-29'),
(7, 'Image', 'http://example.com/image4.jpg', '2023-10-30'),
(8, 'Video', 'http://example.com/video4.mp4', '2023-10-31'),
(9, 'Image', 'http://example.com/image5.jpg', '2023-11-01'),
(10, 'Video', 'http://example.com/video5.mp4', '2023-11-02');


INSERT INTO ratings (place_id, overall_rating, cleanliness_rating, service_rating, value_rating) VALUES
(1, 4.7, 4.5, 4.8, 4.6),
(2, 4.9, 4.9, 5.0, 4.7),
(3, 4.2, 4.1, 4.3, 4.0),
(4, 4.5, 4.6, 4.4, 4.4),
(5, 4.8, 4.7, 4.9, 4.8),
(6, 4.6, 4.7, 4.5, 4.6),
(7, 4.9, 4.8, 4.7, 4.7),
(8, 4.7, 4.8, 4.9, 4.9),
(9, 4.3, 4.2, 4.4, 4.3),
(10, 4.2, 4.1, 4.3, 4.2);



INSERT INTO user_details (user_id, first_name, last_name, date_of_birth, gender) VALUES
(1, 'John', 'Doe', '1990-05-15', 'Male'),
(2, 'Jane', 'Smith', '1985-12-10', 'Female'),
(3, 'Bob', 'Johnson', '2000-08-20', 'Male'),
(4, 'Alice', 'Williams', '1992-03-30', 'Female'),
(5, 'David', 'Brown', '1988-07-22', 'Male'),
(6, 'Eva', 'Davis', '1995-01-05', 'Female'),
(7, 'Michael', 'Wilson', '1987-11-12', 'Male'),
(8, 'Sophia', 'Moore', '1994-06-18', 'Female'),
(9, 'Oliver', 'Jones', '1991-09-28', 'Male'),
(10, 'Emma', 'Martinez', '1997-02-14', 'Female');

INSERT INTO amenities (name, description) VALUES
('Swimming Pool', 'An outdoor pool available for guests'),
('Free Wi-Fi', 'Complimentary internet access for visitors'),
('Gym', 'Fitness center with modern equipment'),
('Parking', 'On-site parking facilities'),
('Restaurant', 'Dining area with various cuisines'),
('Spa', 'Relaxing spa services available'),
('Pet-friendly', 'Allows pets on the premises'),
('Conference Room', 'Meeting and conference facilities'),
('Bar', 'Bar serving a variety of beverages'),
('Laundry', 'Self-service or in-house laundry facilities');

INSERT INTO place_amenities (place_id, amenity_id) VALUES
(1, 5), (1, 2), (1, 10),
(2, 1), (2, 2), (2, 3), (2, 4),
(3, 2), (3, 8),
(4, 4), (4, 7), (4, 9),
(5, 2), (5, 5), (5, 10),
(6, 1), (6, 2), (6, 7),
(7, 2), (7, 8), (7, 9),
(8, 4), (8, 9),
(9, 1), (9, 2), (9, 7),
(10, 3), (10, 4), (10, 9);

