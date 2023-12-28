import arcade

SCREEN: dict = {
    "width": 1000, 
    "height": 650, 
    "title": "Platformer",     
    "center_window": True,  
}

COLOR: dict = {
    "background": arcade.csscolor.DARK_GREEN,
}

class MyGame(arcade.Window):
    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(**SCREEN)

        arcade.set_background_color(COLOR["background"])

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        self.clear()
        # Code to draw the screen goes here
    
    def on_key_press(self, key: int, modifier: int):
        # Modifier-EXAMPLE: modifier & arcade.key.MOD_SHIFT -> close only if the Shift is also being pressed
        if key == arcade.key.ESCAPE and modifier & arcade.key.MOD_SHIFT:
            print(modifier)
            arcade.close_window()

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()