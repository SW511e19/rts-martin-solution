from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_B, OUTPUT_C, SpeedPercent
import time
import datetime as dt

#m1 = MediumMotor(OUTPUT_B)
m2 = LargeMotor(OUTPUT_C)
#m1.on(SpeedPercent(0))
#m1.on_for_rotations(SpeedPercent(0), 1)

def best(array):
    a = array[0]
    for x in array:
        if x < a:
            a = x
    return a

def worst(array):
    c = array[0]
    for x in array:
        if x > c:
            c = x
    return c

def individual_motortest(motor, speed):
    count = 0
    times = []
    while count < 30:
        x = dt.datetime.now().timestamp() * 1000
        motor.on_for_rotations(SpeedPercent(speed), 1)
        #motor.on(SpeedPercent(0))
        y = dt.datetime.now().timestamp() * 1000 - x
        print(y)
        times.append(y)
        count += 1
        time.sleep(0.05)
    print("Best: " + str(best(times)))
    print("Worst: " + str(worst(times)))

def manual_test(motor, speed):
    count = 0
    times = []
    while count < 10:
        input("Awaiting start")
        x = dt.datetime.now().timestamp() * 1000
        motor.on(SpeedPercent(speed))
        input("Awaiting stop")
        motor.on(SpeedPercent(0))
        y = dt.datetime.now().timestamp() * 1000 - x
        print(y)
        times.append(y)
        count += 1
    print("Best: " + str(best(times)))
    print("Worst: " + str(worst(times)))

manual_test(m2, -30)
#individual_motortest(m1, -10)