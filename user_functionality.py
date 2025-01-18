import sys
import pygame

from colors import WHITE, BLACK
from db_manager import load_user, insert_phone, delete_phone, return_book, warning_message, borrow_book, \
    get_available_books, substr_search, get_fine, apply_fine
from utilities import draw_popout, field_input_page
from validate_fields import check_phone

import pygame
from colors import WHITE, BLACK

def fine(WINDOW, HEIGHT, WIDTH, amount):
    """
    Display a fine payment dialog with a message and yes/no buttons.
    """
    while True:
        background = pygame.image.load('assets/Library_background.jpeg').convert()
        WINDOW.blit(background, (0, 0))

        font = pygame.font.SysFont("Arial", 30)

        message = f"You should pay ${amount}"
        message_text = font.render(message, True, WHITE)
        message_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))

        yes_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2, 150, 50)
        no_rect = pygame.Rect(3 * WIDTH // 4 - 150, HEIGHT // 2, 150, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "prev"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_rect.collidepoint(event.pos):
                    return "yes"
                if no_rect.collidepoint(event.pos):
                    return "no"

        WINDOW.blit(message_text, message_rect)

        pygame.draw.rect(WINDOW, WHITE, yes_rect)
        pygame.draw.rect(WINDOW, WHITE, no_rect)

        yes_text = font.render("Yes", True, BLACK)
        no_text = font.render("No", True, BLACK)

        yes_text_rect = yes_text.get_rect(center=yes_rect.center)
        no_text_rect = no_text.get_rect(center=no_rect.center)

        WINDOW.blit(yes_text, yes_text_rect)
        WINDOW.blit(no_text, no_text_rect)

        pygame.display.update()

def user_functionality(WINDOW, HEIGHT, WIDTH, current_user_name , cursor , mydb):
    """
        This function handles the user interface for a library management system in Pygame.
        It allows the user to interact with various functionalities such as viewing their profile,
        borrowing and returning books, adding/removing phone numbers, and searching for books.
    """
    user = load_user(current_user_name, cursor)
    while True:
        first_background = pygame.image.load('assets/Library_background.jpeg').convert()
        WINDOW.blit(first_background, (0, 0))

        profile_rect = pygame.Rect(50, HEIGHT // 3, 230, 50)
        books_rect = pygame.Rect(300, HEIGHT // 3, 230, 50)
        borrow_book_rect = pygame.Rect(300 , HEIGHT // 3 + 120, 230 , 50)
        borrowed_rect = pygame.Rect(550, HEIGHT // 3, 230, 50)

        warning_rect = pygame.Rect(50, HEIGHT // 3 + 120, 230, 50)
        add_phone_rect = pygame.Rect(50, HEIGHT // 3 + 250, 230, 50)
        delete_phone_rect = pygame.Rect(300, HEIGHT // 3 + 250, 230, 50)
        return_book_rect = pygame.Rect(550, HEIGHT // 3 + 250, 230, 50)
        search_for_book_rect = pygame.Rect(550, HEIGHT // 3 + 120, 230, 50)

        font = pygame.font.SysFont("Arial", 30)
        welcome_text = font.render(f"Welcome {user.username}", True, WHITE)
        welcome_rect = welcome_text.get_rect(center=(WIDTH // 2, HEIGHT // 5))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_ESCAPE:
                    return "prev"
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if profile_rect.collidepoint(event.pos):
                    draw_popout(WINDOW , user.__str__())
                if borrowed_rect.collidepoint(event.pos):
                    books = ''
                    for book in user.borrowed_books:
                        books += book.__str__()
                        books += '-------------------------\n'
                    draw_popout(WINDOW , books)
                if add_phone_rect.collidepoint(event.pos):
                    text = field_input_page(WINDOW , HEIGHT , WIDTH , "enter phone number", "enter")
                    if text == "prev":
                        continue
                    while not check_phone(text)[0]:
                        text = field_input_page(WINDOW , HEIGHT , WIDTH , "enter phone number", "enter")
                        if text == "prev":
                            break
                    if text == "prev":
                        continue
                    insert_phone(user.id , text, cursor , mydb)
                    user = load_user(current_user_name, cursor)

                if delete_phone_rect.collidepoint(event.pos):
                    text = field_input_page(WINDOW , HEIGHT , WIDTH , "enter phone number", "enter")
                    if text == "prev":
                        continue
                    while not check_phone(text)[0]:
                        text = field_input_page(WINDOW , HEIGHT , WIDTH , "enter phone number", "enter")
                        if text == "prev":
                            break
                    if text == "prev":
                        continue

                    delete_phone(user.id , text, cursor , mydb)
                    user = load_user(current_user_name, cursor)


                if return_book_rect.collidepoint(event.pos):

                    text = field_input_page(WINDOW , HEIGHT , WIDTH , "enter book id", "enter")
                    if text == "prev":
                        continue
                    while len(text) == 0:
                        text = field_input_page(WINDOW , HEIGHT , WIDTH , "enter book id", "enter")
                        if text == "prev":
                            break
                    if text == "prev":
                        continue

                    x = get_fine(user.id , int(text) ,cursor)
                    fine_respond = ''
                    if x > 0:
                        fine_respond = fine(WINDOW , HEIGHT , WIDTH , x)
                    if fine_respond == "yes":
                        apply_fine(user.id , int(text) , cursor , mydb)
                        return_book(user.id , text, cursor , mydb)
                        user = load_user(current_user_name, cursor)

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
                if warning_rect.collidepoint(event.pos):
                    books = warning_message(current_user_name, cursor)
                    text = "-- borrowing period has finished --"
                    for book_and_date in books:
                        book = book_and_date[0]
                        start_date = book_and_date[1]
                        end_date = book_and_date[2]
                        text += book.__str__()
                        text += f"start date: {start_date}\n"
                        text += f"end date: {end_date}\n"
                        text += '-------------\n'
                    draw_popout(WINDOW, text)

                if books_rect.collidepoint(event.pos):
                    books = get_available_books(cursor)
                    text = ''
                    for book in books:
                        text += book.__str__()
                        text += '-------------\n'
                    draw_popout(WINDOW , text)
                if borrow_book_rect.collidepoint(event.pos):
                    books = warning_message(current_user_name, cursor)
                    if len(books):
                        draw_popout(WINDOW, "you can't borrow books right now \nfirst you must pay your fines")
                    else:
                        text = field_input_page(WINDOW , HEIGHT , WIDTH , "enter book id", "enter")
                        if text == "prev":
                            continue
                        while len(text) == 0:
                            text = field_input_page(WINDOW , HEIGHT , WIDTH , "enter book id", "enter")
                            if text == "prev":
                                break
                        if text == "prev":
                            continue
                        borrow_book(user.id , text, cursor , mydb)
                        user = load_user(current_user_name, cursor)



        # draw

        WINDOW.blit(welcome_text, welcome_rect)

        pygame.draw.rect(WINDOW, WHITE, profile_rect)
        profile_text = font.render("user profile", True, BLACK)
        profile_text_rect = profile_text.get_rect(center=profile_rect.center)
        WINDOW.blit(profile_text, profile_text_rect)

        pygame.draw.rect(WINDOW , WHITE , borrow_book_rect)
        borrow_book_text = font.render("borrow books", True, BLACK)
        borrow_text_rect = borrow_book_text.get_rect(center=borrow_book_rect.center)
        WINDOW.blit(borrow_book_text, borrow_text_rect)

        pygame.draw.rect(WINDOW, WHITE, warning_rect)
        warning_text = font.render("warning", True, BLACK)
        warning_text_rect = warning_text.get_rect(center=warning_rect.center)
        WINDOW.blit(warning_text, warning_text_rect)

        pygame.draw.rect(WINDOW , WHITE, search_for_book_rect)
        search_for_book_text = font.render("book search", True, BLACK)
        search_for_book_text_rect = search_for_book_text.get_rect(center=search_for_book_rect.center)
        WINDOW.blit(search_for_book_text, search_for_book_text_rect)

        pygame.draw.rect(WINDOW, WHITE, books_rect)
        books_text = font.render("available books", True, BLACK)
        books_text_rect = books_text.get_rect(center=books_rect.center)
        WINDOW.blit(books_text, books_text_rect)

        pygame.draw.rect(WINDOW, WHITE, borrowed_rect)
        borrowed_text = font.render("borrowed books", True, BLACK)
        borrowed_text_rect = borrowed_text.get_rect(center=borrowed_rect.center)
        WINDOW.blit(borrowed_text, borrowed_text_rect)

        pygame.draw.rect(WINDOW, WHITE, add_phone_rect)
        add_phone_text = font.render("add phone", True, BLACK)
        add_phone_text_rect = add_phone_text.get_rect(center=add_phone_rect.center)
        WINDOW.blit(add_phone_text, add_phone_text_rect)

        pygame.draw.rect(WINDOW , WHITE, delete_phone_rect)
        delete_phone_text = font.render("delete phone", True, BLACK)
        delete_phone_text_rect = delete_phone_text.get_rect(center=delete_phone_rect.center)
        WINDOW.blit(delete_phone_text, delete_phone_text_rect)

        pygame.draw.rect(WINDOW, WHITE, return_book_rect)
        return_book_text = font.render("return book", True, BLACK)
        return_book_text_rect = return_book_text.get_rect(center = return_book_rect.center)
        WINDOW.blit(return_book_text, return_book_text_rect)

        pygame.display.update()