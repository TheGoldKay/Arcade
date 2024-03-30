import arcade
from supports import Supports
from tiles import Tiles

SCREEN_WIDTH = 560
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Jump Up"


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
        self.tiles = Tiles()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        self.tiles.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.tiles.update(delta_time)

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()