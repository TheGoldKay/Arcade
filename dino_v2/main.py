import os
import arcade
from itertools import cycle 
from globals import *

class DinoBase:
    def __init__(self):
        self.run = cycle(RUNNING)
        self.sprite = RUNNING[0]
        
    def step(self):
        self.sprite = next(self.run)
    
    def draw(self):
        pass

class Dino(arcade.Sprite):
    def __init__(self):
        super().__init__(os.path.join("Assets/Dino", "DinoRun1.png"))
        self.textures = [
            arcade.load_texture(os.path.join("Assets/Dino", "DinoRun1.png")),
            arcade.load_texture(os.path.join("Assets/Dino", "DinoRun2.png"))
        ]
        self.texture_index = 0
        self.left = 0
        self.bottom = GROUND_HEIGHT / 2
        

    def step(self):
        self.texture_index = (self.texture_index + 1) % len(self.textures)
        self.texture = self.textures[self.texture_index]

    def jump(self):
        pass
    
    def squat(self):
        pass

class Game(arcade.Window):
    def __init__(self): 
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Dino Run", center_window=True)

    def setup(self):
        self.background_color = arcade.color.WHITE_SMOKE
        self.sprite_list = arcade.SpriteList()
        self.ground = [
            arcade.Sprite(os.path.join("Assets/Other", "Track.png")),
            arcade.Sprite(os.path.join("Assets/Other", "Track.png"))
        ]
        self.ground[0].bottom = 0
        self.ground[0].left = 0
        self.ground[1].bottom = self.ground[0].bottom 
        self.ground[1].left = self.ground[0].width
        self.sprite_list.append(self.ground[0])
        self.sprite_list.append(self.ground[1])

        self.dino = Dino()
        self.sprite_list.append(self.dino)
    
    def move_ground(self, dt):
        for ground in self.ground:
            ground.left -= BG_SPEED * dt
            if ground.right < 0:
                ground.left = self.ground[1].right
                self.ground = [self.ground[1], ground]
                break
            
    def on_update(self, dt):
        #self.move_ground(dt)
        pass
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
        elif symbol == arcade.key.SPACE:
            self.dino.step()
    
    def on_draw(self):
        self.clear(self.background_color)
        self.sprite_list.draw()
            

game = Game()
game.setup()
arcade.run()