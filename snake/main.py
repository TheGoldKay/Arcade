import arcade
import snake

class GameScreen(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        pass

    def on_draw(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        pass

def main():
    window = GameScreen(800, 600, "Snake Game")
    window.setup()
    arcade.run()
    

if __name__ == "__main__":
    main()