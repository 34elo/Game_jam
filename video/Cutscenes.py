import pygame
import main
import cv2
import Metal_Gear
import sys


def first_cut(f):
    if f == 1:
        video_path = 'video/cut1.mp4'
        cap = cv2.VideoCapture(video_path)
    if f == 2:
        video_path = 'video/cut2.mp4'
        cap = cv2.VideoCapture(video_path)
    if f == 3:
        video_path = 'video/cut3.mp4'
        cap = cv2.VideoCapture(video_path)
    if f == 4:
        video_path = 'video/cut4.mp4'
        cap = cv2.VideoCapture(video_path)


    clock = pygame.time.Clock()
    pygame.init()
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if f == 1:
                    main.play(1)
                if f == 2:
                    Metal_Gear.game3()
                if f == 3:
                    main.play(3)

        ret, frame = cap.read()

        # Если достигнут конец видео, перезапускаем его
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Перейти к первому фрейму
            continue

        # Преобразуем BGR в RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Преобразуем в формат Pygame
        frame = pygame.surfarray.make_surface(frame)
        width_new, height_new = 1280, 720
        frame = pygame.transform.scale(frame, (width_new, height_new))

        # Отображаем фрейм
        screen.blit(frame, (0, 0))
        font = pygame.font.Font(None, 24)
        text_surface = font.render('Для перехода к игре нажмите пробел', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 100))
        screen.blit(text_surface, text_rect)


        pygame.display.flip()
        clock.tick(30)
    pygame.quit()