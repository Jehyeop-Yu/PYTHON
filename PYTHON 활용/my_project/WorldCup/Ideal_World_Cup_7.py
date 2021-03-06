# from math import e
import os
from typing import Tuple
import pygame
from random import *

def display_start_btn():
    pygame.draw.rect(screen, BLACK, startbtn, 3)
    screen.blit(start_btn, (((screen_width/2)-(start_width/2)), ((screen_height/2)-(start_height/2))))

def display_Chance_btn():
    pygame.draw.rect(screen, BLACK, chancebtn, 1)
    screen.blit(chance_btn, ((screen_width)-150, 10))

def display_help_btn():
    pygame.draw.rect(screen, BLACK, helpbtn, 1)
    screen.blit(help_btn, ((screen_width)-230, 10))

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

def display_round():
    global Round_score
    if round_cnt < 5:
        Round_score = round_set // (2**round_cnt)
        txt_curr_round = game_font.render(f"{Round_score}강", True, BLACK)
        if Round_score == 2:
            txt_curr_round = game_font.render(f"준결승", True, BLACK)
        elif Round_score == 1:
            txt_curr_round = game_font.render(f"결승", True, BLACK)
    else:
        txt_curr_round = game_font.render(f"당신의 이상형", True, BLACK)
    screen.blit(txt_curr_round, (50, 20))

def display_situation():
    global situations_list
    situation = game_font.render("{}".format(situations_list), True, BLACK)
    screen.blit(situation, (0, screen_height*3/4))

def check_buttons(pos):
    global start, situation
    if start:
        if select_left.collidepoint(pos):
            check_left_img()
        elif select_right.collidepoint(pos):
            check_right_img()
        elif helpbtn.collidepoint(pos):
            print("click: helpbtn")
            random_situations()
        elif chancebtn.collidepoint(pos):
            print("click: chancebtn")
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

def random_situations():
    global situations_list
    situations_list = [
    " 상황 1 : 바다에 빠졌을 경우 한명만 구할 수 있다.둘중 누구를 구할 것인가?",
    " 상황 2 : 오랫동안 기다려온 영화를 드디어 예매했다. 운좋게 영화관 이벤트로 VVIP 티켓 2장으로 업그레이드 해줬다. 무조건 2명 입장인데 두명 중 누구랑 갈 것인가? ",
    " 상황 3 : 오랜만에 쇼핑하러 백화점에 왔다. 둘러보다가 눈에 띄는 포스터에 이끌려 매장에 들어가 옷을 샀다. 그 포스터에 걸맞는 모델은 누구였으면 하는가? "
    ]
    
    shuffle(situations_list)
    # situations = sample(situations_list , 1)
    print("{}".format(situations_list))

    

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

chance_btn = pygame.image.load(os.path.join(current_path, "chance_btn.png"))
chance_size = chance_btn.get_rect().size
chance_width = chance_size[0]
chance_height = chance_size[1]
chancebtn = pygame.Rect((screen_width)-150, 10, chance_width, chance_height)

help_btn = pygame.image.load(os.path.join(current_path, "help_btn.png"))
help_size = help_btn.get_rect().size
help_width = help_size[0]
help_height = help_size[1]
helpbtn = pygame.Rect((screen_width)-230, 10, help_width, help_height)


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

select_left = pygame.Rect(0, 55, 600, 645)

select_right = pygame.Rect(600, 55, 600, 645)

game_font = pygame.font.SysFont('카페24동동', 30)
# game_font = pygame.font.SysFont("arialrounded", 30)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

round_set = 16
round_cnt = 1
Round_score = 0
round = ()
next_round = ()

situations_list = []

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
        display_help_btn()
        display_Chance_btn()
        pass
    else:
        display_start_btn()

    if click_pos:
        check_buttons(click_pos)

    display_situation()
    display_round()
    pygame.display.update()
    
pygame.quit()