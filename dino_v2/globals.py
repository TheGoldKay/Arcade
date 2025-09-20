import arcade 
import os 

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

RUNNING = [arcade.Sprite(os.path.join("Assets/Dino", "DinoRun1.png")),
           arcade.Sprite(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = arcade.Sprite(os.path.join("Assets/Dino", "DinoJump.png"))
DUCKING = [arcade.Sprite(os.path.join("Assets/Dino", "DinoDuck1.png")),
           arcade.Sprite(os.path.join("Assets/Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [arcade.Sprite(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                arcade.Sprite(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                arcade.Sprite(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [arcade.Sprite(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                arcade.Sprite(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                arcade.Sprite(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [arcade.Sprite(os.path.join("Assets/Bird", "Bird1.png")),
        arcade.Sprite(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = arcade.Sprite(os.path.join("Assets/Other", "Cloud.png"))

BG = arcade.Sprite(os.path.join("Assets/Other", "Track.png"))
BG_SPEED = 100