from EV3Main import dispenser_scan
from EV3Main import run_slave_motor
from Network import host

from ev3dev2.motor import LargeMotor, OUTPUT_C, SpeedPercent

push = LargeMotor(OUTPUT_C)

while True:
    dispenser_scan.dispense_and_scan(100, 100)
    run_slave_motor.send_signal
    push.on_for_rotations(SpeedPercent(100), 1)