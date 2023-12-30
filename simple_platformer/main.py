import arcade

# https://api.arcade.academy/en/latest/api/window.html#arcade.Window
SCREEN: dict = {
    "width": 1000, 
    "height": 650, 
    "title": "Platformer",     
    "center_window": True,  
}

COLOR: dict = {
    "background": arcade.csscolor.DARK_GREEN,
}

# Constants used to scale sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

class MyGame(arcade.Window):
    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(**SCREEN)
        arcade.set_background_color(COLOR["background"])

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Initialize Scene
        self.scene = arcade.Scene()

        # Create the Sprite lists
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)

        # Put some crates on the ground
        # This shows using a coordinate list to place sprites
        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", TILE_SCALING
            )
            wall.position = coordinate
            self.scene.add_sprite("Walls", wall)

    def on_draw(self):
        self.clear()
        # Draw our sprites
        self.scene.draw()
    
    def on_key_press(self, key: int, modifier: int):
        # Modifier-EXAMPLE: modifier & arcade.key.MOD_SHIFT -> close only if the Shift is also being pressed
        if key == arcade.key.ESCAPE:
            arcade.close_window()

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()