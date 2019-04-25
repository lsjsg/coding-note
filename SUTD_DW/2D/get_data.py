import pickle
import time
from w1thermsensor import W1ThermSensor
import os

d = {"time": [], "temperature": []}
sensor = W1ThermSensor.get_available_sensors()[0]
start = time.time()
for i in range(200):
    temperature = sensor.get_temperature()
    d["time"].append(time.time() - start)
    d["temperature"].append(temperature)
    print("Sensor has temperature {0}".format(temperature))
    time.sleep(0.005)

now = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime())
name = "{0}.pickle".format(now)
os.system("touch {0}".format(name))
file = open(name, "wb")
pickle.dump(d, file)
file.close()
