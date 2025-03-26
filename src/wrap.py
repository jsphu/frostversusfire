import pygame

pygame.init()

exec(f"flags = pygame.NOFRAME | pygame.RESIZABLE")

screen = pygame.display.set_mode((100,100), flags)

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
        if event == pygame.K_q:
            pygame.quit()

    screen.fill((255,255,255))
