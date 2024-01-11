import time

import arcade as a
import animate
import sun
from constants import SCREEN_WIDTH


class Plant(animate.Animate):
    def __init__(self, image, health, cost):
        super().__init__(image, 0.12)

        self.health = health
        self.cost = cost
        self.row = 0
        self.column = 0

    def update(self):
        if self.health <= 0:
            self.kill()

    def planting(self, center_x, center_y, row, column):
        self.set_position(center_x, center_y)
        self.row = row
        self.column = column


class Sunflower(Plant):
    def __init__(self, window):
        super().__init__('plants/sun1.png', 80, 50)
        self.append_texture(a.load_texture('plants/sun1.png'))
        self.append_texture(a.load_texture('plants/sun2.png'))
        self.sun_spawn_time = time.time()
        self.window = window

    def update(self):
        if time.time() - self.sun_spawn_time > 14:
            new_sun = sun.Sun(self.right, self.top)
            self.sun_spawn_time = time.time()
            self.window.spawn_suns.append(new_sun)
        self.window.spawn_suns.update()


class Gorohostrel(Plant):
    def __init__(self, window):
        super().__init__('plants/pea1.png', 100, 100)
        for i in range(1, 4):
            self.append_texture(a.load_texture(f'plants/pea{i}.png'))

        self.pea_spawn_time = time.time()
        self.window = window
        self.zombie_online = False

    def update(self):

        for zombie in self.window.zombie_list:
            print(zombie.row)
            if zombie.row == self.row:
                self.zombie_online = True
                break
            self.zombie_online = False
        if time.time() - self.pea_spawn_time > 2:
            print(f'test {self.row}')
            new_pea = Pea(self.center_x, self.center_y, self.window)
            self.pea_spawn_time = time.time()
            self.window.peas.append(new_pea)




class Pea(a.Sprite):
    def __init__(self, center_x, center_y, window):
        super().__init__('items/bul.png', 0.12)
        self.set_position(center_x, center_y)
        self.damage = 1
        self.change_x = 7
        self.window = window

    def update(self):
        self.center_x += self.change_x
        if self.center_x > SCREEN_WIDTH:
            self.kill()

        zombies = a.check_for_collision_with_list(self, self.window.zombie_list)
        for zombie in zombies:
            zombie.health -= self.damage
            self.kill()


