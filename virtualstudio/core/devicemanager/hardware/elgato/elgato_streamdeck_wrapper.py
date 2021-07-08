from virtualstudio.common.structs.hardware.hardware_wrapper import *

from streamdeck.devices.streamdeck import StreamDeck


STREAMDECK_ICON_RESOLUTION = {
    "Stream Deck Mini": (80, 80),
    "Stream Deck Original": (72, 72),
    "Stream Deck Original (V2)": (72, 72),
    "Stream Deck XL": (96, 96),
}


STREAMDECK_ICON_FORMAT = {
    "Stream Deck Mini": "BMP",
    "Stream Deck Original": "BMP",
    "Stream Deck Original (V2)": "JPEG",
    "Stream Deck XL": "JPEG",
}


class StreamdeckDeviceWrapper(HardwareWrapper):

    def __init__(self, device: StreamDeck):
        super().__init__(device, device.id(), device.deck_type(), "Elgato")

    def getHardwareParameters(self) -> Optional[Dict]:
        parameters = {}

        parameters["icon_resolution"] = STREAMDECK_ICON_RESOLUTION[self.name]
        parameters["icon_format"] = STREAMDECK_ICON_FORMAT[self.name]

        return parameters

    def getType(self):
        return HARDWARE_TYPE_ELGATO

    def bindProfile(self, profile):
        self.currentProfile = profile.name