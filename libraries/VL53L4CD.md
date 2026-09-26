# VL53L4CD

Optical range sensor from Adafruit. Uses a time-of-flight algorithm to measure the delay between send and arrival time of a pulse of light. 

There is example code available from [AHSPC](https://github.com/AHSPC/VL53L4CD_micropython). They wrote a wrapper around the Adafruit circuitpython I2C implementations. You also need to upload the [i2c_device.py](https://github.com/AHSPC/adafruit_i2c_device_micropython/blob/main/i2c_device.py) file to the same directory as the driver.
Once both are installed you can run some example code:

```
from vl53l4cd import VL53L4CD
import machine

# Make sure to set the correct pins!
i2c = machine.I2C(sda=machine.Pin(0), scl=machine.Pin(1))

vl53 = VL53L4CD(i2c)
# OPTIONAL: can set non-default values
vl53.inter_measurement = 0 # makes sensor run in "continuous mode" (default)
vl53.timing_budget = 20 # spend 20ms on each measurement

# print model, type
model_id, module_type = vl53.model_info

# start sensor
vl53.start_ranging()

running = True
while running:
    try:
        dist = vl53.get_distance()
        print(f"Distance: {dist} cm")
    except KeyboardInterrupt:
        running = False
```

When you put an object in front of the sensor, the sensor will return the measured distance. 
