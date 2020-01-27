from pygame import mixer
from sprite_library import *
from pygame.sysfont import SysFont
import time


class Button:
    def __init__(self, position, size, colour, hover_colour, text, difficulty, callback):
        self.position = position
        self.size = size
        self.colour = colour
        self.hover_colour = hover_colour
        self.text = text
        self.difficulty = difficulty
        self.callback = callback
        self.font = pygame.font.SysFont("comic sans", 45)
        self.hovering = False

    def draw(self, surface):
        if self.hovering:
            pygame.draw.rect(surface, self.hover_colour, (self.position[0],
                                                          self.position[1], self.size[0], self.size[1]))
        else:
            pygame.draw.rect(surface, self.colour, (self.position[0], self.position[1], self.size[0], self.size[1]))

        label = self.font.render(self.text, 30, (40, 180, 250))
        surface.blit(label, self.position)

    def is_mouse_hovering(self, mouse_x, mouse_y):
        return(self.position[0] <= mouse_x <= self.position[0] + self.size[0]
               and self.position[1] <= mouse_y <= self.position[1] + self.size[1])

    def click(self):
        self.callback()

        if play.click():
            EnemyHandler.difficulty = 5
            mixer.music.pause()
            lvl6()


class Button2:
    def __init__(self, position, size, colour, hover_colour, text, difficulty, callback):
        self.position = position
        self.size = size
        self.colour = colour
        self.hover_colour = hover_colour
        self.text = text
        self.difficulty = difficulty
        self.callback = callback
        self.font = pygame.font.SysFont("comic sans", 20)
        self.hovering = False

    def draw(self, surface):
        if self.hovering:
            pygame.draw.rect(surface, self.hover_colour, (self.position[0],
                                                          self.position[1], self.size[0], self.size[1]))
        else:
            pygame.draw.rect(surface, self.colour, (self.position[0], self.position[1], self.size[0], self.size[1]))

        label = self.font.render(self.text, 30, (40, 180, 250))
        surface.blit(label, self.position)

    def is_mouse_hovering(self, mouse_x, mouse_y):
        return(self.position[0] <= mouse_x <= self.position[0] + self.size[0]
               and self.position[1] <= mouse_y <= self.position[1] + self.size[1])

    def click(self):
        self.callback()

        if play.click():
            EnemyHandler.difficulty = 5
            mixer.music.pause()
            lvl1()


def lvl1():

    while True:
        window2 = UIWindow(Vector(1280, 720), "LEVEL 1")
        brush = window2.get_brush()

        ship = Ship(Vector(100, 140))
        enemy_handler = EnemyHandler(Vector(1000, 500), 55)
        bullet_handler = BulletHandler(Vector(1280, 720))
        background2 = Lvl1Background(Vector(640, 360))
        # to calculate the position, take your x/y value and divide it by 2 and then do 1280(x) or 720(y) - your value

        score = 0
        score_label = HUDLabel(Vector(100, 50), Vector(150, 100), "Score: 0", SysFont("comic sans", 256),
                               (255, 255, 255))

        lives_label = HUDLabel(Vector(300, 50), Vector(150, 100), "Lives: 5", SysFont("comic sans", 256),
                               (255, 255, 255))

        pygame.mixer.music.load('assets/music/8-bitMusic.mp3')
        pygame.mixer.music.play(loops=-1)

        while True:
            delta_time = window2.wait() / 1800

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        ship.add_velocity(Vector(0, -500))
                    elif event.key == pygame.K_a:
                        ship.add_velocity(Vector(-550))
                    elif event.key == pygame.K_s:
                        ship.add_velocity(Vector(0, 500))
                    elif event.key == pygame.K_d:
                        ship.add_velocity(Vector(550))
                    elif event.key == pygame.K_SPACE:
                        ship.fire(bullet_handler)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        ship.add_velocity(Vector(0, 500))
                    elif event.key == pygame.K_a:
                        ship.add_velocity(Vector(550))
                    elif event.key == pygame.K_s:
                        ship.add_velocity(Vector(0, -500))
                    elif event.key == pygame.K_d:
                        ship.add_velocity(Vector(-550))

            ship.update(delta_time)
            bullet_handler.update(delta_time)
            enemy_handler.update(delta_time)
            bullet_handler.check_collisions(enemy_handler)

            score += enemy_handler.get_enemy_destroyed()
            score_label.set_text("Score: " + str(score))
            score_label.update_appearance()

            if ship.check_enemy_collision(enemy_handler):
                lives = ship.get_lives_lost(ship)
                lives_label.set_text("Lives: " + str(lives))
                lives_label.update_appearance()

            if score >= 100:
                lvl2()

            window2.clear()

            background2.render(brush)
            score_label.render(brush)
            lives_label.render(brush)
            enemy_handler.render(brush)
            bullet_handler.render(brush)
            ship.render(brush)

            window2.show_frame()


