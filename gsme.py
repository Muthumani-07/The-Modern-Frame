import pygame
import random
import sys

pygame.init()

# Screen settings
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Racing Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
blue = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Car settings
car_width = 50
car_height = 80
car_x = width // 2 - car_width // 2
car_y = height - car_height - 10
car_speed = 5

# Enemy car settings
enemy_width = 50
enemy_height = 80
enemy_x = random.randint(0, width - enemy_width)
enemy_y = -enemy_height
enemy_speed = 5

# Score
score = 0
font = pygame.font.SysFont("comicsansms", 30)

def show_score(score):
    text = font.render(f"Score: {score}", True, white)
    screen.blit(text, (10, 10))

# Game loop
running = True
while running:
    screen.fill(gray)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key press
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < width - car_width:
        car_x += car_speed

    # Move enemy car
    enemy_y += enemy_speed

    # Respawn enemy car
    if enemy_y > height:
        enemy_y = -enemy_height
        enemy_x = random.randint(0, width - enemy_width)
        score += 1
        enemy_speed += 0.5  # Increase difficulty

    # Draw player car
    pygame.draw.rect(screen, blue, (car_x, car_y, car_width, car_height))

    # Draw enemy car
    pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_width, enemy_height))

    # Check collision
    player_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

    if player_rect.colliderect(enemy_rect):
        screen.fill(black)
        game_over_text = font.render("GAME OVER!", True, red)
        screen.blit(game_over_text, (width // 2 - 80, height // 2 - 20))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    show_score(score)
    pygame.display.update()
    clock.tick(60)