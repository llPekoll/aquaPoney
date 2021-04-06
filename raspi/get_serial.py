import os
import serial
import time


port = "/dev/cu.usbserial-1420"
mirror = serial.Serial(port, 115200)

while True:
    time.sleep(3600) # in sec
    datas = mirror.readline()
    # Got string like 
    # "ctn: 12, pump: open , humi: 12.3, temp: 12.3");

    datas = str(datas)
    datas = datas.replace("b'","").replace(r"\r\n'","")
    splited_datas = datas.split(",")
    val = [splited_data.split(":")[1] for splited_data in splited_datas]
    datas = {
            "cycle_number":val[4],
            "humidity":val[2],
            "temperature":val[3],
    }


    SERVER_IP = os.environ.get("SERVER_IP")
    APIKEY = f"{os.environ.get('API_KEY_NAME')}={os.environ.get('API_KEY')}"
    req = f"https://{SERVER_IP}/bme280?{APIKEY}"
    ret = requests.post(req, json=datas)
    print(ret.json())
