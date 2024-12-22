import sys
import pygame

from colors import BLACK, WHITE
def signup_login_user(WINDOW, HEIGHT, WIDTH):
    """
        signup_login_user(WINDOW, HEIGHT, WIDTH)

        Displays the user interface where users can choose between signing up for a new account or logging into an existing account.
        Provides interactive buttons for navigation to either the login or signup page.

        Parameters:
            WINDOW (pygame.Surface): The Pygame window surface where the interface is rendered.
            HEIGHT (int): The height of the Pygame window.
            WIDTH (int): The width of the Pygame window.

        Features:
            - Two buttons labeled "log-in" and "signup" for navigation.
            - Clicking the "log-in" button navigates to the login page (returns 2).
            - Clicking the "signup" button navigates to the signup page (returns 1).
            - Allows navigation back to the previous screen using the ESC key.

        Return:
            int: Returns `2` if the "log-in" button is clicked.
                 Returns `1` if the "signup" button is clicked.
            str: Returns `"prev"` if the ESC key is pressed.
"""

    while True:
        font = pygame.font.SysFont("Arial", 30)
        log_in_text = font.render("log-in", True, BLACK)
        sign_up_text = font.render("signup", True, BLACK)

        # Button positions and dimensions
        log_in = pygame.Rect(WIDTH // 4 - 75, HEIGHT // 2 - 30, 200, 60)
        sign_up = pygame.Rect(3 * WIDTH // 4 - 75, HEIGHT // 2 - 30, 170, 60)

        # Draw buttons
        pygame.draw.rect(WINDOW, WHITE, log_in)
        pygame.draw.rect(WINDOW, WHITE, sign_up)

        # Render text onto buttons
        WINDOW.blit(log_in_text, (log_in.x + 50, log_in.y + 15))
        WINDOW.blit(sign_up_text, (sign_up.x + 50, sign_up.y + 15))

        pygame.display.update()

        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_ESCAPE:
                    return "prev"
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if log_in.collidepoint(pos):
                    return 2
                elif sign_up.collidepoint(pos):
                    return 1