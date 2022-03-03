from FFT import EQ
import neopixel

class matrix:
    def __init__(self, rows, cols):
        self.arr = [[0]*cols]*rows
    
    
class neopixel:
    def __init__(self, board, rows, cols):
        self.board = board
        self.rows = rows
        self.cols = cols
        self.num = rows*cols
        pixels = neopixel.NeoPixel(self.board, self.num)
        for i in range(num):
            pixels[i] = 0x000000
    
    RED = 0x100000
    
    matrix.__init__(self.rows, self.cols)
    rowwid = rows/8
    
    while true:
        for i in range(rows):
            for w in range(rowwid):
                for j in range(EQ.value[i]):
                    pixels[(i*cols)+j] = RED
            