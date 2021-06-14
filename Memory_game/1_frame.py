import pygame

# 초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

# 게임 루프
running = True
while running:
    # 이벤트 루프
    for event in pygame.event.get(): # 어떠한 이벤트 발생?
        if event.type == pygame.QUIT:
            running = False

# 게임 종료
pygame.quit()
