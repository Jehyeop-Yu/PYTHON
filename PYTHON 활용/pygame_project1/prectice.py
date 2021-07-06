# 1-1.정의
import pygame
import os # "2-1."를 위한 정의

pygame.init()

# 1-2.화면 크기 설정 및 디스플레이
screen_width = 640
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height)) # pygame.display.set_mode((가로길이, 세로길이))

# 1-3.타이틀 설정(게임 이름)
pygame.display.set_caption("creating_again")

# 2-1. 파일 넣기위한 베이스 작업
background = pygame.image.load(os.path.join(os.path.join(os.path.dirname(__file__), "images"), "background.png"))

stage = pygame.image.load(os.path.join(os.path.join(os.path.dirname(__file__), "images"), "stage.png"))
stage_size = stage.get_rect().size # 원래 이미지 크기 값을 가져온다 [0]:가로 , [1]:세로
print(stage_size)




# 1-4.게임 동작 기본 프레임 
    # 동작 확인 (기본 :True)
running = True
    # 원하는 동작 입력 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 나가기 버튼 누르면 running = False 출력 
            running = False

    

    screen.blit(background, (0,0))
    # 1-5.화면 그리기 
    pygame.display.update() # 게임 화면을 다시 그리기 

# 1-6.종료
pygame.quit()
