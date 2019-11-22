from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent
import time

m1 = LargeMotor(OUTPUT_B)
m2 = LargeMotor(OUTPUT_C)

def run(speed, seconds):
    m1.on(SpeedPercent(speed))
    m2.on(SpeedPercent(-(speed * 0.9)))
    time.sleep(seconds)
    print("Ran with " + str(speed) + " speed for " + str(seconds) + " time" )

count = 0
while count < 2:
    run(50, 0.75)
    run(-50, 0.75)
    count += 1
    print("count: " + str(count))


m1.on(SpeedPercent(0))
m2.on(SpeedPercent(0))