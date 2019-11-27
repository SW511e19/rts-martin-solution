from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent
import time

colorsensor = ColorSensor()
colorsensor.MODE_COL_COLOR
m1 = LargeMotor(OUTPUT_B)
m2 = LargeMotor(OUTPUT_C)

def run(speed, seconds):
    m1.on(SpeedPercent(speed))
    m2.on(SpeedPercent((speed * 0.9)))
    time.sleep(seconds)
    print("Ran with " + str(speed) + " speed for " + str(seconds) + " time" )

def reset(speed, seconds):
    m1.on(SpeedPercent(speed))
    m2.on(SpeedPercent(-(speed * 0.9)))
    time.sleep(seconds)
    print("Ran with " + str(speed) + " speed for " + str(seconds) + " time" )

count = 0
while count < 100:
    #reset(-50, 0.1)
    run(50, 0.03)
    reset(10, 0.001)
    #run(-50, 3)
    #reset(20, 0.1)
    count += 1
    if(colorsensor.color == 6):
        print(colorsensor.color)
    print("count: " + str(count))


m1.on(SpeedPercent(0))
m2.on(SpeedPercent(0))