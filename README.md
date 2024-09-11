# MicroPython

Working with sensors creates quite a few libraries. Some are written by me, others are adapted and even more are just used.

Here is an overview of the libraries I collected for various sensors and actuators. For my own libraries I use the [git - subtree](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges) module. 

## Libraries
### Acceleration
* [LIS3DHTR](https://github.com/ddland/mp_lis3dhtr)
  Driver for the [Grove - 3-Axis acceleromter](https://wiki.seeedstudio.com/Grove-3-Axis-Digital-Accelerometer-LIS3DHTR/) for the Rasbperry Pi Pico.
* [MSA301](https://github.com/wojciech-szmyt/msa301-micropython-driver)
  Library for the [Adafruit MSA301](https://learn.adafruit.com/msa301-triple-axis-accelerometer/overview) accelerometer. I had to change the device address (from 0x26 into 0x62, else it did not work). 
### Environment
* [SPS30](https://github.com/ddland/mp_sps30)
  Driver for the [SPS30](https://sensirion.com/products/catalog/SPS30) for the Raspberry Pi Pico. 
### Other
* [CutebotPro](https://github.com/ddland/mp_cutebotpro) 
  MicroPython library for the [CutebotPro](https://shop.elecfreaks.com/products/elecfreaks-smart-cutebot-pro-v2-programming-robot-car-for-micro-bit) with a [Micro:bit](https://microbit.org) running MicroPython.
