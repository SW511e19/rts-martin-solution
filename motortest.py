from ev3dev2.motor import MediumMotor, OUTPUT_A, SpeedPercent

m = MediumMotor(OUTPUT_A)

m.on_for_rotations(SpeedPercent(100), 5)
m.run_forever
print("done")