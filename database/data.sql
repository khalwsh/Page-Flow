-- Insert data into `user` table with `address` column
INSERT INTO user (fname, lname, email, user_name, password, address) VALUES
('John', 'Doe', 'john.doe@example.com', 'johndoe', 'password123', '123 Main St, Springfield'),
('Jane', 'Smith', 'jane.smith@example.com', 'janesmith', 'password456', '456 Elm St, Shelbyville'),
('Alice', 'Johnson', 'alice.j@example.com', 'alicejohnson', 'password789', '789 Oak St, Capital City'),
('Bob', 'Brown', 'bob.brown@example.com', 'bobbrown', 'password321', '101 Maple St, Ogdenville'),
('Charlie', 'Davis', 'charlie.d@example.com', 'charliedavis', 'password654', '202 Pine St, North Haverbrook'),
('Emily', 'Clark', 'emily.c@example.com', 'emilyclark', 'password987', '303 Cedar St, Brockway'),
('David', 'Lopez', 'david.l@example.com', 'davidlopez', 'password112', '404 Birch St, Waverly Hills'),
('Sophia', 'Garcia', 'sophia.g@example.com', 'sophiagarcia', 'password334', '505 Walnut St, Monorail City'),
('Mia', 'Martinez', 'mia.m@example.com', 'miamartinez', 'password556', '606 Chestnut St, Springfield'),
('Liam', 'Harris', 'liam.h@example.com', 'liamharris', 'password778', '707 Ash St, Ogdenville'),
('Emma', 'Hall', 'emma.h@example.com', 'emmahall', 'password990', '808 Poplar St, Shelbyville'),
('Noah', 'Adams', 'noah.a@example.com', 'noahadams', 'password101', '909 Redwood St, Capital City'),
('Olivia', 'Lee', 'olivia.l@example.com', 'olivialee', 'password202', '110 Spruce St, Brockway'),
('James', 'Walker', 'james.w@example.com', 'jameswalker', 'password303', '121 Magnolia St, North Haverbrook'),
('Ava', 'Scott', 'ava.s@example.com', 'avascott', 'password404', '131 Palm St, Waverly Hills');


-- Insert data into `books` table
INSERT INTO books (title, author, status, pages) VALUES
('Book A', 'Author 1', false, 200),
('Book B', 'Author 2', true, 150),
('Book C', 'Author 3', false, 300),
('Book D', 'Author 4', true, 250),
('Book E', 'Author 5', false, 100),
('Book F', 'Author 6', true, 400),
('Book G', 'Author 7', false, 350),
('Book H', 'Author 8', true, 500),
('Book I', 'Author 9', false, 450),
('Book J', 'Author 10', true, 275),
('Book K', 'Author 11', false, 325),
('Book L', 'Author 12', true, 125),
('Book M', 'Author 13', false, 600),
('Book N', 'Author 14', true, 475),
('Book O', 'Author 15', false, 525);

-- Insert data into `phones` table
INSERT INTO phones (user_id, phone_number) VALUES
(10, '1234567890'),
(11 ,'9876543210'),
(12 ,'1122334455'),
(13 ,'6677889900'),
(14 ,'5566778899'),
(15 ,'4433221100'),
(16 ,'7788990011'),
(17 ,'9900112233'),
(19, '6655443322'),
(20, '2233445566'),
(21, '8899001122'),
(22, '3344556677'),
(23, '7788001122'),
(22, '2233441100'),
(10, '6677884455');

-- Insert data into `borrowed` table
INSERT INTO borrowed (user_id, book_id, start_date, end_date) VALUES
(10, 15, '2024-12-01 10:00:00', '2024-12-10 18:00:00'),
(11, 16, '2024-12-02 11:00:00', '2024-12-11 19:00:00'),
(12, 17, '2024-12-03 12:00:00', '2024-12-12 20:00:00'),
(13, 18, '2024-12-04 13:00:00', '2024-12-13 21:00:00'),
(14, 19, '2024-12-05 14:00:00', '2024-12-14 22:00:00'),
(15, 6, '2024-12-06 15:00:00', '2024-12-15 23:00:00'),
(16, 7, '2024-12-07 16:00:00', '2024-12-16 08:00:00'),
(17, 8, '2024-12-08 17:00:00', '2024-12-17 09:00:00'),
(19, 9, '2024-12-09 18:00:00', '2024-12-18 10:00:00'),
(20, 10, '2024-12-10 19:00:00', '2024-12-19 11:00:00'),
(21, 11, '2024-12-11 20:00:00', '2024-12-20 12:00:00'),
(22, 12, '2024-12-12 21:00:00', '2024-12-21 13:00:00'),
(23, 13, '2024-12-13 22:00:00', '2024-12-22 14:00:00'),
(10, 14, '2024-12-14 23:00:00', '2024-12-23 15:00:00');
