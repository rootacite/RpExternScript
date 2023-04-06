
from machine import *
import time
import _thread

import os

P22 = Pin(22, Pin.OUT)
P25 = Pin(25, Pin.OUT)


def Core():
    while True:
        P25.on()
        time.sleep(0.2)
        P25.off()
        time.sleep(0.2)


def main():
    _thread.start_new_thread(Core, ())
    while True:
        P22.on()
        time.sleep(0.2)
        P22.off()
        time.sleep(0.2)

