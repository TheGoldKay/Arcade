import arcade
from itertools import cycle

class Dino:
    def __init__(self, center_x=50, center_y=50):
        self.stand = arcade.load_texture("assets/Dino/DinoStart.png")
        self.walk = cycle([arcade.load_texture("assets/Dino/DinoRun1.png"), 
                           arcade.load_texture("assets/Dino/DinoRun2.png")])
        self.is_walking = False
        self.face = arcade.Sprite("assets/Dino/DinoStart.png")
        self.face.center_x = center_x
        self.face.center_y = center_y
        self.clock = 0
        self.timer = 0.2 # wait this amount of seconds to change sprites
    
    def draw(self):
        self.face.draw()
    
    def update(self, dt):
        if self.is_walking:
            self.clock += dt
            if self.clock > self.timer:
                self.clock = 0
                self.face.texture = next(self.walk)
        else:
            self.face.texture = self.stand
                
    def set_walking(self, is_walking):
        self.is_walking = is_walking