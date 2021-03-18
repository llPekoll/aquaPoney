import threading
import time
from sensor_bme280 import get_bme280_values, push_bme280_values


def infiniteloop2():
    while True:
        print('running the pompe')
        time.sleep(1)
        time.sleep(10)
        print('clossing pompe')


infiniteloop2()
