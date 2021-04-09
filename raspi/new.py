import os
import serial
import time
import logging
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter("%(asctime)s %(funcName)s(%(lineno)d) %(message)s")
logFile = "xxx.log"


my_handler = RotatingFileHandler(
    logFile, mode="a", maxBytes=2 * 1024 * 1024, backupCount=2, encoding=None, delay=0
)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)

app_log = logging.getLogger("root")
app_log.setLevel(logging.INFO)

app_log.addHandler(my_handler)

# port = "/dev/cu.usbserial-1420" # OSX
port = "/dev/ttyUSB0"  # RASPI
ser = serial.Serial(port, 115200, timeout=1)
ser.flush()

while True:
    number = ser.readline()
    if number != b"":
        app_log.info(number)
