#############################
# Collaborators & Sources: (enter people or resources who/that helped you)
# 
#
#
#############################

# Write code here:

import pygame
import random

pygame.init()
# bg = pygame.image.load("C:\\Users\\24834\\Desktop\\1\\imagescxk.jpg")
screen = pygame.display.set_mode((284 * 5, 177 * 5))
bg = pygame.Surface(screen.get_size())
bg.fill((255, 255, 255))
font_size = 150
font = pygame.font.SysFont("Arial", font_size)
x = 300
y = 660
vy = 0
cond = True
figM = [
    (10, 10),
    (10, 20),
    (0, 30),
    (-10, -10),
    (-20, -20),
    (-30, -20),
    (-40, -30),
    (-50, -30),
    (-60, -30),
    (-70, -30),
    (-80, -30),
    (-90, -20),
    (-100, -20),
    (-110, -10),
    (-120, 0),
    (-120, 10),
    (-120, 20),
    (-110, 30),
]
figF = [
    (-30, 0),
    (-30, 10),
    (-70, 0),
    (-70, 10)
]
figFH = [
    (-30, 0),
    (-38, 8),
    (-30, 16),
    (-80, 0),
    (-72, 8),
    (-80, 16)
]
rand_x, rand_y = random.randint(-100, 100), random.randint(-100, 100)

pygame.key.set_repeat(100, 5)


def figure(x1, y1):

    pygame.draw.rect(screen, (70, 160, 230), pygame.Rect(x1, y1, 10, 10))
    for (x, y) in figM:
        pygame.draw.rect(screen, (1, 100, 200), pygame.Rect(x1 + x, y1 + y, 10, 10))
    if cond:
        for (a, z) in figF:
            pygame.draw.rect(screen, (1, 100, 200), pygame.Rect(x1 + a, y1 + z, 10, 10))
    else:
        for (c, d) in figFH:
            pygame.draw.rect(screen, (1, 100, 200), pygame.Rect(x1 + c, y1 + d, 8, 8))
    pygame.draw.rect(screen, (1, 50, 150), pygame.Rect(x1 - 100, y1 + 40, 100, 6))
    pygame.display.update()


while True:
    screen.blit(bg, (0, 0))
    text = font.render("shabi", True, (0, 0, 0))
    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(0, 700, 1600, 5))
    figure(x, y)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYDOWN:
            # if e.key == pygame.K_SPACE:
            #     b = not b
            #     x += rand_x
            #     y += rand_y
            #     rand_x = random.randint(-300, 300)
            #     rand_y = random.randint(-300, 300)
            if e.key == pygame.K_LEFT:
                x -= 4
            if e.key == pygame.K_RIGHT:
                x += 4
            if e.key == pygame.K_UP:
                if not y < 660:
                    vy = -4
            if e.key == pygame.K_DOWN:
                cond = not cond
            if e.key == pygame.K_LSHIFT:
                cond = not cond
        if e.type == pygame.MOUSEBUTTONDOWN:
            print(e.button)
            if e.button == 1:
                pass
                # b = not b
                # x = 600
                # y = 300
    # if b:
    #     figure(x, y, 1)
    y = min(660, y + vy)
    if y < 660:
        if vy == 0:
            vy = 0.02
        vy += vy * (0.03/vy)
    pygame.display.update()
