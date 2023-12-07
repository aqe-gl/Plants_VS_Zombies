import arcade as a
import plants
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Plants VS Zombies'
CELL_WIDTH = 78
CELL_HEIGHT = 100


def lawn_x(x):
    right_x = 240 + CELL_WIDTH
    column = 1
    while right_x <= x:
        right_x += CELL_WIDTH
        column += 1
    center_x = right_x - CELL_WIDTH / 2
    return center_x, column


def lawn_y(y):
    top_y = 29 + CELL_HEIGHT
    row = 1
    while top_y <= y:
        top_y += CELL_HEIGHT
        row += 1
    center_y = top_y - CELL_HEIGHT / 2
    return center_y, row


class Game(a.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # textures
        self.bg = a.load_texture('textures/background.jpg')
        self.menu = a.load_texture('textures/menu_vertical.png')

        # Sprite List
        self.plants = a.SpriteList()
        self.spawn_suns = a.SpriteList()

        # Fields
        self.seed = None
        self.lawns = []
        self.plant_sound = a.Sound('sounds/seed.mp3')
        self.sun = 300

    def setup(self):
        pass

    def update(self, delta_time: float):
        self.plants.update()
        self.plants.update_animation(delta_time)
        # self.spawn_suns.update()

    def on_draw(self):
        self.clear((255, 255, 255))

        a.draw_texture_rectangle(center_x=SCREEN_WIDTH / 2, center_y=SCREEN_HEIGHT / 2, width=SCREEN_WIDTH,
                                 height=SCREEN_HEIGHT, texture=self.bg)
        a.draw_texture_rectangle(67, SCREEN_HEIGHT / 2, 67 + 67, SCREEN_HEIGHT, self.menu)

        self.spawn_suns.draw()

        self.plants.draw()
        if self.seed is not None:
            self.seed.draw()

        a.draw_text(f'{self.sun}', 34, 490, (165, 42, 42), 30)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if 19 < x < 110:
            if 387 < y < 474:
                print('sunflower')
                self.seed = plants.Sunflower(self)
            if 269 < y < 360:
                print('goroshek gorohostrel')
            if 158 < y < 246:
                print('kortoshichka')
            if 42 < y < 130:
                print('derevo zgorit')

        if self.seed is not None:
            self.seed.center_x = x
            self.seed.center_y = y
            self.seed.alpha = 150

        for sun in self.spawn_suns:
            if sun.left < x < sun.right and sun.bottom < y < sun.top:
                sun.kill()
                self.sun += 25


    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if 945 >= x >= 240 and 29 <= y <= 540 and self.seed is not None:
            center_x, column = lawn_x(x)
            center_y, row = lawn_y(y)
            if (row, column) in self.lawns or self.sun < self.seed.cost:
                self.seed = None
                return
            self.lawns.append((row, column))
            self.sun -= self.seed.cost
            self.seed.planting(center_x, center_y, column, row)
            self.seed.alpha = 255
            self.plants.append(self.seed)
            self.seed = None
            self.plant_sound.play()
        else:
            self.seed = None

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.seed is not None:
            self.seed.center_x = x
            self.seed.center_y = y


game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

a.run()
