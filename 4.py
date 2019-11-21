import pygame


pygame.init()
size = w, h = 300, 300
screen = pygame.display.set_mode(size)
pygame.draw.rect(screen, (0, 255, 0), (0, 0, 100, 100))
x1, y1, x2, y2 = 0, 0, 100, 100

running = True
carry = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if event.pos[0] in range(x1, x1 + x2 + 1) and event.pos[1] in range(y1, y1 + y2 + 1):
                carry = True
                coords = list(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            carry = False
    if carry:
        change = list(pygame.mouse.get_pos())
        change = [change[0] - coords[0], change[1] - coords[1]]
        coords[0] += change[0]
        coords[1] += change[1]
        screen.fill((0, 0, 0))
        x1 += change[0]
        y1 += change[1]
        pygame.draw.rect(screen, (0, 255, 0), (x1, y1, x2, y2))
    pygame.display.flip()

pygame.quit()
