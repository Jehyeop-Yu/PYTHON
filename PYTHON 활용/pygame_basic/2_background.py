# 배경 만들기
import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Jehyeop Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("F:/코딩/PYTHON/PYTHON 활용/pygame_basic/background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생 하였는가?
        if event.type == pygame.QUIT: # 창 x 버튼 누르면 동작 
            running = False # 게임이 진행중이 아님
    
    # screen.fill((20, 0, 225)) # 배경색을 직접 설정
    screen.blit(background, (0, 0)) # 배경 그리기

    pygame.display.update() # 게임화면을 다시 그리기

# pygame 종료
pygame.quit()