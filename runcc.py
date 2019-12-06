from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent
import time

colorsensor = ColorSensor()
colorsensor.MODE_COL_COLOR
m1 = LargeMotor(OUTPUT_B) # Cord has to go over the wheel (right of the wheel)
m2 = LargeMotor(OUTPUT_C) # Cord has to go under the wheel

global_speed = 25 # positive is left, negative is right

# Runs the motors. Which motor starts first depends on the direction. 
# The motor not pulling the CC starts first to loosen the string a little.
def run(speed):
    if speed >= 0:
        m2.on(SpeedPercent(speed * 1.5))
        m1.on(SpeedPercent(speed))
    else:
        m1.on(SpeedPercent(speed * 1.3))
        m2.on(SpeedPercent(speed))

# Tightens the string. Which motor starts first depends on the direction. 
def tighten(speed, seconds):
    print("tightens")
    if speed >= 0:
        m2.on(SpeedPercent(-speed))
        m1.on(SpeedPercent(speed))
    else:
        m1.on(SpeedPercent(speed))
        m2.on(SpeedPercent(-speed))
    time.sleep(seconds)
    stop_motor()

# Stops the motors
def stop_motor():
    m1.on(SpeedPercent(0))
    m2.on(SpeedPercent(0))

# Brings the CC to the red line. Should only be called once at the start of the program.
def calibrate():
    iteration = 0
    while (colorsensor.color != colorsensor.COLOR_RED):
        run(25)       
        if iteration % 10 == 0:
            tighten(20, 0.1)
        iteration += 1
    tighten(20, 0.1)

# To compensate for color-sensor characteristics (such as changing color values without moving),
#   a minimum amount of iterations are done before searching for white when moving,
#   this is to prevent that the same white is counted twice when moving between each box.
# If the card collector just calibrated it will read red, it will search for white immediately,
#   because the first white is less than the minimum amount of iterations away from the red.
def cc(box_number, box_offset, speed):
    iteration = 0
    look_for_white = False
    
    if(colorsensor.color == colorsensor.COLOR_RED):
        look_for_white = True

    while box_number != box_offset:
        run(speed)      
        if iteration % 10 == 0 and iteration != 0:
            tighten(20, 0.1)

        if iteration >= 50:
            look_for_white = True

        if look_for_white == True and colorsensor.color == colorsensor.COLOR_WHITE:
            look_for_white = False
            iteration = 0
            stop_motor()
            
            print("was at " + str(box_number))
            if speed >= 0:
                box_number -= 1
            else:
                box_number += 1
            print("is at " + str(box_number))   
        iteration += 1
    stop_motor()
    return box_number

# Go to box 1 to 7. Which direction depends on the current position and which direction it should move.
def go_to_box(current_box, dest_box, speed):
    if 0 <= current_box <= 7 and 1 <= dest_box <= 7:
        if dest_box == current_box:
            print("Was already at box")
        if dest_box < current_box:
            current_box = cc(current_box, dest_box, speed)
        if dest_box > current_box:
            current_box = cc(current_box, dest_box, -speed)
    else:
        print("Box value out of bounds")
    return current_box

calibrate() 
print("done calibrating")
box_num = 1
current_box = 0
num_to_add = 1

while(True):
    current_box = go_to_box(current_box, box_num, global_speed)
    print("Went to box " + str(box_num))
    time.sleep(5)
    if(box_num == 7):
        num_to_add = -1
    if(box_num == 1):
        num_to_add = 1
    box_num += num_to_add
