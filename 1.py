import pygame
import os


def load_file(name):
    path = os.path.join('data', name)
    with open(path) as f:
        lines = [i.strip() for i in f.readlines()]
        h = len(lines)
        w = len(lines[0])
        return lines, w, h


def make_level():
    #player_pos = None
    for i in range(h):
        for j in range(len(lines[0])):
            if lines[i][j] == '.':
                Grass((i * 50, j * 50))
            elif lines[i][j] == '@':
                Hero((i * 50, j * 50))
            else:
                Box((i * 50, j * 50))


pygame.init()
heroes = pygame.sprite.Group()
objects = pygame.sprite.Group()
lines, w, h = load_file('level.txt')
size = w, h
screen = pygame.display.set_mode(size)
make_level()


def load_image(name, colorkey=None):
    path = os.path.join('data', name)
    image = pygame.image.load(path).convert()
    if colorkey:
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Hero(pygame.sprite.Sprite):
    image = load_image('mar.png')

    def __init__(self, pos):
        super().__init__(heroes)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.w, self.h = 24, 40


class Box(pygame.sprite.Sprite):
    image = load_image('box.png')

    def __init__(self, pos):
        super().__init__(objects)
        self.image = Box.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.w, self.h = 50, 50


class Grass(pygame.sprite.Sprite):
    image = load_image('grass.png')

    def __init__(self, pos):
        super().__init__(objects)
        self.image = Grass.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.w, self.h = 50, 50


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    pygame.display.flip()

pygame.quit()