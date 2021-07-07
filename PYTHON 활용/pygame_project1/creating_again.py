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

# 7-1. 공 입력 
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))] 

# 7-2. 공 크기에 따른 최초 스피드 정의
ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3에 해당하는 값

# 7-3-1. 공 리스트 저장 장소
balls = []

# 7-3-2. 최초 발생하는 큰공 리스트에 추가 
balls.append({
    "pos_x" : 50, # 공의 x 좌표
    "pos_y" : 50, # 공의 y 좌표
    "img_idx" : 0, # 공의 이미지 인덱스
    "to_x" : 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
    "to_y" : -6, # y축 이동방향,
    "init_spd_y" : ball_speed_y[0] # y 최초 속도
})

# 8-5-4. 사라질 무기, 공 정보 저장 할 변수 
weapon_to_remove = -1
ball_to_remove = -1

# 10-1. 문자 넣기(폰트, 시간 정의)
game_font = pygame.font.Font(None, 40)
game_result = "Game Over"

# 11-1. 시간 정의
total_time = 100
start_ticks = pygame.time.get_ticks() # 시작 시간 정의

#-------------------------------------------------------------------------------------------------------------------#

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

    # 7-4-1. 공 위치 정의
    for ball_idx, ball_val in enumerate(balls): # enumerate : (인덱스, 원소)로 출력
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"] # index: [0]=큰공 ~ [3]=작은공

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 7-4-2. 가로) 벽에 닿을 때 공의 이동 위치 변경 (튕겨나오는 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width: # 벽에 닿았을 경우
            ball_val["to_x"] = ball_val["to_x"]* -1 # 방향 변경 

        # 7-4-3. 세로) 스테이지에 닿을 때 공의 이동 위치 변경 (튕겨나오는 효과)
        if ball_pos_y >= screen_height - stage_height - ball_height: # 스테이지에 튀겨서 올라가는 처리
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 그 외의 모든 경우에는 속도를 점점 증가
            ball_val["to_y"] += 0.5

        # 7-4-4. 변화값 적용
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 8-1. 충돌 처리 
    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # 8-2. 충돌 처리에 사용될 공 index, value 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # 8-3. 공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # 8-4. 공과 캐릭터 충돌 처리 
        if character_rect.colliderect(ball_rect): # colliderect : 두 직사각형 충돌 여부
            running = False
            break

        # 8-5-1. 공과 무기들 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 8-5-2. 무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # 8-5-3. 충돌 체크 
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # 해당 무기 없에기 위한 값 설정
                ball_to_remove = ball_idx # 해당 공 없에기 위한 값 설정
                
                # 9-1. 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                if ball_img_idx < 3:

                    # 9-2. 현재 공 크기 정보를 가지고 옴
                    ball_width = ball_rect.size[0]
                    ball_height =ball_rect.size[1] 

                    # 9-3. 나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # 9-4. 왼쪽으로 튕겨나가는 작은 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width/2) - (small_ball_width/2), # 공의 x 좌표
                        "pos_y" : ball_pos_y + (ball_height/2) - (small_ball_height/2), # 공의 y 좌표
                        "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
                        "to_x" : -3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                        "to_y" : -6, # y축 이동방향,
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1] }) # y 최초 속도  
                    
                    # 9-4. 오른쪽으로 튕겨나가는 작은 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width/2) - (small_ball_width/2), # 공의 x 좌표
                        "pos_y" : ball_pos_y + (ball_height/2) - (small_ball_height/2), # 공의 y 좌표
                        "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스
                        "to_x" : 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                        "to_y" : -6, # y축 이동방향,
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1] }) # y 최초 속도  
                break

        # 12-1. 버그 및 디테일
        else: # 계속 게임을 진행
            continue # 안쪽 for 문 조건이 맞지 않으면 continue. 바깥 for 문 계속 수행
        break # 안쪽 for 문에서 break 를 만나면 여기로 진입 가능. 2중 for 문을 한번에 탈출    

#-------------------------------------------------------------------------------------------------------------------#

    # 8-6. 충돌된 공,무기 없에기 , 충돌시 ball_to_remove = 0  weapon_to_remove = 0
    if ball_to_remove > -1: 
        del balls[ball_to_remove]
        ball_to_remove = -1
    if weapon_to_remove >-1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 11-2. 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    # 10-2. 모든 공을 없엔 경우 게임 종료 (성공)
    if len(balls) == 0:
        game_result = "Mision Complete"
        running = False

    # 10-3. 시간 초과
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

#-------------------------------------------------------------------------------------------------------------------#

    # 2-3. 배경 그리기 
    screen.blit(background, (0, 0))

    # 5-5. 무기 그리기
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    # 7-5 공 그리기
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    # 3-2. 스테이지 그리기
    screen.blit(stage, (0, screen_height - stage_height))
    # 4-2. 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    # 1-5.화면 그리기 
    pygame.display.update() # 게임 화면을 다시 그리기 

# 10-4. 게임 오버 메시지
msg = game_font.render(game_result, True, (255, 255, 0)) # 노란색
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2))) # 문자 위치 중앙
screen.blit(msg, msg_rect)
pygame.display.update()

# 12-2. 1.5초 대기
pygame.time.delay(1500)

# 1-6.종료
pygame.quit()