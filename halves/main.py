import arcade
import sys

sys.path.append("/home/goldkay/Code/Arcade/helper")

from coordinates import centerTopRight

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Halves"
BACKGROUND_COLOR = arcade.color.PHTHALO_GREEN
LINE_COLOR =(BACKGROUND_COLOR[0] + 50, BACKGROUND_COLOR[1] + 50, BACKGROUND_COLOR[2] + 50)
BOX_SIZE = 25
NWIDTH = SCREEN_WIDTH//BOX_SIZE
NHEIGHT = SCREEN_HEIGHT//BOX_SIZE

def middle():
    cx = ((NWIDTH + 1) //  2) * BOX_SIZE - BOX_SIZE // 2
    for y in range(1, NHEIGHT+1):
        cy = y * BOX_SIZE - BOX_SIZE // 2
        arcade.draw_rectangle_filled(cx, cy, BOX_SIZE, BOX_SIZE, LINE_COLOR)

class Halves(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, center_window=True)
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        arcade.start_render()
        
        middle()
        for y in range(1, NHEIGHT+1):
            for x in range(1, NWIDTH+1):
                top = y * BOX_SIZE
                right = x * BOX_SIZE
                centerx, centery = centerTopRight(top, right, BOX_SIZE, BOX_SIZE)
                arcade.draw_rectangle_outline(centerx, centery, BOX_SIZE, BOX_SIZE, arcade.color.BLACK)

        arcade.finish_render()
    def on_key_press(self, key, modifiers):       
        if key == arcade.key.ESCAPE:
            sys.exit() # close the debugger terminal and game screen at the same time

def main():
    halves = Halves()
    halves.run()

if __name__ == "__main__":
    main()
