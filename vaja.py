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
FPS = 10

WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

font = pygame.font.SysFont(None, 50)

def draw_score(score):
    return None

def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(canvas, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def move_snake(x, y, direction):
    dx, dy = direction
    x += dx
    y += dy
    return x, y

def check_collision(x, y, snake_list):
    if x<0 or x>= WIDTH:
        return True
    
    if y<0 or y>= HEIGHT:
        return True
    
    for block in snake_list[:-1]:
        if block == [x,y]:
            return True
        
    return False

def food_position():
    return [random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE),
            random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)]


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
            if event.key == pygame.K_RIGHT and direction[0] == 0:
                direction = [BLOCK_SIZE, 0]
            if event.key == pygame.K_UP and direction[1] == 0:
                direction = [0, -BLOCK_SIZE]
            if event.key == pygame.K_DOWN and direction[1] == 0:
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
    if len(snake_list) > snake_length:
        del snake_list[0]

    if [x, y] == food_pos:
        snake_length += 1
        food_pos = food_position()

    pygame.draw.rect(canvas, RED, [food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE])
    draw_snake(snake_list)


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()