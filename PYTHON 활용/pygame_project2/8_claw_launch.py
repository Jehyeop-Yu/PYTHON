# 집게 발사
# 현재 위치로부터 집게를 쭉 뻗는 동작
# 화면 밖으로 뻗어나가면 다시 돌아오도록 처리 
# 뻗을 때 속도, 돌아올 때 속도 적용

import pygame
import os

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
        
        offset_rotatied = self.offset.rotate(self.angle) # (각도)에따른 변화된 offset값을 받아온다.

        self.rect = self.image.get_rect(center = self.position + offset_rotatied)
        # pygame.draw.rect(screen, RED, self.rect, 1) # 기존 이미지 회전에 따른 새로운 이미지 변화 시각적으로 보기

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
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center = position)

def setup_gemstone():
    # 작은금
    small_gold = Gemstone(gemstone_images[0], (200, 380)) # 0번재 이미지를 (200, 300) 위치에 
    gemstone_group.add(small_gold) # 그룹에 추가
    # 큰금
    gemstone_group.add(Gemstone(gemstone_images[1] , (300, 500)))
    # 돌
    gemstone_group.add(Gemstone(gemstone_images[2] , (300, 380)))
    # 다이아몬드
    gemstone_group.add(Gemstone(gemstone_images[3] , (900, 420)))



pygame.init() 
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner") 

clock = pygame.time.Clock()

# 게임 관련 변수 
default_offset_x_claw = 40 # 중심점으로부터 집게까지의 기본 x 간격
to_x = 0 # x 좌표 기준으로 집게 이미지를 이동시킬 값 저장 변수 

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
    pygame.image.load(os.path.join(current_path, "small_gold.png")), # 작은금
    pygame.image.load(os.path.join(current_path, "big_gold.png")), # 큰금
    pygame.image.load(os.path.join(current_path, "stone.png")), # 돌
    pygame.image.load(os.path.join(current_path, "diamond.png"))] # 다이아몬드

# 보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone() # 게임에 원하는 만큼의 보석을 정의 

# 집게
claw_image = pygame.image.load(os.path.join(current_path, "claw.png"))
claw = Claw(claw_image, (screen_width // 2 , 110)) # 화면 가로 기준 절반, 위에서 110 픽셀 

running = True
while running:
    dt = clock.tick(30) # FPS값 30으로 고정 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN: # 마우스 버튼 누를 때 집게를 뻗음
            claw.set_direction(STOP) # 좌우 멈춤
            to_x = move_speed # move_speed 만큼 빠르게 뻗는다.

    if claw.rect.left < 0 or claw.rect.right > screen_width or claw.rect.bottom > screen_height: # screen 밖을 벗어나려 할때 돌아오는 결계값 처리
        to_x = -return_speed
    
    if claw.offset.x < default_offset_x_claw: # 원위치에 오면 
        to_x = 0
        claw.set_init_state() # 처음 상태로 되돌림

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))

    gemstone_group.draw(screen) # 그룹 내 모든 스프라이트를 screen에 그림
    claw.update(to_x)
    claw.draw(screen)

    pygame.display.update()

pygame.quit()