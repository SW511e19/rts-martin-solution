from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent

m1 = LargeMotor(OUTPUT_A)
m2 = LargeMotor(OUTPUT_B)

frontcount = 0
countlimit = 3

def back_dispense(speed):
    m1.on_for_rotations(SpeedPercent(speed), 2)

def front_dispense(speed):
    m2.on_for_rotations(SpeedPercent(speed), 1)

def request_scan():
    #Program this to ping the pie, and then have this function return a value based on the result.
    return 0

def dispense_and_scan(speedA, speedB):
    frontcount = 0
    s = 0
    while s == 0:
        if frontcount == countlimit:
            back_dispense(speedA)
            frontcount = 0
        front_dispense(speedB)
        s = request_scan()
    return s

