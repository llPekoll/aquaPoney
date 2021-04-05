import os
import serial
import time
import logging

logging.basicConfig(filename='output.log', encoding='utf-8', level=logging.DEBUG)


port = "/dev/cu.usbserial-1420"
ser = serial.Serial(port, 115200, timeout=1)
ser.flush()

while True:
    number = ser.read()
    if number != b'':
        logging.info(number)
