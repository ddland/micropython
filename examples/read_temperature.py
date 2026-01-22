import machine
import time

def readTemperature(adc):
    # convert 16bit ADC value to voltage (0-3.3V)
    adc_v = (3.3/(2**16-1))*adc.read_u16()
    # according to datasheet RP2350 (p1073)
    temp = 27 - (adc_v - 0.706)/0.001721
    return temp


adc = machine.ADC(4)   # temperature sensor on ADC4
running = True         # stop the loop when False
while running:
    try:
        print(time.time(), readTemperature(adc))
        time.sleep(1)  # measure once per second
    except KeyboardInterrupt:
        running = False # CTRL-C pressed, stop the measurement

