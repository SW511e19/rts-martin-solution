from ev3dev2.sensor.lego import ColorSensor

sensor = ColorSensor()
sensor.MODE_COL_COLOR

while True:
    print("Color name:" + str(sensor.color_name))
    print("Color value:" + str(sensor.color))
