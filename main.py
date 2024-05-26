import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('tanks')
bg = pygame.image.load('bg.png')
square = pygame.Surface((100, 100))
square.fill('Blue')
x = 100
y = 100
run = True
while run:
    screen.blit(bg, (0, 0))
    bg.blit(square, (200, 200))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                x += 15
                bg = pygame.image.load('bg.png')
                right = pygame.image.load('right.png')
                screen.blit(bg, (0, 0))
                bg.blit(square, (200, 200))
                bg.blit(right, (x, y))
                pygame.display.update()
                print('D')
            if event.key == pygame.K_a:
                x -= 15
                bg = pygame.image.load('bg.png')
                left = pygame.image.load('left.png')
                screen.blit(bg, (0, 0))
                bg.blit(square, (200, 200))
                bg.blit(left, (x, y))
                pygame.display.update()
                print('A')
            if event.key == pygame.K_w:
                y -= 15
                bg = pygame.image.load('bg.png')
                up = pygame.image.load('up.png')
                screen.blit(bg, (0, 0))
                bg.blit(square, (200, 200))
                bg.blit(up, (x, y))
                pygame.display.update()
                print('W')
            if event.key == pygame.K_s:
                y += 15
                bg = pygame.image.load('bg.png')
                down = pygame.image.load('down.png')
                screen.blit(bg, (0, 0))
                bg.blit(square, (200, 200))
                bg.blit(down, (x, y))
                pygame.display.update()
                print('S')
        if event.type == pygame.QUIT:
            run = False
            print('Выход из танков...')
            pygame.quit()

