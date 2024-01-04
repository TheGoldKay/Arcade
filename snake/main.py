import arcade, random
from typing import Tuple, List, Dict, Any
import snake

WIN_WIDTH: int = 800
WIN_HEIGHT: int = 600
BG_COLOR: Tuple[int, int, int] = (18, 53, 36) # phthalo green RGB
BOX_SIZE: int = 20
BOX_W: int = WIN_WIDTH // BOX_SIZE
BOX_H: int = WIN_HEIGHT // BOX_SIZE

class GameScreen(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, center_window=True)
        self.background_color = BG_COLOR 

    def setup(self):
        self.snake = snake.Snake(BOX_W // 2, BOX_H // 2, BOX_SIZE)
        self.grid = self.get_grid()
    
    def get_grid(self) -> List[List[Dict]]:
        grid: List[List[Dict]] = []
        for row in range(BOX_H):
            line: List[Dict] = []
            for col in range(BOX_W):
                box: Dict = {"r": row, "c": col}
                box["filled"] = False
                line.append(box)
            grid.append(line)
        return grid
        
    
    def draw_grid(self) -> None:
        for line in self.grid:
            for box in line:
                x: int = box["c"] * BOX_SIZE
                y: int = box["r"] * BOX_SIZE
                # setting the center (Arcade draws from the center_x and center_y)
                x += BOX_SIZE // 2
                y += BOX_SIZE // 2
                if box["filled"]:
                    arcade.draw_rectangle_filled(x, y, BOX_SIZE, BOX_SIZE, arcade.color.RED)
                else:
                    arcade.draw_rectangle_outline(x, y, BOX_SIZE, BOX_SIZE, arcade.color.WHITE)
    
    def on_draw(self):
        self.clear()
        self.draw_grid()
        self.snake.draw()

    def on_update(self, delta_time):
        self.snake.update(delta_time)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()
        elif key == arcade.key.W and self.snake.get_yvel() != -1:
            self.snake.set_yvel(1)
            self.snake.set_xvel(0)
        elif key == arcade.key.S and self.snake.get_yvel() != 1:
            self.snake.set_yvel(-1)
            self.snake.set_xvel(0)
        elif key == arcade.key.A and self.snake.get_xvel() != 1:
            self.snake.set_xvel(-1)
            self.snake.set_yvel(0)
        elif key == arcade.key.D and self.snake.get_xvel() != -1:
            self.snake.set_xvel(1)
            self.snake.set_yvel(0)
            
def main():
    window = GameScreen(WIN_WIDTH, WIN_HEIGHT, "Snake Game")
    window.setup()
    arcade.run()
    

if __name__ == "__main__":
    main()