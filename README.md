## Introduction

Since [Home Assistant](https://github.com/home-assistant) removed support from [Home Assistant Core](https://github.com/home-assistant/core) handling of Geekworm's x735 Shield (V2.5 & V3.0) with PWM Fan Control can't be managed out of the box anymore. Therefore, we've created a custom component to handle the PWM fan control.

## Installation
* Copy contents of folders custom_components and python_scripts into the respective folders within your Home Assistant configuration folder
* Restart Home Assistant
* Copy contents of configuration.yaml into your Home Assistant configuration.yaml
* Copy contents of automations.yaml into your Home Assistant automations.yaml
* Restart Home Assistant

## Configuration
* adjust the fancurve in <config>/python_scripts/x735_fancurve.py to your needs

## How it works
Once set up following happens:
* the automation triggers the python script 'x735_fancurve.py' whenever the temperature of the CPU changes
* the python script calculates the new fan speed based on the fancurve and the current temperature
* the python script sets the fan speed by calling the  service x735_fan.set_speed
