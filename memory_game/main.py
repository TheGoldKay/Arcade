import arcade

class Memory(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PHTHALO_GREEN)
        self.center_window()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_triangle_filled(100, 100, 200, 200, 300, 100, arcade.color.BLUE_GREEN)
        
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()


window = Memory(600, 400, "Phthalo Green")
arcade.run()


