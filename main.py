import pygame, math
from pygame.locals import *

pygame.init()

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
WHITE = (255, 255, 255)
BLACK =  (0, 0, 0)

x_offset = WINDOW_WIDTH / 2
y_offset = WINDOW_HEIGHT / 2

circle_radius = 40
torus_radius = 100
A, B = 0, 0


def draw(x, y):
    pygame.draw.circle(screen, WHITE, (x + x_offset, y + y_offset), 1)

while True:
    screen.fill((BLACK))
    cosB, sinB = math.cos(B), math.sin(B)
    cosA, sinA = math.cos(A), math.sin(A)

    for T in range(0, 628, 40):
        cosT, sinT = math.cos(T/100), math.sin(T/100)
        x2 = torus_radius + circle_radius * cosT
        y2 = circle_radius * sinT

        for P in range(0, 628, 15):
            cosP, sinP = math.cos(P/100), math.sin(P/100)
            x = circle_radius * sinB * sinT + cosB  * cosP * x2
            y = -cosA * sinB * cosP * x2 + circle_radius * cosB * sinT - sinA * sinP * x2
            draw(x, y)

    if A != 2:
        A += 0.001
        B += 0.002
    else:
        A = 0
        B = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()

