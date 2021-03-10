import threading
import time
from sensor_bme280 import get_bme280_values


def infiniteloop1():
    while True:
        bme280 = get_bme280_values()
        print(bme280)
        time.sleep(60)

def infiniteloop2():
    while True:
        print('running the pompe')
        time.sleep(1)
        # infintie loop for pompe
            # every 2 hours open the pompe close the popme after 5 minutes or check the water level
        time.sleep(10)
        print('clossing pompe')



thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()

