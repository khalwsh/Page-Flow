class User:
    '''
    what can admin do ?
    - see all available books
    - delete books from db
    - add books to db
    - see list of all users
    - see list of all users didn't return their book in time

    what the user can do ?
    - see user profile
    - see available books
    - borrow a book
    - return a book
    '''
    def __init__(self ,user_name, password, id, email, fname, lname, Address, phones, borrowed_books):
        self.username = user_name
        self.password = password
        self.id = id
        self.email = email
        self.fname = fname
        self.lname = lname
        self.Address = Address
        self.Phones = phones
        self.borrowed_books = borrowed_books

    # Getters
    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_id(self):
        return self.id

    def get_mail(self):
        return self.mail

    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def get_address(self):
        return self.Address

    def get_phones(self):
        return self.Phones

    def get_borrowed_books(self):
        return self.borrowed_books

    # Setters
    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_id(self, id):
        self.id = id

    def set_mail(self, mail):
        self.mail = mail

    def set_fname(self, fname):
        self.fname = fname

    def set_lname(self, lname):
        self.lname = lname

    def set_address(self, Address):
        self.Address = Address

    def set_phones(self, Phones):
        self.Phones = Phones

    def set_borrowed_books(self, borrowed_books):
        self.borrowed_books = borrowed_books

    # String representation for developers (debugging)
    def __repr__(self):
        return (f"User(username='{self.username}', password='{self.password}', "
                f"id='{self.id}', mail='{self.mail}', fname='{self.fname}', "
                f"lname='{self.lname}', Address='{self.Address}', "
                f"Phones={self.Phones}, borrowed_books={self.borrowed_books})")

    def __str__(self):
        return (f"--User Details--\n"
                f"Name: {self.fname} {self.lname}\n"
                f"Username: {self.username}\n"
                f"Email: {self.email}\n"
                f"ID: {self.id}\n"
                f"Address: {self.Address}\n"
                f"Phones: {self.Phones}\n"
                f"Borrowed Books: {len(self.borrowed_books)}\n")