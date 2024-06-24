import arcade
import math

# Define a custom function to rotate a point
def custom_rotate_point(point, angle):
    x, y = point
    angle_rad = math.radians(angle)
    new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return {x: new_x, y: new_y}
class Rect(object):
    def __init__(self, center_x, center_y, width, height):
        self.x = center_x
        self.y = center_y
        self.w = width
        self.h = height
        self.rect_left = self.x - self.w // 2
        self.rect_right = self.x + self.w // 2
        self.rect_top = self.y - self.h // 2
        self.rect_bottom = self.y + self.h // 2
    
    def draw(self):
        arcade.draw_lrtb_rectangle_outline(self.rect_left, self.rect_right, 
                                           self.rect_bottom, self.rect_top, arcade.color.BLACK)


class Memory(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PHTHALO_GREEN)
        self.center_window()
    

    def on_draw(self):
        arcade.start_render()
        
        rect = Rect(self.width // 2, self.height // 2, 400, 300)
        rect.draw()
        center_x = self.width // 2
        center_y = self.height // 2
        arcade.draw_circle_filled(center_x, center_y, 5, arcade.color.BLACK)
        
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()


window = Memory(600, 400, "Phthalo Green")
arcade.run()


