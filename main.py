import sys

import mysql.connector
from collections import deque

import pygame

from admin.admin_functionality import admin_functonality
from admin.admin_login_page import admin_login
from admin.admin_user_page import admin_user_page
from user.login_signup_user import signup_login_user
from user.user_functionality import user_functionality
from user.user_login import user_login
from user.user_signup import user_signup

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

    while True:
        first_background = pygame.image.load('assets/Library_background.jpeg').convert()
        WINDOW.blit(first_background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if PAGE_INDEX == 1:
            PAGE_INDEX = admin_user_page(WINDOW , HEIGHT , WIDTH)
            stack.append(PAGE_INDEX)

        elif PAGE_INDEX == 2:
            # Admin page
            x = admin_login(WINDOW , HEIGHT , WIDTH)
            if x == "prev":
                previous_page()
            elif x:
                PAGE_INDEX = 4
                stack.append(PAGE_INDEX)


        elif PAGE_INDEX == 3:
            # user login or signup page
            x = signup_login_user(WINDOW , HEIGHT , WIDTH)
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
            x = admin_functonality(WINDOW , HEIGHT , WIDTH , cursor , mydb)
            if x == "prev":
                previous_page()

        elif PAGE_INDEX == 5:
            # user login process
            current_user_name = user_login(WINDOW, HEIGHT, WIDTH , cursor)
            if current_user_name == "prev":
                previous_page()
                current_user_name = None
            else :
                PAGE_INDEX = 7
                stack.append(PAGE_INDEX)

        elif PAGE_INDEX == 6:
            # user signup process
            current_user_name = user_signup(WINDOW, HEIGHT, WIDTH , cursor , mydb)
            if current_user_name == "prev":
                previous_page()
                current_user_name = None
            else:
                PAGE_INDEX = 7
                stack.append(PAGE_INDEX)

        elif PAGE_INDEX == 7:
            if current_user_name is None:
                continue
            x = user_functionality(WINDOW , HEIGHT , WIDTH , current_user_name , cursor , mydb)
            if x == "prev":
                previous_page()

        pygame.display.update()
