import arcade 
from copy import deepcopy as copy

class Snake:
    def __init__(self, row, col, size, limit_c, limit_r):
        # index 0 is the head
        self.body = [{"r": row, "c": col+i} for i in range(3)]
        self.xvel = -1
        self.yvel = 0
        self.size = size
        # regulate the snake's update speed
        self.clock = 0 
        # time to wait before moving a single box (block) in either direction
        self.timer = 0.2
        # last piece - keep track to add it back when the snake eats
        self.last = copy(self.body[-1])
        self.is_dead = False 
        self.limit_c = limit_c
        self.limit_r = limit_r
        
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
            self.last = copy(last)
            last["c"] = self.body[0]["c"] + self.xvel
            last["r"] = self.body[0]["r"] + self.yvel
            if last["c"] < 0:
                last["c"] = self.limit_c
            elif last["c"] > self.limit_c:
                last["c"] = 0
            if last["r"] < 0:
                last["r"] = self.limit_r
            elif last["r"] > self.limit_r:
                last["r"] = 0                
            self.body.insert(0, last)
            self.check_gameover()
    
    def check_gameover(self) -> None:
        head_c = self.body[0]["c"]
        head_r = self.body[0]["r"]
        for part in self.body[1:]:
            if head_c == part["c"] and head_r == part["r"]:
                self.is_dead = True
                break
    
    def ate(self, food) -> bool:
        if food:
            if food["r"] == self.body[0]["r"] and food["c"] == self.body[0]["c"]:
                self.body.append(self.last)
                return True 
        return False
    
    def draw(self) -> None:
        for box in self.body:
            x: int = box["c"] * self.size
            y: int = box["r"] * self.size
            # setting the center (Arcade draws from the center_x and center_y)
            x += self.size // 2
            y += self.size // 2
            arcade.draw_rectangle_filled(x, y, self.size, self.size, arcade.color.FRENCH_WINE)
            