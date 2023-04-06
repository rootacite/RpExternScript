import time
from machine import *

import sys
sys.path.append("/sd/")

from externe import main

try:
    main()
except Exception as r:
    print(r)

while True:
    time.sleep(1)
