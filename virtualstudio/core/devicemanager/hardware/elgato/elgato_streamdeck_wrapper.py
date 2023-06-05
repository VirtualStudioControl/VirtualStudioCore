from virtualstudio.common.structs.hardware.controls.imagebutton_wrapper import ImagebuttonWrapper
from virtualstudio.common.structs.hardware.hardware_wrapper import *

from streamdeck.devices.streamdeck import StreamDeck
from threading import Lock

from virtualstudio.core.net import pytideserver


class StreamdeckDeviceWrapper(HardwareWrapper):

    def __init__(self, device: StreamDeck):
        super().__init__(device, device.id(), device.deck_type(), "Elgato")

        self.imageWriteLock = Lock()

        device.open()

        self.createControlWrappers()
        self.addProfileChangedCallback(self.onProfileChangeEvent)

    def onProfileChangeEvent(self, profileName):
        pytideserver.sendProfileChange(profileName, self)

    def close(self):
        self.device.close()

    def createControlWrappers(self):

        for i in range(self.device.key_count()):
            self.setupImageButtonWrapper(i)
        self.device.set_key_callback(self.__keyCallback)

    def setupImageButtonWrapper(self, idx: int):
        wrapper = ImagebuttonWrapper(imageSetter=self.__generateSetImage(idx), ident=idx)
        self.device : StreamDeck
        wrapper.setImage(self.device.BLANK_KEY_IMAGE)
        self.controls.append(wrapper)

    def __keyCallback(self, device, buttonID: int, isDown: bool):
        control = self.controls[buttonID]

        if isDown:
            control.keyDown()
            pytideserver.sendButtonPress(buttonID, self)
        else:
            control.keyUp()
            pytideserver.sendButtonRelease(buttonID, self)

    def __generateSetImage(self, index):
        def __cb(data: Any) -> bool:
            try:
                with self.imageWriteLock:
                    self.device.set_key_image(index, data)
            except Exception as ex:
                logger.exception(ex)
                return False
            return True

        return __cb

    def getHardwareParameters(self) -> Optional[Dict]:
        parameters = {}

        parameters["icon_resolution"] = (self.device.KEY_PIXEL_WIDTH, self.device.KEY_PIXEL_HEIGHT)
        parameters["icon_format"] = self.device.KEY_IMAGE_FORMAT
        parameters["icon_flip"] = self.device.KEY_FLIP

        return parameters

    def getType(self):
        return HARDWARE_TYPE_ELGATO
