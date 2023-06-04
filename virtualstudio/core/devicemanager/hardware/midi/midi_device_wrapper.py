from typing import Callable

from libmidictrl.controls.abstract_control import AbstractControl
from libmidictrl.controls.button import Button
from libmidictrl.controls.fader import Fader
from libmidictrl.controls.rotary import RotaryEncoder
from libmidictrl.devices.device_interface import IDevice

from virtualstudio.common.structs.hardware.controls.button_wrapper import ButtonWrapper
from virtualstudio.common.structs.hardware.controls.fader_wrapper import FaderWrapper
from virtualstudio.common.structs.hardware.controls.rotaryencoder_wrapper import RotaryEncoderWrapper
from virtualstudio.common.structs.hardware.hardware_wrapper import *
from virtualstudio.core.net import pytideserver

logger = logengine.getLogger()

class MidiDeviceWrapper(HardwareWrapper):

    def __init__(self, device: IDevice):
        super().__init__(device, device.getDeviceID(), device.getDeviceName(), device.getDeviceManufacturer())

        device.open()

        self.createControlWrappers()

    def close(self):
        self.device.close()

    def getType(self):
        return HARDWARE_TYPE_MIDI

    def createControlWrappers(self):
        self.device: IDevice

        controls = []
        controls.extend(self.device.getButtons())
        controls.extend(self.device.getFaders())
        controls.extend(self.device.getRotaryEncoders())

        self.controls: List = [None] * len(controls)

        for c in controls:
            if isinstance(c, Button):
                self.appendButtonWrapper(c)
            elif isinstance(c, Fader):
                self.appendFaderWrapper(c)
            elif isinstance(c, RotaryEncoder):
                self.appendRotaryEncoderWrapper(c)

    #region Button
    def appendButtonWrapper(self, c: Button):
        wrapper = ButtonWrapper(ledStateSetter=self.__generateLEDSetterBTN(c), ident=c.index)
        self.device.addEventListener(c.statusPressed, c.idIn, self.__generateButtonWrapperCallbackPressed(wrapper))
        self.device.addEventListener(c.statusReleased, c.idIn, self.__generateButtonWrapperCallbackReleased(wrapper))
        self.controls[c.index] = wrapper

    def __generateButtonWrapperCallbackPressed(self, wrapper: ButtonWrapper):

        def cb(message: List[int], deltatime):
            wrapper.keyDown()
            pytideserver.sendButtonPress(wrapper.controlID, self)

        return cb

    def __generateButtonWrapperCallbackReleased(self, wrapper: ButtonWrapper):

        def cb(message: List[int], deltatime):
            wrapper.keyUp()
            pytideserver.sendButtonRelease(wrapper.controlID, self)
        return cb


    def __generateLEDSetterBTN(self, c: Button) -> Callable[[int], bool]:
        def __cb(state: int) -> bool:
            c.device.setButtonValue(c, state!=0)
            return True

        return __cb

    #endregion

    #region Fader

    def appendFaderWrapper(self, c: Fader):
        wrapper = FaderWrapper(faderValueSetter=self.__generateValueSetterFader(c), ident=c.index)
        self.device: IDevice
        if c.status_touch_begin == c.status_touch_end:
            self.device.addEventListener(c.status_touch_begin, c.idTouch, self.__generateFaderTouchCallback(wrapper))
        else:
            self.device.addEventListener(c.status_touch_begin, c.idTouch, self.__generateFaderTouchCallback(wrapper))
            self.device.addEventListener(c.status_touch_end, c.idTouch, self.__generateFaderTouchCallback(wrapper))
        self.device.addEventListener(c.status_value_changed, c.idIn, self.__generateFaderValueCallback(wrapper))
        self.controls[c.index] = wrapper

    def __generateFaderTouchCallback(self, wrapper: FaderWrapper):
        def cb(message: List[int], deltatime):
            if message[2] > 63:
                wrapper.touchStart()
                pytideserver.sendFaderTouchBegin(wrapper.controlID, self)
            else:
                wrapper.touchEnd()
                pytideserver.sendFaderTouchEnd(wrapper.controlID, self)

        return cb

    def __generateFaderValueCallback(self, wrapper: FaderWrapper):
        def cb(message: List[int], deltatime):
            wrapper.touchValueChanged(message[2])
            pytideserver.sendFaderValueChange(message[2], wrapper.controlID, self)

        return cb

    def __generateValueSetterFader(self, c: Fader) -> Callable[[int], bool]:
        def __cb(value: int) -> bool:
            if value < 0 or value > 127:
                return False
            c.device.setFaderValue(c, value)
            pytideserver.sendFaderValueChange(value, c.index, self)

            return True

        return __cb

    #endregion

    #region Rotary Encoder
    def appendRotaryEncoderWrapper(self, c: RotaryEncoder):
        wrapper = RotaryEncoderWrapper(ledValueSetter=self.__generateValueSetterRotaryEncoder(c),
                                       ledModeSetter=self.__generateModeSetterRotaryEncoder(c), ident=c.index)
        self.device: IDevice

        if c.status_up == c.status_down:
            self.device.addEventListener(c.status_up, c.idClick, self.__generateRotaryEncoderClickCallback(wrapper))
        else:
            self.device.addEventListener(c.status_up, c.idClick, self.__generateRotaryEncoderClickCallback(wrapper))
            self.device.addEventListener(c.status_down, c.idClick, self.__generateRotaryEncoderClickCallback(wrapper))
        self.device.addEventListener(c.status_value_changed, c.idIn, self.__generateRotaryEncoderValueCallback(wrapper))
        self.controls[c.index] = wrapper

    def __generateRotaryEncoderClickCallback(self, wrapper: RotaryEncoderWrapper):
        def cb(message: List[int], deltatime):
            if message[2] > 63:
                wrapper.keyDown()
                pytideserver.sendRotaryEncoderPress(wrapper.controlID, self)
            else:
                wrapper.keyUp()
                pytideserver.sendRotaryEncoderRelease(wrapper.controlID, self)

        return cb

    def __generateRotaryEncoderValueCallback(self, wrapper: RotaryEncoderWrapper):
        def cb(message: List[int], deltatime):
            wrapper.rotate(message[2])
            pytideserver.sendRotaryEncoderValueChange(message[2], wrapper.controlID, self)
        return cb

    def __generateValueSetterRotaryEncoder(self, c: RotaryEncoder) -> Callable[[int], bool]:
        def __cb(value: int) -> bool:
            if value < 0 or value > 127:
                return False
            c.device.setRotaryValue(c, value)
            pytideserver.sendRotaryEncoderValueChange(value, c.index, self)
            return True

        return __cb

    def __generateModeSetterRotaryEncoder(self, c: RotaryEncoder) -> Callable[[int], bool]:
        def __cb(value: Optional[int]) -> bool:
            if value is None or value < 0 or value > 127:
                return False
            c.device.setLayer(c.layer)
            c.device.setRotaryLEDMode(c, value)
            return True

        return __cb

    #endregion
