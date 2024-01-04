import arcade 

class Snake:
    def __init__(self, row, col, size):
        # index 0 is the head
        self.body = [{"r": row, "c": col+i} for i in range(3)]
        self.xvel = -1
        self.yvel = 0
        self.size = size
        # regulate the snake's update speed
        self.clock = 0 
        # time to wait before moving a single box (block) in either direction
        self.timer = 0.2
        
    def get_xvel(self):
        return self.xvel
    
    def get_yvel(self):
        return self.yvel
    
    def set_xvel(self, nxvel):
        self.xvel = nxvel
    
    def set_yvel(self, nyvel):
        self.yvel = nyvel
    
    def update(self, dt) -> None:
        self.clock += dt
        if self.clock >= self.timer:
            self.clock = 0
            last: dict = self.body.pop()
            last["c"] = self.body[0]["c"] + self.xvel
            last["r"] = self.body[0]["r"] + self.yvel
            self.body.insert(0, last)
    
    def draw(self) -> None:
        for box in self.body:
            x: int = box["c"] * self.size
            y: int = box["r"] * self.size
            # setting the center (Arcade draws from the center_x and center_y)
            x += self.size // 2
            y += self.size // 2
            arcade.draw_rectangle_filled(x, y, self.size, self.size, arcade.color.RED)
            