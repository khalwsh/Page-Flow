import sys
import pygame

from colors import BLACK, WHITE
def admin_user_page(WINDOW, HEIGHT, WIDTH):
    """
        Displays the initial page of the application where the user selects between the Admin and User functionalities.
        Provides interactive buttons for navigation to either the Admin or User page.
    """

    while True:
        font = pygame.font.SysFont("Arial", 30)
        Admin_text = font.render("Admin", True, BLACK)
        User_text = font.render("User", True, BLACK)

        # Button positions and dimensions
        Admin_button = pygame.Rect(WIDTH // 4 - 75, HEIGHT // 2 - 30, 200, 60)
        User_button = pygame.Rect(3 * WIDTH // 4 - 75, HEIGHT // 2 - 30, 170, 60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if Admin_button.collidepoint(pos):
                    return 2
                elif User_button.collidepoint(pos):
                    return 3

        # Draw buttons
        pygame.draw.rect(WINDOW, WHITE, Admin_button)
        pygame.draw.rect(WINDOW, WHITE, User_button)

        WINDOW.blit(Admin_text, (Admin_button.x + 50, Admin_button.y + 15))
        WINDOW.blit(User_text, (User_button.x + 50, User_button.y + 15))

        pygame.display.update()