import machine

wdt = machine.WDT()
# feed the watchdog every few seconds (atmost every 8.388 s)
# https://docs.micropython.org/en/latest/library/machine.WDT.html

# copy this line to disable the watchdog
# handy if main.py file has a watchdog, while you still want to update it.

import sys
version = sys.platform
if sys.platform == 'rp2':
    import machine; machine.mem32[0x400d8000] = machine.mem32[0x400d8000] & ~(1<<30)
else:
    import machine; machine.mem32[0x40058000] = machine.mem32[0x40058000] & ~(1<<30)
