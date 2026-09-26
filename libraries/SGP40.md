# SGP40

The SGP40 VOC sensor has a micropython library from [Agners](https://github.com/agners/micropython-sgp40). 
Once the sgp40.py is installed (either in the `lib` folder on your Raspberrypi Pico or in the same folder as your main script) you can interface it:

```python
import time
from machine import I2C, Pin
from sgp40 import SGP40

sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)
sgp40 = SGP40(i2c, 0x59)
 
while True:
    sgp40.measure_raw()
    time.sleep(1)
```

The sensor returns a `raw` value which needs to be converted. The measure_raw call has arguments for temperature and humidity. You should add an extra sensor in order to get the right raw value for the environment you are measureing. With the default call the measurements are done without temperature and humidity compensation. 

Sensirion has a [gas-index-algorithm]([https://github.com/Sensirion/gas-index-algorithm), but that is not yet implemented on a Raspberrypi Pico. You can run the algorithm on measured data.


