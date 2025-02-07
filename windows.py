import pygame
import sys
import pygame.mixer
import sqlite3
import cv2
import Buttons
import Cutscenes



video_path = 'video/runner.mp4'
cap = cv2.VideoCapture(video_path)

clock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()
size = width, height = (1280, 720)
bg = pygame.image.load("scene/menu_club.jpg")
bg4 = pygame.image.load("menu_assets/Gear.jpeg")
bg5 = pygame.image.load("menu_assets/Ultimate.png")
st = pygame.transform.scale(bg, (size))
image5 = pygame.transform.scale(bg5, (200, 50))
image4 = pygame.transform.scale(bg4, (size))
screen = pygame.display.set_mode(size)
pygame.mixer.music.load('music/Menu_tr.mp3')



def menu():
    screen = pygame.display.set_mode(size)
    st_but = Buttons.Button(width / 8 - (252 / 2), 270, 252, 74, 'Новая игра', 'menu_assets/1.png', 'music/kn2.mp3', 'menu_assets/chang.png')
    sett_but = Buttons.Button(width / 8 - (252 / 2), 370, 252, 74, 'Настройки', 'menu_assets/1.png', 'music/kn2.mp3', 'menu_assets/chang.png')
    exit_but = Buttons.Button(width / 8 - (252 / 2), 470, 252, 74, 'Выйти', 'menu_assets/1.png', 'music/kn2.mp3', 'menu_assets/chang.png')
    sp = [st_but, sett_but, exit_but]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT and event.button == sett_but:
                sett()
            if event.type == pygame.USEREVENT and event.button == exit_but:
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == st_but:
                Cutscenes.first_cut(1)
            for i in sp:
                i.hand_ev(event)
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
        font = pygame.font.Font(None, 72)
        text_surface = font.render('Hangover 4', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 100))
        screen.blit(text_surface, text_rect)
        im_rect = text_surface.get_rect(center=(width / 4 - 100, 120))
        screen.blit(image5, im_rect)
        for j in sp:
            j.draw(screen)
            j.check(pygame.mouse.get_pos())
        pygame.display.flip()

        clock.tick(20)

    pygame.quit()


def sett():
    exit_but = Buttons.Button(width / 2 - (252 / 2), 450, 252, 74, 'Назад', 'menu_assets/1.png', 'music/kn2.mp3', 'menu_assets/chang.png')
    reg_but = Buttons.Button(width / 2 - (252 / 2), 350, 240, 74, 'Регистрация', 'menu_assets/1.png', 'music/kn2.mp3', 'menu_assets/chang.png')
    sp = [exit_but, reg_but]
    COLOR_INACTIVE = pygame.Color('lightskyblue3')
    COLOR_ACTIVE = pygame.Color('white')
    FONT = pygame.font.Font(None, 32)


    class InputBox:

        def __init__(self, x, y, w, h, text=''):
            self.rect = pygame.Rect(x, y, w, h)
            self.color = COLOR_ACTIVE
            self.text = text
            self.txt_surface = FONT.render(text, True, self.color)
            self.active = False

        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                self.color = COLOR_INACTIVE if self.active else COLOR_ACTIVE
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print('АХАХАХАХАХАХАХАХА')
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode

                    self.txt_surface = FONT.render(self.text, True, self.color)


        def regist(self):
            return self.text
            self.text = ''

        def update(self):
            width = max(200, self.txt_surface.get_width() + 10)
            self.rect.w = width

        def draw(self, screen):
            screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
            pygame.draw.rect(screen, self.color, self.rect, 5)

    input_box1 = InputBox(width / 2 - (180 / 2), 200, 180, 32)
    input_box2 = InputBox(width / 2 - (180 / 2), 270, 180, 32)
    input_boxes = [input_box1, input_box2]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            for box in input_boxes:
                box.handle_event(event)
            if event.type == pygame.USEREVENT and event.button == exit_but:
                menu()
            if event.type == pygame.USEREVENT and event.button == reg_but:
                a = input_box1.regist()
                b = input_box2.regist()
                con = sqlite3.connect('tab.db')
                cur = con.cursor()
                result = cur.execute("""SELECT name from users""").fetchall()
                sp = [el[0] for el in result]
                if a not in sp:
                    cur.execute(f"INSERT INTO users VALUES ('{a}', '{b}')")
                    con.commit()
                    window(1)
                    con.close()
                else:
                    window(0)
            for i in sp:
                i.hand_ev(event)
        screen.fill((0, 0, 0))
        screen.blit(st, (0, 0))
        for box in input_boxes:
            box.update()
        for box in input_boxes:
            box.draw(screen)
        font = pygame.font.Font(None, 72)
        text_surface = font.render('Settings', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, 100))
        screen.blit(text_surface, text_rect)
        for j in sp:
            j.draw(screen)
            j.check(pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()




def window(f):
    pygame.init()
    size = width, height = (1280, 720)
    exit_but = Buttons.Button(width / 2 - (252 / 2), 450, 252, 74, 'Назад', 'menu_assets/1.png', 'music/kn2.mp3', 'menu_assets/chang.png')
    sp = [exit_but]
    screen = pygame.display.set_mode(size)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT and event.button == exit_but:
                pygame.mixer.music.stop()
                sett()
            for i in sp:
                i.hand_ev(event)
        screen.fill((0, 0, 0))
        screen.blit(image4, (0, 0))
        font = pygame.font.Font(None, 50)
        if f == 1:
            text_surface = font.render('Вы зарегистрировались или вошли', True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 100))
            screen.blit(text_surface, text_rect)
        else:
            text_surface = font.render('Вы  не зарегистрировались', True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(width / 2, 100))
            screen.blit(text_surface, text_rect)
        for j in sp:
            j.draw(screen)
            j.check(pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()



menu()