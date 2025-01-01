import arcade
import sys

sys.path.append("/home/goldkay/Code/Arcade/helper")

from coordinates import centerTopRight

# Constants
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Halves"
BACKGROUND_COLOR = arcade.color.PHTHALO_GREEN
LINE_COLOR =(BACKGROUND_COLOR[0] + 50, BACKGROUND_COLOR[1] + 50, BACKGROUND_COLOR[2] + 50)
BOX_SIZE = 25
NWIDTH = SCREEN_WIDTH//BOX_SIZE
NHEIGHT = SCREEN_HEIGHT//BOX_SIZE
MIDDLE = ((NWIDTH + 1) //  2, (NHEIGHT + 1) //  2)

def middle():
    cx = MIDDLE[0] * BOX_SIZE - BOX_SIZE // 2
    for y in range(1, NHEIGHT+1):
        cy = y * BOX_SIZE - BOX_SIZE // 2
        arcade.draw_rectangle_filled(cx, cy, BOX_SIZE, BOX_SIZE, LINE_COLOR)

class Ball:
    def __init__(self):
        self.x = MIDDLE[0]
        self.y = MIDDLE[1]
        self.x_vel = 1
        self.y_vel = 1
        self.clock = 0
        self.wait_time = 0.001
        self.last_move = []
    
    def _center(self):
        cx = self.x * BOX_SIZE - BOX_SIZE // 2
        cy = self.y * BOX_SIZE - BOX_SIZE // 2
        return (cx, cy)
    
    def update(self, dt):
        self.clock += dt
        if self.clock > self.wait_time:
            self.clock = 0
            self.last_move = [self.x, self.y]
            self.x += self.x_vel
            self.y += self.y_vel
            self._check_bounds()   
    
    def _check_bounds(self):
        if self.x == NWIDTH or self.x == 1:
            self.x_vel *= -1
        if self.y == NHEIGHT or self.y == 1:
            self.y_vel *= -1
    
    def draw(self):
        arcade.draw_circle_filled(*self._center(), BOX_SIZE // 2, arcade.color.RED)

class Reds:
    def __init__(self):
        """
        Initialize a new Reds object.

        The `colored` attribute is a list of tuples of coordinates, representing the
        boxes that have been colored red.
        """
        self.colored = self._make_reds()
    
    def _make_reds(self):
        colored = []
        for y in range(1, NHEIGHT+1):
            colored.append({"pos": (1, y), "color": False})
            colored.append({"pos": (NWIDTH, y), "color": False})
        return colored
    
    def collision1(self, ball, dt):
        if (ball.x, ball.y) in self.colored:
            if ball.x > MIDDLE[0]:
                self.colored.append((ball.x-1, ball.y))
                ball.x -= 2
                ball.x_vel = -1
            if ball.x < MIDDLE[0]:
                self.colored.append((ball.x+1, ball.y))
                ball.x += 2
                ball.x_vel = 1
            return ball
        elif ball.x in (NWIDTH, 1):
            self.colored.append((ball.x, ball.y))
            if ball.x == NWIDTH:
                ball.x -= 2
                ball.x_vel = -1
            if ball.x == 1:
                ball.x += 2
                ball.x_vel = 1
            return ball
        ball.update(dt)
        return ball
    
    def collision(self, ball, dt):
        for i, box in enumerate(self.colored):
            if (ball.x+1, ball.y) == box["pos"] and ball.x+1 != ball.last_move[0]:
                self.colored[i]["color"] = True
                ball.x_vel = -1
                ball.x -= 2
                print('right')
                x, y = box["pos"]
                self.colored.append({"pos": (x-2, y), "color": False})
                
                return ball
            if (ball.x-1, ball.y) == box["pos"] and ball.x-1 != ball.last_move[0]:
                self.colored[i]["color"] = True
                ball.x_vel = 1
                ball.x += 2
                print('left')
                x, y = box["pos"]
                self.colored.append({"pos": (x+2, y), "color": False})
                return ball
        ball.update(dt)
        return ball        
            
    def draw(self):
        for box in self.colored:
            if box["color"]:
                x, y = box["pos"]
                cx = x * BOX_SIZE - BOX_SIZE // 2
                cy = y * BOX_SIZE - BOX_SIZE // 2
                arcade.draw_rectangle_filled(cx, cy, BOX_SIZE, BOX_SIZE, arcade.color.RED)

class Halves(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, center_window=True)
        arcade.set_background_color(BACKGROUND_COLOR)
    
    def setup(self):
        self.ball = Ball()
        self.reds = Reds()

    def on_draw(self):
        arcade.start_render()
        
        middle()
        for y in range(1, NHEIGHT+1):
            for x in range(1, NWIDTH+1):
                top = y * BOX_SIZE
                right = x * BOX_SIZE
                centerx, centery = centerTopRight(top, right, BOX_SIZE, BOX_SIZE)
                arcade.draw_rectangle_outline(centerx, centery, BOX_SIZE, BOX_SIZE, arcade.color.BLACK)
        self.ball.draw()
        self.reds.draw()
        
        arcade.finish_render()
        
    def on_update(self, dt):
        self.ball = self.reds.collision(self.ball, dt)
        
    def on_key_press(self, key, modifiers):       
        if key == arcade.key.ESCAPE:
            sys.exit() # close the debugger terminal and game screen at the same time

def main():
    halves = Halves()
    halves.setup()
    halves.run()

if __name__ == "__main__":
    main()
