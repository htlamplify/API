from FFT import EQ
import neopixel
import board


class matrix:
    def __init__(self, rows, cols):
        self.arr = [[0]*cols]*rows
    
    
class neopixel:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.num = rows*cols
        pixels = neopixel.NeoPixel(board.D21, self.num)
        for i in range(num):
            pixels[i] = 0x000000
    
    RED = 0x100000
    
    matrix.__init__(self.rows, self.cols)
    rowwid = rows/7
    
    while true:
        for i in range(rows):
            for w in range(rowwid):                 #rowwid = rows per frequencyband
                for j in range(EQ.value[i]):
                    if(i%2):
                        pixels[(i*cols)-j] = RED    #every even row is from top to bottom
                    else:
                        pixels[(i*cols)+j] = RED    #every odd row is from bottom to top

            