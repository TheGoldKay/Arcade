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

PLAYER: dict = {
    "img_path": ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
    "speed": 5,
    "jump": 20,
}

# Constants used to scale sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
GRAVITY = 4

class MyGame(arcade.Window):
    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(**SCREEN)
        arcade.set_background_color(COLOR["background"])

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None
        
        # our physics engine
        self.physics_engine = None
        
        # others
        self.ground_level = 0
        self.can_jump = True
        self.jump_counter = 0
        self.jump_limit = 2

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Initialize Scene
        self.scene = arcade.Scene()

        # Create the Sprite lists
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite(PLAYER["img_path"], CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)
        
        # create ``physics engine``
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene.get_sprite_list("Walls")
        )
        
        # better keyboard handling
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        
        # define ground level 
        ground_tile = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
        self.ground_level = 32 + ground_tile.height / 2

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
            wall.guid = "box"
            self.scene.add_sprite("Walls", wall)
            #print(wall.guid)

    def on_draw(self):
        self.clear()
        # Draw our sprites
        self.scene.draw()
    
    def on_update(self, dt):
        # Move the player with the physics engine
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.check_ground_level()
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER["speed"]
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER["speed"]
        self.physics_engine.update()
        self.check_ground_level()
        
    def check_ground_level(self, y_distance: float = 5):
        self.can_jump = False
        for wall in self.scene["Walls"]:
            if wall.guid == "box":
                if arcade.check_for_collision(self.player_sprite, wall):
                    # the player is on top of the box
                    if self.player_sprite.center_y > wall.top:
                        self.player_sprite.bottom = wall.top
                        return
                    else:
                        # the player is to the left of the box
                        if self.player_sprite.right > wall.left and self.player_sprite.left < wall.left:
                            self.player_sprite.right = wall.left
                            return
                        # player is at the right of the box (there are only three possibilities)                        
                        else: 
                            self.player_sprite.left = wall.right
                            return
            if arcade.check_for_collision(self.player_sprite, wall):
                self.player_sprite.bottom = wall.top
                self.can_jump = True
                return 
        

    def on_key_press(self, key: int, modifier: int):
        # Modifier-EXAMPLE: modifier & arcade.key.MOD_SHIFT -> close only if the Shift is also being pressed
        if key == arcade.key.ESCAPE:
            arcade.close_window()
        if key == arcade.key.UP or key == arcade.key.W: # JUMP ONE TIME
            self.player_sprite.center_y += PLAYER["jump"] * 5
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True 

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False 

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()