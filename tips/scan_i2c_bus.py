# scan all i2c on picopi
# connect a i2c device and run the scripts
# whenever there is a device detected, the bus and GPIO pins are printed.

import machine
        
sda0 = [0,4,8,12,16,20]
sda1 = [2,6,10,14,18,26]

buses = {0:sda0, 1:sda1}

for bus in buses.keys():
    for sda in buses[bus]:
        s = machine.I2C(bus, sda=sda, scl=sda+1)
        devs = s.scan()
        if len(devs) > 0:
            print(bus, sda, sda+1, devs)
        