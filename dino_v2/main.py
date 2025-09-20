import os
import arcade
from globals import *

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
    
    def on_update(self, dt):
        for ground in self.ground:
            ground.left -= BG_SPEED * dt * 3
            if ground.right < 0:
                ground.left = self.ground[1].right
                self.ground = [self.ground[1], ground]
                break 
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
    
    def on_draw(self):
        self.clear(self.background_color)
        self.sprite_list.draw()
            

game = Game()
game.setup()
arcade.run()