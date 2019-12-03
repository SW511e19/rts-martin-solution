from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent
import time

colorsensor = ColorSensor()
colorsensor.MODE_COL_COLOR
m1 = LargeMotor(OUTPUT_B) #Cord has to go over the wheel
m2 = LargeMotor(OUTPUT_C) #Cord has to go under the wheel

box_number = 0 #THE CURRENT BOX WE ARE AT
speed = -25
emergency_escape = 0

def run(speed, seconds):
    m1.on(SpeedPercent(speed))
    m2.on(SpeedPercent((speed * 0.9)))
    time.sleep(seconds)

def reset(speed, seconds):
    m1.on(SpeedPercent(speed))
    m2.on(SpeedPercent(-(speed * 0.9)))
    time.sleep(seconds)

def start_motor(speed, modifier):
    run(speed, 0.03 * modifier)
    reset(speed, 0.001 * modifier)
    stop_motor()

def stop_motor():
    m1.on(SpeedPercent(0))
    m2.on(SpeedPercent(0))

def calibrate(speed):
    while (colorsensor.color != colorsensor.COLOR_RED):
        start_motor(speed, 1)
    stop_motor()

def cc(box_offset, speed):
    box_number = 0
    clr_is_white = True
    while ( (box_number < box_offset)  ): #& (emergencyescape <= 50)
        start_motor(speed, 2)
        print(colorsensor.color)
        if(box_number < box_offset):
            if( (clr_is_white == False) & (colorsensor.color == colorsensor.COLOR_WHITE) ):
                clr_is_white = True
                box_number += 1
 
            else: 
                if(colorsensor.color != colorsensor.COLOR_WHITE):
                    clr_is_white = False
                    print("Passed a box.")
    stop_motor()

calibrate(-speed)
#run(6, speed)
while True:
    cc(6, speed)
    cc(6, -speed)
m1.off()
m2.off()