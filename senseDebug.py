from time import sleep
from sense_hat import SenseHat
from random import randint
import math
sense = SenseHat()
#i2cdetect -y 1

timer = 0

while True:
    apressure = 0
    ahumidity = 0
    atemp = 0

    print("--------------------------------------")

    orientation = sense.get_orientation()
    pitch = int(orientation["pitch"]/1.42)
    roll = int(orientation["roll"]/1.42)
    yaw = int(orientation["yaw"]/1.42)

    rpitch = round(pitch, 1)
    rroll = round(roll, 1)
    ryaw = round(yaw, 1)
    print(f" pitch: {rpitch} roll: {rroll} yaw: {ryaw}")
    
    acceleration = sense.get_accelerometer_raw()
    x = acceleration["x"]
    y = acceleration["y"]
    z = acceleration["z"]
    rx = round(x, 1)
    ry = round(y, 1)
    rz = round(z, 1)
    print(f" acceleration, x = {rx} y = {ry} z = {rz}")

    compass = sense.get_compass_raw()
    x = float(compass['z'])
    y = float(compass['y'])
    z = float(compass['x'])
    h = math.sqrt(x ** 2 + y ** 2)
    f = math.sqrt(h ** 2 + z ** 2)
    d = math.degrees(math.atan(y / x))
    index = round(math.degrees(math.atan(z / h)),1)

    print(f" north = {index}")

    for i in range(0,4):
        pressure = sense.get_pressure()
        apressure = apressure + pressure

        humidity = sense.get_humidity()
        ahumidity = ahumidity + humidity

        temp = sense.get_temperature()
        atemp = atemp + temp

    apressure = apressure/5
    rpressure = round(apressure, 1)
    ahumidity = ahumidity/5
    rhumid = round(ahumidity, 1)
    atemp  = atemp/5
    rtemp = round(atemp, 1)

    print(f" pressure = {rpressure}")
    print(f" humidity = {rhumid}")
    print(f" temperature = {rtemp}")

    if timer % 5 == 0:
        r = randint(0,255)
        b = randint(0,255)
        g = randint(0,255)
        print(f" r = {r} b = {b} g = {g}")
    
    color = (r,b,g)
    #color = (255,255,255)

    sense.show_message("",back_colour=color)

    for event in sense.stick.get_events():
        print(event.direction,event.action)

    timer = timer + 1
    #sleep(1)

