import os
import pygame
import pyautogui
from random import*

pygame.init() 

# 이미지 클래스
class img(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center = position)

# def setting_img():
#     img_group.add(img(img_lst[0], (200, 400)))
#     img_group.add(img(img_lst[1], (1000, 400)))
#     img_group.add(img(img_lst[2], (200, 400)))
#     img_group.add(img(img_lst[3], (1000, 400)))
#     img_group.add(img(img_lst[4], (200, 400)))
#     img_group.add(img(img_lst[5], (1000, 400)))
#     img_group.add(img(img_lst[6], (200, 400)))


# 화면 크기 설정
screen_width = 1200 # 가로 크기
screen_height = 800 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("이상형 월드컵") 

# 이미지 섞기 
list = range(0, 7)
mix1_img = randint(0, 6)
mix2_img = sample(list, 2)


# FPS
clock = pygame.time.Clock()
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 이미지 리스트 만들기
img_lst = [
    pygame.image.load(os.path.join(current_path, "img1.png")),
    pygame.image.load(os.path.join(current_path, "img2.png")),
    pygame.image.load(os.path.join(current_path, "img3.png")),
    pygame.image.load(os.path.join(current_path, "img4.png")),
    pygame.image.load(os.path.join(current_path, "img5.png")),
    pygame.image.load(os.path.join(current_path, "img6.png")),
    pygame.image.load(os.path.join(current_path, "img7.png"))]

img_group = pygame.sprite.Group()
# setting_img() # 원하는 만큼의 이미지 정의



running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   

    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리

    # 5. 화면에 그리기

    screen.blit(background, (0, 0))
    img_group.draw(screen)

    pygame.display.update() # 게임화면을 다시 그리기
    
pygame.quit()