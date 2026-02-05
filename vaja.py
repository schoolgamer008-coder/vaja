# snake game

import pygame

pygame.init()

WIDTH, HEIGHT = 1920, 1080
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame")

exit_game = False
clock = pygame.time.Clock()

picture = pygame.image.load("pygameimage1.jpg")
picture = pygame.transform.scale(picture, (WIDTH, HEIGHT))

while not exit_game:
    canvas.blit(picture, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True


    pygame.display.update()
    clock.tick(3600)

pygame.quit()