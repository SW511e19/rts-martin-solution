from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent

m1 = LargeMotor(OUTPUT_C)
m2 = LargeMotor(OUTPUT_B)

m1.on(SpeedPercent(0))
m2.on(SpeedPercent(0))