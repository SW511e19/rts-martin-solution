from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_B, OUTPUT_C, SpeedPercent
import time
import datetime as dt

m1 = MediumMotor(OUTPUT_B)
#m2 = LargeMotor(OUTPUT_C)
#m1.on(SpeedPercent(0))
#m1.on_for_rotations(SpeedPercent(0), 1)

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
    a = times[0]
    for x in times:
        if x < a:
            a = x
    print("Best: " + str(a))
    c = 0
    for x in times:
        if x > c:
            c = x
    print("Worst: " + str(c))

individual_motortest(m1, -10)