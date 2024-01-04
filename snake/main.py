import arcade
import snake

class GameScreen(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, center_window=True)
        self.background_color = (18, 53, 36)  # phthalo green

    def setup(self):
        self.snake = snake.Snake()
        self.grid = self.get_grid()
    
    def get_grid(self):
        pass
    
    def draw_grid(self):
        pass
    
    def on_draw(self):
        self.clear()
        self.draw_grid()
        self.snake.draw()
    
    def update_grid(self):
        pass

    def on_update(self, delta_time):
        self.snake.update(delta_time)
        self.update_grid()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.close_window()
            
def main():
    window = GameScreen(800, 600, "Snake Game")
    window.setup()
    arcade.run()
    

if __name__ == "__main__":
    main()