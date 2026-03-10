import arcade
import random
from grid import TileSprite
from globals import *

class MemoryGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE, update_rate=1/60, center_window=True)
        arcade.set_background_color(BG_COLOR)

        self.tile_list = arcade.SpriteList()
        self.label_list = []  # store (value, tile) for drawing text
        self.mouse_moving = False
        values = list(range(12)) * 2
        random.shuffle(values)

        for r in range(ROWS):
            for c in range(COLS):
                tile = TileSprite(c, r, values.pop())
                self.tile_list.append(tile)

        self.mouse_x = WIDTH // 2
        self.mouse_y = HEIGHT // 2

        self.selected = []
        self.all_visible = []

        self.timer = False
        self.countdown = 1
        self.clock = 0

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y
        self.mouse_moving = True

    def get_pressed_tile(self, x, y):
        for idx, tile in enumerate(self.tile_list):
            if tile.mouse_hit(x, y):
                if not tile in self.all_visible:
                    return idx
        return -1

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        idx = self.get_pressed_tile(x, y)
        if not self.timer and idx != -1 and not idx in self.selected:
            self.tile_list[idx].invisible = False
            self.selected.append(idx)
            if len(self.selected) == 2:
                self.timer = True

    def on_update(self, delta_time):
        if self.timer:
            self.clock += delta_time
            if self.clock > self.countdown:
                idx1, idx2 = self.selected
                if self.tile_list[idx1].value != self.tile_list[idx2].value:
                    self.tile_list[idx1].invisible = True
                    self.tile_list[idx2].invisible = True
                else:
                    self.all_visible.append(self.tile_list[idx1])
                    self.all_visible.append(self.tile_list[idx2])
                self.clock = 0
                self.selected = []
                self.timer = False
        if self.mouse_moving:
            for tile in self.tile_list:
                if tile.mouse_hit(self.mouse_x, self.mouse_y) and tile not in self.all_visible:
                    tile.update_wave(self.mouse_x, self.mouse_y)
                else:
                    tile.go_back()

    def on_draw(self):
        self.clear()

        # Draw all tile sprites (batched)
        self.tile_list.draw()

        # Draw value labels on top of each tile
        for tile in self.tile_list:
            if not tile.invisible:
                color = BG_COLOR
                if tile in self.all_visible:
                    color = arcade.color.WHITE
                arcade.draw_text(
                    str(tile.value),
                    tile.center_x,
                    tile.center_y,
                    color,
                    font_size=18*2,
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