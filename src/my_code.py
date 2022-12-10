#############################
# Collaborators & Sources: (enter people or resources who/that helped you)
#
# Leo
#
#############################
import time
import pygame

pygame.init()
font_size = 25
font = pygame.font.SysFont("Cooper", font_size)
# bg = pygame.image.load("C:\\Users\\24834\\Desktop\\1\\imagescxk.jpg")
x = 1150
y = 660
x2 = 350
y2 = 660
vy = 0
vx = 0
vx2 = 0
vy2 = 0
hp1 = 100
hp2 = 100
mt = 0
mt2 = 0
damage = 1
cond = True
cond2 = True
DashCD = True
DashCD2 = True
directionR = False
directionR2 = True
stop = True
p1_onhit = False
p2_onhit = False
mad1 = False
mad2 = False
period = time.time()
period2 = time.time()
mad_t1 = 0
mad_t2 = 0
mCD = True
mCD2 = True
h1 = 660
h2 = 660
color1 = 0
color2 = 0
start = input("Game start?: ")
if start != "yes" or "Yes":
    screen = pygame.display.set_mode((284 * 5, 177 * 5))
    bg = pygame.Surface(screen.get_size())
    bg.fill((255, 255, 255))
else:
    exit()
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
figFM = [
    (-30, -3),
    (-38, 1),
    (-38, 5),
    (-38, 13),
    (-78, -3),
    (-70, 1),
    (-70, 5),
    (-70, 13),
]


# class Slime:
#     is_p1 = False
#
#     def __init__(self, is_p1: bool):
#         self.is_p1 = is_p1
#
#     def figure(self, x1, y1, x2, y2):
#         pass
#

def figure(x1, y1, x2, y2):
    global font_size, font
    if hp1 >= 0:
        pygame.draw.rect(screen, (70 + color1 * 2, 160, 230), pygame.Rect(x1, y1, 10, 10))
        for (x, y) in figMR:
            pygame.draw.rect(screen, (1 + color1 * 2, 100, 200), pygame.Rect(x1 + x, y1 + y, 10, 10))
        if mad1:
            for (i, j) in figFM:
                pygame.draw.rect(screen, (1 + color1 * 2, 100, 200), pygame.Rect(x1 + i, y1 + j, 10, 10))
        elif cond:
            if directionR:
                for (a, z) in figFL:
                    pygame.draw.rect(screen, (1 + color1 * 2, 100, 200), pygame.Rect(x1 + a, y1 + z, 10, 10))
            else:
                for (a, z) in figFR:
                    pygame.draw.rect(screen, (1 + color1 * 2, 100, 200), pygame.Rect(x1 + a, y1 + z, 10, 10))
        else:
            for (c, d) in figFH:
                pygame.draw.rect(screen, (1 + color1 * 2, 100, 200), pygame.Rect(x1 + c, y1 + d, 8, 8))
        font_size = 25
        font = pygame.font.SysFont("Cooper", font_size)
        pygame.draw.rect(screen, (1 + color1 * 2, 50, 150), pygame.Rect(x1 - 100, y1 + 40, 100, 6))
        text1 = font.render(f"p1", True, (1, 100, 200))
        screen.blit(text1, (x1 - 60, y1 - 70))
    else:
        font_size = 200
        font = pygame.font.SysFont("Cooper", font_size)
        text3 = font.render("p2 wins", True, (200, 120, 50))
        screen.blit(text3, (300, 100))
        print("p2 won")
    if hp2 >= 0:
        font_size = 25
        font = pygame.font.SysFont("Cooper", font_size)
        text2 = font.render(f"p2", True, (230, 160, 70))
        screen.blit(text2, (x2 - 60, y2 - 70))
        pygame.draw.rect(screen, (200 + color2, 120, 50), pygame.Rect(x2, y2, 10, 10))
        for (x, y) in figMR:
            pygame.draw.rect(screen, (200 + color2, 120, 50), pygame.Rect(x2 + x, y2 + y, 10, 10))
        if mad2:
            for (i, j) in figFM:
                pygame.draw.rect(screen, (200 + color2, 120, 50), pygame.Rect(x2 + i, y2 + j, 10, 10))
        elif cond2:
            if directionR2:
                for (a, z) in figFL:
                    pygame.draw.rect(screen, (200 + color2, 120, 50), pygame.Rect(x2 + a, y2 + z, 10, 10))
            else:
                for (a, z) in figFR:
                    pygame.draw.rect(screen, (200 + color2, 120, 50), pygame.Rect(x2 + a, y2 + z, 10, 10))

        else:
            for (c, d) in figFH:
                pygame.draw.rect(screen, (200 + color2, 120, 50), pygame.Rect(x2 + c, y2 + d, 8, 8))
        pygame.draw.rect(screen, (200 + color2, 120, 50), pygame.Rect(x2 - 100, y2 + 40, 100, 6))
    else:
        font_size = 200
        font = pygame.font.SysFont("Cooper", font_size)
        text4 = font.render("p1 wins", True, (1, 100, 200))
        screen.blit(text4, (300, 100))
        print("p1 won")

    health_bar()
    pygame.display.update()


def dust(x1, y1):
    for (x, y) in dusty:
        pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(x1 + x, y1 + y, 5, 5))


def detect_keyboard():
    pass


