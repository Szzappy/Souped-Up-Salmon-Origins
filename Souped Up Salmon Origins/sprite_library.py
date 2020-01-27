from random import randint
from hud_library import *
pygame.mixer.init()
import time

class Sprite(UIElement):
    def __init__(self, position, size):
        UIElement.__init__(self, position, size)
        brush = UIBrush(self._surface)
        self._velocity = Vector()
        self.should_delete = False
        self.destroyed_by_bullet = False
        self.life_loss = False
        self.difficulty = 20

    def add_velocity(self, velocity_to_add):
        self._velocity.add(velocity_to_add)

    def update(self, delta_time: float):
        move_distance = Vector(self._velocity.x, self._velocity.y)
        move_distance.scale(delta_time)
        self._position.add(move_distance)

    def get_position(self):
        return self._position

    def left(self):
        return self._position.x - self._size.x / 2

    def right(self):
        return self._position.x + self._size.x / 2

    def top(self):
        return self._position.y - self._size.y / 2

    def bottom(self):
        return self._position.y + self._size.y / 2

    def does_collide_with(self, other_sprite):
        return (self.left() <= other_sprite.right()
                and self.right() >= other_sprite.left()
                and self.top() <= other_sprite.bottom()
                and self.bottom() >= other_sprite.top())


