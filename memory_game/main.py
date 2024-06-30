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

class TriangleFormation(object):
    def __init__(self, rect):
        self.left = {"pos": (rect.x, rect.y, rect.left, rect.top, rect.left, rect.bottom), "on": False}
        self.right = {"pos":(rect.x, rect.y, rect.right, rect.top, rect.right, rect.bottom), "on": False}
        self.top = {"pos": (rect.x, rect.y, rect.left, rect.top, rect.right, rect.top), "on": False}
        self.bottom = {"pos": (rect.x, rect.y, rect.left, rect.bottom, rect.right, rect.bottom), "on": False}
    
    def draw(self):
        if self.left["on"]:
            arcade.draw_triangle_filled(*self.left["pos"], color=arcade.color.WHITE)
        else:
            arcade.draw_triangle_outline(*self.left["pos"], color=arcade.color.BLACK)
        if self.right["on"]:
            arcade.draw_triangle_filled(*self.right["pos"], color=arcade.color.WHITE)
        else:
            arcade.draw_triangle_outline(*self.right["pos"], color=arcade.color.BLACK)
        if self.top["on"]:
            arcade.draw_triangle_filled(*self.top["pos"], color=arcade.color.WHITE)
        else:
            arcade.draw_triangle_outline(*self.top["pos"], color=arcade.color.BLACK)
        if self.bottom["on"]:
            arcade.draw_triangle_filled(*self.bottom["pos"], color=arcade.color.WHITE)
        else:
            arcade.draw_triangle_outline(*self.bottom["pos"], color=arcade.color.BLACK)

class Memory(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.PHTHALO_GREEN)
        self.center_window()
        self.setup()
    
    def setup(self):
        print("over here")
        self.rect = Rect(self.width // 2, self.height // 2, 400, 300)
        self.tri = TriangleFormation(self.rect)
        self.seq = []
        
    def on_draw(self):
        arcade.start_render()
        self.tri.draw()
        arcade.draw_circle_filled(self.rect.x, self.rect.y, 5, arcade.color.WHITE)
        
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
        if symbol == arcade.key.LEFT:
            self.tri.left["on"] = not self.tri.left["on"]
        if symbol == arcade.key.RIGHT:
            self.tri.right["on"] = not self.tri.right["on"]
        if symbol == arcade.key.UP:
            self.tri.top["on"] = not self.tri.top["on"]
        if symbol == arcade.key.DOWN:
            self.tri.bottom["on"] = not self.tri.bottom["on"]
        if symbol == arcade.key.SPACE:
            self.seq = []


window = Memory(600, 400, "Phthalo Green")
arcade.run()


