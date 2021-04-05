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
        print(number)

# while True:
#     time.sleep(1) # in sec
#     datas = mirror.readline()
#     logging.info(datas)
# #!/usr/bin/env python3
# import serial
# import time

# if __name__ == '__main__':
#     ser = serial.Serial(port, 115200, timeout=1)
#     ser.flush()

#     while True:
#         ser.write(b"Hello from Raspberry Pi!\n")
#         line = ser.readline().decode('utf-8').rstrip()
#         print(line)
#         time.sleep(1)