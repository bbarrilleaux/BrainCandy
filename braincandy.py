#!/usr/bin/env python
# must do sudo python from within the rpi-rgb-led-matrix-master folder
# must have animated gifs in your folder

def gen_map():
   matrix = (32, 32)
   top = []
   mid = []
   bot = []
   cur_index = 0
   for y in range(matrix[1]):
       row_top = [x+cur_index for x in range(matrix[0]*3)]
       cur_index = row_top[len(row_top)-1] + 1
       top.append(row_top)
       row_mid = [x+cur_index for x in reversed(range(matrix[0]*3))]
       cur_index = row_mid[0] + 1
       mid.insert(0,row_mid)
       row_bot = [x+cur_index for x in range(matrix[0]*3)]
       cur_index = row_bot[len(row_top)-1] + 1
       bot.append(row_bot)
   matrix_map = top + mid + bot
   return matrix_map



# LED panel constants
PANEL_ARRAY_WIDTH = 3
PANEL_ARRAY_HEIGHT = 3
CHAIN_LENGTH = PANEL_ARRAY_WIDTH * PANEL_ARRAY_HEIGHT
SQUARE_SIZE = 32
WIDTH = PANEL_ARRAY_WIDTH * SQUARE_SIZE
HEIGHT = PANEL_ARRAY_HEIGHT * SQUARE_SIZE

# initialize LED matrix
from ada_matrix import DriverAdaMatrix
driver = DriverAdaMatrix(rows=SQUARE_SIZE, chain=CHAIN_LENGTH)
driver.SetPWMBits(6) #decrease bit-depth for better performance
from bibliopixel import *
led = LEDMatrix(driver, WIDTH, HEIGHT, coordMap = gen_map())

from BiblioPixelAnimations.matrix import ImageAnim

import os
import glob
image_path = os.path.abspath(os.path.dirname(__file__)) + '/braincandygifs/'
gifs = glob.glob(image_path + '/*.gif')

while 1:
    try:
        for gif in gifs:
            anim = ImageAnim.ImageAnim(led, gif)
            anim.run(untilComplete = True, max_cycles = 25, fps=10)
    except KeyboardInterrupt:
        led.all_off()
        led.update()
        raise


