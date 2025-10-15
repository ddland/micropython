# MicroPython

Working with sensors creates quite a few libraries. Some are written by me, others are adapted and even more are just used.

Here is an overview of the libraries I collected for various sensors and actuators. For my own libraries I use the [git - subtree](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges) module. 

## Tips and Tricks
Some example code in order to explain software concepts. 
* [Threading](https://github.com/ddland/micropython/threading) 
  Threading on the Raspberrypi Pico. Allowing 

## Libraries
### Acceleration
* [LIS3DHTR](https://github.com/ddland/mp_lis3dhtr)
  Driver for the [Grove - 3-Axis acceleromter](https://wiki.seeedstudio.com/Grove-3-Axis-Digital-Accelerometer-LIS3DHTR/) for the Rasbperry Pi Pico.
* [MSA301](https://github.com/wojciech-szmyt/msa301-micropython-driver)
  Library for the [Adafruit MSA301](https://learn.adafruit.com/msa301-triple-axis-accelerometer/overview) accelerometer. I had to change the device address (from 0x26 into 0x62, else it did not work). 
### Display
* [SSD1306](https://github.com/stlehmann/micropython-ssd1306) 
  Library for the SSD1306 screens (works also with SSD1315).
### Environment
* [SPS30](https://github.com/ddland/mp_sps30)
  Driver for the [SPS30](https://sensirion.com/products/catalog/SPS30) for the Raspberry Pi Pico. 
* [SEN66](https://github.com/ddland/mp_sen66)
  Driver for the [SEN66](https://sensirion.com/products/catalog/SEN66) for the Raspberry Pi Pico.
* [TLV493D](https://github.com/ddland/mp_tlv493d)
  Driver for the [TLV493D](https://learn.adafruit.com/adafruit-tlv493-triple-axis-magnetometer), based on the work from [Adafruit](https://learn.adafruit.com/) and [Maarten Doves](https://github.com/MDoves).
### Other
* [CutebotPro](https://github.com/ddland/mp_cutebotpro) 
  MicroPython library for the [CutebotPro](https://shop.elecfreaks.com/products/elecfreaks-smart-cutebot-pro-v2-programming-robot-car-for-micro-bit) with a [Micro:bit](https://microbit.org) running MicroPython.
* [MCP4725](https://github.com/ddland/mp_mcp4725) 
  Driver for the [MCP4725](https://www.sparkfun.com/sparkfun-i2c-dac-breakout-mcp4725.html) DAC. Based on work from [Wayoda](https://github.com/wayoda/micropython-mcp4725).
