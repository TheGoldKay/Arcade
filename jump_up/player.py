import arcade 
from random import choice

class Player(arcade.Sprite):
    def __init__(self, support_list, vertial_vel):
        super().__init__()
        self.texture = arcade.load_texture("assets/player.png")
        support = support_list[-5]
        self.bottom = support.top
        self.center_x = support.center_x
        self.yvel = vertial_vel * 4
        self.xvel = 100
        self.avel = 5
        self.support_collison = True
    
    def on_update(self, dt, key, supports):
        print(self.center_x, self.center_y)
        if arcade.key.A == key:
            self.angle += self.avel
            self.center_x -= dt * self.xvel
        if arcade.key.D == key:
            self.angle -= self.avel
            self.center_x += dt * self.xvel
        self._place_on_support(supports)
        if self.support_collison == False:
            self.center_y -= dt * self.yvel
        if self.bottom < 0:
            self.bottom = 0
        if self.left < 0:
            self.left = 0
        if self.right > arcade.get_window().width:
            self.right = arcade.get_window().width
    
    def _place_on_support(self, supports):
        self.support_collison = False 
        for support in supports:
            if self.collides_with_sprite(support):
                self.bottom = support.top
                self.support_collison = True 