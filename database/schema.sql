CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    user_name VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    Address VARCHAR(100) NOT NULL,
    CONSTRAINT valid_email CHECK (email LIKE '%@%.%'),
    CONSTRAINT valid_address CHECK (
        Address REGEXP '[0-9]' AND 
        Address REGEXP '[a-zA-Z]'
    )
);

CREATE TABLE books (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    status BOOLEAN DEFAULT true,
    pages SMALLINT UNSIGNED
);

CREATE TABLE phones (
    user_id INT,
    phone_number VARCHAR(15),
    PRIMARY KEY (user_id, phone_number),
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    CONSTRAINT valid_phone CHECK (
        LENGTH(phone_number) IN (11, 13)
    )
);

CREATE TABLE borrowed (
    user_id INT,
    book_id INT,
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP NOT NULL,
    PRIMARY KEY (user_id, book_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    CONSTRAINT valid_due_date CHECK (
        end_date > start_date
    )
);

CREATE TABLE Fines (
    user_id INT,
    cost DECIMAL(10,2) NOT NULL,
    Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, Date),
    FOREIGN KEY (user_id) REFERENCES user(id),
    CONSTRAINT valid_fine CHECK (cost > 0)
);