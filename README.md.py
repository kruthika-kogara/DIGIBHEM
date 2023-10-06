import pygame
import sys
import random

pygame.init()
     
WIDTH, HEIGHT = 800, 700
GRID_SIZE = 10
GRID_WIDTH = WIDTH//GRID_SIZE
GRID_HEIGHT = HEIGHT//GRID_SIZE
FPS = 15

WHITE = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

snake = [(20, 20)]
snake_direction = (0, 0)

food = (random.randint(0, GRID_WIDTH- 1),random.randint(0, GRID_HEIGHT- 1))

game_over=False

clock = pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, 1):
        snake_direction = (0, -1)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -1):
        snake_direction = (0, 1)
    elif keys[pygame.K_LEFT] and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
        snake_direction = (1, 0)
 
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    
    if new_head == food:
        print('snake:',len(snake))
        snake.insert(0, food)
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.insert(0, new_head)
        snake.pop()
  
    if (
        new_head[0] < 0
        or new_head[0] >= GRID_WIDTH
        or new_head[1] < 0
        or new_head[1] >= GRID_HEIGHT
        or new_head in snake[1:]
    ):
        game_over = True
    
    screen.fill(WHITE)
   
    pygame.draw.rect(screen, RED, pygame.Rect(food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
   
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
   
    clock.tick(FPS)

     #to restart game
    def restart_game():
     restart_game()

pygame.quit()
sys.exit()
