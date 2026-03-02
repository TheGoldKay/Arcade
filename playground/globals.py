# --- Config ---
WIDTH, HEIGHT = 800, 600
TITLE = "Memory Game - Wave Grid"

COLS, ROWS = 6, 4
TILE_W, TILE_H = 100, 100
GAP = 12
MAX_TILT = 15
WAVE_RADIUS = 200
SMOOTHING = 0.12
MAX_SCALE_BOOST = 0.05

grid_w = COLS * (TILE_W + GAP) - GAP
grid_h = ROWS * (TILE_H + GAP) - GAP
START_X = (WIDTH - grid_w) // 2
START_Y = (HEIGHT - grid_h) // 2
BG_COLOR = (30, 30, 45)