def pvp():
    global hp2, hp1, p1_onhit, p2_onhit, vx, vy, x2, x, cond, cond2, vx2
    if (x2 - 125 <= x - 125 <= x2 + 10 or x2 - 125 <= x + 10 <= x2 + 10) \
            and (y2 - 30 <= y + 30 <= y2 + 30 or y2 - 30 <= y - 30 <= y2 + 30):
        if p1_onhit:
            hp2 -= 1
            vx2 = 0
            cond2 = False
        if p2_onhit:
            hp1 -= 1
            vx = 0
            cond = False
        if x >= x2:
            x2 -= 6
            x += 6
        elif x <= x2:
            x2 += 6
            x -= 6


def platform():
    global h1, h2
    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(400, 550, 600, 5))
    pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(400, 555, 600, 145))
    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(0, 350, 200, 5))
    pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(0, 355, 200, 345))
    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(284 * 5 - 200, 350, 200, 5))
    pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(284 * 5 - 200, 355, 200, 345))
    if (400 < x and x - 110 < 1000) and y <= 510:
        h1 = 510
    elif (x - 100 < 200 or x > 284 * 5 - 200) and y <= 320:
        h1 = 310
    else:
        h1 = 660
    if (400 < x2 and x2 - 110 < 1000) and y2 <= 510:
        h2 = 510
    elif (x2 - 100 < 200 or x2 > 284 * 5 - 200) and y2 <= 320:
        h2 = 310
    else:
        h2 = 660


def acc(v):
    if v > 0:
        v -= v * (0.1 / v)
        if v < 0:
            v = 0
    elif v < 0:
        v += v * (0.1 / v)
        if v > 0:
            v = 0
    return v


def health_bar():
    global font_size, font
    font_size = 25
    font = pygame.font.SysFont("Cooper", font_size)
    th = font.render(f"p2", True, (200, 200, 200))
    screen.blit(th, (40, 40))
    pygame.draw.rect(screen, (255, 50, 50), pygame.Rect(70, 40, 3 * hp2, 15))
    th = font.render(f"p1", True, (200, 200, 200))
    screen.blit(th, (284 * 5 - 65, 40))
    pygame.draw.rect(screen, (255, 50, 50), pygame.Rect(284 * 5 - 75 - 3 * hp1, 40, 3 * hp1, 15))


while True:
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(0, 700, 1600, 5))
    platform()
    if mad1:
        p1_onhit = True
        color1 = 50
        if time.time() - mad_t1 > 3:
            mad1 = False
            mt = time.time()

    else:
        p1_onhit = False
        color1 = 0
    if not mad1 and not mCD:
        if time.time() - mt > 6:
            mCD = True

    if mad2:
        p2_onhit = True
        color2 = 50
        if time.time() - mad_t2 > 3:
            mad2 = False
            mt2 = time.time()

    else:
        p2_onhit = False
        color2 = 0
    if not mad2 and not mCD2:
        if time.time() - mt2 > 6:
            mCD2 = True

    print(mCD)
    pvp()
    figure(x, y, x2, y2)

    pygame.display.flip()
    if time.time() - period > 4:
        DashCD = True
        period = time.time()
    if time.time() - period2 > 4:
        DashCD2 = True
        period2 = time.time()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_m and mCD:
                mad1 = True
                mad_t1 = time.time()
                mCD = False
            if e.key == pygame.K_f and mCD2:
                mad2 = True
                mad_t2 = time.time()
                mCD2 = False

    pressed = pygame.key.get_pressed()

    # f1m>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if pressed[pygame.K_LEFT]:
        directionR = False
        if vx > -6:
            vx -= 0.15
    if pressed[pygame.K_RIGHT]:
        directionR = True
        if vx < 6:
            vx += 0.15
    if pressed[pygame.K_UP]:
        if not y < h1:
            vy = -4
        cond = True
    if pressed[pygame.K_DOWN]:
        vy = 4
        if h1 != 660:
            h1 = 660
        dust(x, y)

    if pressed[pygame.K_RSHIFT] and DashCD:
        DashCD = False
        if directionR:
            vx = 6
        else:
            vx = -6
        vy = -5

    # f2m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if pressed[pygame.K_a]:
        if vx2 > -6:
            vx2 -= 0.15
        directionR2 = False
    if pressed[pygame.K_d]:
        directionR2 = True
        if vx2 < 6:
            vx2 += 0.15
    if pressed[pygame.K_w]:
        if not y2 < h2:
            vy2 = -4
        cond2 = True
    if pressed[pygame.K_s]:
        vy2 = 4
        if h2 != 660:
            h2 = 660

    if pressed[pygame.K_LSHIFT] and DashCD2:
        DashCD2 = False
        if directionR2:
            vx2 = 6
        else:
            vx2 = -6
        vy2 = -5

    # >>>>>>>>>>>>>>>>>>>>>>>>
    y = min(h1, y + vy)
    if y < h1:
        if vy == 0:
            vy = 0.04
        vy += vy * (0.04 / vy)
    y2 = min(h2, y2 + vy2)
    if y2 < h2:
        if vy2 == 0:
            vy2 = 0.04
        vy2 += vy2 * (0.04 / vy2)

    vx = acc(vx)
    vx2 = acc(vx2)
    x2 += vx2
    x += vx

    # >>>>>>>>>>>>>>>>>>>>
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
