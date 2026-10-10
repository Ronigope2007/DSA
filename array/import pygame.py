import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (135, 206, 235)
YELLOW = (255, 255, 0)

bird = pygame.Rect(80, 250, 30, 30)
velocity = 0
gravity = 0.5
jump = -8

pipes = []
pipe_width = 60
gap = 170
pipe_speed = 4

score = 0
font = pygame.font.SysFont(None, 40)

def new_pipe():
    top = random.randint(80, 350)
    return [
        pygame.Rect(WIDTH, 0, pipe_width, top),
        pygame.Rect(WIDTH, top + gap, pipe_width, HEIGHT),
    ]

pipes.extend(new_pipe())

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity = jump

    velocity += gravity
    bird.y += int(velocity)

    if pipes[0][0].x < WIDTH - 220:
        pipes.extend(new_pipe())

    for pair in pipes:
        pair[0].x -= pipe_speed
        pair[1].x -= pipe_speed

    if pipes and pipes[0][0].right < 0:
        pipes.pop(0)
        score += 1

    for pair in pipes:
        if bird.colliderect(pair[0]) or bird.colliderect(pair[1]):
            running = False

    if bird.top <= 0 or bird.bottom >= HEIGHT:
        running = False

    screen.fill(BLUE)

    pygame.draw.ellipse(screen, YELLOW, bird)

    for pair in pipes:
        pygame.draw.rect(screen, GREEN, pair[0])
        pygame.draw.rect(screen, GREEN, pair[1])

    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()