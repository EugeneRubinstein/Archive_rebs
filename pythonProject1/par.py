import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Параметры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Параметры змейки
snake_speed = 15
snake_size = 10
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Параметры яблока
apple_pos = [random.randrange(1, screen_width//10)*10, random.randrange(1, screen_height//10)*10]
apple_size = 10

# Параметры игры
game_over = False
direction = 'RIGHT'
change_to = direction

# Основной цикл игры
while  game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Изменение направления змейки
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Изменение позиции змейки
    if direction == 'UP':
        snake_pos[1] -= snake_size
    elif direction == 'DOWN':
        snake_pos[1] += snake_size
    elif direction == 'LEFT':
        snake_pos[0] -= snake_size
    elif direction == 'RIGHT':
        snake_pos[0] += snake_size

    # Проверка столкновения змейки с границами экрана
    if snake_pos[0] < 0 or snake_pos[0] > screen_width - snake_size:
        game_over = True
    elif snake_pos[1] < 0 or snake_pos[1] > screen_height - snake_size:
        game_over = True

    # Проверка столкновения змейки с собой
    snake_body.insert(0, list(snake_pos))
    if snake_body[0] in snake_body[1:]:
        game_over = True

    # Проверка столкновения змейки с яблоком
    if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
        apple_pos = [random.randrange(1, screen_width//10)*10, random.randrange(1, screen_height//10)*10]
    else:
        snake_body.pop()

    # Отрисовка змейки и яблока
    screen.fill((0, 0, 0))
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], snake_size, snake_size))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(apple_pos[0], apple_pos[1], apple_size, apple_size))
    pygame.display.flip()

    # Задержка
    pygame.time.delay(snake_speed)

# Завершение игры
pygame.quit()
sys.exit()