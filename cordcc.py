from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent
import time

colorsensor = ColorSensor()
colorsensor.MODE_COL_COLOR
m1 = LargeMotor(OUTPUT_B) #Cord has to go over the wheel (right of the wheel)
m2 = LargeMotor(OUTPUT_C) #Cord has to go under the wheel

global_speed = 25 # positive is left, negative is right

# Runs the motors for a small amount of time before stopping
def run(speed):
    m1.on(SpeedPercent(speed))
    m2.on(SpeedPercent((speed * 0.9))) # m2 runs slower to compensate for higher physical motor speed
    #time.sleep(seconds)
    #stop_motor()

def tighten(speed, seconds):
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
        run(50)       
        if count % 10 == 0:
            tighten(20, 0.1)
        count += 1
    stop_motor()

def cc(box_number, box_offset, speed):
    count = 0
    count2 = 0
    temp = False

    clr_is_white = True
    # To compensate for sensor getting false positive by reading a change away from white and back to white again despite not having moved much,
    # count a minimum amount of iterations that at least should have passed before looking for a new white. There will be a certain minimum distance
    # because there always are a few iterations when moving between each box
    # If the card collector just calibrated there is very little distance to the first box so count will be less than 50 when reaching it.
    look_for_white = False
    if(colorsensor.color == colorsensor.COLOR_RED):
        look_for_white = True

    while box_number != box_offset:
        # The first case where count is 0, a initial tighten is done
        run(speed)      
        if count % 10 == 0:
            tighten(20, 0.1)
            print("tightens")

        if count2 >= 50:
            look_for_white = True
            count2 = 0

        if look_for_white:
            if clr_is_white == False and colorsensor.color == colorsensor.COLOR_WHITE:
                clr_is_white = True
                print("was at " + str(box_number))
                if speed >= 0:
                    box_number -= 1
                else:
                    box_number += 1
                print("is at " + str(box_number))   
                temp = True
                look_for_white = False

            else: 
                if colorsensor.color != colorsensor.COLOR_WHITE:
                    clr_is_white = False

        if temp and colorsensor.color == colorsensor.COLOR_RED:
            stop_motor()
            print("overran")
            return

        count += 1
        count2 += 1
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
    
#time.sleep(10)
#current_box = go_to_box(current_box, 1, global_speed)

#print("returns: " + str(current_box))
#current_box = go_to_box(2, 4)
