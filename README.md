## Introduction

This custom component for Home Assistant enables PWM fan control for [Geekworm's x735 Shield (V2.5 & V3.0)](https://github.com/geekworm-com/x735-v2.5) on RPis running Home Assistant OS.

## Installation
* Copy contents of folder 'custom_components' to Home Assistant's \<CONFIG\>/custom_components/ folder
* Copy contents of folder 'python_scripts' to Home Assistant's \<CONFIG\>/python_scripts/ folder
* Restart Home Assistant
* Copy contents of configuration.yaml into your Home Assistant configuration.yaml
* Copy contents of automations.yaml into your Home Assistant automations.yaml
* Restart Home Assistant

## Configuration
* adjust the fancurve in \<CONFIG\>/python_scripts/x735_fancurve.py to your needs

## How it works
Once set up following happens:
* the automation triggers the python script 'x735_fancurve.py' whenever the temperature of the CPU changes
* the python script then reads the cpu temperature from 'sensor.processor_temperature', calculates the new fan speed, calls the service 'x735_fan.set_speed' and updates the sensor 'x735_fan.speed'
* the service 'x735_fan.set_speed' then changes the fan speed using RPi.GPIO
