import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("PONG")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    plr1 = pygame.draw.rect(screen, (255,255,255), rect=(100,300,20,150))
    plr2 = pygame.draw.rect(screen, (255,255,255), rect=(1180,300,20,150))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()