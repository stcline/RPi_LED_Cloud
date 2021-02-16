# Simple test script for WS2812b LEDs

import board
import neopixel
pixels = neopixel.NeoPixel(board.D12, 30)

pixels[1] = (255, 0, 0)