def lvl2():

    while True:
        window2 = UIWindow(Vector(1280, 720), "LEVEL 2")
        brush = window2.get_brush()

        ship = Lvl2Ship(Vector(100, 140))
        enemy_handler = Lvl2EnemyHandler(Vector(1000, 500), 28)
        bullet_handler = Lvl2BulletHandler(Vector(1280, 720))
        background2 = Lvl2Background(Vector(640, 360))
        # to calculate the position, take your x/y value and divide it by 2 and then do 1280(x) or 720(y) - your value

        score = 0
        score_label = HUDLabel(Vector(100, 50), Vector(150, 100), "Score: 0", SysFont("comic sans", 256),
                               (255, 255, 255))

        lives_label = HUDLabel(Vector(300, 50), Vector(150, 100), "Lives: 4", SysFont("comic sans", 256),
                               (255, 255, 255))

        pygame.mixer.music.load('assets/music/Jurassic Park.mp3')
        pygame.mixer.music.play(loops=-1)

        while True:
            delta_time = window2.wait() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        ship.add_velocity(Vector(0, -400))
                    elif event.key == pygame.K_a:
                        ship.add_velocity(Vector(-450))
                    elif event.key == pygame.K_s:
                        ship.add_velocity(Vector(0, 400))
                    elif event.key == pygame.K_d:
                        ship.add_velocity(Vector(450))
                    elif event.key == pygame.K_SPACE:
                        ship.fire(bullet_handler)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        ship.add_velocity(Vector(0, 400))
                    elif event.key == pygame.K_a:
                        ship.add_velocity(Vector(450))
                    elif event.key == pygame.K_s:
                        ship.add_velocity(Vector(0, -400))
                    elif event.key == pygame.K_d:
                        ship.add_velocity(Vector(-450))

            ship.update(delta_time)
            bullet_handler.update(delta_time)
            enemy_handler.update(delta_time)
            bullet_handler.check_collisions(enemy_handler)

            score += enemy_handler.get_enemy_destroyed()
            score_label.set_text("Score: " + str(score))
            score_label.update_appearance()

            if ship.check_enemy_collision(enemy_handler):
                lives = ship.get_lives_lost(ship)
                lives_label.set_text("Lives: " + str(lives))
                lives_label.update_appearance()

            if score >= 150:
                lvl3()

            window2.clear()

            background2.render(brush)
            score_label.render(brush)
            lives_label.render(brush)
            enemy_handler.render(brush)
            bullet_handler.render(brush)
            ship.render(brush)

            print("You achieved a score of: " + str(score))

            window2.show_frame()


