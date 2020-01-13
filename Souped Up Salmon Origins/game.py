import time

from sprite_library import *
from hud_library import *

window = UIWindow(Vector(1280, 720), "Souped-up Salmon 2")
brush = window.get_brush()

ship = Ship(Vector(100, 140))
enemy_handler = EnemyHandler(Vector(1000, 500), 5)
bullet_handler = BulletHandler(Vector(1280, 720))
star_handler = StarHandler(Vector(1280, 720), 7)
background = Background(Vector(640, 360))
shipwreck = Shipwreck(Vector(900, 483.75))
seaweed1 = Seaweed(Vector(100, 517.5))
seaweed2 = Seaweed(Vector(550, 517.5))
seaweed3 = Seaweed(Vector(300, 517.5))
seaweed4 = Seaweed(Vector(425, 517.5))
sebastian = Sebastian(Vector(690, 360))
squidward_house = SquidwardHouse(Vector(300, (720 - (629 / 1.5) + 225)))
# to calculate the position, take your x/y value and divide it by 2 and then do 1280(x) or 720(y) - your value

score = 0
score_label = HUDLabel(Vector(100, 50), Vector(150, 100), "Score: 0", SysFont("comic sans", 256), (255, 255, 255))

lives = 5
lives_label = HUDLabel(Vector(300, 50), Vector(150, 100), "Lives: 5", SysFont("comic sans", 256), (255, 255, 255))

pygame.mixer.music.load('assets/music/Under The Sea.mp3')
pygame.mixer.music.play(-1)

while True:
    delta_time = window.wait() / 1000

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
    star_handler.update(delta_time)

    score += enemy_handler.get_enemy_destroyed()
    score_label.set_text("Score: " + str(score))
    score_label.update_appearance()

    if ship.check_enemy_collision(enemy_handler):
        lives = ship.get_lives_lost(ship)
        lives_label.set_text("Lives: " + str(lives))
        lives_label.update_appearance()

    window.clear()

    background.render(brush)
    score_label.render(brush)
    lives_label.render(brush)
    sebastian.render(brush)
    seaweed1.render(brush)
    seaweed2.render(brush)
    seaweed3.render(brush)
    seaweed4.render(brush)
    squidward_house.render(brush)
    enemy_handler.render(brush)
    bullet_handler.render(brush)
    star_handler.render(brush)
    ship.render(brush)
    shipwreck.render(brush)

    print("You achieved a score of: " + str(score))

    window.show_frame()

