temp = float(hass.states.get('sensor.processor_temperature').state)

logger.info("Pi CPU Temp is {} ".format(temp))

if temp > 70:                            
    speed = 100                             
elif temp > 60:
    speed = 75
elif temp > 50:
    speed = 50
elif temp > 40:
    speed = 40
elif temp > 32:
    speed = 25
elif temp > 25:
    speed = 15
else:
    speed = 0

service_data = {"new_speed": speed}
hass.services.call("x735_fan", "set_speed", service_data, False)
hass.states.set('x735_fan.speed', speed, {'friendly_name': 'x735 Fan Speed', 'unit_of_measurement': '%'})
logger.info("x735 fan speed set to {} ".format(speed))