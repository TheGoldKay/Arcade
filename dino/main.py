import arcade, sys
from dino import Dino 

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, center_window=True)
        self.background_color = arcade.color.WHITE
        self.ground = None        
        self.dino = None
    
    def setup(self):
        self.ground = arcade.Sprite("assets/ground.png")
        self.ground.left = 0
        self.ground.bottom = 0
        self.dino = Dino()

        
    def on_draw(self):
        self.clear()
        self.ground.draw()
        self.dino.draw()

    def on_update(self, delta_time):
        self.dino.update(delta_time)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()
        if key == arcade.key.D:
            self.dino.set_walking(True)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.D:
            self.dino.set_walking(False)


def main():
    window = Game(1000, 500, "Dino")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()