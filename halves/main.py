import arcade
import sys

sys.path.append("/home/goldkay/Code/Arcade/helper")

from coordinates import centerTopRight

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Halves"
BACKGROUND_COLOR = arcade.color.PHTHALO_GREEN
BOX_SIZE = 25

class Halves(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, center_window=True)
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        arcade.start_render()
        for y in range(1, SCREEN_HEIGHT//BOX_SIZE+1):
            for x in range(1, SCREEN_WIDTH//BOX_SIZE+1):
                top = y * BOX_SIZE
                right = x * BOX_SIZE
                centerx, centery = centerTopRight(top, right, BOX_SIZE, BOX_SIZE)
                arcade.draw_rectangle_outline(centerx, centery, BOX_SIZE, BOX_SIZE, arcade.color.BLACK)

    def on_key_press(self, key, modifiers):       
        if key == arcade.key.ESCAPE:
            sys.exit() # close the debugger terminal and game screen at the same time

def main():
    halves = Halves()
    halves.run()

if __name__ == "__main__":
    main()
