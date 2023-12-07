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
    def __init__(self):
        super().__init__('plants/pea1.png', 100, 100)
        for i in range(1, 4):
            self.append_texture(a.load_texture(f'plants/pea{i}.png'))


class Pea(a.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__('items/bul.png', 0.12)
        self.set_position(center_x, center_y)
        self.damage = 1
        self.change_x = 7

    def update(self):
        self.center_x += self.change_x
        if self.center_x > SCREEN_WIDTH:
            self.kill()