def lvl3():

    while True:
        window2 = UIWindow(Vector(1280, 720), "LEVEL 3")
        brush = window2.get_brush()

        ship = Lvl3Ship(Vector(100, 140))
        enemy_handler = EnemyHandler3(Vector(1000, 500), 13)
        enemy_handler2 = EnemyHandler4(Vector(500, 1000), 3)
        bullet_handler = Lvl3BulletHandler(Vector(1280, 720))
        background2 = Lvl3Background(Vector(640, 360))
        # to calculate the position, take your x/y value and divide it by 2 and then do 1280(x) or 720(y) - your value

        score = 0
        score_label = HUDLabel(Vector(100, 50), Vector(150, 100), "Score: 0", SysFont("comic sans", 256),
                               (255, 255, 255))

        lives_label = HUDLabel(Vector(300, 50), Vector(150, 100), "Lives: 4", SysFont("comic sans", 256),
                               (255, 255, 255))

        pygame.mixer.music.load('assets/music/Pirates of the Caribbean - Hes a Pirate.mp3')
        pygame.mixer.music.play(loops=-1)

        while True:
            delta_time = window2.wait() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        ship.add_velocity(Vector(0, -400))
                    elif event.key == pygame.K_a:
                        ship.add_velocity(Vector(-450))
                    elif event.key == pygame.K_s:
                        ship.add_velocity(Vector(0, 400))
                    elif event.key == pygame.K_d:
                        ship.add_velocity(Vector(450))
                    elif event.key == pygame.K_SPACE:
                        ship.fire(bullet_handler)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        ship.add_velocity(Vector(0, 400))
                    elif event.key == pygame.K_a:
                        ship.add_velocity(Vector(450))
                    elif event.key == pygame.K_s:
                        ship.add_velocity(Vector(0, -400))
                    elif event.key == pygame.K_d:
                        ship.add_velocity(Vector(-450))

            ship.update(delta_time)
            bullet_handler.update(delta_time)
            enemy_handler.update(delta_time)
            enemy_handler2.update(delta_time)
            bullet_handler.check_collisions(enemy_handler)
            bullet_handler.check_collisions(enemy_handler2)

            score += enemy_handler.get_enemy_destroyed()
            score_label.set_text("Score: " + str(score))
            score_label.update_appearance()

            score += enemy_handler2.get_enemy_destroyed()
            score_label.set_text("Score: " + str(score))
            score_label.update_appearance()

            if ship.check_enemy_collision(enemy_handler):
                lives = ship.get_lives_lost(ship)
                lives_label.set_text("Lives: " + str(lives))
                lives_label.update_appearance()

            if ship.check_enemy_collision(enemy_handler2):
                lives = ship.get_lives_lost(ship)
                lives_label.set_text("Lives: " + str(lives))
                lives_label.update_appearance()

            if score >= 150:
                lvl4()

            window2.clear()

            background2.render(brush)
            score_label.render(brush)
            lives_label.render(brush)
            enemy_handler.render(brush)
            enemy_handler2.render(brush)
            bullet_handler.render(brush)
            ship.render(brush)

            print("You achieved a score of: " + str(score))

            window2.show_frame()


def lvl4():

    while True:
        window2 = UIWindow(Vector(1280, 720), "LEVEL 4")
        brush = window2.get_brush()

        ship = Lvl4Ship(Vector(640, 360))
        enemy_handler = EnemyHandler5(Vector(1000, 500), 10)
        enemy_handler3 = EnemyHandler6(Vector(1000, 500), 7)
        enemy_handler4 = EnemyHandler7(Vector(1000, 500), 4)
        background2 = Lvl4Background(Vector(640, 360))
        # to calculate the position, take your x/y value and divide it by 2 and then do 1280(x) or 720(y) - your value

        timep = 3000
        time_label = HUDLabel(Vector(100, 50), Vector(190, 100), "Time Left: 3000", SysFont("comic sans", 256),
                               (255, 255, 255))

        lives_label = HUDLabel(Vector(300, 50), Vector(150, 100), "Lives: 3", SysFont("comic sans", 256),
                               (255, 255, 255))

        pygame.mixer.music.load('assets/music/Bobby-Darin-Beyond-the-Sea.mp3')
        pygame.mixer.music.play(loops=-1)

        while True:
            delta_time = window2.wait() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        ship.add_velocity(Vector(0, -300))
                    elif event.key == pygame.K_a:
                        ship.add_velocity(Vector(-350))
                    elif event.key == pygame.K_s:
                        ship.add_velocity(Vector(0, 300))
                    elif event.key == pygame.K_d:
                        ship.add_velocity(Vector(350))

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        ship.add_velocity(Vector(0, 300))
                    elif event.key == pygame.K_a:
                        ship.add_velocity(Vector(350))
                    elif event.key == pygame.K_s:
                        ship.add_velocity(Vector(0, -300))
                    elif event.key == pygame.K_d:
                        ship.add_velocity(Vector(-350))

            ship.update(delta_time)
            enemy_handler.update(delta_time)
            enemy_handler3.update(delta_time)
            enemy_handler4.update(delta_time)

            timep = timep - 1
            time_label.set_text("Time Left: " + str(timep))
            time_label.update_appearance()

            if ship.check_enemy_collision(enemy_handler):
                lives = ship.get_lives_lost(ship)
                lives_label.set_text("Lives: " + str(lives))
                lives_label.update_appearance()

            if ship.check_enemy_collision(enemy_handler4):
                lives = ship.get_lives_lost(ship)
                lives_label.set_text("Lives: " + str(lives))
                lives_label.update_appearance()

            if ship.check_enemy_collision(enemy_handler3):
                lives = ship.get_lives_lost(ship)
                lives_label.set_text("Lives: " + str(lives))
                lives_label.update_appearance()

            if timep == 0:
                lvl5()

            window2.clear()

            background2.render(brush)
            time_label.render(brush)
            lives_label.render(brush)
            enemy_handler.render(brush)
            enemy_handler3.render(brush)
            enemy_handler4.render(brush)
            ship.render(brush)

            window2.show_frame()


