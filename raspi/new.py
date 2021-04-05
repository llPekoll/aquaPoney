import os
import serial
import time
import logging

logging.basicConfig(filename='output.log', level=logging.DEBUG)


port = "/dev/ttyUSB0"
ser = serial.Serial(port, 115200, timeout=1)
ser.flush()

while True:
    number = ser.readline()
    if number != b'':
        logging.info(number)
