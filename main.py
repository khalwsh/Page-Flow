import sys
import pygame
from colors import *
from pages import *
import mysql.connector
from collections import deque

# stack to track last page was opened
stack = deque()

# make database connection here
mydb = mysql.connector.connect(host="localhost", user="root", passwd="adkhyono234", database="khalwsh")
cursor = mydb.cursor()
PAGE_INDEX = 1

stack.append(PAGE_INDEX)
def previous_page():
    global PAGE_INDEX
    if len(stack) == 1:
        return
    stack.pop()
    PAGE_INDEX = stack[-1]

current_user_name = None
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Library Management system')

    # creating the main window
    WIDTH, HEIGHT = 800, 600
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    # to keep track which page we already in
    while True:
        # loading the image from assets and draw it
        first_background = pygame.image.load('assets/Library_background.jpeg').convert()
        WINDOW.blit(first_background, (0, 0))
        # from any page I have option to close the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if PAGE_INDEX == 1:
            PAGE_INDEX = loadFirstPage(WINDOW , HEIGHT , WIDTH)
            stack.append(PAGE_INDEX)

        elif PAGE_INDEX == 2:
            # Admin page
            x = loadSecondPage(WINDOW , HEIGHT , WIDTH)
            print(x)
            if x == "prev":
                previous_page()
            elif x:
                PAGE_INDEX = 4
                stack.append(PAGE_INDEX)


        elif PAGE_INDEX == 3:
            # user login or signup page
            x = loadThirdPage(WINDOW , HEIGHT , WIDTH)
            if x == "prev":
                previous_page()
            elif x == 2:
                PAGE_INDEX = 5
                stack.append(PAGE_INDEX)
            else:
                PAGE_INDEX = 6
                stack.append(PAGE_INDEX)
            pass

        elif PAGE_INDEX == 4:
            # admin functions
            x = loadFourthPage(WINDOW , HEIGHT , WIDTH , cursor , mydb)
            if x == "prev":
                previous_page()

        elif PAGE_INDEX == 5:
            # user login process
            current_user_name = loadFifthPage(WINDOW, HEIGHT, WIDTH , cursor)
            if current_user_name == "prev":
                previous_page()
                current_user_name = None
            else :
                PAGE_INDEX = 7
                stack.append(PAGE_INDEX)

        elif PAGE_INDEX == 6:
            # user signup process
            current_user_name = loadSixthPage(WINDOW, HEIGHT, WIDTH , cursor , mydb)
            if current_user_name == "prev":
                previous_page()
                current_user_name = None
            else:
                PAGE_INDEX = 7
                stack.append(PAGE_INDEX)

        elif PAGE_INDEX == 7:
            x = loadSeventhPage(WINDOW , HEIGHT , WIDTH , current_user_name , cursor , mydb)
            if x == "prev":
                previous_page()

        pygame.display.update()
