# snake game

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1920, 1080
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame")

exit_game = False
clock = pygame.time.Clock()

picture = pygame.image.load("pygameimage1.jpg")
picture = pygame.transform.scale(picture, (WIDTH, HEIGHT))

BLOCK_SIZE = 20
FPS = 360

WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

font = pygame.font.SysFont(None, 50)

def draw_score(score):
    return None

def draw_snake(snake_list):
    return None

def move_snake(x, y, direction):
    dx, dy = direction
    x += dx
    y += dy
    return x, y

def check_collision(x, y, snake_list):
    return None

def food_position():
    return None


x = WIDTH // 2
y = HEIGHT // 2

direction = [0, 0]

snake_list = []
snake_length = 1

food_pos = food_position()

while not exit_game:
    canvas.blit(picture, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit_game = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction[0] == 0:
                direction = [-BLOCK_SIZE, 0]
            if event.key == pygame.K_LEFT and direction[0] == 0:
                direction = [BLOCK_SIZE, 0]
            if event.key == pygame.K_LEFT and direction[0] == 0:
                direction = [0, -BLOCK_SIZE]
            if event.key == pygame.K_LEFT and direction[0] == 0:
                direction = [0, BLOCK_SIZE]

    x,y = move_snake(x,y, direction)

    if check_collision(x, y, snake_list):
        x = WIDTH // 2
        y = HEIGHT // 2

        direction = [0, 0]

        snake_list = []
        snake_length = 1

        food_pos = food_position()

    snake_list.append([x, y])

    if [x, y] == food_pos:
        snake_length += 1
        food_pos = food_position()

        
    pygame.display.update()
    clock.tick(3600)

pygame.quit()