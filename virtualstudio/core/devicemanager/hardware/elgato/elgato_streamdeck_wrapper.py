from virtualstudio.common.structs.hardware.hardware_wrapper import *

from streamdeck.devices.streamdeck import StreamDeck

class StreamdeckDeviceWrapper(HardwareWrapper):

    def __init__(self, device: StreamDeck):
        super(StreamdeckDeviceWrapper, self).__init__(device, device.id(), device.deck_type(), "Elgato")

    def getType(self):
        return HARDWARE_TYPE_ELGATO

    def bindProfile(self, profile):
        pass