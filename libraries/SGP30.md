# SGP30

The [Adafruit SGP30 libary](https://github.com/adafruit/Adafruit_CircuitPython_SGP30) works with the Raspberrypi Pico. Example code for interfacing with the hardware:

```python
if __name__ == "__main__":
    import time
    from machine import I2C, Pin
    from Adafruit_SGP30 import Adafruit_SGP30

    sda = machine.Pin(0)
    scl = machine.Pin(1)
    i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)
    sgp30 = Adafruit_SGP30(i2c, 0x58)
    
    print("eCO2, VOC")
    print(sgp30.iaq_measure())
```

Where the `Adafruit_SGP30.py` file is either in the `lib` folder, or in the same folder as were the example script is executed. 
