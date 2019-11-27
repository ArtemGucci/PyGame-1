import pygame
from random import randint
from time import sleep


COLORS = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 0, 255)]


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[randint(2, 3)] * width for i in range(height)]
        self.count = 0

        self.x = 10
        self.y = 10
        self.size = 50

        self.paint()

    def set_view(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def set_board(self, width, height):
        self.width = width
        self.height = height
        self.board = [[randint(2, 3)] * width for i in range(height)]

    def paint(self):
        screen.fill(COLORS[0])
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, COLORS[1],
                                 (j * self.size + self.x, i * self.size + self.y, self.size, self.size), 1)
                pygame.draw.rect(screen, COLORS[self.board[j][i]],
                                 (j * self.size + 1 + self.x, i * self.size + 1 + self.y, self.size - 1, self.size - 1))

    def render(self, coords):
        col = (coords[0] - self.x) // self.size
        row = (coords[1] - self.y) // self.size
        for i in range(self.width):
            self.board[i][row] = self.board[col][row]
        for i in range(self.height):
            self.board[col][i] = self.board[col][row]
        self.paint()

    def check_coords(self, coords):
        if (coords[0] not in range(self.x, self.size * self.width + 1) or
                coords[1] not in range(self.y, self.size * self.height + 1)):
            return False
        return True

    def check_color(self, coords):
        col = (coords[0] - self.x) // self.size
        row = (coords[1] - self.y) // self.size
        if COLORS[self.board[col][row]] == NAMES[self.count]:
            self.count = not self.count
            return True
        return False

    def click(self, coords):
        if self.check_coords(coords) and self.check_color(coords):
            self.render(coords)


n = int(input())
first = input()
if first.strip().lower() == 'красный':
    NAMES = [(255, 0, 0), (0, 0, 255)]
else:
    NAMES = [(0, 0, 255), (255, 0, 0)]

pygame.init()
size = w, h = 800, 800
screen = pygame.display.set_mode(size)
board = Board(n, n)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.click(event.pos)
    color = board.board[0][0]
    flag = True
    for i in range(board.width):
        for j in range(board.height):
            if board.board[i][j] != color:
                flag = False
                break
        if not flag:
            break
    if flag:
        running = False
        sleep(2)
    pygame.display.flip()

pygame.quit()