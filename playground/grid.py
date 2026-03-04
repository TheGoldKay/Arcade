"""
The grid will have the floating window effect.

As the cursor hovers over the tiles they will
tilt and form a wave as the mause moves.

They must tilt (incline) in the direction the
cursor's pointer lays.

In order to achive all that, the square tile
must move through a false sense of depth.
"""
import math, arcade
from globals import *


class TileSprite(arcade.Sprite):
    def __init__(self, col, row):
        super().__init__("tile.png")

        self.col = col
        self.row = row
        self.value = (col + row * COLS) % 8 + 1

        # Scale sprite to fit TILE_W x TILE_H
        self.width = TILE_W
        self.height = TILE_H

        # Base center position (Arcade: Y from bottom)
        self.base_x, self.base_y = self.initial_pos()
        self.base_pos = self.base_x, self.base_y

        self.center_x = self.base_x
        self.center_y = self.base_y

        # Animated state
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.tilt = 0.0
        self.current_scale = 1.0

        # Targets
        self.target_ox = 0.0
        self.target_oy = 0.0
        self.target_tilt = 0.0
        self.target_scale = 1.0

    def initial_pos(self):
        return (START_X + self.col * (TILE_W + GAP) + TILE_W // 2,
                HEIGHT - (START_Y + self.row * (TILE_H + GAP) + TILE_H // 2))

    def go_back(self):
        self.center_x, self.center_y = self.initial_pos()
        #self.tilt = 0.0
        self.angle = 0.0

    def mouse_hit(self, mouse_x, mouse_y):
        left = self.center_x - self.width / 2
        right = self.center_x + self.width / 2
        bottom = self.center_y - self.height / 2
        top = self.center_y + self.height / 2

        return left <= mouse_x <= right and bottom <= mouse_y <= top

    def update_wave(self, mouse_x, mouse_y):
        dx = mouse_x - self.base_x
        dy = mouse_y - self.base_y
        dist = math.sqrt(dx * dx + dy * dy)

        # Cosine falloff within wave radius
        if dist < WAVE_RADIUS:
            influence = math.cos((dist / WAVE_RADIUS) * (math.pi / 2))
        else:
            influence = 0.0

        if dist > 0.1:
            norm_x = dx / dist
            norm_y = dy / dist
        else:
            norm_x = norm_y = 0.0

        # Tiles lean and shift toward mouse
        self.target_ox = norm_x * (TILE_W * 0.1) * influence
        self.target_oy = norm_y * (TILE_H * 0.1) * influence
        self.target_tilt = norm_x * MAX_TILT * influence
        self.target_scale = 1.0 + MAX_SCALE_BOOST * influence

        # Lerp everything
        self.offset_x    += (self.target_ox    - self.offset_x)    * SMOOTHING
        self.offset_y    += (self.target_oy    - self.offset_y)    * SMOOTHING
        self.tilt        += (self.target_tilt  - self.tilt)        * SMOOTHING
        self.current_scale += (self.target_scale - self.current_scale) * SMOOTHING

        # Apply to sprite
        self.center_x = self.base_x + self.offset_x
        self.center_y = self.base_y + self.offset_y
        self.angle = self.tilt
        self.width  = TILE_W * self.current_scale
        self.height = TILE_H * self.current_scale