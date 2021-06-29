# 게임 오버 처리
import os
import math
import pygame

# 집게 클래스 
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.original_image = image

        self.rect = image.get_rect(center = position)

        self.offset = pygame.math.Vector2(default_offset_x_claw, 0) # Vecter2 에서는 로테이션 함수 제공해준다 (중심점으로부터의 거리, 0)
        self.position = position

        self.direction = LEFT # 집게의 이동 방향
        self.angle_speed = 2.5 # 집게의 각도 변경 폭 (좌우 이동 속도)
        self.angle = 10 # 최초 각도 정의 (오른쪽 끝)

    def update(self, to_x):
        if self.direction == LEFT: # 왼쪽 방향으로 이동하고 있다면
            self.angle += self.angle_speed # 이동 속도만큼 각도 증가
        elif self.direction == RIGHT: # 오른쪽 방향으로 이동하고 있다면
            self.angle -= self.angle_speed # 이동 속도만큼 각도 감소

        # 만약에 허용 각도 범위를 벗어나면?
        if self.angle > 170:
            self.angle = 170
            self.set_direction(RIGHT)
        elif self.angle < 10:
            self.angle = 10
            self.set_direction(LEFT)

        self.offset.x += to_x # offset 값의 x 좌표에 to_x 값만큼 더해줘서 변화를 준다. "line 18 : self.offset = pygame.math.Vector2(x, y)"

        self.rotate() # 회전 처리

    def rotate(self):
        # pygame.transform.rotate() # 아래 함수와 같은 동작이나 화면상 매끄럽지 않다.
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1) # 회전하고 난 뒤의 새로운 이미지를 넣기 위한 이미지 ( 원본 이미지, 각도(+윗각도, - 아래각도), 이미지 크기 )
        
        offset_rotated = self.offset.rotate(self.angle) # (각도)에따른 변화된 offset값을 받아온다.

        self.rect = self.image.get_rect(center = self.position + offset_rotated)
        pygame.draw.rect(screen, RED, self.rect, 1) # 기존 이미지의 사각형 구역 보기

    def set_direction(self, direction):
        self.direction = direction


    def draw(self, screen): # 그리기
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, RED, self.position, 3) # 중심점 표시
        pygame.draw.line(screen, BLACK, self.position, self.rect.center, 5)

    def set_init_state(self):
        self.offset.x = default_offset_x_claw # 줄 원래 길이로 초기화
        self.angle = 10 # 각도 원래 각도로 초기화
        self.direction = LEFT # 회전 방향 초기화

# 보석 클래스 
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position, price, speed):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center = position)
        self.price = price
        self.speed = speed

    def set_position(self, position, angle):
        r = self.rect.size[0] // 2 # 동그라미 이미지 기준으로 반지름 
        rad_angle = math.radians(angle) # 각도 
        to_x = r * math.cos(rad_angle) # 삼각형의 밑변
        to_y = r * math.sin(rad_angle) # 삼각형의 높이
        self.rect.center = (position[0] + to_x, position[1] + to_y) 

def setup_gemstone():
    small_gold_price, small_gold_speed = 100, 5
    big_gold_price, big_gold_speed = 300, 2
    stone_price, stone_speed = 10, 2
    diamond_price, diamond_speed = 600, 7

    # 작은금
    small_gold = Gemstone(gemstone_images[0], (200, 380), small_gold_price, small_gold_speed) # 0번재 이미지를 (200, 300) 위치에 
    gemstone_group.add(small_gold) # 그룹에 추가
    # 큰금
    gemstone_group.add(Gemstone(gemstone_images[1] , (300, 500), big_gold_price, big_gold_speed))
    # 돌
    gemstone_group.add(Gemstone(gemstone_images[2] , (300, 380), stone_price, stone_speed))
    # 다이아몬드
    gemstone_group.add(Gemstone(gemstone_images[3] , (900, 420), diamond_price, diamond_speed))
    
def update_score(score):
    global curr_score # 전역변수
    curr_score += score

def display_score():
    txt_curr_score = game_font.render(f"Curr Score : {curr_score:,}", True, BLACK)
    screen.blit(txt_curr_score, (50, 20)) # 보여줄것, 위치
    
    txt_goal_score = game_font.render(f"Goal Score : {goal_score:,}", True, BLACK)
    screen.blit(txt_goal_score, (50, 80))

def display_time(time):
    txt_timer = game_font.render(f"Time : {time}", True, BLACK)
    screen.blit(txt_timer, (1100, 50))

