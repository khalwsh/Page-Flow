import sys
import pygame

from colors import WHITE, BLACK
def adding_new_book(WINDOW, HEIGHT, WIDTH):
    """
        adding_new_book(WINDOW, HEIGHT, WIDTH)

        Creates an interactive Pygame interface for adding a new book to the library system.
        Users are prompted to input the book's title, author, and page count.

        Parameters:
            WINDOW (pygame.Surface): The Pygame window surface where the interface is rendered.
            HEIGHT (int): The height of the Pygame window.
            WIDTH (int): The width of the Pygame window.

        Features:
            - Displays labeled input fields for book title, author, and number of pages.
            - Provides real-time validation for user inputs:
                - Title and author fields accept printable characters.
                - Pages field accepts only numeric input.
            - Displays error messages for incomplete fields or invalid page input.
            - Pressing "Enter" or clicking the "Enter" button submits the input.
            - Pressing "Escape" returns to the previous page.

        Return:
            tuple: A tuple containing the book title, author, and page count if valid inputs are provided.
                   If the Escape key is pressed, returns ("prev", "prev", "prev").

        Error Handling:
            - Ensures all fields are filled.
            - Validates that the number of pages is a numeric value.

        Navigation:
            - Press ESC to return to the previous page.
"""

    # Fonts
    title_font = pygame.font.SysFont("Arial", 40)
    input_font = pygame.font.SysFont("Arial", 30)
    field_font = pygame.font.SysFont("Arial", 40)

    # Title
    title_text = title_font.render("Adding Book", True, WHITE)
    book_title_text = field_font.render("title: ", True, WHITE)
    author_text = field_font.render("author: ", True, WHITE)
    pages_text = field_font.render("pages: ", True, WHITE)

    # Position the text elements
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    book_title_rect = book_title_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 2 - 100))
    author_rect = author_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 2))
    pages_rect = pages_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 2 + 100))

    # Input boxes
    input_box_title = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 120, 300, 50)
    input_box_author = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 20, 300, 50)
    input_box_pages = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 80, 300, 50)

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')

    colors = [color_inactive] * 3
    active = [False] * 3
    texts = [''] * 3

    # Enter button
    enter_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT * 3 // 4, 150, 50)

    # Error message
    error_font = pygame.font.SysFont("Arial", 25)
    error_text = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_ESCAPE:
                    return "prev", "prev" ,"prev"
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check which input box was clicked
                boxes = [input_box_title, input_box_author, input_box_pages]
                for i, box in enumerate(boxes):
                    if box.collidepoint(event.pos):
                        active = [False] * 3
                        colors = [color_inactive] * 3
                        active[i] = True
                        colors[i] = color_active

                # Check if enter button was clicked
                if enter_button.collidepoint(event.pos):
                    # Validate inputs
                    if any(not text.strip() for text in texts):
                        error_text = error_font.render("All fields must be filled", True, (255, 0, 0))
                    else:
                        try:
                            pages = int(texts[2])  # Convert pages to integer
                            return texts[0], texts[1], pages  # Return book details
                        except ValueError:
                            error_text = error_font.render("Pages must be a number", True, (255, 0, 0))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Validate inputs
                    if any(not text.strip() for text in texts):
                        error_text = error_font.render("All fields must be filled", True, (255, 0, 0))
                    else:
                        try:
                            pages = int(texts[2])  # Convert pages to integer
                            return texts[0], texts[1], pages  # Return book details
                        except ValueError:
                            error_text = error_font.render("Pages must be a number", True, (255, 0, 0))

            if event.type == pygame.KEYDOWN:
                for i in range(3):
                    if active[i]:
                        if event.key == pygame.K_BACKSPACE:
                            texts[i] = texts[i][:-1]
                        else:
                            if i == 2:  # Pages field - only accept numbers
                                if event.unicode.isnumeric():
                                    texts[i] += event.unicode
                            else:  # Title and author fields - accept printable characters
                                if event.unicode.isprintable():
                                    texts[i] += event.unicode

        # Draw background
        first_background = pygame.image.load('assets/Library_background.jpeg').convert()
        WINDOW.blit(first_background, (0, 0))

        # Draw labels
        WINDOW.blit(title_text, title_rect)
        WINDOW.blit(book_title_text, book_title_rect)
        WINDOW.blit(author_text, author_rect)
        WINDOW.blit(pages_text, pages_rect)

        # Draw input boxes
        pygame.draw.rect(WINDOW, colors[0], input_box_title, 2)
        pygame.draw.rect(WINDOW, colors[1], input_box_author, 2)
        pygame.draw.rect(WINDOW, colors[2], input_box_pages, 2)

        # Render input text
        boxes = [input_box_title, input_box_author, input_box_pages]
        for i, (box, text) in enumerate(zip(boxes, texts)):
            txt_surface = input_font.render(text, True, WHITE)
            WINDOW.blit(txt_surface, (box.x + 5, box.y + 5))

        # Draw enter button
        pygame.draw.rect(WINDOW, WHITE, enter_button)
        enter_text = input_font.render("Enter", True, BLACK)
        enter_text_rect = enter_text.get_rect(center=enter_button.center)
        WINDOW.blit(enter_text, enter_text_rect)

        # Draw error message if exists
        if error_text:
            error_rect = error_text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4 + 100))
            WINDOW.blit(error_text, error_rect)

        pygame.display.update()


