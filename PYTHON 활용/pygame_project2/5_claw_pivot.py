# 집게 어느 지접(pivot, 중심점)으로 부터 떨어트려서 배치하는 것
import pygame
import os

# 집게 클래스 
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center = position)

        self.offset = pygame.math.Vector2(default_offset_x_claw, 0)
        self.position = position

    def update(self):
        rect_center = self.position + self.offset
        self.rect = self.image.get_rect(center = rect_center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.circle(screen, RED, self.position, 3) # 중심점 표시

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

# 색깔 변수 
RED = (255, 0, 0)

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

    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))

    gemstone_group.draw(screen) # 그룹 내 모든 스프라이트를 screen에 그림
    claw.update()
    claw.draw(screen)

    pygame.display.update()

pygame.quit()