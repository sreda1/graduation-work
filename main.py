import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 300))

player_x = 200
player_y = 250
player_speed = 5
obstacle_x = random.randint(0, 400)
obstacle_y = 0
obstacle_speed = 3
score = 0
level = 1
level_threshold = 10


font = pygame.font.SysFont('Arial', 20)


running = True
clock = pygame.time.Clock()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed


    obstacle_y += obstacle_speed
    if obstacle_y > 300:
        obstacle_x = random.randint(0, 400)
        obstacle_y = 0
        score += 1
        if score >= level_threshold:
            level += 1
            level_threshold += 10
            obstacle_speed += 1



    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, 20, 20))
    pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle_y, 20, 20))


    score_text = font.render('Score: {}'.format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    level_text = font.render('Level: {}'.format(level), True, (0, 0, 0))
    screen.blit(level_text, (10, 30))

    pygame.display.flip()
    clock.tick(100)

    if player_x < obstacle_x + 20 and player_x + 20 > obstacle_x and player_y < obstacle_y + 20 and player_y + 20 > obstacle_y:
        running = False