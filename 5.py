from math import sqrt, ceil
import pygame


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __mul__(self, other):
        self.x *= other
        self.y *= other

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        if x - int(x) <= ceil(x) - x:
            x = int(x)
        else:
            x = ceil(x)
        if y - int(y) <= ceil(y) - y:
            y = int(y)
        else:
            y = ceil(y)
        return x, y


coords = input().split(', ')
for i in range(len(coords)):
    c = coords[i]
    x = int(c[1:c.index(';')]) + 501 // 2
    y = -int(c[c.index(';') + 1:-1]) + 501 // 2
    coords[i] = Point(x, y)
p = Point(*(coords[1] + coords[0]))
p * 0.5
vectors = []
for i in range(len(coords)):
    vectors.append(Point(*(coords[i] - p)))


pygame.init()
size = w, h = 501, 501
screen = pygame.display.set_mode(size)


running = True
k_1 = 1
eps = 1
scroll = 0
color1 = (0, 0, 0)
color2 = (255, 0, 0)
pygame.draw.polygon(screen, color2, [(i.x, i.y) for i in coords], 1)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 4:
                scroll = 1
            else:
                scroll = -1

    if scroll == 1:
        screen.fill(color1)
        points = []
        for i in range(1, len(vectors)):
            dist = vectors[i].dist()
            k_i = k_1 * dist / vectors[0].dist()
            num = (dist + k_i) / dist
            vectors[i] * num
            points.append(vectors[i] + p)
        num = (vectors[0].dist() + 1) / vectors[0].dist()
        vectors[0] * num
        points.append(vectors[0] + p)
        pygame.draw.polygon(screen, color2, points, 1)
        scroll = 0
    elif scroll == -1:
        points = []
        vectors1 = []
        flag = False
        for i in range(1, len(vectors)):
            dist = vectors[i].dist()
            if dist <= eps or flag:
                flag = True
                continue
            k_i = -k_1 * dist / vectors[0].dist()
            num = (dist + k_i) / dist
            vectors[i] * num
            vectors1.append(vectors[i])
        if not flag and vectors[0].dist() >= eps:
            num = (vectors[0].dist() - 1) / vectors[0].dist()
            vectors[0] * num
            vectors1.insert(0, vectors[0])
        if len(vectors1) == len(vectors):
            for i in vectors1:
                points.append(i + p)
            vectors = vectors1
            screen.fill(color1)
            pygame.draw.polygon(screen, color2, points, 1)
        scroll = 0
    pygame.display.flip()

pygame.quit()