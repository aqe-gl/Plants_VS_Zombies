import arcade as a
import animate


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
    def __init__(self):
        super().__init__('plants/sun1.png', 80, 50)
        self.append_texture(a.load_texture('plants/sun1.png'))
        self.append_texture(a.load_texture('plants/sun2.png'))

