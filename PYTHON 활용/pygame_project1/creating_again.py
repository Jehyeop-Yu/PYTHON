# 1-1.정의
import pygame
import os # "2-1."를 위한 정의

pygame.init()

# 1-2.화면 크기 설정 및 디스플레이
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height)) # pygame.display.set_mode((가로길이, 세로길이))

# 1-3.타이틀 설정(게임 이름)
pygame.display.set_caption("creating_again")

# 6-1. FPS 설정 정의
clock = pygame.time.Clock()

# 2-1. 파일 넣기위한 베이스 작업
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환 (dirname() : 입력된 경로로부터 디렉토리를 추출)
image_path = os.path.join(current_path, "images") # os.path.join("결합할 경로", "이미지를 넣어둔 폴더 이름") 경로와 파일명을 결합하거나 분할된 경로를 하나로 정리

# 2-2. 배경 이미지 입력
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 3-1. 스테이지 이미지 입력
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size # 원래 이미지 크기 값을 가져온다 (가로([0]) , 세로([1]))
stage_height = stage_size[1]

# 4-1. 캐릭터 이미지 입력
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 캐릭터의 기본 위치 x좌표 설정 
character_y_pos = screen_height - stage_height - character_height # 캐릭터의 기본 위치 y좌표 설정

# 4-3-1. 캐릭터 이동방향설정(캐릭터 이동에 따른 값 저장을 위한 설정)
character_to_x = 0

# 4-3-2. 캐릭터 이동 속도설정(character_to_x 값의 증가량 설정)
character_speed = 5

# 5-1. 무기 이미지 입력
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 5-3-1. 무기 여러개 저장 할 리스트 
weapons = []

# 5-4-1. 무기 이동 속도
weapon_speed = 10


# 1-4.게임 동작 기본 프레임 
running = True # 동작 확인 (기본 :True)
while running:  # 원하는 동작 입력 
    # 6-2. FPS tick(1초동안 출력 할 tick 수) 설정
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 나가기 버튼 누르면 running = False 출력 
            running = False
        
        # 4-3. 캐릭터 움직이기 
        if event.type == pygame.KEYDOWN: # 키가 눌렸을 경우
            if event.key == pygame.K_LEFT: # 왼쪽 키가 눌렸을 경우
                character_to_x -= character_speed 
            elif event.key == pygame.K_RIGHT: # 오른쪽 키가 눌렸을 경우
                character_to_x += character_speed 
            # 5-2. 무기 발사
            elif event.key == pygame.K_SPACE: # 스페이스바가 눌렸을 경우
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2) # 무기가 나가는 x좌표 설정(캐릭터 중앙)
                weapon_y_pos = character_y_pos

                # 5-3-2. 생성되는 무기 좌표값 리스트에 저장
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP: # 키에서 손을 땔 경우
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0 # character_speed 값을 더해주지 않아 값이 변하지 않게 한다.


    # 4-4. 캐릭터 위치 정의
    character_x_pos += character_to_x # 변화하는 character_to_x 값을 캐릭터에 적용

    # 4-5. 캐릭터 경계값 설정 
    if character_x_pos < 0: # 좌측 경계값 설정
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width: # 우측 경계값 설정
        character_x_pos = screen_width - character_width

    # 5-4-2. 무기 위치 조정 
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons] 
    # weapons 의 값을 w 리스트에 넣고 w 리스트의 x값 w[0], y값 w[1]을 가져와서 계산 
    # w 리스트 안에 있는 weapons의 x값 w[0], y값 w[1]을 가져와 [w[0], w[1] - weapon_speed]와 같이 계산한다.

    # 5-4-3. 천장에 닿은 무기 없에기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0] # weapons는 y값(w[1])이 0보다 큰 값만 존재한다.

    # 2-3. 배경 그리기 
    screen.blit(background, (0, 0))
    # 3-2. 스테이지 그리기
    screen.blit(stage, (0, screen_height - stage_height))
    # 4-2. 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    # 5-5. 무기 그리기
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
        
    # 1-5.화면 그리기 
    pygame.display.update() # 게임 화면을 다시 그리기 

# 1-6.종료
pygame.quit()