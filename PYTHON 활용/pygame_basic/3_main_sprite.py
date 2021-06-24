# 캐릭터 넣기
import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Jehyeop Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("PYTHON/PYTHON 활용/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("PYTHON/PYTHON 활용/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기 구해옴
character_with = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = screen_width / 2 - 35 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로위치)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로위치)

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생 하였는가?
        if event.type == pygame.QUIT: # 창 x 버튼 누르면 동작 
            running = False # 게임이 진행중이 아님
    
    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임화면을 다시 그리기

# pygame 종료
pygame.quit()