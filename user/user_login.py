import sys
import pygame

from utilities.colors import WHITE, BLACK
from database.db_manager import check_user_exist


def user_login(WINDOW, HEIGHT, WIDTH, cursor):
    """
        Displays a login screen where the user can input their username and password to log into the system.
    """
    title_font = pygame.font.SysFont("Arial", 40)
    input_font = pygame.font.SysFont("Arial", 30)
    user_font = pygame.font.SysFont("Arial", 40)
    pass_font = pygame.font.SysFont("Arial", 40)

    title_text = title_font.render("user Login", True, WHITE)
    username_text = user_font.render("user name: ", True, WHITE)
    password_text = pass_font.render("password: ", True, WHITE)

    # Correct Rect positions for username and password
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    username_rect = username_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 2 - 60))
    password_rect = password_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 2 + 20))

    WINDOW.blit(title_text, title_rect)
    WINDOW.blit(username_text, username_rect)
    WINDOW.blit(password_text, password_rect)

    # Password input box
    input_box_password = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2, 300, 50)
    input_box_username = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 80, 300, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color1 = color_inactive
    color2 = color_inactive
    active1 = False
    active2 = False
    text1 = ''
    text2 = ''

    login_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT * 3 // 4, 150, 50)

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
                # Check if the input box was clicked
                if input_box_password.collidepoint(event.pos):
                    active1 = True
                    color1 = color_active
                else:
                    active1 = False
                    color1 = color_inactive
                if input_box_username.collidepoint(event.pos):
                    active2 = True
                    color2 = color_active
                else:
                    active2 = False
                    color2 = color_inactive
                # Check if login button was clicked
                if login_button.collidepoint(event.pos):
                    # check user exist in database or not
                    if check_user_exist(text2, text1, cursor):
                        return text2
                    else:
                        error_text = error_font.render("Incorrect Password", True, (255, 0, 0))
                        text2 = ''
                        text1 = ''  # Clear input

            # Handle text input
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_RETURN:
                        # check user exist in database or not
                        if check_user_exist(text2, text1, cursor):
                            return text2
                        else:
                            error_text = error_font.render("Incorrect Password", True, (255, 0, 0))
                            text2 = ''
                            text1 = ''
                    elif event.key == pygame.K_BACKSPACE and len(text1) != 0:
                        text1 = text1[0: len(text1) - 1]
                    else:
                        if event.unicode.isprintable():
                            text1 += event.unicode
                if active2:
                    if event.key == pygame.K_BACKSPACE and len(text2) != 0:
                        text2 = text2[0: len(text2) - 1]
                    else:
                        if event.unicode.isprintable():
                            text2 += event.unicode

        first_background = pygame.image.load('assets/Library_background.jpeg').convert()
        WINDOW.blit(first_background, (0, 0))

        WINDOW.blit(title_text, title_rect)
        WINDOW.blit(username_text, username_rect)
        WINDOW.blit(password_text, password_rect)
        pygame.draw.rect(WINDOW, color1, input_box_password, 2)
        pygame.draw.rect(WINDOW, color2, input_box_username, 2)

        txt_surface1 = input_font.render(text2, True, WHITE)
        WINDOW.blit(txt_surface1, (input_box_username.x + 5, input_box_username.y + 5))

        txt_surface2 = input_font.render('*' * len(text1), True, WHITE)
        WINDOW.blit(txt_surface2, (input_box_password.x + 5, input_box_password.y + 5))

        pygame.draw.rect(WINDOW, WHITE, login_button)
        login_text = input_font.render("Login", True, BLACK)
        login_text_rect = login_text.get_rect(center=login_button.center)
        WINDOW.blit(login_text, login_text_rect)

        if error_text:
            error_rect = error_text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4 + 100))
            WINDOW.blit(error_text, error_rect)

        pygame.display.update()