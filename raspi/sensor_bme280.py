# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import os
from datetime import datetime

import board
import busio
import adafruit_bme280
import requests
# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# OR create library object using our Bus SPI port
# spi = busio.SPI(board.SCK, board.MOSI, board.<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  ISO)
# bme_cs = digitalio.DigitalInOut(board.D10)
# bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

def get_bme280_values():
    vals = f"\nTemperature: {bme280.temperature:0.1f} C"
    vals += f"\nHumidity: {bme280.relative_humidity:0.1f} %"
    vals += f"\nPressure: {bme280.pressure:0.1f} hPa"
    vals += f"\nAltitude: {bme280.altitude:0.2f} meters"
    return vals

def push_bme280_values():
    print(1)
    datas = {
        "humidity": float(f"{bme280.relative_humidity:0.1f}"),
        "temperature":float(f"{bme280.temperature:0.1f}"),
        "pressure": float(f"{bme280.pressure:0.1f}"),
        "altitude": float(f"{bme280.altitude:0.2f}"),
    }
    print(2)
    SERVER_IP = os.environ.get("SERVER_IP")
    print(3)
    APIKEY = f"{os.environ.get('API_KEY_NAME')}={os.environ.get('API_KEY')}"
    print(4)
    req = f"https://{SERVER_IP}/bme280?{APIKEY}"
    print(req)
    print(datas)
    ret = requests.post(req, json=datas)
    print(ret.json())

