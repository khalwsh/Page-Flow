# Page Flow
<div align="center">
  <img src="https://github.com/user-attachments/assets/9687cf7d-cd06-445d-b328-d9c9b3124411" alt="logo" style="width:350px;">
</div>

PageFlow – Smooth management of books and records.

## About the Project

# Library Management System
A Python-based library management system using Pygame for the GUI and MySQL for data storage.

## Table of Contents
- [Core Capabilities](#core-capabilities)
- [Key Features](#key-features)
- [Database Design](#database-design)
  - [ER Diagram](#er-diagram)
  - [Database Schema](#database-schema)
  - [Constraints](#constraints)
- [Installation & Setup](#Getting Started)
- [Usage](#usage)

## Core Capabilities
- User authentication and role-based access (Admin/User)
- Book management (add, remove, search, track)
- User management (registration, removal, search)
- Borrowing system with due dates
- Fine calculation for overdue books
- Real-time book availability tracking

## Key Features

### Admin Features
- Add new books to the library inventory
- Remove books from the system
- View all available books
- Search books by title
- View all registered users
- Remove users from the system
- Track borrowed books and return dates
- Monitor and manage fines
- Search for specific user details

### User Features
- Account creation and management
- Browse available books
- Borrow books with automated due dates
- Return borrowed books
- View personal borrowing history
- Receive notifications for overdue books
- Track personal fines

## Database Design

### ER Diagram
```mermaid
erDiagram
    USER ||--o{ PHONES : has
    USER ||--o{ BORROWED : borrows
    USER ||--o{ FINES : receives
    BOOKS ||--o{ BORROWED : "is borrowed in"
    
    USER {
        int id PK
        string fname
        string lname
        string email
        string user_name
        string password
        string Address
    }
    
    PHONES {
        int user_id FK
        string phone_number
    }
    
    BOOKS {
        int id PK
        string title
        string author
        boolean status
        int pages
    }
    
    BORROWED {
        int user_id FK
        int book_id FK
        datetime start_date
        datetime end_date
    }
    
    FINES {
        int user_id FK
        float cost
        datetime date
    }
```
### Database Schema

#### User
```sql
CREATE TABLE user(
	id INT PRIMARY KEY auto_increment,
    fname varchar(50) NOT NULL, 
    lname varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    user_name varchar(50) UNIQUE NOT NULL,
    password varchar(50) NOT NULL 
);
```
#### books
```sql
CREATE TABLE books(
	id INT PRIMARY KEY auto_increment,
    title varchar(50) NOT NULL, 
    author varchar(50) NOT NULL,
    status boolean default false,
    pages smallint    
);
```
#### phones
```sql
CREATE TABLE phones(
	user_id INT , 
    phone_number VARCHAR(15),
    primary key (user_id , phone_number), 
    FOREIGN KEY (user_id) references user(id)
);
```
#### borrowed
```sql
CREATE TABLE borrowed(
	user_id INT , 
    book_id INT ,
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP , 
    end_date TIMESTAMP NOT NULL,
    primary key (user_id , book_id),
	FOREIGN KEY (user_id) references user(id),
    FOREIGN KEY (book_id) references books(id)
);
```
#### Fines
```sql
CREATE TABLE Fines(
	user_id INT ,
    cost INT ,
    Date timestamp default current_timestamp,
    primary key(user_id , Date)
);
```
### Constraints

- **Users must have unique usernames**
- **Books can only be borrowed if they are available (status = 1)**
- **Loan period is set to 10 days by default**
- **Late returns incur a fine of $5 per day**
- **Phone numbers must be either 11 digits or 13 digits (with country code)**
- **Email addresses must contain '@'**
- **Passwords must meet minimum security requirements**
- **Address must contain both numbers and text**
- **All core fields (username, password, name, email, address) are required**

## GUI

### Initial Page
First page offering login options for users or admins (admin credentials hardcoded)

![First Page](https://github.com/user-attachments/assets/2010fd73-2b4a-4019-9ea0-e7e3adfa5743)

### Admin Flow
1. Admin Login Screen
![Admin Login](https://github.com/user-attachments/assets/17804583-395b-44d8-9608-06025c735d13)

2. Admin Dashboard with Management Options
![Admin Options](https://github.com/user-attachments/assets/2dfa45e0-7d6b-4858-8512-72758d17b17b)

### User Flow
1. User Authentication Options
![User Auth Options](https://github.com/user-attachments/assets/0523cb73-a952-4f7c-bacb-204c214bbe49)

2. User Registration Form
![User Registration](https://github.com/user-attachments/assets/84e14487-e7b3-4176-a167-2cb985c8affa)

3. User Login Screen
![User Login](https://github.com/user-attachments/assets/2807fbd9-5c9d-4bfb-b582-32138576145f)

4. User Dashboard
![User Dashboard](https://github.com/user-attachments/assets/79b8e314-852a-47e4-b161-5a7d52d1a5ff)

## Features

- **User Management**: Role-based account control system
- **Book Inventory**: Complete book collection management
- **Borrowing System**: Book checkout and return tracking
- **Search Functionality**: Multi-filter search for books and users
- **Validation**: Comprehensive data integrity checks
- **Fine System**: Automated late return fee calculation

## Built With

- **Python**: Core programming language
- **MySQL**: Database management
- **Pygame**: GUI framework

## Getting Started

### Prerequisites

- Python 3.x ([Download](https://www.python.org/downloads/))
- Pygame module
- MySQL-connector
- Local [database setup](https://github.com/khalwsh/Library-Management-app/tree/main/database)

### Installation

1. Clone repository:
```bash
git clone https://github.com/khalwsh/Library-Management-app.git
cd Library-Management-app
python main.py
```
[demo](https://www.youtube.com/watch?v=0uzFFTsNlHk)
