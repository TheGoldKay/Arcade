import arcade
from itertools import cycle

class Dino:
    def __init__(self, center_x=50, center_y=50):
        self.stand = arcade.load_texture("assets/Dino/DinoStart.png")
        self.idle = self._load_idle_texture()
        self.walk = cycle([arcade.load_texture("assets/Dino/DinoRun1.png"), 
                           arcade.load_texture("assets/Dino/DinoRun2.png")])
        self.is_walking = False
        #self.face = self.idle #arcade.Sprite("assets/Dino/DinoStart.png")
        self.face = arcade.Sprite(scale=2)
        self.face.texture = next(self.idle)
        self.face.center_x = center_x
        self.face.center_y = center_y
        self.clock = 0
        self.timer = 0.2 # wait this amount of seconds to change sprites
    
    def _load_idle_texture(self):
        idle = []
        w = 24
        i = 0
        while i < 3:
            x = i * w
            idle.append(arcade.load_texture("assets/little_dinos/male/cole/base/idle.png", x, 0, w, w))
            i += 1
        return cycle(idle)
    
    def draw(self):
        self.face.draw()
    
    def update(self, dt):
        self.clock += dt
        if self.is_walking:
            if self.clock > self.timer:
                self.clock = 0
                self.face.texture = next(self.walk)
        else:
            if self.clock > self.timer:
                self.clock = 0
                self.face.texture = next(self.idle)
                
    def set_walking(self, is_walking):
        self.is_walking = is_walking