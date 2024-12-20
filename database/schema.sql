show databases;
use khalwsh;
CREATE TABLE user(
	id INT PRIMARY KEY auto_increment,
    fname varchar(50) NOT NULL, 
    lname varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    user_name varchar(50) UNIQUE NOT NULL,
    password varchar(50) NOT NULL 
);
CREATE TABLE books(
	id INT PRIMARY KEY auto_increment,
    title varchar(50) NOT NULL, 
    author varchar(50) NOT NULL,
    status boolean default false,
    pages smallint    
);

CREATE TABLE phones(
	user_id INT , 
    phone_number VARCHAR(15),
    primary key (user_id , phone_number), 
    FOREIGN KEY (user_id) references user(id)
);
CREATE TABLE borrowed(
	user_id INT , 
    book_id INT ,
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP , 
    end_date TIMESTAMP NOT NULL,
    primary key (user_id , book_id),
	FOREIGN KEY (user_id) references user(id),
    FOREIGN KEY (book_id) references books(id)
);