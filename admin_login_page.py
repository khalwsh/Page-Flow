import sys
import pygame

from colors import BLACK, WHITE
def admin_login(WINDOW, HEIGHT, WIDTH):
    """
        admin_login(WINDOW, HEIGHT, WIDTH)

        Handles the login interface for the admin in a Pygame application.
        Displays a login screen with a password input box, a login button, and an error message for incorrect login attempts.

        Parameters:
            WINDOW (pygame.Surface): The Pygame window surface where the login UI is rendered.
            HEIGHT (int): The height of the Pygame window.
            WIDTH (int): The width of the Pygame window.

        Features:
            - Displays a login title and input box for the admin password.
            - Supports user interaction with mouse clicks and keyboard inputs.
            - Masks password input with asterisks (*) for security.
            - Verifies the entered password and provides feedback on incorrect attempts.
            - Allows navigation back to the previous screen using the ESC key.

        Return:
            bool: Returns `True` for a successful login when the correct password is entered.
            str: Returns `"prev"` if the user opts to return to the previous screen by pressing ESC.
"""

    # Fonts
    title_font = pygame.font.SysFont("Arial", 40)
    input_font = pygame.font.SysFont("Arial", 30)

    # Title
    title_text = title_font.render("khalwsh Login", True, WHITE)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    WINDOW.blit(title_text, title_rect)

    # Password input box
    input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2, 300, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    # Login button
    login_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT * 3 // 4, 150, 50)

    # Error message
    error_font = pygame.font.SysFont("Arial", 25)
    error_text = None

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the input box was clicked
                if input_box.collidepoint(event.pos):
                    active = True
                    color = color_active
                else:
                    active = False
                    color = color_inactive

                # Check if login button was clicked
                if login_button.collidepoint(event.pos):
                    if text == 'adkhyono234':
                        return True  # Successful login
                    else:
                        error_text = error_font.render("Incorrect Password", True, (255, 0, 0))
                        text = ''  # Clear input

            # Handle text input
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_ESCAPE:
                    return "prev"
                if active:
                    if event.key == pygame.K_RETURN:
                        # Check password on enter
                        if text == 'adkhyono234':
                            return True
                        else:
                            error_text = error_font.render("Incorrect Password", True, (255, 0, 0))
                            text = ''  # Clear input
                    elif event.key == pygame.K_BACKSPACE:
                        if len(text) != 0:
                            text = text[0: len(text) - 1]
                    else:
                        # Limit input to alphanumeric and some symbols
                        if event.unicode.isprintable():
                            text += event.unicode

        first_background = pygame.image.load('assets/Library_background.jpeg').convert()
        WINDOW.blit(first_background, (0, 0))

        # Draw title
        WINDOW.blit(title_text, title_rect)

        # Draw input box
        pygame.draw.rect(WINDOW, color, input_box, 2)

        # Render password (masked)
        txt_surface = input_font.render('*' * len(text), True, WHITE)
        WINDOW.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        # Draw login button
        pygame.draw.rect(WINDOW, WHITE, login_button)
        login_text = input_font.render("Login", True, BLACK)
        login_text_rect = login_text.get_rect(center=login_button.center)
        WINDOW.blit(login_text, login_text_rect)

        # Draw error message if exists
        if error_text:
            error_rect = error_text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4 + 100))
            WINDOW.blit(error_text, error_rect)

        pygame.display.update()