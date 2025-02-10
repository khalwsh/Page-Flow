import sys
import pygame

from utilities.colors import BLACK, WHITE
def signup_login_user(WINDOW, HEIGHT, WIDTH):
    """
    display the page which make the user of the system to choose to login as admin or as user
    """

    while True:
        font = pygame.font.SysFont("Arial", 30)
        log_in_text = font.render("log-in", True, BLACK)
        sign_up_text = font.render("signup", True, BLACK)

        log_in = pygame.Rect(WIDTH // 4 - 75, HEIGHT // 2 - 30, 200, 60)
        sign_up = pygame.Rect(3 * WIDTH // 4 - 75, HEIGHT // 2 - 30, 170, 60)

        pygame.draw.rect(WINDOW, WHITE, log_in)
        pygame.draw.rect(WINDOW, WHITE, sign_up)

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