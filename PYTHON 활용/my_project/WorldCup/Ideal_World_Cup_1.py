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
    if select_left.collidepoint(pos): # 클릭한 위치가 pos 안에 있는지 확인
        print("LEFT")
    else: # 클릭한 위치가 pos 안에 있는지 확인
        print("RIGHT")

def shuffle_img():
    img_left = randrange(0, 16) # len(img)
    img_right = randrange(0, 16)
    while img_left == img_right:
        # print("left = right")
        img_right = randrange(0, 2)
    else:
        print("left={}".format(img_left))
        print("right={}".format(img_right))


pygame.init() 
screen_width = 1200 # 가로 크기
screen_height = 800 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("이상형 월드컵") 

# FPS
clock = pygame.time.Clock()
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

select_left = pygame.Rect(0, 0, 600, 800)
select_left.center = (screen_width / 4, screen_height / 2)

select_right = pygame.Rect(600, 0, 600, 800)
select_right.center = (screen_width / 4, screen_height / 2)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

select_img_1 = [] # 16강
select_img_2 = [] # 8강
select_img_3 = [] # 4강
select_img_4 = [] # 결승

running = True

while running:
    dt = clock.tick(30)
    click_pos = None
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭 했을 때
            click_pos = pygame.mouse.get_pos() # 클릭한 위치 값 가져오기
            print(click_pos)
            shuffle_img()
   
    screen.blit(background, (0, 0))
    display_left_screen()

    if click_pos:
        check_buttons(click_pos)

    pygame.display.update() # 게임화면을 다시 그리기
    
pygame.quit()