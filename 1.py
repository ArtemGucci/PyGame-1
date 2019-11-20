import pygame
from math import sqrt
from time import time
from random import randint, choice


def change_deg(ball):
    global x1, y1, x2, y2, h, w
    x, y, d, r = ball[0], ball[1], ball[2], ball[3]
    if x == r and d == 135:
        ball[2] -= 90
    elif x == r and d == 225:
        ball[2] += 90
    elif x == w - r and d == 45:
        ball[2] += 90
    elif x == w - r and d == 315:
        ball[2] -= 90
    if y == r and d == 45:
        ball[2] = 315
    elif y == r and d == 135:
        ball[2] += 90
    if y == y1 - r and x in range(x1, x1 + x2 + 1):
        if d == 225:
            ball[2] -= 90
        elif d == 315:
            ball[2] = 45
    elif (x1 - x)**2 + (y1 - y)**2 <= r**2 or (x1 + x2 - x)**2 + (y1 - y)**2 <= r**2:
        ball[2] = (ball[2] + 180) % 360
        return ball
    if y == h - r:
        return False
    return ball


pygame.init()
w, h = map(int, input().split())
size = width, height = w, h
screen = pygame.display.set_mode(size)
balls = []
running = True
clock = pygame.time.Clock()
start = time()
x1, y1, x2, y2 = w // 2 - 50, h - 10, 100, 10
pygame.mouse.set_visible(False)


while running:
    k = time()
    if k - start >= 15:
        r = randint(10, min(50, h // 4))
        x3 = randint(2 * r, w - 2 * r)
        y3 = randint(r, h // 2)
        balls.append([x3, y3, choice([45, 135, 225, 315]), r])
        pygame.draw.circle(screen, (255, 255, 255), (x3, y3), r)
        start = k
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEMOTION:
            coord = event.pos[0]
            if coord + 100 <= w:
                x1 = coord

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, pygame.Color('red'), (x1, y1, x2, y2))
    for i in range(len(balls)):
        balls[i] = change_deg(balls[i])
        if not balls[i]:
            running = False
            break
        if balls[i][2] == 45:
            balls[i][0] += int(sqrt((clock.tick() / 500)**2 / 2)) + 1
            balls[i][1] -= int(sqrt((clock.tick() / 500)**2 / 2)) + 1
        elif balls[i][2] == 135:
            balls[i][0] -= int(sqrt((clock.tick() / 500) ** 2 / 2)) + 1
            balls[i][1] -= int(sqrt((clock.tick() / 500) ** 2 / 2)) + 1
        elif balls[i][2] == 225:
            balls[i][0] -= int(sqrt((clock.tick() / 500) ** 2 / 2)) + 1
            balls[i][1] += int(sqrt((clock.tick() / 500) ** 2 / 2)) + 1
        else:
            balls[i][0] += int(sqrt((clock.tick() / 500) ** 2 / 2)) + 1
            balls[i][1] += int(sqrt((clock.tick() / 500) ** 2 / 2)) + 1
        pygame.draw.circle(screen, (255, 255, 255), (balls[i][0], balls[i][1]), balls[i][3])
    pygame.display.flip()


pygame.quit()