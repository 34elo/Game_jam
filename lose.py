import main
import pygame
import Buttons
import Metal_Gear


bg3 = pygame.image.load("scene/menu_club.jpg")
image123 = pygame.transform.scale(bg3, (800, 600))
clock = pygame.time.Clock()

def lose(f):
    size = width, height = (800, 600)
    exit_but = Buttons.Button(width / 2 - (252 / 2), 450, 252, 74, 'Заново', 'menu_assets/1.png', 'music/kn2.mp3', 'menu_assets/chang.png')
    sp = [exit_but]
    pygame.init()
    screen = pygame.display.set_mode(size)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT and event.button == exit_but:
                if f == 1:

                    main.play(1)
                elif f == 2:

                    Metal_Gear.game3()
                elif f == 3:

                    main.play(3)


            for i in sp:
                i.hand_ev(event)
        screen.fill((0, 0, 0))
        screen.blit(image123, (0, 0))
        font = pygame.font.Font(None, 72)
        text_surface = font.render('', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 100))
        screen.blit(text_surface, text_rect)
        for j in sp:
            j.draw(screen)
            j.check(pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()