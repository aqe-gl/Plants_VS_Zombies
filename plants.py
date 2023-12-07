import time

import arcade as a
import animate
import sun


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

