import pygame
import random
import Cutscenes
import lose

kills = 20

def game3():
    clock = pygame.time.Clock()
    pygame.init()
    size = width, height = (1024, 1024)
    bg = pygame.image.load("menu_assets/fon.png")
    screen = pygame.display.set_mode(size)
    global kills
    kills = 20




    w_left = [pygame.image.load('menu_assets/1_pixian_ai_pixian_ai.png'),
              pygame.image.load('menu_assets/2_pixian_ai_pixian_ai.png'),
              pygame.image.load('menu_assets/3_pixian_ai_pixian_ai.png'),
              pygame.image.load('menu_assets/4_pixian_ai_pixian_ai.png'),
              pygame.image.load('menu_assets/5_pixian_ai_pixian_ai.png'),
              pygame.image.load('menu_assets/6_pixian_ai_pixian_ai.png'),
              pygame.image.load('menu_assets/7_pixian_ai_pixian_ai.png'),
              pygame.image.load('menu_assets/8_pixian_ai_pixian_ai.png')]

    w_right = [pygame.image.load('menu_assets/1_r_pixian_ai.png'),
               pygame.image.load('menu_assets/2_r_pixian_ai.png'),
               pygame.image.load('menu_assets/3_r_pixian_ai.png'),
               pygame.image.load('menu_assets/4_r_pixian_ai.png'),
               pygame.image.load('menu_assets/5_r_pixian_ai.png'),
               pygame.image.load('menu_assets/6_r_pixian_ai.png'),
               pygame.image.load('menu_assets/7_r_pixian_ai.png'),
               pygame.image.load('menu_assets/8_r_pixian_ai.png')]

    class Enemy(pygame.sprite.Sprite):
        image = pygame.image.load("menu_assets/sprit.png")


        def __init__(self, group):
            super().__init__(group)
            self.image = Enemy.image
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(width - self.image.get_width())
            self.rect.y = random.randrange(width - 500)

        def update(self):
            global kills
            self.rect.y += 10
            if pygame.sprite.spritecollideany(self, bullets1):
                self.kill()
                kills -= 1
                print(kills)
            screen_rect = (0, 0, width, height)
            if kills <= 0:
                print('ggd')
                Cutscenes.first_cut(3)

            if not self.rect.colliderect(screen_rect):
                self.kill()

    all_enemies = pygame.sprite.Group()

    class AnimatedSprite(pygame.sprite.Sprite):
        def __init__(self, player_image, x, y, w, h, spr):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(pygame.image.load(player_image), (w, h))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.left = False
            self.right = False
            self.count = 0
            self.onGround = False
            self.jump = False
            self.yvel = 0
            self.d = 0
            self.spr = spr
            self.f = 0
            self.xvel = 0

    class Player(AnimatedSprite):

        def pos(self):
            return [self.rect.x, self.rect.y]

        def update(self):

            keys = pygame.key.get_pressed()
            if self.rect.y < 0:
                pass
            #
            #
            #

            if keys[pygame.K_a] and self.rect.x > 5:
                self.xvel = -25
                self.left = True
                self.right = False
                self.d = -10

            elif keys[pygame.K_d] and self.rect.x < width - 80:
                self.xvel = 25
                self.left = False
                self.right = True
                self.d = 10

            else:
                self.xvel = 0
                self.left = False
                self.right = False
                self.count = 0

            if keys[pygame.K_UP]:
                if self.onGround:
                    self.yvel = -20

            if not self.onGround:
                self.yvel += 1

            self.onGround = False;
            self.rect.y += self.yvel
            self.collide(0, self.yvel, self.spr)

            self.rect.x += self.xvel
            self.collide(self.xvel, 0, self.spr)

            if pygame.sprite.spritecollideany(self, all_enemies):

                lose.lose(2)
                #
                #


        def collide(self, xvel, yvel, platforms):
            for p in platforms:
                if pygame.sprite.collide_rect(self, p):

                    if xvel > 0:
                        self.rect.right = p.rect.left

                    if xvel < 0:
                        self.rect.left = p.rect.right

                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.onGround = True
                        self.yvel = 0

                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 0

        def animat(self):
            if self.count + 1 >= 30:
                self.count = 0
            if self.left == True:
                screen.blit(w_left[self.count // 5], (self.rect.x, self.rect.y))
                self.count += 1
            elif self.right == True:
                screen.blit(w_right[self.count // 5], (self.rect.x, self.rect.y))
                self.count += 1
            else:
                screen.blit(self.image, (self.rect.x, self.rect.y))

    class level(pygame.sprite.Sprite):
        image1 = pygame.image.load("menu_assets/aiq.png")
        image = pygame.transform.scale(image1, (66, 66))

        def __init__(self, group, x, y):
            super().__init__(group)
            self.image = level.image
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        def coor(self):
            return [self.rect.x, self.rect.y]

    all_sprites = pygame.sprite.Group()

    br = ['----------------',
          '----------------',
          '----------------',
          '----------------',
          '---------------',
          '----------------',
          '--------------',
          '---------------',
          '---------------',
          '---------------',
          '---------------',
          '---------------',
          '----------------',
          '----------------',
          '****************',
          '----------------']

    spr = []
    sp_of_en = []
    for _ in range(1):
        Enemy(all_enemies)

    for i in range(len(br)):
        for j in range(len(br[i])):
            if br[i][j] == '*':
                sp = level(all_sprites, j * 64, i * 64)
                spr.append(sp)

    hero = Player('menu_assets/qwe_pixian_ai_pixian_ai.png', 80, 750, 60, 92, spr)

    class Attack(pygame.sprite.Sprite):
        image = pygame.image.load("menu_assets/bullet.png")

        def __init__(self, group, x):

            super().__init__(group)

            self.image = Attack.image
            self.rect = self.image.get_rect()
            self.rect.x = x[0] + 15
            self.rect.y = x[1] + 50

        def update(self, group, sp_b):
            if pygame.sprite.spritecollideany(self, all_enemies):
                for i in sp_b:
                    if pygame.sprite.collide_rect(self, i):
                        bullets1.remove(i)

            if pygame.sprite.spritecollideany(self, all_sprites):
                for i in sp_b:
                    if pygame.sprite.collide_rect(self, i):
                        bullets1.remove(i)

            if group == bullets1:
                self.rect.y -= 10

            screen_rect = (0, 0, width, height)

            if not self.rect.colliderect(screen_rect):
                self.kill()






    sp_bull = []

    bullets1 = pygame.sprite.Group()

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x = hero.pos()
                    pat = Attack(bullets1, x)
                    sp_bull.append(pat)

        screen.blit(bg, (0, 0))
        all_sprites.draw(screen)
        all_enemies.draw(screen)
        all_enemies.update()
        hero.update()
        hero.animat()
        bullets1.draw(screen)
        bullets1.update(bullets1, sp_bull)
        for _ in range(1):
            Enemy(all_enemies)
        pygame.display.flip()
        clock.tick(20)
    pygame.quit()

if __name__ == '__main__':
    Game = game3()
    Game.run()