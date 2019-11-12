from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent
import time

colorsensor = ColorSensor()
colorsensor.MODE_COL_COLOR
m1 = LargeMotor(OUTPUT_C)
m2 = LargeMotor(OUTPUT_B)

box_number = 0 #THE CURRENT BOX WE ARE AT
speed = -15
emergency_escape = 0

def start_motor(speed):
    m1.on(SpeedPercent(speed))
    m2.on(SpeedPercent(-speed))

def stop_motor():
    m1.on(SpeedPercent(0))
    m2.on(SpeedPercent(0))

def calibrate(speed):
    start_motor(speed)
    time.sleep(5)
    stop_motor()
    run(1, -40)

def run(box_offset, speed):
    box_number = 0
    clr_is_white = True
    start_motor(speed)
    while ( (box_number < box_offset)  ): #& (emergencyescape <= 50)
        #print(colorsensor.color)
        if(box_number < box_offset):
            if( (clr_is_white == False) & (colorsensor.color == colorsensor.COLOR_WHITE) ):
                
                clr_is_white = True
                box_number += 1
                print("Registered a box. \nBoxes moved:" + str(box_number))
                stop_motor()
                time.sleep(3)
                start_motor(speed)
 
            else: 
                if(colorsensor.color != colorsensor.COLOR_WHITE):
                    clr_is_white = False
                    print("Passed a box.")
    stop_motor()

calibrate(25)
#run(6, speed)
while True:
    run(6, speed)
    run(6, -speed)