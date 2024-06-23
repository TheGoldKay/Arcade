import arcade
import math

# Define a custom function to rotate a point
def custom_rotate_point(point, angle):
    x, y = point
    angle_rad = math.radians(angle)
    new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return {x: new_x, y: new_y}


class Memory(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PHTHALO_GREEN)
        self.center_window()
    

    def on_draw(self):
        arcade.start_render()
        
        center_x = self.width // 2
        center_y = self.height // 2
        arcade.draw_circle_filled(center_x, center_y, 5, arcade.color.BLACK)
        
        
        rect_center_x = self.width // 2
        rect_center_y = self.height // 2
        rect_width = 400
        rect_height = 300
        rect_left = rect_center_x - rect_width // 2
        rect_right = rect_center_x + rect_width // 2
        rect_top = rect_center_y - rect_height // 2
        rect_bottom = rect_center_y + rect_height // 2

        arcade.draw_lrtb_rectangle_outline(rect_left, rect_right, rect_bottom, rect_top, arcade.color.BLACK)
        
        
        
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()


window = Memory(600, 400, "Phthalo Green")
arcade.run()


