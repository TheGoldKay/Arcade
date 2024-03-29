import arcade 

class Tile(arcade.Sprite):
    def __init__(self, row=0, col=0):
        tile_texture = arcade.load_texture("assets/tile_aqua.png")
        super().__init__(texture=tile_texture)
        self.set_position(row, col)
    
    def get_size(self):
        return self.width, self.height
    
    def set_position(self, row=None, col=None):
        if col != None:
            self.left = self.width * col
        if row != None:
            self.top = self.height * (row + 1)


class Tiles(arcade.SpriteList):
    def __init__(self, tile_vel=100):
        super().__init__()
        self.vel = tile_vel
        self.last_row = 0
        test_tile = Tile()
        self.tile_width, self.tile_height = test_tile.get_size()
        self.min_lines = int(arcade.get_window().height / self.tile_height)
        self.num_col = int(arcade.get_window().width / self.tile_width)
        self.min_lines += 3
        self._set_tile_list()
        self._line_to_remove = False
    
    def _set_tile_list(self):
        for _ in range(self.min_lines):
            self._add_line()
    
    def _add_line(self):                        
        for col in range(self.num_col):
            tile = Tile(self.last_row, col)
            self.append(tile)
        self.last_row += 1
    
    def _remove_line(self):
        for tile in self:
            if tile.top <= 0:
                self.remove(tile)
           
    def update(self, dt):
        self._move_up(dt)
        if self._line_to_remove:
            self._remove_line()
            self._add_line()
    
    def _move_up(self, dt):
        self._line_to_remove = False
        for tile in self:
            tile.top -= self.vel * dt
            if tile.top <= 0:
                self._line_to_remove = True