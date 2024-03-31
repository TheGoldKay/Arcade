import arcade 
from random import choice

class Supports(arcade.SpriteList):
    def __init__(self, tiles, speed):
        super().__init__()
        self.list = [
            arcade.load_texture("assets/supports/grass.png"),
            arcade.load_texture("assets/supports/green_rope.png"),
            arcade.load_texture("assets/supports/ground.png"),
            arcade.load_texture("assets/supports/small_grass.png"),
            arcade.load_texture("assets/supports/small_ground.png"),
            arcade.load_texture("assets/supports/wood.png"),
        ]
        self._place_supports(tiles)
        self.vel = speed 
        
    
    def _place_supports(self, tiles):
        # set the position of the supports based on tile's position
        # supports will be placed on top of the tiles
        for line in tiles:
            self.new_support(line)
    
    def new_support(self, line):
        tile = choice(line)
        support = arcade.Sprite()
        support.texture = choice(self.list)
        support.bottom = tile.top
        support.center_x = tile.center_x
        support.scale = 2
        self.append(support)
            
    def update(self, dt):
        for support in self:
            support.top -= self.vel * dt
            if support.top <= 0:
                self.remove(support)