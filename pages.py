from colors import *
from db_manager import *
import pygame
import sys


def adding_new_book(WINDOW, HEIGHT, WIDTH):
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


def loadFirstPage(WINDOW, HEIGHT, WIDTH):
    '''
    this function loads the first page which is the admin , user page
    just make 2 buttons to make the user choose where to go to admin ? or to user
    if he choose user then he go to user page [login , create] other wise he goes to admin page [login]
    the admin is pre defined user which has name khalwsh and password: adkhyono234
    '''
    # design the buttons
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

        # Render text onto buttons
        WINDOW.blit(Admin_text, (Admin_button.x + 50, Admin_button.y + 15))
        WINDOW.blit(User_text, (User_button.x + 50, User_button.y + 15))

        pygame.display.update()


def loadSecondPage(WINDOW, HEIGHT, WIDTH):
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


def loadThirdPage(WINDOW, HEIGHT, WIDTH):
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


# admin functions
def loadFourthPage(WINDOW, HEIGHT, WIDTH, cursor, mydb):
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


# user login
def loadFifthPage(WINDOW, HEIGHT, WIDTH, cursor):
    # Fonts
    title_font = pygame.font.SysFont("Arial", 40)
    input_font = pygame.font.SysFont("Arial", 30)
    user_font = pygame.font.SysFont("Arial", 40)
    pass_font = pygame.font.SysFont("Arial", 40)

    # Title
    title_text = title_font.render("user Login", True, WHITE)
    username_text = user_font.render("user name: ", True, WHITE)
    password_text = pass_font.render("password: ", True, WHITE)

    # Correct Rect positions for username and password
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    username_rect = username_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 2 - 60))
    password_rect = password_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 2 + 20))

    # Blit to the window
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

    # Login button
    login_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT * 3 // 4, 150, 50)

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
                        return text2  # Successful login
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
                            text1 = ''  # Clear input
                    elif event.key == pygame.K_BACKSPACE and len(text1) != 0:
                        text1 = text1[0: len(text1) - 1]
                    else:
                        # Limit input to alphanumeric and some symbols
                        if event.unicode.isprintable():
                            text1 += event.unicode
                if active2:
                    if event.key == pygame.K_BACKSPACE and len(text2) != 0:
                        text2 = text2[0: len(text2) - 1]
                    else:
                        # Limit input to alphanumeric and some symbols
                        if event.unicode.isprintable():
                            text2 += event.unicode

        first_background = pygame.image.load('assets/Library_background.jpeg').convert()
        WINDOW.blit(first_background, (0, 0))

        # Draw title
        WINDOW.blit(title_text, title_rect)
        WINDOW.blit(username_text, username_rect)
        WINDOW.blit(password_text, password_rect)
        # Draw input box
        pygame.draw.rect(WINDOW, color1, input_box_password, 2)
        pygame.draw.rect(WINDOW, color2, input_box_username, 2)

        # Render user name
        txt_surface1 = input_font.render(text2, True, WHITE)
        WINDOW.blit(txt_surface1, (input_box_username.x + 5, input_box_username.y + 5))

        # Render password (masked)
        txt_surface2 = input_font.render('*' * len(text1), True, WHITE)
        WINDOW.blit(txt_surface2, (input_box_password.x + 5, input_box_password.y + 5))

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


