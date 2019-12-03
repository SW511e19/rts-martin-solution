from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent
import time

colorsensor = ColorSensor()
colorsensor.MODE_COL_COLOR
m1 = LargeMotor(OUTPUT_B) #Cord has to go over the wheel (right of the wheel)
m2 = LargeMotor(OUTPUT_C) #Cord has to go under the wheel

speed = 50 # positive is left, negative is right

# Runs the motors for a small amount of time before stopping
def run(speed, seconds):
    m1.on(SpeedPercent(speed))
    m2.on(SpeedPercent((speed * 0.9))) # m2 runs slower to compensate for higher physical motor speed
    time.sleep(seconds)
    stop_motor()

def reset(speed, seconds):
    if speed >= 0:
        m1.on(SpeedPercent(speed))
        m2.on(SpeedPercent(-(speed * 0.9 * 2)))
    else:
        m1.on(SpeedPercent(speed * 2))
        m2.on(SpeedPercent(-(speed * 0.9)))
    time.sleep(seconds)
    stop_motor()

def stop_motor():
    m1.on(SpeedPercent(0))
    m2.on(SpeedPercent(0))

def calibrate():
    count = 0
    while (colorsensor.color != colorsensor.COLOR_RED):
        run(50, 0.03)
        if count >= 10:
            print("reset")
            reset(20, 0.1)
            count = 0
        count += 1
    stop_motor()

def cc(box_number, box_offset, speed):
    count = 0
    clr_is_white = True
    temp = 0
    reset(20, 0.1) # Resets before running first time
    
    while box_number != box_offset:
        run(speed, 0.03)
        if count >= 10:
            print("reset")
            reset(20, 0.1)
            count = 0

        if clr_is_white == False and colorsensor.color == colorsensor.COLOR_WHITE:
            clr_is_white = True
            print("was at " + str(box_number))
            if speed >= 0:
                box_number -= 1
            else:
                box_number += 1
            print("is at " + str(box_number))
            temp = 1
            time.sleep(10)

        else: 
            if colorsensor.color != colorsensor.COLOR_WHITE:
                clr_is_white = False
                print("Passed a box.")

        if temp == 1 and colorsensor.color == colorsensor.COLOR_RED:
            stop_motor()
            print("overran")
            return

        count += 1
    print("returning")
    return box_number


calibrate()
cc(0, 6, -speed)
#cc(0, 0, speed)
stop_motor()