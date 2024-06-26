import arcade
from supports import Supports
from tiles import Tiles
from player import Player

SCREEN_WIDTH = 560
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Jump Up"
SPEED = 50


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)
        
        # centering the game's window
        # THE SAME COULD BE ACHIEVED WITH: super().__init__(center_window=True) - but I like to be explicit here
        monitor = arcade.get_screens()[0] # get the primary monitor
        self.set_location(monitor.width // 2 - SCREEN_WIDTH // 2, monitor.height // 2 - SCREEN_HEIGHT // 2)
        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        self.tiles = Tiles(SPEED)
        self.supports = Supports(self.tiles.get_tiles(), SPEED)
        self.player = Player(self.supports.get_supports(), SPEED)
        self.key_pressed = None # last key pressed

    def on_draw(self):
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        self.tiles.draw()
        self.supports.draw()
        self.player.draw()

    def on_update(self, delta_time):
        self.tiles.update(delta_time)
        self.supports.update(delta_time)
        if self.tiles.removed:
            self.supports.new_support(self.tiles.get_tiles()[-1])
        self.player.on_update(delta_time, self.key_pressed, self.supports.get_supports())

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()
        self.key_pressed = key
        
    def on_key_release(self, key, key_modifiers):
        if key == self.key_pressed:
            self.key_pressed = None

def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()