def field_input_page(WINDOW , WIDTH , HEIGHT ,label_message, button_message):
    """
        field_input_page(WINDOW, WIDTH, HEIGHT, label_message, button_message)

        Creates an interactive Pygame interface for accepting a single line of user input.

        Parameters:
            WINDOW (pygame.Surface): The Pygame window surface where the interface is rendered.
            WIDTH (int): The width of the Pygame window.
            HEIGHT (int): The height of the Pygame window.
            label_message (str): The label displayed at the top of the input field (e.g., prompt text).
            button_message (str): The text displayed on the button (e.g., "Enter" or "Submit").

        Features:
            - Displays a label, an input field, and a button for user interaction.
            - Allows users to type in the input field and submit by clicking the button or pressing "Enter".
            - Handles alphanumeric input and some printable characters.
            - Pressing "Escape" exits the page and returns "prev".
            - Input box highlights when active to indicate focus.

        Return:
            str: Returns the user-entered text when submitted.
                 If the Escape key is pressed, returns "prev".

        Error Handling:
            - Prevents unintended text input by validating characters as printable.

        Navigation:
            - Press ESC to return to the previous page.
"""
    # Fonts
    title_font = pygame.font.SysFont("Arial", 40)
    input_font = pygame.font.SysFont("Arial", 30)

    # Title
    title_text = title_font.render(label_message, True, WHITE)
    title_rect = title_text.get_rect(center=(WIDTH  // 2 + 120, HEIGHT // 6))
    WINDOW.blit(title_text, title_rect)

    # Password input box
    input_box = pygame.Rect(WIDTH // 2 - 20, HEIGHT // 3, 300, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    # Login button
    login_button = pygame.Rect(WIDTH // 2 + 50, HEIGHT // 2 + 50, 150, 50)

    # Error message
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
                if input_box.collidepoint(event.pos):
                    active = True
                    color = color_active
                else:
                    active = False
                    color = color_inactive

                if login_button.collidepoint(event.pos):
                    return text

            # Handle text input
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
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

        txt_surface = input_font.render(text, True, WHITE)
        WINDOW.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        # Draw login button
        pygame.draw.rect(WINDOW, WHITE, login_button)
        login_text = input_font.render(button_message, True, BLACK)
        login_text_rect = login_text.get_rect(center=login_button.center)
        WINDOW.blit(login_text, login_text_rect)

        # Draw error message if exists
        if error_text:
            error_rect = error_text.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4 + 100))
            WINDOW.blit(error_text, error_rect)

        pygame.display.update()


def draw_popout(screen, message):
    """
        draw_popout(screen, message)

        Displays a pop-up window with a scrollable message content inside a Pygame application.

        Parameters:
            screen (pygame.Surface): The Pygame window surface where the pop-out is drawn.
            message (str): The content to display inside the pop-out, with lines separated by '\n'.

        Features:
            - Displays a scrollable message area within a bordered pop-out box.
            - Includes a functional vertical scrollbar for navigation.
            - Allows scrolling using both the mouse wheel and a draggable scrollbar thumb.
            - Pressing the "Escape" key exits the pop-out.

        Detailed Breakdown:
            - **Pop-out Rectangle**: Defines the visible area for the pop-out and includes padding for content.
            - **Scrollbar**: Dynamically adjusts size and position based on the total content height and visible area.
            - **Drag and Scroll**: Enables smooth scrolling using both the mouse wheel and mouse dragging.

        Error Handling:
            - Ensures scroll position remains within valid bounds.
            - Prevents rendering text outside the visible content area.

        Navigation:
            - Press ESC to close the pop-out.
"""

    first_background = pygame.image.load('assets/Library_background.jpeg').convert()
    screen.blit(first_background, (0, 0))
    font = pygame.font.Font(None, 36)

    # Define constants
    SCROLLBAR_WIDTH = 20
    PADDING = 20
    LINE_SPACING = 10

    # Define the pop-out rectangle
    popout_rect = pygame.Rect(150, 150, 500, 300)
    content_rect = pygame.Rect(
        popout_rect.left + PADDING,
        popout_rect.top + PADDING,
        popout_rect.width - PADDING * 2 - SCROLLBAR_WIDTH,
        popout_rect.height - PADDING * 2
    )

    # Split and render all lines first to calculate total height
    lines = message.split('\n')
    line_height = font.size("Tg")[1]
    rendered_lines = []
    for line in lines:
        text = font.render(line, True, BLACK)
        rendered_lines.append(text)

    total_content_height = len(lines) * (line_height + LINE_SPACING)
    scroll_position = 0
    max_scroll = max(0, total_content_height - content_rect.height)

    # Scrollbar properties
    scrollbar_rect = pygame.Rect(
        popout_rect.right - SCROLLBAR_WIDTH - PADDING,
        popout_rect.top + PADDING,
        SCROLLBAR_WIDTH,
        popout_rect.height - PADDING * 2
    )

    # Calculate scroll thumb size and position
    visible_ratio = min(1, content_rect.height / total_content_height)
    thumb_height = max(20, scrollbar_rect.height * visible_ratio)

    dragging = False
    drag_start_y = 0
    drag_start_scroll = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            # Mouse wheel scrolling
            if event.type == pygame.MOUSEWHEEL:
                scroll_position = max(0, min(max_scroll,
                                             scroll_position - event.y * 20))

            # Handle scrollbar dragging
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and scrollbar_rect.collidepoint(event.pos):
                    dragging = True
                    drag_start_y = event.pos[1]
                    drag_start_scroll = scroll_position

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False

            if event.type == pygame.MOUSEMOTION and dragging:
                drag_delta = event.pos[1] - drag_start_y
                scroll_ratio = drag_delta / (scrollbar_rect.height - thumb_height)
                scroll_position = max(0, min(max_scroll,
                                             drag_start_scroll + scroll_ratio * max_scroll))

        # Draw pop-out background
        pygame.draw.rect(screen, WHITE, popout_rect, border_radius=10)
        pygame.draw.rect(screen, BLACK, popout_rect, 3, border_radius=10)

        # Create a surface for the content area and enable clipping
        content_surface = screen.subsurface(content_rect)

        # Draw text
        y_offset = -scroll_position
        for text in rendered_lines:
            if -line_height <= y_offset <= content_rect.height:
                text_rect = text.get_rect(
                    x=0,
                    y=y_offset
                )
                content_surface.blit(text, text_rect)
            y_offset += line_height + LINE_SPACING

        # Draw scrollbar background
        pygame.draw.rect(screen, (200, 200, 200), scrollbar_rect)

        # Draw scrollbar thumb
        if max_scroll > 0:
            thumb_pos = scrollbar_rect.top + (scroll_position / max_scroll) * (scrollbar_rect.height - thumb_height)
            thumb_rect = pygame.Rect(
                scrollbar_rect.x,
                thumb_pos,
                SCROLLBAR_WIDTH,
                thumb_height
            )
            pygame.draw.rect(screen, (150, 150, 150), thumb_rect)

        pygame.display.update()