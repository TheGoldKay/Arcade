import arcade
import sys

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
        for top in range(SCREEN_HEIGHT//BOX_SIZE+1):
            for right in range(SCREEN_WIDTH//BOX_SIZE+1):
                centerx = right * BOX_SIZE - (BOX_SIZE//2)
                centery = top * BOX_SIZE - (BOX_SIZE//2)
                arcade.draw_rectangle_outline(centerx, centery, BOX_SIZE, BOX_SIZE, arcade.color.BLACK)

    def on_key_press(self, key, modifiers):       
        if key == arcade.key.ESCAPE:
            sys.exit() # close the debugger terminal and game screen at the same time

def main():
    game = Halves()
    arcade.run()

if __name__ == "__main__":
    main()
