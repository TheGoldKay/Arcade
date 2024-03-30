import arcade 

class Tile(arcade.Sprite):
    def __init__(self, row=None, col=None, pos=(None, None)):
        tile_texture = arcade.load_texture("assets/tile_aqua.png")
        super().__init__(texture=tile_texture)
        if pos == (None, None):
            self.set_position(row, col)
        else:
            self.set_bottom_left(pos[0], pos[1])
    
    def get_size(self):
        return self.width, self.height
    
    def set_position(self, row=None, col=None):
        if col != None:
            self.left = self.width * col
        if row != None:
            self.top = self.height * (row + 1)
        
    def set_bottom_left(self, bottom, left):
        self.bottom = bottom
        self.left = left 


class Tiles(arcade.SpriteList):
    def __init__(self, tile_vel=100):
        super().__init__()
        self.vel = tile_vel
        test_tile = Tile()
        self.tile_width, self.tile_height = test_tile.get_size()
        self.min_lines = int(arcade.get_window().height / self.tile_height)
        self.num_col = int(arcade.get_window().width / self.tile_width)
        self.min_lines += 3
        # a list of list, each list is a line, each line with a list of tiles
        self.list = self._set_tile_list()
    
    def _set_tile_list(self):
        return list(map(lambda row: self._new_line(row=row), range(self.min_lines)))

    def _new_line(self, row=None, bottom=None):
        if bottom == None:
            return self._add_line(row)
        elif row == None:
            return self._update_line(bottom)
        else:
            raise Exception('bottom and row cannot be both None')
    
    def _add_line(self, row):       
        return list(map(lambda col: Tile(row, col), range(self.num_col)))
    
    def _update_line(self, bottom):
        return list(map(lambda tile: Tile(pos=(bottom, tile.left)), self.list[-1]))

    def _remove_line(self):
        # remove the first line (the one at the bottom) if it's below the window max height (check only one)
        # then add a new line at the top (set the bottom of the last as the top of the previous last line)
        if self.list[0][0].top <= 0:
            self.list.pop(0)
            bottom = self.list[-1][-1].top
            self.list.append(self._new_line(bottom=bottom))
           
    def update(self, dt):
        self._move_up(dt)
        self._remove_line()
    
    def draw(self):
        for line in self.list:
            for tile in line:
                tile.draw()
    
    def _move_up(self, dt):
        for line in self.list:
            for tile in line:
                tile.top -= self.vel * dt