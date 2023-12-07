import arcade


class Sun(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__('items/sun.png', 0.12)
        self.center_x = center_x
        self.center_y = center_y

    def update(self):
        self.angle += 1