# sign user up
def loadSixthPage(WINDOW, HEIGHT, WIDTH, cursor, mydb):
    '''
                         Sign-up
         username:
         password:
         fname:
         lname:
         email:
         Address:
         phone:
                         sign-up!
    '''
    input_font = pygame.font.SysFont("Arial", 30)

    # title
    title_font = pygame.font.SysFont("Arial", 40)
    title_text = title_font.render("Sign-up", True, WHITE)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 8))

    # colors for input box
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')

    # user_name
    user_name_font = pygame.font.SysFont("Arial", 25)
    user_name_text = user_name_font.render("User-name: ", True, WHITE)
    user_name_rect = user_name_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 50))

    user_name_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 30, 300, 40)
    user_name_color = color_inactive
    user_name_active = False
    user_name_input_text = ''

    # password
    password_font = pygame.font.SysFont("Arial", 25)
    password_text = password_font.render("Password: ", True, WHITE)
    password_rect = password_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 100))

    password_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 80, 300, 40)
    password_color = color_inactive
    password_active = False
    password_input_text = ''

    # fname
    fname_font = pygame.font.SysFont("Arial", 25)
    fname_text = fname_font.render("First Name: ", True, WHITE)
    fname_rect = fname_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 150))

    fname_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 130, 300, 40)
    fname_color = color_inactive
    fname_active = False
    fname_input_text = ''

    # lname
    lname_font = pygame.font.SysFont("Arial", 25)
    lname_text = lname_font.render("Last Name: ", True, WHITE)
    lname_rect = lname_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 200))

    lname_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 180, 300, 40)
    lname_color = color_inactive
    lname_active = False
    lname_input_text = ''

    # email
    email_font = pygame.font.SysFont("Arial", 25)
    email_text = email_font.render("Email: ", True, WHITE)
    email_rect = email_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 250))

    email_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 230, 300, 40)
    email_color = color_inactive
    email_active = False
    email_input_text = ''

    # Address
    Address_font = pygame.font.SysFont("Arial", 25)
    Address_text = Address_font.render("Address: ", True, WHITE)
    Address_rect = Address_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 300))

    Address_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 280, 300, 40)
    Address_color = color_inactive
    Address_active = False
    Address_input_text = ''

    # Phone
    Phone_font = pygame.font.SysFont("Arial", 25)
    Phone_text = Phone_font.render("Phone: ", True, WHITE)
    Phone_rect = Phone_text.get_rect(center=(WIDTH // 2 - 250, HEIGHT // 6 + 350))

    Phone_input_box = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 6 + 330, 300, 40)
    Phone_color = color_inactive
    Phone_active = False
    Phone_input_text = ''

    # sign-up button
    signup_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT * 4 // 5, 150, 50)

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
                # Check if any input box was clicked
                input_boxes = [
                    (user_name_input_box, "user_name"),
                    (password_input_box, "password"),
                    (fname_input_box, "fname"),
                    (lname_input_box, "lname"),
                    (email_input_box, "email"),
                    (Address_input_box, "address"),
                    (Phone_input_box, "phone")
                ]

                # Reset all boxes to inactive
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

        # Draw input boxes
        pygame.draw.rect(WINDOW, user_name_color, user_name_input_box, 2)
        pygame.draw.rect(WINDOW, password_color, password_input_box, 2)
        pygame.draw.rect(WINDOW, fname_color, fname_input_box, 2)
        pygame.draw.rect(WINDOW, lname_color, lname_input_box, 2)
        pygame.draw.rect(WINDOW, email_color, email_input_box, 2)
        pygame.draw.rect(WINDOW, Address_color, Address_input_box, 2)
        pygame.draw.rect(WINDOW, Phone_color, Phone_input_box, 2)

        # Render text surfaces
        user_name_txt_surface = input_font.render(user_name_input_text, True, WHITE)
        password_txt_surface = input_font.render(len(password_input_text) * '*', True, WHITE)
        fname_txt_surface = input_font.render(fname_input_text, True, WHITE)
        lname_txt_surface = input_font.render(lname_input_text, True, WHITE)
        email_txt_surface = input_font.render(email_input_text, True, WHITE)
        Address_txt_surface = input_font.render(Address_input_text, True, WHITE)
        Phone_txt_surface = input_font.render(Phone_input_text, True, WHITE)

        # Draw text surfaces
        WINDOW.blit(user_name_txt_surface, (user_name_input_box.x + 5, user_name_input_box.y + 5))
        WINDOW.blit(password_txt_surface, (password_input_box.x + 5, password_input_box.y + 5))
        WINDOW.blit(fname_txt_surface, (fname_input_box.x + 5, fname_input_box.y + 5))
        WINDOW.blit(lname_txt_surface, (lname_input_box.x + 5, lname_input_box.y + 5))
        WINDOW.blit(email_txt_surface, (email_input_box.x + 5, email_input_box.y + 5))
        WINDOW.blit(Address_txt_surface, (Address_input_box.x + 5, Address_input_box.y + 5))
        WINDOW.blit(Phone_txt_surface, (Phone_input_box.x + 5, Phone_input_box.y + 5))

        # Draw sign-up button
        pygame.draw.rect(WINDOW, WHITE, signup_button)
        login_text = input_font.render("sign-up", True, BLACK)
        login_text_rect = login_text.get_rect(center=signup_button.center)
        WINDOW.blit(login_text, login_text_rect)

        if error_text:
            x = error_font.render(error_text, True, (255, 0, 0))
            error_rect = x.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4 + 100))
            WINDOW.blit(x, error_rect)

        pygame.display.update()


# user functions
def loadSeventhPage(WINDOW, HEIGHT, WIDTH, current_user_name , cursor , mydb):
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

        # event loop
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
