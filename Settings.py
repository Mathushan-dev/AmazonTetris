CANVAS_WIDTH = 800
CANVAS_HEIGHT = 700
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
SQUARE_SIZE = 30

SCREEN_TOP_LEFT_X = (CANVAS_WIDTH - SCREEN_WIDTH) // 2
SCREEN_TOP_LEFT_Y = CANVAS_HEIGHT - SCREEN_HEIGHT

S = [['.....',
      '.....',
      '..**.',
      '.**..',
      '.....'],
     ['.....',
      '..*..',
      '..**.',
      '...*.',
      '.....']]

Z = [['.....',
      '.....',
      '.**..',
      '..**.',
      '.....'],
     ['.....',
      '..*..',
      '.**..',
      '.*...',
      '.....']]

I = [['..*..',
      '..*..',
      '..*..',
      '..*..',
      '.....'],
     ['.....',
      '****.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.**..',
      '.**..',
      '.....']]

J = [['.....',
      '.*...',
      '.***.',
      '.....',
      '.....'],
     ['.....',
      '..**.',
      '..*..',
      '..*..',
      '.....'],
     ['.....',
      '.....',
      '.***.',
      '...*.',
      '.....'],
     ['.....',
      '..*..',
      '..*..',
      '.**..',
      '.....']]

L = [['.....',
      '...*.',
      '.***.',
      '.....',
      '.....'],
     ['.....',
      '..*..',
      '..*..',
      '..**.',
      '.....'],
     ['.....',
      '.....',
      '.***.',
      '.*...',
      '.....'],
     ['.....',
      '.**..',
      '..*..',
      '..*..',
      '.....']]

T = [['.....',
      '..*..',
      '.***.',
      '.....',
      '.....'],
     ['.....',
      '..*..',
      '..**.',
      '..*..',
      '.....'],
     ['.....',
      '.....',
      '.***.',
      '..*..',
      '.....'],
     ['.....',
      '..*..',
      '.**..',
      '..*..',
      '.....']]

BLOCKS = [S, Z, I, O, J, L, T]
BLOCK_COLOURS = [(0, 255, 255), (255, 255, 0), (128, 0, 128), (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 127, 0)]