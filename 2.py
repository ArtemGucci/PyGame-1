import pygame
from math import sqrt


def change_deg(ball):
    x, y, d = ball[0], ball[1], ball[2]
    if x == 10 and d == 135:
        ball[2] -= 90
    elif x == 10 and d == 225:
        ball[2] += 90
    elif x == 790 and d == 45:
        ball[2] += 90
    elif x == 790 and d == 315:
        ball[2] -= 90
    if y == 10 and d == 45:
        ball[2] = 315
    elif y == 10 and d == 135:
        ball[2] += 90
    elif y == 790 and d == 315:
        ball[2] = 45
    elif y == 790 and d == 225:
        ball[2] = 135
    return ball


pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
balls = []


running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append([event.pos[0], event.pos[1], 135])
            pygame.draw.circle(screen, (255, 255, 255), event.pos, 10)
    screen.fill((0, 0, 0))
    for i in range(len(balls)):
        balls[i] = change_deg(balls[i])
        if balls[i][2] == 45:
            balls[i][0] += int(sqrt((clock.tick() / 10)**2 / 2)) + 1
            balls[i][1] -= int(sqrt((clock.tick() / 10)**2 / 2)) + 1
        elif balls[i][2] == 135:
            balls[i][0] -= int(sqrt((clock.tick() / 10) ** 2 / 2)) + 1
            balls[i][1] -= int(sqrt((clock.tick() / 10) ** 2 / 2)) + 1
        elif balls[i][2] == 225:
            balls[i][0] -= int(sqrt((clock.tick() / 10) ** 2 / 2)) + 1
            balls[i][1] += int(sqrt((clock.tick() / 10) ** 2 / 2)) + 1
        else:
            balls[i][0] += int(sqrt((clock.tick() / 10) ** 2 / 2)) + 1
            balls[i][1] += int(sqrt((clock.tick() / 10) ** 2 / 2)) + 1
        pygame.draw.circle(screen, (255, 255, 255), (balls[i][0], balls[i][1]), 10)
    pygame.display.flip()


pygame.quit()
