from typing import Dict, Optional, List

from libmidictrl.device_manager.device_manager import getDevices as getMIDIDevices

from streamdeck.device_manager import DeviceManager as ElgatoDeviceManager
from virtualstudio.common.profile_manager import profilemanager

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


def getLoadedDeviceNames() -> List[str]:
    global DEVICES
    if DEVICES is not None:
        result = []
        for key in DEVICES:
            result.append(DEVICES[key].getHardwareFamily())
        return result
    return []


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

    for id in DEVICES:
        pset = profilemanager.getOrCreateProfileSet(DEVICES[id])
        DEVICES[id].bindProfile(pset.getDefaultProfile())

    return DEVICES


def closeDevices():
    for dev in DEVICES:
        DEVICES[dev].close()


def getDeviceByID(deviceID: str) -> Optional[HardwareWrapper]:
    if DEVICES is None or deviceID not in DEVICES:
        return None
    return DEVICES[deviceID]


def getCurrentProfileNameDict():
    res = {}

    for dev in DEVICES:
        res[dev] = DEVICES[dev].currentProfile