def display_game_over():
    game_font = pygame.font.SysFont("arialrounded", 60) # 큰 폰트
    txt_game_over = game_font.render(game_result, True, BLACK)
    rect_game_over = txt_game_over.get_rect(center = (int(screen_width / 2), (screen_height / 2))) # 화면 중앙 표시
    screen.blit(txt_game_over, rect_game_over)

pygame.init() 
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner") 

clock = pygame.time.Clock()

# 폰트
game_font = pygame.font.SysFont("arialrounded", 30)

# 점수 관련 변수
goal_score = 500 # 목표 점수
curr_score = 0 # 현재 점수 

# 게임 오버 관련 변수 
game_result = None # 게임 결과
total_time = 30 # 총 시간 

start_ticks = pygame.time.get_ticks() # 현재 tick을 받아옴 

# 게임 관련 변수 
default_offset_x_claw = 40 # 중심점으로부터 집게까지의 기본 x 간격
to_x = 0 # x 좌표 기준으로 집게 이미지를 이동시킬 값 저장 변수 
caught_gemstone = None # 집게를 뻗어 집은 보석 정보 

# 속도 변수
move_speed = 12 # 발사할 때 이동 스피드 (x 좌표 기준으로 증가된는 값)
return_speed = 20 # 아무것도없이 돌아올때 스피드 

# 방향 변수
LEFT = -1 # 왼쪽 방향
STOP = 0 # 이동방향이 좌우가 아닌 고정상태 (뻗은 상태)
RIGHT = 1 # 오른쪽 방향


# 색깔 변수 
RED = (255, 0, 0) # 빨간색
BLACK = (0, 0, 0) # 검정색

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 4개의 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_gold.png")).convert_alpha(), # 작은금 # convert_alpha() : 이미지에 투명도를 넣어준다.
    pygame.image.load(os.path.join(current_path, "big_gold.png")).convert_alpha(), # 큰금
    pygame.image.load(os.path.join(current_path, "stone.png")).convert_alpha(), # 돌
    pygame.image.load(os.path.join(current_path, "diamond.png")).convert_alpha()] # 다이아몬드
    

# 보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone() # 게임에 원하는 만큼의 보석을 정의 

# 집게
claw_image = pygame.image.load(os.path.join(current_path, "claw.png")).convert_alpha() # convert_alpha() : 이미지에 투명도를 넣어준다.
claw = Claw(claw_image, (screen_width // 2 , 110)) # 화면 가로 기준 절반, 위에서 110 픽셀 

running = True
while running:
    clock.tick(30) # FPS값 30으로 고정 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN: # 마우스 버튼 누를 때 집게를 뻗음
            if claw.direction != STOP:
                claw.set_direction(STOP) # 좌우 멈춤
                to_x = move_speed # move_speed 만큼 빠르게 뻗는다.

    if claw.rect.left < 0 or claw.rect.right > screen_width or claw.rect.bottom > screen_height: # screen 밖을 벗어나려 할때 돌아오는 결계값 처리
        to_x = -return_speed
    
    if claw.offset.x < default_offset_x_claw: # 원위치에 오면 
        to_x = 0
        claw.set_init_state() # 처음 상태로 되돌림

        if caught_gemstone: # 잡힌 보석이 있다면 
            update_score(caught_gemstone.price) # 점수 업데이트 처리
            gemstone_group.remove(caught_gemstone) # 그룹에서 잡힌 보석 제외
            caught_gemstone = None

    if not caught_gemstone: # 잡힌 보석이 없다면 충돌 체크 
        for gemstone in gemstone_group:
            # if claw.rect.colliderect(gemstone.rect): # 직사각형 기준 충돌 처리
            if pygame.sprite.collide_mask(claw, gemstone): # 투명 영역은 제외하고 실제 이미지 영역에 대해 충돌 처리
                caught_gemstone = gemstone # 잡힌 보석 정보
                to_x = -gemstone.speed # 잡힌 보석의 속도의 - 한 값을 이동 속도로 설정
                break

    if caught_gemstone:
        caught_gemstone.set_position(claw.rect.center, claw.angle)

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))

    gemstone_group.draw(screen) # 그룹 내 모든 스프라이트를 screen에 그림
    claw.update(to_x)
    claw.draw(screen)

    # 점수 정보 보여줌
    display_score()

    # 시간 계산 
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    display_time(total_time - int(elapsed_time)) # 시간 표시 

    # 만약에 시간이 0 이하이면 게임 종료 
    if total_time - int(elapsed_time) <= 0:
        running = False
        game_result = "Game Over"
        display_game_over()
    elif curr_score >= goal_score:
        running = False
        game_result = "Mission Complete"
        display_game_over()
    
    # 게임 종료 메시지 표시

    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()