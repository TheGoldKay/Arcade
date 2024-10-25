import arcade
import sys

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Halves"
BACKGROUND_COLOR = arcade.color.PHTHALO_GREEN

class Halves(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, center_window=True)
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        arcade.start_render()

    def on_key_press(self, key, modifiers):       
        if key == arcade.key.ESCAPE:
            sys.exit() # close the debugger terminal and game screen at the same time

def main():
    game = Halves()
    arcade.run()

if __name__ == "__main__":
    main()
