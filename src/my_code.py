#############################
# Collaborators & Sources: (enter people or resources who/that helped you)
# 
#
#
#############################
import time

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
x = 1000
y = 660
x2 = 300
y2 = 660
vy = 0
vx = float(600)
vy2 = 0
cond = True
cond2 = True
DashCD = True
directionR = False
directionR2 = True
stop = False
period = time.time()
figMR = [
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
figFR = [
    (-40, 0),
    (-40, 10),
    (-80, 0),
    (-80, 10)
]
figFL = [
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
dusty = [
    (10, 30),
    (20, 40),
    (-110, 30),
    (-120, 40)
]
# rand_x, rand_y = random.randint(-100, 100), random.randint(-100, 100)

pygame.key.set_repeat(100, 5)


def figure(x1, y1, x2, y2):
    pygame.draw.rect(screen, (70, 160, 230), pygame.Rect(x1, y1, 10, 10))
    for (x, y) in figMR:
        pygame.draw.rect(screen, (1, 100, 200), pygame.Rect(x1 + x, y1 + y, 10, 10))
    if cond:
        if directionR:
            for (a, z) in figFL:
                pygame.draw.rect(screen, (1, 100, 200), pygame.Rect(x1 + a, y1 + z, 10, 10))
        else:
            for (a, z) in figFR:
                pygame.draw.rect(screen, (1, 100, 200), pygame.Rect(x1 + a, y1 + z, 10, 10))
    else:
        for (c, d) in figFH:
            pygame.draw.rect(screen, (1, 100, 200), pygame.Rect(x1 + c, y1 + d, 8, 8))
    pygame.draw.rect(screen, (1, 50, 150), pygame.Rect(x1 - 100, y1 + 40, 100, 6))
    pygame.draw.rect(screen, (230, 160, 70), pygame.Rect(x2, y2, 10, 10))
    for (x, y) in figMR:
        pygame.draw.rect(screen, (230, 160, 70), pygame.Rect(x2 + x, y2 + y, 10, 10))
    if cond2:
        if directionR2:
            for (a, z) in figFL:
                pygame.draw.rect(screen, (230, 160, 70), pygame.Rect(x2 + a, y2 + z, 10, 10))
        else:
            for (a, z) in figFR:
                pygame.draw.rect(screen, (230, 160, 70), pygame.Rect(x2 + a, y2 + z, 10, 10))
    else:
        for (c, d) in figFH:
            pygame.draw.rect(screen, (230, 160, 70), pygame.Rect(x2 + c, y2 + d, 8, 8))
    pygame.draw.rect(screen, (230, 160, 70), pygame.Rect(x2 - 100, y2 + 40, 100, 6))
    pygame.display.update()


def dust(x1, y1):
    for (x, y) in dusty:
        pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(x1 + x, y1 + y, 5, 5))


def detect_keyboard():
    pass


while True:
    screen.blit(bg, (0, 0))
    text = font.render("shabi", True, (0, 0, 0))
    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(0, 700, 1600, 5))
    figure(x, y, x2, y2)
    pygame.display.flip()
    if time.time() - period > 4:
        DashCD = True
        period = time.time()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYDOWN:
            pass
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        vx -= 2
        directionR = False
    if pressed[pygame.K_RIGHT]:
        directionR = True
        vx += 2
    if pressed[pygame.K_UP] and cond:
        if not y < 660:
            vy = -4
    else:
        cond = True
    if pressed[pygame.K_DOWN]:
        vy = 4
        dust(x, y)
    if pressed[pygame.K_a]:
        x2 -= 4
        directionR2 = False
    if pressed[pygame.K_d]:
        directionR2 = True
        x2 += 4
    if pressed[pygame.K_w]:
        if not y2 < 660:
            vy2 = -4
        cond2 = True
    if pressed[pygame.K_s]:
        vy2 = 4

    if pressed[pygame.K_LSHIFT] and DashCD:
        DashCD = False
        if directionR:
            vx += 4
            vy = -3
        else:
            vx -= 4
            vy = -3
    y = min(660, y + vy)
    if y < 660:
        if vy == 0:
            vy = 0.04
        vy += vy * (0.04 / vy)
    y2 = min(660, y2 + vy2)
    if y2 < 660:
        if vy2 == 0:
            vy2 = 0.04
        vy2 += vy2 * (0.04 / vy2)
    x = vx
    if pressed[pygame.K_LEFT]:
        vx += vx * (0.5 / vx)
    elif pressed[pygame.K_RIGHT]:
        vx -= vx * (0.5 / vx)
    if x < -20:
        x = 300 * 5
    elif x > 310 * 5:
        x = 0
    if x2 < -20:
        x2 = 300 * 5
    elif x2 > 310 * 5:
        x2 = 0
    pygame.display.update()
    detect_keyboard()
