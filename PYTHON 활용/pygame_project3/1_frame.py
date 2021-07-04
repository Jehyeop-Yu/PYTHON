# 기본 틀 
import pygame

pygame.init() 
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(30) # FPS값 30으로 고정 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()