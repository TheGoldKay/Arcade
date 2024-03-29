import arcade 

class Tile(arcade.Sprite):
    def __init__(self):
        tile_texture = arcade.load_texture("assets/tile_aqua.png")
        super().__init__(texture=tile_texture)
    
    def get_size(self):
        return self.width, self.height
    
    def set_position(self, row, col):
        self.left = self.width * col
        self.top = self.height * (row + 1)


class Tiles(arcade.SpriteList):
    def __init__(self):
        super().__init__()
        test_tile = Tile()
        width, height = test_tile.get_size()
        window_width = arcade.get_window().width
        window_height = arcade.get_window().height
        for row in range(int(window_height / height)):
            for col in range(int(window_width / width)):
                tile = Tile()
                tile.set_position(row, col)
                self.append(tile)