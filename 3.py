import pygame
from math import cos, sin, pi


pygame.init()
size = w, h = 201, 201
screen = pygame.display.set_mode(size)
color1 = (255, 255, 255)
color2 = (0, 0, 0)
clock = pygame.time.Clock()


pygame.draw.circle(screen, color1, (201 // 2, 201 // 2), 10)
coords = [[[int(70 * cos(105 / 180 * pi) + 201 // 2), int(-70 * sin(105 / 180 * pi) + 201 // 2), 105],
           [int(70 * cos(75 / 180 * pi) + 201 // 2), int(-70 * sin(75 / 180 * pi) + 201 // 2), 75]],
          [[int(70 * cos(345 / 180 * pi) + 201 // 2), int(-70 * sin(345 / 180 * pi) + 201 // 2), 345],
           [int(70 * cos(315 / 180 * pi) + 201 // 2), int(-70 * sin(315 / 180 * pi) + 201 // 2), 315]],
          [[int(70 * cos(225 / 180 * pi) + 201 // 2), int(-70 * sin(225 / 180 * pi) + 201 // 2), 225],
           [int(70 * cos(195 / 180 * pi) + 201 // 2), int(-70 * sin(195 / 180 * pi) + 201 // 2), 195]]]
running = True
v = 0
side = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if side:
                    v -= 50
                    if v < 0:
                        side = not side
                        v *= -1
                else:
                    v += 50
            elif event.button == 3:
                if side:
                    v += 50
                else:
                    v -= 50
                    if v < 0:
                        side = not side
                        v *= -1
    screen.fill(color2)
    pygame.draw.circle(screen, color1, (201 // 2, 201 // 2), 10)
    deg = v * clock.tick() / 1000
    for i in range(3):
        coord = coords[i]
        if side:
            ang1 = (coord[0][2] - deg) % 360
            ang2 = (coord[1][2] - deg) % 360
            x1 = int(70 * cos(ang1 / 180 * pi) + 201 // 2)
            y1 = int(70 * sin(ang1 / 180 * pi) + 201 // 2)
            x2 = int(70 * cos(ang2 / 180 * pi) + 201 // 2)
            y2 = int(70 * sin(ang2 / 180 * pi) + 201 // 2)
            pygame.draw.polygon(screen, color1, ((201 // 2, 201 // 2), (x1, y1), (x2, y2)))
            coords[i] = [[x1, y1, ang1], [x2, y2, ang2]]
        else:
            ang1 = (coord[0][2] + deg) % 360
            ang2 = (coord[1][2] + deg) % 360
            x1 = int(70 * cos(ang1 / 180 * pi) + 201 // 2)
            y1 = int(70 * sin(ang1 / 180 * pi) + 201 // 2)
            x2 = int(70 * cos(ang2 / 180 * pi) + 201 // 2)
            y2 = int(70 * sin(ang2 / 180 * pi) + 201 // 2)
            pygame.draw.polygon(screen, color1, ((201 // 2, 201 // 2), (x1, y1), (x2, y2)))
            coords[i] = [[x1, y1, ang1], [x2, y2, ang2]]
    pygame.display.flip()
