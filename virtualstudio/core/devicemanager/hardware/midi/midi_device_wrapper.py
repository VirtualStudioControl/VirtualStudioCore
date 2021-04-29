from virtualstudio.common.structs.hardware.hardware_wrapper import *

from libmidictrl.devices.device_interface import IDevice

class MidiDeviceWrapper(HardwareWrapper):

    def __init__(self, device: IDevice):
        super(MidiDeviceWrapper, self).__init__(device, device.getDeviceID(), device.getDeviceName(), device.getDeviceManufacturer())

    def getType(self):
        return HARDWARE_TYPE_MIDI

    def bindProfile(self, profile):
        pass