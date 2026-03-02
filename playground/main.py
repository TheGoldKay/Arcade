import arcade
from grid import TileSprite
from globals import *

class MemoryGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE, update_rate=1/60)
        arcade.set_background_color(BG_COLOR)

        self.tile_list = arcade.SpriteList()
        self.label_list = []  # store (value, tile) for drawing text

        for r in range(ROWS):
            for c in range(COLS):
                tile = TileSprite(c, r)
                self.tile_list.append(tile)

        self.mouse_x = WIDTH // 2
        self.mouse_y = HEIGHT // 2

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

    def on_update(self, delta_time):
        for tile in self.tile_list:
            tile.update_wave(self.mouse_x, self.mouse_y)

    def on_draw(self):
        self.clear()

        # Draw all tile sprites (batched)
        self.tile_list.draw()

        # Draw value labels on top of each tile
        for tile in self.tile_list:
            arcade.draw_text(
                str(tile.value),
                tile.center_x,
                tile.center_y,
                arcade.color.WHITE,
                font_size=18,
                bold=True,
                anchor_x="center",
                anchor_y="center",
                rotation=tile.angle,
            )


def main():
    game = MemoryGame()
    arcade.run()


if __name__ == "__main__":
    main()