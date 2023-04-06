
from machine import *

import os
import uos
import sdcard

freq(250000000)

try:
    spi0 = SPI(1, baudrate=20_000_000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
    sd = sdcard.SDCard(spi0, Pin(9), baudrate=20_000_000)
    vfs = uos.VfsFat(sd)
    os.mount(sd, '/sd')
except Exception as e:
    print(e)

