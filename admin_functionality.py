import sys
import pygame

from colors import BLACK, WHITE
from db_manager import insert_book, delete_book, substr_search, get_available_books, get_all_users, delete_user, \
    load_user, get_borrowed_books
from utilities import adding_new_book, field_input_page, draw_popout


def admin_functonality(WINDOW, HEIGHT, WIDTH, cursor, mydb):
    """
        admin_functionality(WINDOW, HEIGHT, WIDTH, cursor, mydb)

        Provides the main functionality page for the admin in the library management system.
        Allows the admin to perform various operations related to books and users.

        Parameters:
            WINDOW (pygame.Surface): The Pygame window surface where the interface is rendered.
            HEIGHT (int): The height of the Pygame window.
            WIDTH (int): The width of the Pygame window.
            cursor (MySQLCursor): The database cursor to execute queries.
            mydb (MySQLConnection): The database connection to commit changes.

        Features:
            - Add a new book to the library.
            - Remove a book from the library by its ID.
            - Search for books by their name (substring search).
            - View a list of all available books.
            - View a list of all registered users.
            - Remove a user from the system by their ID.
            - Search for user details by their name.
            - View a list of all borrowed books with their borrowing and return dates.

        Navigation:
            - Press ESC to return to the previous page.

        Database Integration:
            - Uses various functions from `db_manager` for database operations like `insert_book`, `delete_book`, `substr_search`, and others.

        Return:
            str: Returns `"prev"` if the ESC key is pressed to navigate back.
"""
    while True:
        library_background = pygame.image.load('assets/Library_background.jpeg').convert()
        WINDOW.blit(library_background, (0, 0))

        # Top row button rectangles
        add_book_button = pygame.Rect(50, HEIGHT // 3, 230, 50)
        remove_book_button = pygame.Rect(300, HEIGHT // 3, 230, 50)
        available_books_button = pygame.Rect(550, HEIGHT // 3, 230, 50)

        # Bottom row button rectangles
        all_users_button = pygame.Rect(50, HEIGHT // 3 + 250, 230, 50)
        remove_user_button = pygame.Rect(300, HEIGHT // 3 + 250, 230, 50)
        borrowed_books_button = pygame.Rect(550, HEIGHT // 3 + 250, 230, 50)

        font = pygame.font.SysFont("Arial", 30)
        welcome_text = font.render("Welcome khalwsh", True, WHITE)
        welcome_text_position = welcome_text.get_rect(center=(WIDTH // 2, HEIGHT // 5))
        search_for_book_rect = pygame.Rect(420, HEIGHT // 3 + 120, 230, 50)
        search_for_user_rect = pygame.Rect(150, HEIGHT // 3 + 120, 230, 50)
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "prev"
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if add_book_button.collidepoint(event.pos):
                    title , author , pages = adding_new_book(WINDOW , HEIGHT , WIDTH)
                    if title == "prev":
                        continue
                    insert_book(title , author , pages, cursor, mydb)

                if remove_book_button.collidepoint(event.pos):
                    id = field_input_page(WINDOW , HEIGHT , WIDTH , "book id" , "enter")
                    if id == "prev":
                        continue
                    delete_book(id , cursor , mydb)
                if search_for_book_rect.collidepoint(event.pos):
                    text = field_input_page(WINDOW , HEIGHT , WIDTH , "enter book name", "enter")
                    if text == "prev":
                        continue
                    while len(text) == 0:
                        text = field_input_page(WINDOW , HEIGHT , WIDTH , "enter book name", "enter")
                        if text == "prev":
                            break
                    if text == "prev":
                        continue
                    books = substr_search(text , cursor)
                    text = ''
                    for book in books:
                        text += book.__str__()
                        text += '-------------\n'
                    if len(text) == 0:
                        text = "No book with this name exist!"
                    draw_popout(WINDOW , text)

                if available_books_button.collidepoint(event.pos):
                    books = get_available_books(cursor)
                    text = ''
                    for book in books:
                        text += book.__str__()
                        text += '-------------\n'
                    draw_popout(WINDOW , text)
                if all_users_button.collidepoint(event.pos):
                    users = get_all_users(cursor)
                    text = ''
                    for user in users:
                        text += user.__str__()
                        text += '-------------\n'
                    draw_popout(WINDOW , text)
                if remove_user_button.collidepoint(event.pos):
                    id = field_input_page(WINDOW , HEIGHT , WIDTH , "user id" , "enter")
                    if id == "prev":
                        continue
                    delete_user(id , cursor , mydb)
                if search_for_user_rect.collidepoint(event.pos):
                    text = field_input_page(WINDOW , HEIGHT , WIDTH , "enter user name", "enter")
                    if text == "prev":
                        continue
                    while len(text) == 0:
                        text = field_input_page(WINDOW , HEIGHT , WIDTH , "enter user name", "enter")
                        if text == "prev":
                            break
                    if text == "prev":
                        continue
                    draw_popout(WINDOW , load_user(text , cursor).__str__())
                if borrowed_books_button.collidepoint(event.pos):
                    books = get_borrowed_books(cursor)
                    text = ''
                    for book_and_date in books:
                        book = book_and_date[0]
                        start_date = book_and_date[1]
                        end_date = book_and_date[2]
                        text += book.__str__()
                        text += f"start date: {start_date}\n"
                        text += f"end date: {end_date}\n"
                        text += '-------------\n'
                    draw_popout(WINDOW , text)


        # Draw welcome text
        WINDOW.blit(welcome_text, welcome_text_position)

        # Draw top row buttons
        pygame.draw.rect(WINDOW, WHITE, add_book_button)
        add_book_label = font.render("add book", True, BLACK)
        add_book_position = add_book_label.get_rect(center=add_book_button.center)
        WINDOW.blit(add_book_label, add_book_position)

        pygame.draw.rect(WINDOW , WHITE, search_for_book_rect)
        search_for_book_text = font.render("book search", True, BLACK)
        search_for_book_text_rect = search_for_book_text.get_rect(center=search_for_book_rect.center)
        WINDOW.blit(search_for_book_text, search_for_book_text_rect)

        pygame.draw.rect(WINDOW, WHITE, search_for_user_rect)
        search_for_user_text = font.render("user search", True, BLACK)
        search_for_user_text_rect = search_for_user_text.get_rect(center=search_for_user_rect.center)
        WINDOW.blit(search_for_user_text, search_for_user_text_rect)

        pygame.draw.rect(WINDOW, WHITE, remove_book_button)
        remove_book_label = font.render("remove book", True, BLACK)
        remove_book_position = remove_book_label.get_rect(center=remove_book_button.center)
        WINDOW.blit(remove_book_label, remove_book_position)

        pygame.draw.rect(WINDOW, WHITE, available_books_button)
        available_books_label = font.render("available books", True, BLACK)
        available_books_position = available_books_label.get_rect(center=available_books_button.center)
        WINDOW.blit(available_books_label, available_books_position)

        # Draw bottom row buttons
        pygame.draw.rect(WINDOW, WHITE, all_users_button)
        all_users_label = font.render("all users", True, BLACK)
        all_users_position = all_users_label.get_rect(center=all_users_button.center)
        WINDOW.blit(all_users_label, all_users_position)

        pygame.draw.rect(WINDOW, WHITE, remove_user_button)
        remove_user_label = font.render("remove user", True, BLACK)
        remove_user_position = remove_user_label.get_rect(center=remove_user_button.center)
        WINDOW.blit(remove_user_label, remove_user_position)

        pygame.draw.rect(WINDOW, WHITE, borrowed_books_button)
        borrowed_books_label = font.render("borrowed books", True, BLACK)
        borrowed_books_position = borrowed_books_label.get_rect(center=borrowed_books_button.center)
        WINDOW.blit(borrowed_books_label, borrowed_books_position)

        pygame.display.update()