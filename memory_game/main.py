import arcade

class Rect(object):
    def __init__(self, center_x, center_y, width, height):
        self.x = center_x
        self.y = center_y
        self.w = width
        self.h = height
        self.left = self.x - self.w // 2
        self.right = self.x + self.w // 2
        self.top = self.y + self.h // 2
        self.bottom = self.y - self.h // 2
        self.middle = (center_x, center_y)
    
def draw_tris(rect):
    #arcade.draw_triangle_filled(rect.x, rect.y, rect.left, rect.top, rect.left, rect.bottom)
    left = (rect.x, rect.y, rect.left, rect.top, rect.left, rect.bottom)
    right = (rect.x, rect.y, rect.right, rect.top, rect.right, rect.bottom)
    top = (rect.x, rect.y, rect.left, rect.top, rect.right, rect.top)
    bottom = (rect.x, rect.y, rect.left, rect.bottom, rect.right, rect.bottom)
    arcade.draw_triangle_outline(*left, color=arcade.color.BLACK)
    arcade.draw_triangle_outline(*right, color=arcade.color.BLACK)
    arcade.draw_triangle_outline(*top, color=arcade.color.BLACK)
    arcade.draw_triangle_outline(*bottom, color=arcade.color.BLACK)

class Memory(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PHTHALO_GREEN)
        self.center_window()
    

    def on_draw(self):
        arcade.start_render()
        
        rect = Rect(self.width // 2, self.height // 2, 400, 300)
        draw_tris(rect)
        arcade.draw_circle_filled(rect.x, rect.y, 5, arcade.color.WHITE)
        
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()


window = Memory(600, 400, "Phthalo Green")
arcade.run()