def lvl5():

    while True:
        window2 = UIWindow(Vector(1000, 720), "LEVEL 5")
        brush = window2.get_brush()

        ship = Lvl5ship(Vector(100, 140))
        enemy_handler = EnemyHandler8(Vector(1000, 500), 40)
        enemy_handler2 = EnemyHandler9(Vector(1000, 500), 40)
        bullet_handler = BulletHandler5(Vector(1000, 720))
        background2 = Lvl5Background(Vector(640, 360))
        # to calculate the position, take your x/y value and divide it by 2 and then do 1280(x) or 720(y) - your value

        score = 0
        score_label = HUDLabel(Vector(100, 50), Vector(150, 100), "Score: 0", SysFont("comic sans", 256),
                               (255, 255, 255))

        lives_label = HUDLabel(Vector(300, 50), Vector(150, 100), "Lives: 4", SysFont("comic sans", 256),
                               (255, 255, 255))

        pygame.mixer.music.load('assets/music/Under The Sea.mp3')
        pygame.mixer.music.play(loops=-1)

        while True:
            delta_time = window2.wait() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        ship.add_velocity(Vector(0, -400))
                    elif event.key == pygame.K_a:
                        ship.add_velocity(Vector(-450))
                    elif event.key == pygame.K_s:
                        ship.add_velocity(Vector(0, 400))
                    elif event.key == pygame.K_d:
                        ship.add_velocity(Vector(450))
                    elif event.key == pygame.K_SPACE:
                        ship.fire(bullet_handler)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        ship.add_velocity(Vector(0, 400))
                    elif event.key == pygame.K_a:
                        ship.add_velocity(Vector(450))
                    elif event.key == pygame.K_s:
                        ship.add_velocity(Vector(0, -400))
                    elif event.key == pygame.K_d:
                        ship.add_velocity(Vector(-450))

            ship.update(delta_time)
            bullet_handler.update(delta_time)
            enemy_handler.update(delta_time)
            enemy_handler2.update(delta_time)
            bullet_handler.check_collisions(enemy_handler)
            bullet_handler.check_collisions(enemy_handler2)

            score += enemy_handler.get_enemy_destroyed()
            score_label.set_text("Score: " + str(score))
            score_label.update_appearance()

            score += enemy_handler2.get_enemy_destroyed()
            score_label.set_text("Score: " + str(score))
            score_label.update_appearance()

            if ship.check_enemy_collision(enemy_handler):
                lives = ship.get_lives_lost(ship)
                lives_label.set_text("Lives: " + str(lives))
                lives_label.update_appearance()

            if ship.check_enemy_collision(enemy_handler2):
                lives = ship.get_lives_lost(ship)
                lives_label.set_text("Lives: " + str(lives))
                lives_label.update_appearance()

            if score == 200:
                lvl6()
            window2.clear()

            background2.render(brush)
            score_label.render(brush)
            lives_label.render(brush)
            enemy_handler.render(brush)
            enemy_handler2.render(brush)
            bullet_handler.render(brush)
            ship.render(brush)

            window2.show_frame()


