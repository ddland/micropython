import _thread

class BaseSensor:
    """ BaseClass for the sensor
    After filling in the __init__ and run methods you can run
    sensor readings on a different thread.
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
    