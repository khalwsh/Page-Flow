class Book:
    def __init__(self, id , title , author , status , pages):
        self.title = title
        self.author = author
        self.id = id
        self.pages = pages
        self.status = status


    # Getters
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_id(self):
        return self.id

    def get_pages(self):
        return self.pages

    # Setters
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_id(self, id):
        self.id = id

    def set_pages(self, pages):
        self.pages = pages

    # String representation for developers (debugging)
    def __repr__(self):
        return (f"Book(title='{self.title}', author='{self.author}', id='{self.id}', "
                f"pages={self.pages}, ")

    # Human-readable string representation
    def __str__(self):
        return (f"-Book Details-\n"
                f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"ID: {self.id}\n"
                f"Pages: {self.pages}\n")