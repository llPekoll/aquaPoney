import serial
import time

import logging
from logging.handlers import RotatingFileHandler

# port = "/dev/cu.usbserial-1420" # OSX
port = "/dev/ttyUSB0"  # RASPI

ser = serial.Serial(port, 115200, timeout=1)
ser.flush()


class Counter:
    counter = 0
    time_left_open = 17
    cycle_time = 180
    cycle_number = 0
    pump_is_open = False


counter_one = Counter()


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


while True:
    counter_one.counter += 1
    app_log.info(f" counter = {counter_one.counter}")
    string_to_Send = f"{counter_one.counter} sec"
    ser.write(b"string_to_Send\n")
    if counter_one.counter == 0:
        ser.write(b"openPump\n")
        app_log.info(f" open pump")
        counter_one.pump_is_open = True
    if counter_one.counter > counter_one.time_left_open:
        ser.write(b"closePump\n")
        app_log.info(f" open close")
        counter_one.pump_is_open = False

    if counter_one.counter > counter_one.cycle_time:
        counter_one.counter = 0
        counter_one.cycle_number += 1

    app_log.info(f" counter = {counter_one.cycle_number}")

    #  read raspi
    line = ser.readline().decode("utf-8").rstrip()
    print(line)
    time.sleep(1)
