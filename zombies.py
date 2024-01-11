import arcade
import animate
from constants import SCREEN_WIDTH


class Zombie(animate.Animate):
    def __init__(self, image, health, row, center_y):
        super().__init__(image, 0.09)
        self.health = health
        self.row = row
        self.set_position(SCREEN_WIDTH, center_y)
        self.change_x = -0.2

    def update(self):
        self.center_x += self.change_x
        if self.health <= 0:
            self.kill()


class Ordinary(Zombie):
    def __init__(self, row, center_y):
        super().__init__('zombies/zom1.png', 12, row, center_y)
        self.append_texture(arcade.load_texture('zombies/zom1.png'))
        self.append_texture(arcade.load_texture('zombies/zom2.png'))
        print(f'zom {self.row}')


