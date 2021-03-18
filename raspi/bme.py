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
        print("values pushed")
        time.sleep(3600)



infiniteloop1()

