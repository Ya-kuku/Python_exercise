import pygame

# 시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60 ,5)

def display_game_screen():
    print("Game Start")

# pos 에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True

# 초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 시작 버튼
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120,screen_height - 120)

# 색깔
BLACK = (0,0,0) # RGB
WHITE = (255,255,255)

# 게임 시작 여부
start = False

# 게임 루프
running = True
while running:
    click_pos = None

    # 이벤트 루프
    for event in pygame.event.get(): # 어떠한 이벤트 발생?
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭
            click_pos = pygame.mouse.get_pos()


    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)

    if start:
        # 게임 화면 표시
        display_game_screen()
    else:
        # 시작 화면 표시
        display_start_screen()

    # 사용자가 클릭한 좌표값이 있다면
    if click_pos:
        check_buttons(click_pos)

    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()
