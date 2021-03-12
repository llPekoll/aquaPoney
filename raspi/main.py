import threading
import time
from sensor_bme280 import get_bme280_values, push_bme280_values


def infiniteloop1():
    while True:
        bme280 = get_bme280_values()
        try:
            push_bme280_values()
        except Exception as e:
            print(e)
        print(bme280)
        print("values pusehs")
        time.sleep(3600)

def infiniteloop2():
    while True:
        print('running the pompe')
        time.sleep(1)
        time.sleep(10)
        print('clossing pompe')



thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()

