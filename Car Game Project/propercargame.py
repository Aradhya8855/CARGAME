# Creating a pygame using a pygame Module:-->
import pygame
pygame.init()
import math 
import random

# SCREEN SETUP

wn = pygame.display.set_mode((840,650))     
pygame.display.set_caption('Car Game')
logo = pygame.image.load('GameLogo.jpg')
pygame.display.set_icon(logo)

# Scoring Part->
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
score_x = 200
score_y = 250

# Crashing Part ->
crash_x = 290
crash_y = 290

# Variable ->
game_exit = False
bg = pygame.image.load('Road.png')

# Maincar Image ->
maincar = pygame.image.load('Maincar.png')
maincar_x = 392
maincar_y = 516
maincar_xchange = 0
maincar_ychange = 0

# Car 1 Image ->
car1 = pygame.image.load('Car1.png')
car1_x = 400
car1_y = 100
car1_xchange = 0
car1_ychange = 8

# Car 2 Image ->
car2 = pygame.image.load('Car2.png')
car2_x = 400
car2_y = 100
car2_xchange = 0
car2_ychange = 8

# Car 3 Image ->
car3 = pygame.image.load('Car3.png')
car3_x = 400
car3_y = 100
car3_xchange = 0
car3_ychange = 8

# Function ->
def picture (x,y):
    wn.blit(maincar,(x,y))

def picture1 (x,y):
    wn.blit(car1,(x,y))

def picture2 (x,y):
    wn.blit(car2,(x,y))

def picture3 (x,y):
    wn.blit(car3,(x,y))

def iscollision (maincar_x,maincar_y,car1_x,car1_y):
    distance = math.sqrt(math.pow(maincar_x-car1_x,2)+math.pow(maincar_y-car1_y,2))
    if distance < 60:
        return True
    else:
        return False

def iscollision (maincar_x,maincar_y,car2_x,car2_y):
    distance = math.sqrt(math.pow(maincar_x-car2_x,2)+math.pow(maincar_y-car2_y,2))
    if distance < 60:
        return True
    else:
        return False

def iscollision (maincar_x,maincar_y,car3_x,car3_y):
    distance = math.sqrt(math.pow(maincar_x-car3_x,2)+math.pow(maincar_y-car3_y,2))
    if distance < 70:
        return True
    else:
        return False

def show_score(x,y):
    font_score = font.render("Score : " + str(score_value),True,(255,255,0))
    wn.blit(font_score,(x,y))

def show_crash(x,y):
    font_crash = font.render("GAME OVER !!",True,(255,255,255))
    wn.blit(font_crash,(x,y))



# Main() ->

while not game_exit:
    wn.blit(bg,(0,0))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                maincar_xchange = +5
            if event.key == pygame.K_LEFT:
                maincar_xchange = -5

    maincar_x += maincar_xchange
    car1_y += car1_ychange
    car2_y += car2_ychange
    car3_y += car3_ychange

    # Boundaries-->
    if maincar_x <= 140:
        maincar_x = 140
    elif maincar_x >= 650:
        maincar_x = 650

    # Car continue moving--

    if car1_y > 650:
        car1_y =-100
        car1_x = random.randint(140,650)
        score_value += 1
        print(score_value)

    if car2_y > 650:
        car2_y =-300
        car2x = random.randint(140,650)
        score_value += 1
        print(score_value)

    if car3_y > 650:
        car3_y =-500
        car3_x = random.randint(140,650)
        score_value += 1
        print(score_value)

    collisionone = iscollision(maincar_x,maincar_y,car1_x,car1_y)
    collisiontwo = iscollision(maincar_x,maincar_y,car2_x,car2_y)
    collisionthree = iscollision(maincar_x,maincar_y,car3_x,car3_y)
       
    # Function Calling
    picture(maincar_x,maincar_y)
    show_score(score_x,score_y)

    picture1(car1_x,car1_y)

    picture2(car2_x,car2_y)

    picture3(car3_x,car3_y)

    if collisionone :
        wn.fill((255,0,255))
        car1_ychange = 0
        car2_ychange = 0
        car3_ychange = 0
        maincar_xchange = 0
        show_crash(crash_x,crash_y)
        show_score(320,330)

    elif collisiontwo :
        wn.fill((255,0,255))
        car1_ychange = 0
        car2_ychange = 0
        car3_ychange = 0
        maincar_xchange = 0
        show_crash(crash_x,crash_y)
        show_score(320,330)

    elif collisionthree :
        wn.fill((255,0,255))
        car1_ychange = 0
        car2_ychange = 0
        car3_ychange = 0
        maincar_xchange = 0
        show_crash(crash_x,crash_y)
        show_score(320,330)

    pygame.display.update()

pygame.quit()
quit()
