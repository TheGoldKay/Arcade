import arcade, sys

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, center_window=True)
        self.background_color = arcade.color.GRAY
        self.ground = None        
    
    def setup(self):
        self.ground = arcade.Sprite("assets/ground.png")
        self.ground.left = 0
        self.ground.bottom = 0

    def on_draw(self):
        self.clear()
        self.ground.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()


def main():
    window = Game(1000, 500, "Dino")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()