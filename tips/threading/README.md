# Threading

With 2 cores available on the Raspberrypi Pico it is a waist to let one be idle!

With help from the `_thread` library it is possible to run code on the second core (or thread). 
For this you need to setup a helper class. The code in the second class will be running on the 2nd thread (or core). An example is given an [example code](example_sensor.py) for utilizing one core for a counter (could also be a sensor continuously measuring) and allowing interaction with the second core from the first.

With many different sensors, but always almost the same setup for a thread-based measurement it can be convenient to create a base-class. For example the base class `BaseSensor` in the file `basesensor.py`:

```python
import _thread

class BaseSensor:
    """ Class for the ADC sensor
    Once running, will print the measured values from the ADC channel.
    """
    
    nthreads = 0
    running = False
    
    def __init__(self):
        """ Sensor class initializing
        Add your own hardware and variables!
        """
        pass
    
    def start(self):
        if self.nthreads > 0:
            return
        self.nthreads = 1
        _thread.start_new_thread(self.run, ())
        
    def run(self):
        raise NotImplementedError("You need to implement the run method!")
            
    def stop(self):
        self.running = False
        self.nthreads = 0
    
```

Implements the basic `start`, `stop` and requires a `run` method. Using this class you only have to implement your own Sensor class with the `run`- and `__init__`-method. The other methods are already taken care of.

```python
import machine
import time
import basesensor

class Sensor(basesensor.BaseSensor):
 
    def __init__(self, ADC=0, dt=1):
        super(Sensor, self).__init__()
        """ Sensor class initializing

        arguments: ADC: ADC number from the Pico Pi (0,1,2,3)
                   dt: delay between prints from the ADC
        """
        self.dt = dt
        self.adc = machine.ADC(ADC)
                
    def run(self):
        self.running = True
        while self.running:
            print(3.3*self.adc.read_u16()/(2**16-1))
            time.sleep(self.dt)

if __name__ == "__main__":
    sensor = Sensor()
    sensor.start()

```

Creating an instance of the Sensor class and calling it's `start` method. An fully worked example is in the [MPC4725 DAC](https://github.com/ddland/mp_mcp4725) repository.


