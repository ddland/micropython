import _thread
import time

""" Multithread example for the RaspberryPi Pico

Small example where on a different thread a counter is counting upwards.
Every second it is incremented by one.

In another thread (the main thread) you can interact with the counter.

"""

class Sensor:
    counter = 0
    nthreads = 0
    running = False
    """ Mock-up sensor class.

    Class provides some insights in the _thread micropython library.
    """
    
    def __init__(self):
        """ Initialize the sensor (object).
        
        attributes:
           counter: increments by one every second
           nthreads: number of threads active (should be 0 or 1)
           running: boolean which stops (False) or starts (True) the measurement. 
        """
        pass
        
        
    def start(self, debug=False):
        """ start a new thread """
        # make sure there is not another thread running
        if self.nthreads > 0:
            if debug:
                print("Another thread already running!")
            return
        self.nthreads = 1
        _thread.start_new_thread(self.run, ())
        
    def output(self):
        """ Returns the value of the counter. """
        return self.counter

    def stop(self):
        """ Stop the running thread

        Function stops the running thread and waits 5 seconds before continuing.
        """
        self.running = False
        time.sleep(5) # provide some time to kill the thread
        self.nthreads = 0
        
    
    def reset(self):
        """ Reset the counter to 0."""
        self.counter = 0
    
    def run(self):
        """ Main function which is executed on the 2nd core.

        Sets the attribute 'running' of this class to True and executes the
        main loop. The loop will run forever until the attribute 'running' is
        set to False, or the program is killed.
        """
        self.running = True
        while self.running:
            self.counter += 1
            time.sleep(1)
    
    
if __name__ == "__main__":
    # Example useage:
    # Create a sensor object and start the thread
    s = Sensor()
    s.start() # counter should increment by 1 every second
    
    # start a local loop to poll the output method of the thread every few
    # seconds
    running = True
    counter = 0
    try:
        while running:
            print(counter, s.output())
            time.sleep(3)
            counter += 1
            if counter % 7 == 0: # every 7th run the sensor-counter is reset
                s.reset()
    except KeyboardInterrupt:
        running = False
    # even now the thread is not closed. You can still interact with the object
    # using s.stop() / s.start() / s.reset() or s.output()
        