class Enemy(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(80, 48))
        image = pygame.image.load("assets/images/lvl1/8-bitEnemy.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class EnemyX(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(125, 78))
        image = pygame.image.load("assets/images/bear.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl2Enemy(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(200, 95))
        image = pygame.image.load("assets/images/lvl2/dinoEnemy.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl3Enemy(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(200, 95))
        image = pygame.image.load("assets/images/lvl3/sharkEnemy.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl3Enemy2(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(70, 130))
        image = pygame.image.load("assets/images/lvl3/sharkEnemy2.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl4Enemy(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(135, 72))
        image = pygame.image.load("assets/images/lvl4/fangtooth.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl4Enemy2(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(70, 125))
        image = pygame.image.load("assets/images/lvl4/jelly.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl4Enemy3(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(120, 65))
        image = pygame.image.load("assets/images/lvl4/squid2.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl5Enemy1(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(120, 65))
        image = pygame.image.load("assets/images/lvl5/fish.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl5Enemy2(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(120, 65))
        image = pygame.image.load("assets/images/lvl5/fish3.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl5Enemy3(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(120, 65))
        image = pygame.image.load("assets/images/lvl5/fish4.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Boss(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(500, 200))
        image = pygame.image.load("assets/images/lvl6/boss.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class EnemyHandler(UIElement):
    def __init__(self, size, difficulty):
        UIElement.__init__(self, Vector(), size)
        self.__enemies = []
        self.__difficulty = difficulty
        self.add_enemies(difficulty)

    def add_enemies(self, difficulty):
        for count in range(difficulty):
            x = 1400
            y = randint(0, self._size.y)
            vx = randint(-600, -100)
            vy = randint(-100, 100)
            enemy = Enemy(Vector(x, y))
            enemy.add_velocity(Vector(vx, vy))
            self.__enemies.append(enemy)

    def update(self, delta_time: float):
        for enemy in self.__enemies:
            enemy.update(delta_time)

        self.__enemies[:] = [enemy for enemy in self.__enemies if enemy.get_position().x > 0
                             and not enemy.should_delete]
        self.__enemies[:] = [enemy for enemy in self.__enemies if 720 > enemy.get_position().y > 0
                             and not enemy.should_delete]

        difference = self.__difficulty - len(self.__enemies)

        if difference > 0:
            self.add_enemies(difference)

    def render(self, brush: UIBrush):
        for bullet in self.__enemies:
            bullet.render(brush)

    def add_enemy(self, enemy_to_add):
        self.__enemies.append(enemy_to_add)

    def get_enemies(self):
        return self.__enemies

    def get_enemy_destroyed(self):
        score = 0
        for enemy in self.__enemies:
            if enemy.destroyed_by_bullet:
                score += 1
        return score


class EnemyHandlerX(UIElement):
    def __init__(self, size, difficulty):
        UIElement.__init__(self, Vector(), size)
        self.__enemies = []
        self.__difficulty = difficulty
        self.add_enemies(difficulty)

    def add_enemies(self, difficulty):
        for count in range(difficulty):
            x = 1400
            y = randint(0, self._size.y)
            vx = randint(-600, -100)
            vy = randint(-100, 100)
            enemy = EnemyX(Vector(x, y))
            enemy.add_velocity(Vector(vx, vy))
            self.__enemies.append(enemy)

    def update(self, delta_time: float):
        for enemy in self.__enemies:
            enemy.update(delta_time)

        self.__enemies[:] = [enemy for enemy in self.__enemies if enemy.get_position().x > 0
                             and not enemy.should_delete]
        self.__enemies[:] = [enemy for enemy in self.__enemies if 720 > enemy.get_position().y > 0
                             and not enemy.should_delete]

        difference = self.__difficulty - len(self.__enemies)

        if difference > 0:
            self.add_enemies(difference)

    def render(self, brush: UIBrush):
        for bullet in self.__enemies:
            bullet.render(brush)

    def add_enemy(self, enemy_to_add):
        self.__enemies.append(enemy_to_add)

    def get_enemies(self):
        return self.__enemies

    def get_enemy_destroyed(self):
        score = 0
        for enemy in self.__enemies:
            if enemy.destroyed_by_bullet:
                score += 1
        return score


class Lvl2EnemyHandler(UIElement):
    def __init__(self, size, difficulty):
        UIElement.__init__(self, Vector(), size)
        self.__enemies = []
        self.__difficulty = difficulty
        self.add_enemies(difficulty)

    def add_enemies(self, difficulty):
        for count in range(difficulty):
            x = 1400
            y = randint(0, self._size.y)
            vx = randint(-600, -300)
            vy = randint(-200, 200)
            enemy = Lvl2Enemy(Vector(x, y))
            enemy.add_velocity(Vector(vx, vy))
            self.__enemies.append(enemy)

    def update(self, delta_time: float):
        for enemy in self.__enemies:
            enemy.update(delta_time)

        self.__enemies[:] = [enemy for enemy in self.__enemies if enemy.get_position().x > 0
                             and not enemy.should_delete]
        self.__enemies[:] = [enemy for enemy in self.__enemies if 720 > enemy.get_position().y > 0
                             and not enemy.should_delete]

        difference = self.__difficulty - len(self.__enemies)

        if difference > 0:
            self.add_enemies(difference)

    def render(self, brush: UIBrush):
        for bullet in self.__enemies:
            bullet.render(brush)

    def add_enemy(self, enemy_to_add):
        self.__enemies.append(enemy_to_add)

    def get_enemies(self):
        return self.__enemies

    def get_enemy_destroyed(self):
        score = 0
        for enemy in self.__enemies:
            if enemy.destroyed_by_bullet:
                score += 1
        return score


class EnemyHandler3(UIElement):
    def __init__(self, size, difficulty):
        UIElement.__init__(self, Vector(), size)
        self.__enemies = []
        self.__difficulty = difficulty
        self.add_enemies(difficulty)

    def add_enemies(self, difficulty):
        for count in range(difficulty):
            x = 1400
            y = randint(0, self._size.y)
            vx = randint(-400, -100)
            vy = randint(-50, 50)
            enemy = Lvl3Enemy(Vector(x, y))
            enemy.add_velocity(Vector(vx, vy))
            self.__enemies.append(enemy)

    def update(self, delta_time: float):
        for enemy in self.__enemies:
            enemy.update(delta_time)

        self.__enemies[:] = [enemy for enemy in self.__enemies if enemy.get_position().x > 0
                             and not enemy.should_delete]
        self.__enemies[:] = [enemy for enemy in self.__enemies if 720 > enemy.get_position().y > 0
                             and not enemy.should_delete]

        difference = self.__difficulty - len(self.__enemies)

        if difference > 0:
            self.add_enemies(difference)

    def render(self, brush: UIBrush):
        for bullet in self.__enemies:
            bullet.render(brush)

    def add_enemy(self, enemy_to_add):
        self.__enemies.append(enemy_to_add)

    def get_enemies(self):
        return self.__enemies

    def get_enemy_destroyed(self):
        score = 0
        for enemy in self.__enemies:
            if enemy.destroyed_by_bullet:
                score += 1
        return score


class EnemyHandler4(UIElement):
    def __init__(self, size, difficulty):
        UIElement.__init__(self, Vector(), size)
        self.__enemies = []
        self.__difficulty = difficulty
        self.add_enemies(difficulty)

    def add_enemies(self, difficulty):
        for count in range(difficulty):
            x = randint(0, 600)
            y = randint(800, 900)
            vx = randint(50, 50)
            vy = randint(-500, -300)
            enemy = Lvl3Enemy2(Vector(x, y))
            enemy.add_velocity(Vector(vx, vy))
            self.__enemies.append(enemy)

    def update(self, delta_time: float):
        for enemy in self.__enemies:
            enemy.update(delta_time)

        self.__enemies[:] = [enemy for enemy in self.__enemies if enemy.get_position().y > -40
                             and not enemy.should_delete]

        difference = self.__difficulty - len(self.__enemies)

        if difference > 0:
            self.add_enemies(difference)

    def render(self, brush: UIBrush):
        for bullet in self.__enemies:
            bullet.render(brush)

    def add_enemy(self, enemy_to_add):
        self.__enemies.append(enemy_to_add)

    def get_enemies(self):
        return self.__enemies

    def get_enemy_destroyed(self):
        score = 0
        for enemy in self.__enemies:
            if enemy.destroyed_by_bullet:
                score += 3
        return score


class EnemyHandler5(UIElement):
    def __init__(self, size, difficulty):
        UIElement.__init__(self, Vector(), size)
        self.__enemies = []
        self.__difficulty = difficulty
        self.add_enemies(difficulty)

    def add_enemies(self, difficulty):
        for count in range(difficulty):
            x = 1400
            y = randint(0, self._size.y)
            vx = randint(-250, -100)
            vy = randint(-20, 20)
            enemy = Lvl4Enemy(Vector(x, y))
            enemy.add_velocity(Vector(vx, vy))
            self.__enemies.append(enemy)

    def update(self, delta_time: float):
        for enemy in self.__enemies:
            enemy.update(delta_time)

        self.__enemies[:] = [enemy for enemy in self.__enemies if enemy.get_position().x > 0
                             and not enemy.should_delete]
        self.__enemies[:] = [enemy for enemy in self.__enemies if 720 > enemy.get_position().y > 0
                             and not enemy.should_delete]

        difference = self.__difficulty - len(self.__enemies)

        if difference > 0:
            self.add_enemies(difference)

    def render(self, brush: UIBrush):
        for bullet in self.__enemies:
            bullet.render(brush)

    def add_enemy(self, enemy_to_add):
        self.__enemies.append(enemy_to_add)

    def get_enemies(self):
        return self.__enemies

    def get_enemy_destroyed(self):
        score = 0
        for enemy in self.__enemies:
            if enemy.destroyed_by_bullet:
                score += 1
        return score


class EnemyHandler6(UIElement):
    def __init__(self, size, difficulty):
        UIElement.__init__(self, Vector(), size)
        self.__enemies = []
        self.__difficulty = difficulty
        self.add_enemies(difficulty)

    def add_enemies(self, difficulty):
        for count in range(difficulty):
            x = randint(0, 1000)
            y = randint(800, 900)
            vx = randint(0, 0)
            vy = randint(-200, -100)
            enemy = Lvl4Enemy2(Vector(x, y))
            enemy.add_velocity(Vector(vx, vy))
            self.__enemies.append(enemy)

    def update(self, delta_time: float):
        for enemy in self.__enemies:
            enemy.update(delta_time)

        self.__enemies[:] = [enemy for enemy in self.__enemies if enemy.get_position().y > -40
                             and not enemy.should_delete]

        difference = self.__difficulty - len(self.__enemies)

        if difference > 0:
            self.add_enemies(difference)

    def render(self, brush: UIBrush):
        for bullet in self.__enemies:
            bullet.render(brush)

    def add_enemy(self, enemy_to_add):
        self.__enemies.append(enemy_to_add)

    def get_enemies(self):
        return self.__enemies

    def get_enemy_destroyed(self):
        score = 0
        for enemy in self.__enemies:
            if enemy.destroyed_by_bullet:
                score += 1
        return score


class EnemyHandler7(UIElement):
    def __init__(self, size, difficulty):
        UIElement.__init__(self, Vector(), size)
        self.__enemies = []
        self.__difficulty = difficulty
        self.add_enemies(difficulty)

    def add_enemies(self, difficulty):
        for count in range(difficulty):
            x = -200
            y = randint(0, 600)
            vx = randint(200, 400)
            vy = randint(-30, 30)
            enemy = Lvl4Enemy3(Vector(x, y))
            enemy.add_velocity(Vector(vx, vy))
            self.__enemies.append(enemy)

    def update(self, delta_time: float):
        for enemy in self.__enemies:
            enemy.update(delta_time)

        self.__enemies[:] = [enemy for enemy in self.__enemies if enemy.get_position().x < 1280
                             and not enemy.should_delete]

        self.__enemies[:] = [enemy for enemy in self.__enemies if 720 > enemy.get_position().y > 0
                             and not enemy.should_delete]

        difference = self.__difficulty - len(self.__enemies)

        if difference > 0:
            self.add_enemies(difference)

    def render(self, brush: UIBrush):
        for bullet in self.__enemies:
            bullet.render(brush)

    def add_enemy(self, enemy_to_add):
        self.__enemies.append(enemy_to_add)

    def get_enemies(self):
        return self.__enemies

    def get_enemy_destroyed(self):
        score = 0
        for enemy in self.__enemies:
            if enemy.destroyed_by_bullet:
                score += 1
        return score


class EnemyHandler8(UIElement):
    def __init__(self, size, difficulty):
        UIElement.__init__(self, Vector(), size)
        self.__enemies = []
        self.__difficulty = difficulty
        self.add_enemies(difficulty)

    def add_enemies(self, difficulty):
        for count in range(difficulty):
            x = 1400
            y = randint(0, self._size.y)
            vx = randint(-250, -100)
            vy = randint(-20, 20)
            enemy = Lvl5Enemy1(Vector(x, y))
            enemy.add_velocity(Vector(vx, vy))
            self.__enemies.append(enemy)

    def update(self, delta_time: float):
        for enemy in self.__enemies:
            enemy.update(delta_time)

        self.__enemies[:] = [enemy for enemy in self.__enemies if enemy.get_position().x > 0
                             and not enemy.should_delete]
        self.__enemies[:] = [enemy for enemy in self.__enemies if 720 > enemy.get_position().y > 0
                             and not enemy.should_delete]

        difference = self.__difficulty - len(self.__enemies)

        if difference > 0:
            self.add_enemies(difference)

    def render(self, brush: UIBrush):
        for bullet in self.__enemies:
            bullet.render(brush)

    def add_enemy(self, enemy_to_add):
        self.__enemies.append(enemy_to_add)

    def get_enemies(self):
        return self.__enemies

    def get_enemy_destroyed(self):
        score = 0
        for enemy in self.__enemies:
            if enemy.destroyed_by_bullet:
                score += 1
        return score


class EnemyHandler9(UIElement):
    def __init__(self, size, difficulty):
        UIElement.__init__(self, Vector(), size)
        self.__enemies = []
        self.__difficulty = difficulty
        self.add_enemies(difficulty)

    def add_enemies(self, difficulty):
        for count in range(difficulty):
            x = 1400
            y = randint(0, self._size.y)
            vx = randint(-250, -100)
            vy = randint(-20, 20)
            enemy = Lvl5Enemy2(Vector(x, y))
            enemy.add_velocity(Vector(vx, vy))
            self.__enemies.append(enemy)

    def update(self, delta_time: float):
        for enemy in self.__enemies:
            enemy.update(delta_time)

        self.__enemies[:] = [enemy for enemy in self.__enemies if enemy.get_position().x > 0
                             and not enemy.should_delete]
        self.__enemies[:] = [enemy for enemy in self.__enemies if 720 > enemy.get_position().y > 0
                             and not enemy.should_delete]

        difference = self.__difficulty - len(self.__enemies)

        if difference > 0:
            self.add_enemies(difference)

    def render(self, brush: UIBrush):
        for bullet in self.__enemies:
            bullet.render(brush)

    def add_enemy(self, enemy_to_add):
        self.__enemies.append(enemy_to_add)

    def get_enemies(self):
        return self.__enemies

    def get_enemy_destroyed(self):
        score = 0
        for enemy in self.__enemies:
            if enemy.destroyed_by_bullet:
                score += 1
        return score


class BossHandler(UIElement):
    def __init__(self, size, difficulty):
        UIElement.__init__(self, Vector(), size)
        self.__enemies = []
        self.__difficulty = difficulty
        self.add_enemies(difficulty)

    def add_enemies(self, difficulty):
        for count in range(difficulty):
            x = 1400
            y = randint(0, self._size.y)
            vx = randint(-250, -100)
            vy = randint(-20, 20)
            enemy = Lvl5Enemy2(Vector(x, y))
            enemy.add_velocity(Vector(vx, vy))
            self.__enemies.append(enemy)

    def update(self, delta_time: float):
        for enemy in self.__enemies:
            enemy.update(delta_time)

        self.__enemies[:] = [enemy for enemy in self.__enemies if enemy.get_position().x > 0
                             and not enemy.should_delete]
        self.__enemies[:] = [enemy for enemy in self.__enemies if 720 > enemy.get_position().y > 0
                             and not enemy.should_delete]

        difference = self.__difficulty - len(self.__enemies)

        if difference > 0:
            self.add_enemies(difference)

    def render(self, brush: UIBrush):
        for bullet in self.__enemies:
            bullet.render(brush)

    def add_enemy(self, enemy_to_add):
        self.__enemies.append(enemy_to_add)

    def get_enemies(self):
        return self.__enemies

    def get_enemy_destroyed(self):
        score = 0
        for enemy in self.__enemies:
            if enemy.destroyed_by_bullet:
                score += 1
        return score


class Bullet(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(36, 24))
        image = pygame.image.load("assets/images/lvl1/8-bitBullet.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl2Bullet(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(36, 24))
        image = pygame.image.load("assets/images/lvl2/card.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl3Bullet(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(40, 27))
        image = pygame.image.load("assets/images/reverse.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl5Bullet(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(40, 27))
        image = pygame.image.load("assets/images/lvl5/ace.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl6Bullet(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(30, 50))
        image = pygame.image.load("assets/images/lvl6/bullet.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class LvlXBullet(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(50, 30))
        image = pygame.image.load("assets/images/reverse.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class BulletHandler(UIElement):
    def __init__(self, size):
        UIElement.__init__(self, Vector(), size)
        self.__bullets = []

    def update(self, delta_time: float):
        for bullet in self.__bullets:
            bullet.update(delta_time)
        self.__bullets[:] = [bullet for bullet in self.__bullets if bullet.get_position().x < self._size.x and not bullet.should_delete]
        self.__bullets[:] = [enemy for enemy in self.__bullets if bullet.get_position().x > 0 and not bullet.should_delete]

    def render(self, brush: UIBrush):
        for bullet in self.__bullets:
            bullet.render(brush)

    def add_bullet(self, bullet_to_add):
        self.__bullets.append(bullet_to_add)

    def check_collisions(self, enemy_handler):
        enemies = enemy_handler.get_enemies()
        for bullet in self.__bullets:
            for enemy in enemies:
                if bullet.does_collide_with(enemy):
                    bullet.should_delete = True
                    enemy.should_delete = True
                    enemy.destroyed_by_bullet = True


class BulletHandlerX(UIElement):
    def __init__(self, size):
        UIElement.__init__(self, Vector(), size)
        self.__bullets = []

    def update(self, delta_time: float):
        for bullet in self.__bullets:
            bullet.update(delta_time)
        self.__bullets[:] = [bullet for bullet in self.__bullets if bullet.get_position().x < self._size.x and not bullet.should_delete]
        self.__bullets[:] = [enemy for enemy in self.__bullets if bullet.get_position().x > 0 and not bullet.should_delete]

    def render(self, brush: UIBrush):
        for bullet in self.__bullets:
            bullet.render(brush)

    def add_bullet(self, bullet_to_add):
        self.__bullets.append(bullet_to_add)

    def check_collisions(self, enemy_handler):
        enemies = enemy_handler.get_enemies()
        for bullet in self.__bullets:
            for enemy in enemies:
                if bullet.does_collide_with(enemy):
                    bullet.should_delete = True
                    enemy.should_delete = True
                    enemy.destroyed_by_bullet = True


class Lvl2BulletHandler(UIElement):
    def __init__(self, size):
        UIElement.__init__(self, Vector(), size)
        self.__bullets = []

    def update(self, delta_time: float):
        for bullet in self.__bullets:
            bullet.update(delta_time)
        self.__bullets[:] = [bullet for bullet in self.__bullets if bullet.get_position().x < self._size.x and not bullet.should_delete]
        self.__bullets[:] = [enemy for enemy in self.__bullets if bullet.get_position().x > 0 and not bullet.should_delete]

    def render(self, brush: UIBrush):
        for bullet in self.__bullets:
            bullet.render(brush)

    def add_bullet(self, bullet_to_add):
        self.__bullets.append(bullet_to_add)

    def check_collisions(self, enemy_handler):
        enemies = enemy_handler.get_enemies()
        for bullet in self.__bullets:
            for enemy in enemies:
                if bullet.does_collide_with(enemy):
                    bullet.should_delete = True
                    enemy.should_delete = True
                    enemy.destroyed_by_bullet = True


class Lvl3BulletHandler(UIElement):
    def __init__(self, size):
        UIElement.__init__(self, Vector(), size)
        self.__bullets = []

    def update(self, delta_time: float):
        for bullet in self.__bullets:
            bullet.update(delta_time)
        self.__bullets[:] = [bullet for bullet in self.__bullets if bullet.get_position().x < self._size.x and not bullet.should_delete]
        self.__bullets[:] = [enemy for enemy in self.__bullets if bullet.get_position().x > 0 and not bullet.should_delete]

    def render(self, brush: UIBrush):
        for bullet in self.__bullets:
            bullet.render(brush)

    def add_bullet(self, bullet_to_add):
        self.__bullets.append(bullet_to_add)

    def check_collisions(self, enemy_handler):
        enemies = enemy_handler.get_enemies()
        for bullet in self.__bullets:
            for enemy in enemies:
                if bullet.does_collide_with(enemy):
                    bullet.should_delete = True
                    enemy.should_delete = True
                    enemy.destroyed_by_bullet = True


class BulletHandler5(UIElement):
    def __init__(self, size):
        UIElement.__init__(self, Vector(), size)
        self.__bullets = []

    def update(self, delta_time: float):
        for bullet in self.__bullets:
            bullet.update(delta_time)
        self.__bullets[:] = [bullet for bullet in self.__bullets if bullet.get_position().x < self._size.x and not bullet.should_delete]
        self.__bullets[:] = [enemy for enemy in self.__bullets if bullet.get_position().x > 0 and not bullet.should_delete]

    def render(self, brush: UIBrush):
        for bullet in self.__bullets:
            bullet.render(brush)

    def add_bullet(self, bullet_to_add):
        self.__bullets.append(bullet_to_add)

    def check_collisions(self, enemy_handler):
        enemies = enemy_handler.get_enemies()
        for bullet in self.__bullets:
            for enemy in enemies:
                if bullet.does_collide_with(enemy):
                    bullet.should_delete = True
                    enemy.should_delete = True
                    enemy.destroyed_by_bullet = True


class BulletHandler6(UIElement):
    def __init__(self, size):
        UIElement.__init__(self, Vector(), size)
        self.__bullets = []

    def update(self, delta_time: float):
        for bullet in self.__bullets:
            bullet.update(delta_time)
        self.__bullets[:] = [bullet for bullet in self.__bullets if bullet.get_position().x < self._size.x and not bullet.should_delete]
        self.__bullets[:] = [enemy for enemy in self.__bullets if bullet.get_position().x > 0 and not bullet.should_delete]

    def render(self, brush: UIBrush):
        for bullet in self.__bullets:
            bullet.render(brush)

    def add_bullet(self, bullet_to_add):
        self.__bullets.append(bullet_to_add)

    def check_collisions(self, enemy_handler):
        enemies = enemy_handler.get_enemies()
        for bullet in self.__bullets:
            for enemy in enemies:
                if bullet.does_collide_with(enemy):
                    bullet.should_delete = True
                    enemy.should_delete = True
                    enemy.destroyed_by_bullet = True


class Ship(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(80, 38))
        image = pygame.image.load("assets/images/lvl1/8-bit.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)
        self.lives = 5
        self.assault = False

    def fire(self, bullet_handler):
        bullet = Bullet(Vector(self._position.x, self._position.y))
        bullet.add_velocity(Vector(750))
        bullet_handler.add_bullet(bullet)

    def get_lives_lost(self, ship):
        if self.assault:
            self.lives = self.lives - 1
            self.assault = False
        if self.lives <= 0:
            pygame.quit()
            quit(0)
        return self.lives

    def check_enemy_collision(self, enemy_handler):
        for enemy in enemy_handler.get_enemies():
            if enemy.does_collide_with(self):
                enemy.should_delete = True
                self.assault = True
                return True
        return False


class ShipX(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(110, 52))
        image = pygame.image.load("assets/images/salmon.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)
        self.lives = 5
        self.assault = False

    def fire(self, bullet_handler):
        bullet = LvlXBullet(Vector(self._position.x, self._position.y))
        bullet.add_velocity(Vector(750))
        bullet_handler.add_bullet(bullet)

    def get_lives_lost(self, ship):
        if self.assault:
            self.lives = self.lives - 1
            self.assault = False
        if self.lives <= 0:
            pygame.quit()
            quit(0)
        return self.lives

    def check_enemy_collision(self, enemy_handler):
        for enemy in enemy_handler.get_enemies():
            if enemy.does_collide_with(self):
                enemy.should_delete = True
                self.assault = True
                return True
        return False


class Lvl3Ship(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(70, (38*0.875)))
        image = pygame.image.load("assets/images/salmon.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)
        self.lives = 4
        self.assault = False

    def fire(self, bullet_handler):
        bullet = Lvl3Bullet(Vector(self._position.x, self._position.y))
        bullet.add_velocity(Vector(950))
        bullet_handler.add_bullet(bullet)

    def get_lives_lost(self, ship):
        if self.assault:
            self.lives = self.lives - 1
            self.assault = False
        if self.lives <= 0:
            pygame.quit()
            quit(0)
        return self.lives

    def check_enemy_collision(self, enemy_handler):
        for enemy in enemy_handler.get_enemies():
            if enemy.does_collide_with(self):
                enemy.should_delete = True
                self.assault = True
                return True
        return False

    def check_enemy_collision2(self, enemy_handler2):
        for enemy in enemy_handler2.get_enemies():
            if enemy.does_collide_with(self):
                enemy.should_delete = True
                self.assault = True
                return True
        return False


class Lvl2Ship(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(80, 38))
        image = pygame.image.load("assets/images/lvl2/bruh.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)
        self.lives = 4
        self.assault = False

    def fire(self, bullet_handler):
        bullet = Lvl2Bullet(Vector(self._position.x, self._position.y))
        bullet.add_velocity(Vector(750))
        bullet_handler.add_bullet(bullet)

    def get_lives_lost(self, ship):
        if self.assault:
            self.lives = self.lives - 1
            self.assault = False
        if self.lives <= 0:
            pygame.quit()
            quit(0)
        return self.lives

    def check_enemy_collision(self, enemy_handler):
        for enemy in enemy_handler.get_enemies():
            if enemy.does_collide_with(self):
                enemy.should_delete = True
                self.assault = True
                return True
        return False


class Lvl4Ship(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(35, 33))
        image = pygame.image.load("assets/images/lvl4/heart.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)
        self.lives = 3
        self.assault = False

    def fire(self, bullet_handler):
        bullet = Lvl2Bullet(Vector(self._position.x, self._position.y))
        bullet.add_velocity(Vector(750))
        bullet_handler.add_bullet(bullet)

    def get_lives_lost(self, ship):
        if self.assault:
            self.lives = self.lives - 1
            self.assault = False
        if self.lives <= 0:
            pygame.quit()
            quit(0)
        return self.lives

    def check_enemy_collision(self, enemy_handler):
        for enemy in enemy_handler.get_enemies():
            if enemy.does_collide_with(self):
                enemy.should_delete = True
                self.assault = True
                return True
        return False

    def check_enemy_collision2(self, enemy_handler2):
        for enemy in enemy_handler2.get_enemies():
            if enemy.does_collide_with(self):
                enemy.should_delete = True
                self.assault = True
                return True
        return False

    def check_enemy_collision3(self, enemy_handler3):
        for enemy in enemy_handler3.get_enemies():
            if enemy.does_collide_with(self):
                enemy.should_delete = True
                self.assault = True
                return True
        return False


class Lvl5ship(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(125, 50))
        image = pygame.image.load("assets/images/salmon.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)
        self.lives = 4
        self.assault = False

    def fire(self, bullet_handler):
        bullet = Lvl5Bullet(Vector(self._position.x, self._position.y))
        bullet.add_velocity(Vector(900))
        bullet_handler.add_bullet(bullet)

    def get_lives_lost(self, ship):
        if self.assault:
            self.lives = self.lives - 1
            self.assault = False
        if self.lives <= 0:
            pygame.quit()
            quit(0)
        return self.lives

    def check_enemy_collision(self, enemy_handler):
        for enemy in enemy_handler.get_enemies():
            if enemy.does_collide_with(self):
                enemy.should_delete = True
                self.assault = True
                return True
        return False


class Lvl6ship(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(125, 50))
        image = pygame.image.load("assets/images/salmon.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)
        self.lives = 3
        self.assault = False

    def fire(self, bullet_handler):
        bullet = Lvl6Bullet(Vector(self._position.x, self._position.y))
        bullet.add_velocity(Vector(0, -900))
        bullet_handler.add_bullet(bullet)

    def get_lives_lost(self, ship):
        if self.assault:
            self.lives = self.lives - 1
            self.assault = False
        if self.lives <= 0:
            pygame.quit()
            quit(0)
        return self.lives

    def check_enemy_collision(self, enemy_handler):
        for enemy in enemy_handler.get_enemies():
            if enemy.does_collide_with(self):
                enemy.should_delete = True
                self.assault = True
                return True
        return False


class Lvl1Background(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(1280, 720))
        image = pygame.image.load("assets/images/lvl1/8-bitBack.jpg")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl2Background(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(1280, 720))
        image = pygame.image.load("assets/images/lvl2/dinoBackground.jpg")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl3Background(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(1280, 720))
        image = pygame.image.load("assets/images/lvl3/darkBackground.jpg")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl4Background(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(1280, 720))
        image = pygame.image.load("assets/images/lvl4/deepBack.jpg")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl5Background(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(1280, 720))
        image = pygame.image.load("assets/images/lvl5/backG.png")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class Lvl6Background(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(650, 850))
        image = pygame.image.load("assets/images/lvl6/backG.jpg")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class LvlXBackground(Sprite):
    def __init__(self, position):
        Sprite.__init__(self, position, Vector(1280, 720))
        image = pygame.image.load("assets/images/ocean.jpg")
        brush = UIBrush(self._surface)
        brush.draw_image((0.5, 0.5), (1, 1), image, scaled_mode=True)


class DifficultyBackground:
    def __init__(self, position):
        self.position = position
        self.image = pygame.image.load("assets/images/1.png")

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def render(self, brush):
        pass



