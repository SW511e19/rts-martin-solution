from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent
from ev3dev2.sensor.lego import InfraredSensor

m1 = LargeMotor(OUTPUT_A)
m2 = LargeMotor(OUTPUT_B)
s = InfraredSensor
s.MODE_IR_PROX

motortime = 0.05

#Sensor gets closer to the edge of the platform
def moveforward(targetdistance):
    while s.num_values > targetdistance:
        m1.on_for_seconds(SpeedPercent(50), motortime)
        m2.on_for_seconds(SpeedPercent(50), motortime)

#Sensor gets further away from the edge of the platform
def movebackward(targetdistance):
    while s.num_values < targetdistance:
        m1.on_for_seconds(SpeedPercent(-50), motortime)
        m2.on_for_seconds(SpeedPercent(-50), motortime)