import pygame
import sys


def win(f):
    pygame.init()
    size = width, height = (800, 600)
    bg2 = pygame.image.load("menu_assets/zaq.jpg")
    image12 = pygame.transform.scale(bg2, (size))
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        screen.fill((0, 0, 0))
        screen.blit(image12, (0, 0))
        font = pygame.font.Font(None, 72)
        text_surface = font.render('Вы потратили 5 минут жизни', True, (255, 255, 255))
        text_surface1 = font.render('Поздравляем!', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, height / 2 - 50)) # Изменили позицию по высоте
        text_rect1 = text_surface1.get_rect(center=(width / 2, height / 2 + 50)) # Изменили позицию по высоте
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface1, text_rect1)
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()