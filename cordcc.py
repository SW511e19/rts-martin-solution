from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent
import time

colorsensor = ColorSensor()
colorsensor.MODE_COL_COLOR
m1 = LargeMotor(OUTPUT_B) #Cord has to go over the wheel (right of the wheel)
m2 = LargeMotor(OUTPUT_C) #Cord has to go under the wheel

global_speed = 50 # positive is left, negative is right

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
        m1.on(SpeedPercent(speed * 1.5))
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
        if count % 10 == 0:
            reset(20, 0.1)
        count += 1
    stop_motor()

def cc(box_number, box_offset, speed):
    count = 0
    temp = False

    # Detect if CC already is at a box
    clr_is_white = False
    if(clr_is_white == colorsensor.COLOR_WHITE):
        clr_is_white = True
    else:
        clr_is_white = False
    
    while box_number != box_offset:
        run(speed, 0.03)      
        if count % 10 == 0:
            print("reset")
            reset(20, 0.1)

        if clr_is_white == False and colorsensor.color == colorsensor.COLOR_WHITE:
            clr_is_white = True
            print("was at " + str(box_number))
            if speed >= 0:
                box_number -= 1
            else:
                box_number += 1
            print("is at " + str(box_number))
            time.sleep(4)
            temp = True

        else: 
            if colorsensor.color != colorsensor.COLOR_WHITE:
                clr_is_white = False
                #print("Passed a box.")

        if temp and colorsensor.color == colorsensor.COLOR_RED:
            stop_motor()
            print("overran")
            return

        count += 1
    return box_number

# Go to box 1 to 7. Which direction it goes depends on the current box position and which box it should go to
def go_to_box(current_box, dest_box, speed):
    if(dest_box == current_box):
        print("Was already at box")
    if dest_box < current_box:
        current_box = cc(current_box, dest_box, speed)
    else:
        current_box = cc(current_box, dest_box, -(speed))
    stop_motor()
    return current_box

calibrate() # Goes to the red line at the end of the machine before any boxes, position 0
print("done calibrating")
current_box = go_to_box(0, 5, global_speed)
#time.sleep(10)
#current_box = go_to_box(5, 1, global_speed)

#print("returns: " + str(current_box))
#current_box = go_to_box(2, 4)
