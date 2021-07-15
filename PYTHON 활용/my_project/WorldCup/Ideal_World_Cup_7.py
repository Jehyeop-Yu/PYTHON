from math import e
import os
import pygame
from random import *

def display_start_btn():
    pygame.draw.rect(screen, BLACK, startbtn, 3)
    screen.blit(start_btn, (((screen_width/2)-(start_width/2)), ((screen_height/2)-(start_height/2))))

def display_img(i):
    global round
    left_img_size = round[i].get_rect().size
    left_img_width = left_img_size[0]
    left_img_height = left_img_size[1]
    left_img_center = ((screen_width/4) - (left_img_width / 2)), ((screen_height / 2) - (left_img_height / 2))
    screen.blit(round[i], left_img_center)

    right_img_size = round[i+1].get_rect().size
    right_img_width = right_img_size[0]
    right_img_height = right_img_size[1]
    right_img_center = (600 + (screen_width/4) - (right_img_width / 2)), ((screen_height / 2) - (right_img_height / 2))
    screen.blit(round[i+1], right_img_center)

def display_last_img():
    last_img = round[0].get_rect().size
    last_img_width = last_img[0]
    last_img_height = last_img[1]
    last_img_center = (((screen_width/2)-(last_img_width/2)), ((screen_height/2)-(last_img_height/2)))
    screen.blit(round[0], last_img_center)

def check_buttons(pos):
    global start
    if start:
        if select_left.collidepoint(pos):
            check_left_img()
        else:
            check_right_img()
    elif startbtn.collidepoint(pos):     
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

start_btn = pygame.image.load(os.path.join(current_path, "img0.png"))
start_size = start_btn.get_rect().size
start_width = start_size[0]
start_height = start_size[1]
startbtn = pygame.Rect(((screen_width/2)-(start_width/2)), ((screen_height/2)-(start_height/2)), start_width, start_height)



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


# start_btn = pygame.Rect((screen_width / 2) - 50, screen_height / 2, 100, 50)

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
           display_last_img()
    elif(round_cnt % 2) == 0:
        round = select_img_2
        next_round = select_img_1


    if len(round) <= 0:
        round_cnt += 1
        print(round_cnt)
    elif len(round) >= 2:
        if start == True:
            display_img(0)
    else:
        pass
    

    if start == True:    
        pass
    else:
        display_start_btn()

    if click_pos:
        check_buttons(click_pos)

    pygame.display.update()
    
pygame.quit()