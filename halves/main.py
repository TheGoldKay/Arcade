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
BOX_SIZE = 10#25
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
        self.wait_time = 0#0.001
        self.last_move = [self.x, self.y]
    
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
        colored = {}
        for y in range(1, NHEIGHT+1):
            colored[(1, y)] = False
            colored[(NWIDTH, y)] = False
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
    
    def collision2v2(self, ball, dt):
        for i, box in enumerate(self.colored):
            if (ball.x + ball.x_vel, ball.y) == box["pos"] and ball.x != ball.last_move[0] and box["color"] == False:
                x, y = box["pos"]
                self.colored.append({"pos": (x - ball.x_vel, y), "color": False})
                ball.x_vel *= -1
                ball.x += 2 * ball.x_vel
                self.colored[i]["color"] = True
                return ball
        ball.update(dt)
        return ball
    
    def _check_reds(self, x_vel):
        for pos in self.colored:
            if self.colored[pos]:
                x, y = pos
                x += x_vel
                if x >= 1 and x <= NWIDTH and self.colored.get((x, y), True):
                    self.colored[(x, y)] = False
                    print(f"hit: {x_vel} ({x}, {y})")
                    break
            
    def collision3(self, ball, dt):
        for pos in self.colored:
            if self.colored[pos] == False and ball.x != ball.last_move[0]:
                if (ball.x, ball.y) == pos or (ball.x + ball.x_vel, ball.y) == pos:
                    self.colored[pos] = True          
                    x, y = pos
                    self.colored[(x - ball.x_vel, y)] = False
                    ball.x_vel *= -1
                    ball.y_vel *= -1
                    ball.x, ball.y = ball.last_move
                    print(len(self.colored)) 
                    return ball
        ball.update(dt)
        self._check_reds(ball.x_vel)
        return ball
    
    def draw(self):
        for pos in self.colored:
            x, y = pos
            cx = x * BOX_SIZE - BOX_SIZE // 2
            cy = y * BOX_SIZE - BOX_SIZE // 2
            if self.colored[pos]:
                arcade.draw_rectangle_filled(cx, cy, BOX_SIZE, BOX_SIZE, arcade.color.RED)
            else:
                arcade.draw_rectangle_outline(cx, cy, BOX_SIZE, BOX_SIZE, arcade.color.WHITE_SMOKE)

class Halves(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, center_window=True, update_rate=1/360)
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
        self.reds.collision3(self.ball, dt)
        
    def on_key_press(self, key, modifiers):       
        if key == arcade.key.ESCAPE:
            sys.exit() # close the debugger terminal and game screen at the same time

def main():
    halves = Halves()
    halves.setup()
    halves.run()

if __name__ == "__main__":
    main()
