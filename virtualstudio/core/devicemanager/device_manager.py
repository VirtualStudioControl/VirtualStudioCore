from typing import Dict, Optional

from libmidictrl.device_manager.device_manager import getDevices as getMIDIDevices

from streamdeck.device_manager import DeviceManager as ElgatoDeviceManager

from virtualstudio.common.structs.hardware.hardware_wrapper import HardwareWrapper
from virtualstudio.core.devicemanager.hardware.midi.midi_device_wrapper import MidiDeviceWrapper
from virtualstudio.core.devicemanager.hardware.elgato.elgato_streamdeck_wrapper import StreamdeckDeviceWrapper

DEVICES: Optional[Dict[str, HardwareWrapper]] = None


def areDevicesLoaded():
    return DEVICES is not None


def getLoadedDevices() -> Dict[str, HardwareWrapper]:
    global DEVICES
    if DEVICES is not None:
        return DEVICES
    return {}


def loadDevices() -> Dict[str, HardwareWrapper]:
    global DEVICES
    if DEVICES is not None:
        return DEVICES

    DEVICES = {}

    midi_devices = getMIDIDevices()
    elgato_devices = ElgatoDeviceManager().enumerate()

    for dev in midi_devices:
        DEVICES[dev.getDeviceID()] = MidiDeviceWrapper(dev)

    for dev in elgato_devices:
        DEVICES[dev.id()] = StreamdeckDeviceWrapper(dev)

    return DEVICES

