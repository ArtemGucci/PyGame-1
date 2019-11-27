import pygame
from time import sleep

COLORS = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 0, 255)]


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]
        self.size = 30
        self.x = 10
        self.y = 10
        self.render()

    def set_board(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for i in range(height)]

    def set_square(self, size, x, y):
        self.x = x
        self.y = y
        self.size = size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (j * self.size + self.x, i * self.size + self.y, self.size, self.size), 1)

    def check(self, coords):
        if (coords[0] not in range(self.x, self.size * self.width + 1) or
                coords[1] not in range(self.y, self.size * self.height + 1)):
            return False
        return True

    def click(self, coords):
        if not self.check(coords):
            return
        x = (coords[0] - self.x) // self.size
        y = (coords[1] - self.y) // self.size
        if self.board[x][y] == 1:
            self.board[x][y] = 2
            pygame.draw.circle(screen, COLORS[2],
                               (self.x + x * self.size + self.size // 2, self.y + y * self.size + self.size // 2),
                               self.size // 2)
        elif self.board[x][y] == 2:
            self.board[x][y] = 1
            pygame.draw.circle(screen, COLORS[3],
                               (self.x + x * self.size + self.size // 2, self.y + y * self.size + self.size // 2),
                               self.size // 2)
        else:
            flag = False
            for g in range(n):
                for j in range(m):
                    if board.board[g][j] == 2:
                        flag = True
                        way = board.has_path(g, j, x, y)
                        if way:
                            for i in range(1, len(way)):
                                pygame.draw.rect(screen, COLORS[0],
                                                 (
                                                 self.x + way[i - 1][0] * self.size, self.y + way[i - 1][1] * self.size,
                                                 self.size, self.size))
                                pygame.draw.rect(screen, COLORS[1],
                                                 (
                                                     self.x + way[i - 1][0] * self.size,
                                                     self.y + way[i - 1][1] * self.size,
                                                     self.size, self.size), 1)
                                pygame.draw.circle(screen, COLORS[2] if i != len(way) - 1 else COLORS[3],
                                                   (self.x + way[i][0] * self.size + self.size // 2,
                                                    self.y + way[i][1] * self.size + self.size // 2),
                                                   self.size // 2)
                                pygame.display.flip()
                                sleep(0.1)

                            self.board[g][j] = 0
                            self.board[x][y] = 1
                            return
            if flag:
                return
            self.board[x][y] = 1
            pygame.draw.circle(screen, COLORS[3],
                               (self.x + x * self.size + self.size // 2, self.y + y * self.size + self.size // 2),
                               self.size // 2)


class Lines(Board):

    def has_path(self, x1, y1, x2, y2):
        distances = [[-1 for i in range(m)] for j in range(n)]
        distances[x1][y1] = 0
        q = [(x1, y1)]
        while q:
            v = q.pop(0)
            for i in [(v[0] + 1, v[1]), (v[0] - 1, v[1]), (v[0], v[1] + 1), (v[0], v[1] - 1)]:
                if i[0] in range(n) and i[1] in range(m):
                    if distances[i[0]][i[1]] == -1:
                        if not self.board[i[0]][i[1]]:
                            distances[i[0]][i[1]] = distances[v[0]][v[1]] + 1
                            q.append(i)
        if distances[x2][y2] == -1:
            return False
        way = [(x2, y2)]
        v = (x2, y2)
        while distances[v[0]][v[1]]:
            for i in [(v[0] + 1, v[1]), (v[0] - 1, v[1]), (v[0], v[1] + 1), (v[0], v[1] - 1)]:
                if i[0] in range(n) and i[1] in range(m):
                    if distances[v[0]][v[1]] - 1 == distances[i[0]][i[1]]:
                        way.append(i)
                        v = i
                        break
        way.reverse()
        return way


n, m = map(int, input().split())
pygame.init()
size = h, w = 800, 800
screen = pygame.display.set_mode(size)
board = Lines(n, m)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.click(event.pos)
    pygame.display.flip()

pygame.quit()
