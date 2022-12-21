"""Example of a custom component exposing a service."""
from __future__ import annotations

import logging
import RPi.GPIO as IO

from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "x735_fan"
_LOGGER = logging.getLogger(__name__)

servo = 13
IO.setwarnings(False)
IO.setmode (IO.BCM)
IO.setup(servo,IO.OUT)
fan = IO.PWM(servo,25000)
fan.start(0)

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the sync service example component."""
    def set_speed_service(call: ServiceCall) -> None:
        """My first service."""
        _LOGGER.info(f'Received request to change fan speed to: {call.data}')
        if call.data['new_speed']:
            speed = call.data['new_speed']
        else:
            speed = 10
        fan.ChangeDutyCycle(speed)
        _LOGGER.info('Fan Speed Adjusted') 

    # Register our service with Home Assistant.
    hass.services.register(DOMAIN, 'set_speed', set_speed_service)

    # Return boolean to indicate that initialization was successfully.
    _LOGGER.info('tmf-one: expose_service_sync setup complete')
    return True