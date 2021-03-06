from math import e
import os
import pygame
from random import *

def display_left_screen():
    pygame.draw.rect(screen, BLACK, start_btn, 1)

# def check_buttons(pos):
#     if select_left.collidepoint(pos):
#         check_left_img()
#     else:
#         check_right_img()

def check_buttons(pos):
    global start
    if start:
        if select_left.collidepoint(pos):
            check_left_img()
        else:
            check_right_img()
    elif start_btn.collidepoint(pos):     
        start = True
        shfl()
    # print("list1={}".format(round))
    # print("list2={}".format(next_round))

def shfl():
    shuffle(round)

def check_left_img():
    next_round.append(round[0])
    del round[0:2]

def check_right_img():
    next_round.append(round[1])
    del round[0:2]

pygame.init() 
screen_width = 1200 # 가로 크기
screen_height = 800 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("이상형 월드컵") 

# FPS
clock = pygame.time.Clock()
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

imges = [
    pygame.image.load(os.path.join(current_path, "img1.png")),
    pygame.image.load(os.path.join(current_path, "img2.png")),
    pygame.image.load(os.path.join(current_path, "img3.png")),
    pygame.image.load(os.path.join(current_path, "img4.png")),
    pygame.image.load(os.path.join(current_path, "img5.png")),
    pygame.image.load(os.path.join(current_path, "img6.png")),
    pygame.image.load(os.path.join(current_path, "img7.png")),
    pygame.image.load(os.path.join(current_path, "img8.png")),
    pygame.image.load(os.path.join(current_path, "img9.png")),
    pygame.image.load(os.path.join(current_path, "img10.png")),
    pygame.image.load(os.path.join(current_path, "img11.png")),
    pygame.image.load(os.path.join(current_path, "img12.png")),
    pygame.image.load(os.path.join(current_path, "img13.png")),
    pygame.image.load(os.path.join(current_path, "img14.png")),
    pygame.image.load(os.path.join(current_path, "img15.png")),
    pygame.image.load(os.path.join(current_path, "img16.png")),]

start_btn = pygame.Rect((screen_width / 2) - 50, screen_height / 2, 100, 50)

select_left = pygame.Rect(0, 0, 600, 800)
select_left.center = (screen_width / 4, screen_height / 2)

select_right = pygame.Rect(600, 0, 600, 800)
select_right.center = (screen_width / 4, screen_height / 2)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

round_cnt = 1
round = ()
next_round = ()


# select_img_1 = list(enumerate(imges))
select_img_1 = list(imges)
select_img_2 = [] 

running = True

start = False

for lst_idx, lst_val in enumerate(imges):
    print(lst_idx, lst_val)


while running:
    dt = clock.tick(30)
    click_pos = None
    # screen.blit(imges[0], (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos() 
            print(click_pos)

    screen.blit(background, (0, 0))

    
    if (round_cnt % 2) >= 1:
        round = select_img_1
        next_round = select_img_2
        if round_cnt == 5:
            break
    elif(round_cnt % 2) == 0:
        round = select_img_2
        next_round = select_img_1

    if len(round) <= 0:
        round_cnt += 1
        print(round_cnt)

    if len(round) >= 2:
        screen.blit(round[0], (0, 0))
        screen.blit(round[1], (600, 0))
    else:
        pass


    display_left_screen()

    if click_pos:
        check_buttons(click_pos)



    pygame.display.update()
    
pygame.quit()