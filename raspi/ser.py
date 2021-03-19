import serial


port = "/dev/cu.usbserial-1420"
mirror = serial.Serial(port, 115200)

while True:
    donnee = mirror.readline()
    water_level = str(donnee)
    water_level = water_level.replace("b'","").replace(r"\r\n'","")
    print(f"water level {water_level}%")