def lvl6():
    while True:
        window2 = UIWindow(Vector(1280, 720), "LEVEL 7")
        brush = window2.get_brush()

        ship = ShipX(Vector(100, 140))
        enemy_handler = EnemyHandlerX(Vector(1000, 500), 25)
        bullet_handler = BulletHandlerX(Vector(1280, 720))
        background2 = LvlXBackground(Vector(640, 360))
        # to calculate the position, take your x/y value and divide it by 2 and then do 1280(x) or 720(y) - your value

        score = 0
        score_label = HUDLabel(Vector(100, 50), Vector(150, 100), "Score: 0", SysFont("comic sans", 256),
                               (255, 255, 255))

        lives_label = HUDLabel(Vector(300, 50), Vector(150, 100), "Lives: 5", SysFont("comic sans", 256),
                               (255, 255, 255))

        pygame.mixer.music.load('assets/music/SmashMouth-AllStar.mp3')
        pygame.mixer.music.play(loops=-1)

        while True:
            delta_time = window2.wait() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        ship.add_velocity(Vector(0, -400))
                    elif event.key == pygame.K_a:
                        ship.add_velocity(Vector(-450))
                    elif event.key == pygame.K_s:
                        ship.add_velocity(Vector(0, 400))
                    elif event.key == pygame.K_d:
                        ship.add_velocity(Vector(450))
                    elif event.key == pygame.K_SPACE:
                        ship.fire(bullet_handler)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        ship.add_velocity(Vector(0, 400))
                    elif event.key == pygame.K_a:
                        ship.add_velocity(Vector(450))
                    elif event.key == pygame.K_s:
                        ship.add_velocity(Vector(0, -400))
                    elif event.key == pygame.K_d:
                        ship.add_velocity(Vector(-450))

            ship.update(delta_time)
            bullet_handler.update(delta_time)
            enemy_handler.update(delta_time)
            bullet_handler.check_collisions(enemy_handler)

            score += enemy_handler.get_enemy_destroyed()
            score_label.set_text("Score: " + str(score))
            score_label.update_appearance()

            if ship.check_enemy_collision(enemy_handler):
                lives = ship.get_lives_lost(ship)
                lives_label.set_text("Lives: " + str(lives))
                lives_label.update_appearance()

            window2.clear()

            background2.render(brush)
            score_label.render(brush)
            lives_label.render(brush)
            enemy_handler.render(brush)
            bullet_handler.render(brush)
            ship.render(brush)

            window2.show_frame()


window = pygame.display.set_mode((800, 600))
current_state = 0

play = Button((350, 350), (80, 30), (140, 20, 120), (0, 0, 0), "PLAY", 5, lvl6)

title_label = Button((250, 150), (320, 30), (0, 0, 0), (0, 0, 0), "SOUPED UP SALMON", 0,  None)
title_label2 = Button((345, 180), (140, 30), (0, 0, 0), (0, 0, 0), "ORIGINS", 0,  None)
title_label3 = Button2((0, 0), (0, 0), (0, 0, 0), (0, 0, 0), "lift your finger from wasd before you enter "
                                                                "the next level to avoid the glitch", 0,  None)

background = DifficultyBackground((0, 0))
buttons = [play]


def dif_get_input():
    if current_state == 0:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        hovered_button = None

        for button in buttons:
            button.hovering = button.is_mouse_hovering(mouse_x, mouse_y)
            if button.hovering:
                hovered_button = button

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == pygame.BUTTON_LEFT:
                    if hovered_button:
                        hovered_button.click()


def dif_update():
    if current_state == 0:
        pass


def dif_render():
    if current_state == 0:
        background.draw(window)
        play.draw(window)
        title_label.draw(window)
        title_label2.draw(window)
        title_label3.draw(window)
    pygame.display.flip()
    pygame.mixer.pause()


pygame.mixer.music.load('assets/music/Monsta.mp3')
pygame.mixer.music.play(loops=-1)
while True:
    dif_get_input()
    dif_update()
    dif_render()
