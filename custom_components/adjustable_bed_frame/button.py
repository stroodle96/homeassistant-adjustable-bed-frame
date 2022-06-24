from __future__ import annotations

import logging

from .adjustable_bed_frame import BedframeInstance

# Import the device class from the component that you want to support
import homeassistant.helpers.config_validation as cv
from homeassistant.components.button.ButtonEntity import (ButtonEntity, PLATFORM_SCHEMA)
from homeassistant.const import CONF_NAME, CONF_MAC
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

_LOGGER = logging.getLogger("adjustable_bed_frame")

# Validation of the user's configuration 
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME): cv.string,
    vol.Required(CONF_MAC): cv.string,
})

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the Bed Frame Button Platform"""
    # Add devices
    _LOGGER.info(pformat(config))

    button = {
        "name": config[CONF_NAME],
        "mac": config[CONF_MAC]
    }

    add_entities([BedFrame(ButtonEntity)])




class MyButton(ButtonEntity):

    # Properties
    def __init__(self, ButtonEntity) -> None:
        """Initialize the bedframe"""
        _LOGGER.info(pformat(button))
        self._button = BedframeInstance(button["mac"])
        self._name = ButtonEntity["name"]
        self._state = None

    @property
    def name(self) -> str:
        return self._name


    # Implement one of these methods.
    async def async_press(self) -> None:
        """Handle the button press."""
        await self._button.button1()


