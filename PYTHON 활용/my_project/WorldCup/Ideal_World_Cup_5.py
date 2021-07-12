# 이상형 월드컵 파이썬 작업 순서
# 이미지 구역 나누기 
# 화면 크기 설정 및 배경 넣기
# 이미지 리스트1 만들기 
# 리스트1에서 랜덤으로 2개의 사진 선택 및 화면에 출력
# 화면에 출력시 리스트에서 삭제 
# 선택 이미지는 리스트2에 저장
# 리스트 1 에서 더이상 출력할게 없을시 게임 2로 넘어감 
# 리스트 2 리스트 1과 같은 동작 반복 

# left right 값이 같지않게 출력 구현 하였으나 
# 리스트를 만들어 같은 값이 안나오게 하고 출력한 값을 그 리스트에서 빼는 과정으로 수정 해야함 

import os
import pygame
from random import *


def display_left_screen():
    pygame.draw.rect(screen, BLACK, select_left, 1)

    
def check_buttons(pos):
    global round_cnt, select_img_1, select_img_2, round, next_round

    if (round_cnt % 2) >= 1:
        round = select_img_1
        next_round = select_img_2
    else:
        round = select_img_2
        next_round = select_img_1
        
    shuffle(round)

    img_left = round[0]
    img_right = round[1]
    del round[0:2]
    print("left={}".format(img_left))
    print("right={}".format(img_right))
    print("list1={}".format(round))
        
    if select_left.collidepoint(pos):
        next_round.append(img_left)
        print("LEFT")
        print("list2={}".format(next_round))
    else:
        next_round.append(img_right)
        print("RIGHT")
        print("list2={}".format(next_round))
        
    if len(round) <= 0:
        round_cnt += 1
        print(round_cnt)


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
    pygame.image.load(os.path.join(current_path, "img6.png"))]

select_left = pygame.Rect(0, 0, 600, 800)
select_left.center = (screen_width / 4, screen_height / 2)

select_right = pygame.Rect(600, 0, 600, 800)
select_right.center = (screen_width / 4, screen_height / 2)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

round_cnt = 1
round = ()
next_round = ()

select_img_1 = list(enumerate(imges))
select_img_2 = [] 

running = True

for lst_idx in enumerate(imges):
    print(lst_idx)

while running:
    dt = clock.tick(30)
    click_pos = None
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭 했을 때
            click_pos = pygame.mouse.get_pos() # 클릭한 위치 값 가져오기
            print(click_pos)
   
    screen.blit(background, (0, 0))



    display_left_screen()

    if click_pos:
        check_buttons(click_pos)

    pygame.display.update() # 게임화면을 다시 그리기
    
pygame.quit()