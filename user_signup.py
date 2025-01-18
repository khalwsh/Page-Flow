import sys
import pygame

from colors import WHITE, BLACK
from db_manager import insert_user, check_create_user


def user_signup(WINDOW, HEIGHT, WIDTH, cursor, mydb):
    """

        Displays a sign-up screen where the user can input their details to create a new account.
        The function collects the user's information, validates it, and inserts the data into the database.

        what it should look like:
                        Sign-up
        username:
        password:
        fname:
        lname:
        email:
        Address:
        phone:
                        sign-up!
    """
    input_font = pygame.font.SysFont("Arial", 30)

    title_font = pygame.font.SysFont("Arial", 40)
    title_text = title_font.render("Sign-up", True, WHITE)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 8))

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')

    user_name_font = pygame.font.SysFont("Arial", 25)
    user_name_text = user_name_font.render("User-name: ", True, WHITE)
    user_name_rect = user_name_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 50))

    user_name_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 30, 300, 40)
    user_name_color = color_inactive
    user_name_active = False
    user_name_input_text = ''

    password_font = pygame.font.SysFont("Arial", 25)
    password_text = password_font.render("Password: ", True, WHITE)
    password_rect = password_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 100))

    password_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 80, 300, 40)
    password_color = color_inactive
    password_active = False
    password_input_text = ''

    fname_font = pygame.font.SysFont("Arial", 25)
    fname_text = fname_font.render("First Name: ", True, WHITE)
    fname_rect = fname_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 150))

    fname_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 130, 300, 40)
    fname_color = color_inactive
    fname_active = False
    fname_input_text = ''

    lname_font = pygame.font.SysFont("Arial", 25)
    lname_text = lname_font.render("Last Name: ", True, WHITE)
    lname_rect = lname_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 200))

    lname_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 180, 300, 40)
    lname_color = color_inactive
    lname_active = False
    lname_input_text = ''

    email_font = pygame.font.SysFont("Arial", 25)
    email_text = email_font.render("Email: ", True, WHITE)
    email_rect = email_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 250))

    email_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 230, 300, 40)
    email_color = color_inactive
    email_active = False
    email_input_text = ''

    Address_font = pygame.font.SysFont("Arial", 25)
    Address_text = Address_font.render("Address: ", True, WHITE)
    Address_rect = Address_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 300))

    Address_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 280, 300, 40)
    Address_color = color_inactive
    Address_active = False
    Address_input_text = ''

    Phone_font = pygame.font.SysFont("Arial", 25)
    Phone_text = Phone_font.render("Phone: ", True, WHITE)
    Phone_rect = Phone_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 350))

    Phone_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 330, 300, 40)
    Phone_color = color_inactive
    Phone_active = False
    Phone_input_text = ''

    signup_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT * 4 // 5, 150, 50)

    error_font = pygame.font.SysFont("Arial", 25)
    error_text = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_ESCAPE:
                    return "prev"
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                input_boxes = [
                    (user_name_input_box, "user_name"),
                    (password_input_box, "password"),
                    (fname_input_box, "fname"),
                    (lname_input_box, "lname"),
                    (email_input_box, "email"),
                    (Address_input_box, "address"),
                    (Phone_input_box, "phone")
                ]

                user_name_active = password_active = fname_active = lname_active = email_active = Address_active = Phone_active = False
                user_name_color = password_color = fname_color = lname_color = email_color = Address_color = Phone_color = color_inactive

                # Set clicked box to active
                for box, name in input_boxes:
                    if box.collidepoint(event.pos):
                        if name == "user_name":
                            user_name_active = True
                            user_name_color = color_active
                        elif name == "password":
                            password_active = True
                            password_color = color_active
                        elif name == "fname":
                            fname_active = True
                            fname_color = color_active
                        elif name == "lname":
                            lname_active = True
                            lname_color = color_active
                        elif name == "email":
                            email_active = True
                            email_color = color_active
                        elif name == "address":
                            Address_active = True
                            Address_color = color_active
                        elif name == "phone":
                            Phone_active = True
                            Phone_color = color_active

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if user_name_active and len(user_name_input_text) > 0:
                        user_name_input_text = user_name_input_text[:-1]
                    elif password_active and len(password_input_text) > 0:
                        password_input_text = password_input_text[:-1]
                    elif fname_active and len(fname_input_text) > 0:
                        fname_input_text = fname_input_text[:-1]
                    elif lname_active and len(lname_input_text) > 0:
                        lname_input_text = lname_input_text[:-1]
                    elif email_active and len(email_input_text) > 0:
                        email_input_text = email_input_text[:-1]
                    elif Address_active and len(Address_input_text) > 0:
                        Address_input_text = Address_input_text[:-1]
                    elif Phone_active and len(Phone_input_text) > 0:
                        Phone_input_text = Phone_input_text[:-1]
                elif event.unicode.isprintable():
                    if user_name_active:
                        user_name_input_text += event.unicode
                    elif password_active:
                        password_input_text += event.unicode
                    elif fname_active:
                        fname_input_text += event.unicode
                    elif lname_active:
                        lname_input_text += event.unicode
                    elif email_active:
                        email_input_text += event.unicode
                    elif Address_active:
                        Address_input_text += event.unicode
                    elif Phone_active:
                        Phone_input_text += event.unicode
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    error_text = check_create_user(user_name_input_text, password_input_text, fname_input_text,
                                                   lname_input_text, email_input_text, Address_input_text,
                                                   Phone_input_text, cursor)
                    if error_text is None:
                        insert_user(user_name_input_text, password_input_text, fname_input_text, lname_input_text,
                                    email_input_text, Address_input_text, Phone_input_text, cursor, mydb)
                        return user_name_input_text
            if event.type == pygame.MOUSEBUTTONDOWN:
                if signup_button.collidepoint(event.pos):
                    error_text = check_create_user(user_name_input_text, password_input_text, fname_input_text,
                                                   lname_input_text, email_input_text, Address_input_text,
                                                   Phone_input_text, cursor)
                    if error_text is None:
                        insert_user(user_name_input_text, password_input_text, fname_input_text, lname_input_text,
                                    email_input_text, Address_input_text, Phone_input_text, cursor, mydb)
                        return user_name_input_text

        # Clear screen
        first_background = pygame.image.load('assets/Library_background.jpeg').convert()
        WINDOW.blit(first_background, (0, 0))

        # Draw labels
        WINDOW.blit(title_text, title_rect)
        WINDOW.blit(user_name_text, user_name_rect)
        WINDOW.blit(password_text, password_rect)
        WINDOW.blit(fname_text, fname_rect)
        WINDOW.blit(lname_text, lname_rect)
        WINDOW.blit(email_text, email_rect)
        WINDOW.blit(Address_text, Address_rect)
        WINDOW.blit(Phone_text, Phone_rect)

        pygame.draw.rect(WINDOW, user_name_color, user_name_input_box, 2)
        pygame.draw.rect(WINDOW, password_color, password_input_box, 2)
        pygame.draw.rect(WINDOW, fname_color, fname_input_box, 2)
        pygame.draw.rect(WINDOW, lname_color, lname_input_box, 2)
        pygame.draw.rect(WINDOW, email_color, email_input_box, 2)
        pygame.draw.rect(WINDOW, Address_color, Address_input_box, 2)
        pygame.draw.rect(WINDOW, Phone_color, Phone_input_box, 2)

        user_name_txt_surface = input_font.render(user_name_input_text, True, WHITE)
        password_txt_surface = input_font.render(len(password_input_text) * '*', True, WHITE)
        fname_txt_surface = input_font.render(fname_input_text, True, WHITE)
        lname_txt_surface = input_font.render(lname_input_text, True, WHITE)
        email_txt_surface = input_font.render(email_input_text, True, WHITE)
        Address_txt_surface = input_font.render(Address_input_text, True, WHITE)
        Phone_txt_surface = input_font.render(Phone_input_text, True, WHITE)

        WINDOW.blit(user_name_txt_surface, (user_name_input_box.x + 5, user_name_input_box.y + 5))
        WINDOW.blit(password_txt_surface, (password_input_box.x + 5, password_input_box.y + 5))
        WINDOW.blit(fname_txt_surface, (fname_input_box.x + 5, fname_input_box.y + 5))
        WINDOW.blit(lname_txt_surface, (lname_input_box.x + 5, lname_input_box.y + 5))
        WINDOW.blit(email_txt_surface, (email_input_box.x + 5, email_input_box.y + 5))
        WINDOW.blit(Address_txt_surface, (Address_input_box.x + 5, Address_input_box.y + 5))
        WINDOW.blit(Phone_txt_surface, (Phone_input_box.x + 5, Phone_input_box.y + 5))

        pygame.draw.rect(WINDOW, WHITE, signup_button)
        login_text = input_font.render("sign-up", True, BLACK)
        login_text_rect = login_text.get_rect(center=signup_button.center)
        WINDOW.blit(login_text, login_text_rect)

        if error_text:
            x = error_font.render(error_text, True, (255, 0, 0))
            error_rect = x.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4 + 100))
            WINDOW.blit(x, error_rect)

        pygame.display.update()