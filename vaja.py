# snake game

"""
#2. dodatna naloga:
#naredi branch "multiplayer"
#v tem branchu naredi logiko, da sta na zacetku igre 2 kaci, ena se upravlja z wasd, druga z gumbi s puscicami
#ce se aca zabije vase, v drugo kaco ali v steno, izgubi

#3. dodatna naloga
#naredi merge obeh branchov 
"""
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1920, 1080
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

exit_game = False
clock = pygame.time.Clock()

picture = pygame.image.load("pygameimage1.jpg")
picture = pygame.transform.scale(picture, (WIDTH, HEIGHT))

BLOCK_SIZE = 20
FPS = 30

WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)

snake1_color = GREEN
snake2_color = BLUE

font = pygame.font.SysFont(None, 50)

def draw_snake(snake_list, color):
    
    for block in snake_list:
        pygame.draw.rect(canvas, color, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def move_snake(x, y, direction):
    dx, dy = direction
    x += dx
    y += dy
    return x, y

def check_collision(x, y, snake_list, other_snake_list):

    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return True

    for block in snake_list[:-1]:
        if block == [x, y]:
            return True

    for block in other_snake_list:
        if block == [x, y]:
            return True
        
    return False

def food_position(snake1_list, snake2_list):
    while True:
        position = [
            random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE),
            random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
        ]
        if position not in snake1_list and position not in snake2_list:
            return position

def game_over_screen(loser):
    waiting = True
    while waiting:
        canvas.fill((0, 0, 0))
        text_lose = font.render(f"Player {loser} lost!", True, RED)
        text_restart = font.render("Press R to restart", True, WHITE)
        text_quit = font.render("Press Q to quit", True, WHITE)
        canvas.blit(text_lose, (WIDTH // 2 - text_lose.get_width() // 2, HEIGHT // 2 - 100))
        canvas.blit(text_restart, (WIDTH // 2 - text_restart.get_width() // 2, HEIGHT // 2))
        canvas.blit(text_quit, (WIDTH // 2 - text_quit.get_width() // 2, HEIGHT // 2 + 100))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"
                if event.key == pygame.K_q:
                    return "quit"

x1, y1 = WIDTH // 4, HEIGHT // 2
direction1 = [0, 0]
snake1_list = []
snake1_length = 1

x2, y2 = 3 * WIDTH // 4, HEIGHT // 2
direction2 = [0, 0]
snake2_list = []
snake2_length = 1

food_pos = food_position(snake1_list, snake2_list)

score1 = 0
score2 = 0

while not exit_game:
    canvas.blit(picture, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit_game = True

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a and direction1[0] == 0:
                direction1 = [-BLOCK_SIZE, 0]
            if event.key == pygame.K_d and direction1[0] == 0:
                direction1 = [BLOCK_SIZE, 0]
            if event.key == pygame.K_w and direction1[1] == 0:
                direction1 = [0, -BLOCK_SIZE]
            if event.key == pygame.K_s and direction1[1] == 0:
                direction1 = [0, BLOCK_SIZE]

            if event.key == pygame.K_LEFT and direction2[0] == 0:
                direction2 = [-BLOCK_SIZE, 0]
            if event.key == pygame.K_RIGHT and direction2[0] == 0:
                direction2 = [BLOCK_SIZE, 0]
            if event.key == pygame.K_UP and direction2[1] == 0:
                direction2 = [0, -BLOCK_SIZE]
            if event.key == pygame.K_DOWN and direction2[1] == 0:
                direction2 = [0, BLOCK_SIZE]

            if event.key == pygame.K_SPACE:
                snake1_color = tuple(random.randint(0,255) for _ in range(3))

    x1, y1 = move_snake(x1, y1, direction1)
    x2, y2 = move_snake(x2, y2, direction2)

    if check_collision(x1, y1, snake1_list, snake2_list):
        action = game_over_screen(loser=1)
        if action == "quit":
            exit_game = True
            break
        elif action == "restart":
            x1, y1, direction1, snake1_list, snake1_length, score1 = WIDTH // 4, HEIGHT // 2, [0,0], [], 1, 0
            x2, y2, direction2, snake2_list, snake2_length, score2 = 3*WIDTH//4, HEIGHT//2, [0,0], [], 1, 0
            food_pos = food_position(snake1_list, snake2_list)

    if check_collision(x2, y2, snake2_list, snake1_list):
        action = game_over_screen(loser=2)
        if action == "quit":
            exit_game = True
            break
        elif action == "restart":
            x1, y1, direction1, snake1_list, snake1_length, score1 = WIDTH // 4, HEIGHT // 2, [0,0], [], 1, 0
            x2, y2, direction2, snake2_list, snake2_length, score2 = 3*WIDTH//4, HEIGHT//2, [0,0], [], 1, 0
            food_pos = food_position(snake1_list, snake2_list)

    snake1_list.append([x1, y1])
    snake2_list.append([x2, y2])

    if len(snake1_list) > snake1_length:
        del snake1_list[0]
    if len(snake2_list) > snake2_length:
        del snake2_list[0]

    if [x1, y1] == food_pos:
        snake1_length += 1
        score1 += snake1_length
        food_pos = food_position(snake1_list, snake2_list)
    if [x2, y2] == food_pos:
        snake2_length += 1
        score2 += snake2_length
        food_pos = food_position(snake1_list, snake2_list)

    pygame.draw.rect(canvas, RED, [food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE])
    draw_snake(snake1_list, snake1_color)
    draw_snake(snake2_list, snake2_color)

    score_text1 = font.render(f"P1: {score1}", True, WHITE)
    score_text2 = font.render(f"P2: {score2}", True, WHITE)
    canvas.blit(score_text1, (50, 50))
    canvas.blit(score_text2, (50, 100))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()