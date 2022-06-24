import asyncio
from bleak import BleakClient, BleakScanner
from crccheck.crc import Crc8Maxim
import logging

WRITE_UUID = "?????"
LOGGER = logging.getLogger(__name__)

async def discover():
    """Discover Bluetooth LE devices."""
    devices = await BleakScanner.discover()
    LOGGER.debug("Discovered devices: %s", [{"address": device.address, "name": device.name} for device in devices])
    return [device for devices if device.name.startswith("base-i5")]

    class BedframeInstance:
        def __init__(self, mac: str) -> None:
            self._mac = mac
            self._device = BleakClient(self._mac)
#            self._is_on = None
#            self._brightness = None

        async def _send(self, data: bytearray):
            LOGGER.debug(''.join(format(x, ' 03x') for x in data))

            if (not self._connected):
                await self.connect()

            crcinst = Crc8Maxim()
            crcinst.process(data)
            await self._device.write_gatt_char(WRITE_UUID, data + crcinst.finalbytes())

        @property
        def mac(self):
            return self._mac

#        @property
#        def is_on(self):
#            return self._is_on
#
#        @property
#        def brightness(self):
#            return self._brightness

        async def button1(self):
            header = bytes.fromhex("")
            command = bytes.fromhex("01")
            params = bytes.fromhex("000")

            await self._send(header + command + params)
#            self._is_on = True

