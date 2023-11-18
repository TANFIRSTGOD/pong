import pygame

plr1y = 300
plr2y = 300

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
    plr1 = pygame.draw.rect(screen, (255,255,255), rect=(100,plr1y,20,150))
    plr2 = pygame.draw.rect(screen, (255,255,255), rect=(1180,plr2y,20,150))
    ball = pygame.draw.circle(screen, (255,255,255), radius=10, center=(640,360))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        plr1y -= 5
    elif keys[pygame.K_s]:
        plr1y += 5
    elif keys[pygame.K_UP]:
        plr2y -= 5
    elif keys[pygame.K_DOWN]:
        plr2y += 5

    pygame.display.flip()
    clock.tick(60)
pygame.quit()