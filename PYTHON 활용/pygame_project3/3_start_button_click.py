# 스타트 버튼 만들기 
import pygame

# 원그리기 
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 흰색으로 동그라미를 그리는데 중심좌표는 start_button의 좌표를 따라가고,
    # 반지름은 60, 두께는 5

# 게임 화면보여주기 
def display_game_screen():
    print("Game Start")

def check_buttons(pos):
    global start 
    if start_button.collidepoint(pos): # 클릭한 위치가 pos 안에 있는지 확인
        start = True

pygame.init() 
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 시작 버튼 
start_button =  pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

# 색깔
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 게임 시작 여부 
start = False

running = True
while running:
    click_pos = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭 했을 때
            click_pos = pygame.mouse.get_pos() # 클릭한 위치 값 가져오기
            print(click_pos)

    # 화면 전체를 까맣게 칠하기
    screen.fill(BLACK)

    if start: # 게임 화면 표시
        display_game_screen()
    else:
        display_start_screen() # 시작 원 표시

    # 사용자가 클릭한 좌표값이 있다면 (어딘가 클릭했다면)
    if click_pos:
        check_buttons(click_pos)


    # 화면 업데이트
    pygame.display.update()

pygame.quit()