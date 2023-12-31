import arcade
from itertools import cycle

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
    "img_idle": ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
    "img_jump": ":resources:images/animated_characters/female_adventurer/femaleAdventurer_jump.png",
    "img_walk": ":resources:images/animated_characters/female_adventurer/femaleAdventurer_walk{}.png",
    "speed": 5,
    "jump": 80,
}

# Constants used to scale sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
GRAVITY = 3

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
        self.on_ground = True
        
        # walk
        self.walk_timer = 0.09
        self.walk_clock = 0
        
        # CAMERA    
        self.camera = None
        
        # flip
        self.flipped_horizontally = False
        self.going_right = True

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Initialize Scene
        self.scene = arcade.Scene()

        # Create the Sprite lists
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)

        # set left and right facing sprites
        self.idle_texture = [arcade.load_texture(PLAYER["img_idle"]), 
                             arcade.load_texture(PLAYER["img_idle"], flipped_horizontally=True)]
        self.jump_texture = [arcade.load_texture(PLAYER["img_jump"]), 
                             arcade.load_texture(PLAYER["img_jump"], flipped_horizontally=True)]
        self.idle_right = True
        self.walk_textures = cycle([
            [arcade.load_texture(PLAYER["img_walk"].format(i)), 
             arcade.load_texture(PLAYER["img_walk"].format(i), flipped_horizontally=True)] 
            for i in range(8)])
        # set player sprite
        self.player_sprite = arcade.Sprite(PLAYER["img_idle"], CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        # Add the player to the scene
        self.scene.add_sprite("Player", self.player_sprite)
        
        #create ``physics engine``
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene.get_sprite_list("Walls")
        )
        
        # better keyboard handling
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        
        # camera
        self.camera = arcade.Camera(self.width, self.height)
        
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
            
    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)

        # Don't let camera travel past 0, 0
        player_centered = max(screen_center_x, 0), max(screen_center_y, 0)

        self.camera.move_to(player_centered)

    def on_draw(self):
        self.clear()
        # Draw our sprites
        self.scene.draw()
        self.camera.use()
    
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
        self.move_player(dt)
        self.check_ground_level()
        self.center_camera_to_player()

    def move_player(self, dt):
        if self.right_pressed or self.left_pressed:
            self.walk_clock += dt   
            if self.walk_clock > self.walk_timer:
                self.walk_clock = 0
                texture_pair = next(self.walk_textures)
                if self.going_right:
                    self.player_sprite.texture = texture_pair[0]
                else:
                    self.player_sprite.texture = texture_pair[1]
        elif self.on_ground:
            if self.going_right:
                self.player_sprite.texture = self.idle_texture[0]        
            else:
                self.player_sprite.texture = self.idle_texture[1]
        
    def check_ground_level(self, y_distance: float = 5):
        # break at the first collision
        for wall in self.scene["Walls"]:
            if wall.guid == "box":
                if arcade.check_for_collision(self.player_sprite, wall):
                    # the player is on top of the box
                    if self.player_sprite.center_y > wall.top:
                        self.player_sprite.bottom = wall.top
                        self.on_ground = True
                        break
                    else:
                        # the player is to the left of the box
                        if self.player_sprite.right > wall.left and self.player_sprite.left < wall.left:
                            self.player_sprite.right = wall.left
                            self.on_ground = True
                            break
                        # player is at the right of the box (there are only three possibilities)                        
                        else: 
                            self.player_sprite.left = wall.right
                            self.on_ground = True
                            break
            if arcade.check_for_collision(self.player_sprite, wall):
                self.player_sprite.bottom = wall.top
                self.on_ground = True
                break 
        

    def on_key_press(self, key: int, modifier: int):
        # Modifier-EXAMPLE: modifier & arcade.key.MOD_SHIFT -> close only if the Shift is also being pressed
        if key == arcade.key.ESCAPE:
            arcade.close_window()
        if key == arcade.key.UP or key == arcade.key.W: # JUMP ONE TIME
            self.player_sprite.center_y += PLAYER["jump"]
            self.on_ground = False
            if self.going_right:
                self.player_sprite.texture = self.jump_texture[0]
            else:
                self.player_sprite.texture = self.jump_texture[1]
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
            self.going_right = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True 
            self.going_right = True

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