from virtualstudio.common.structs.hardware.hardware_wrapper import HardwareWrapper


class RemoteDeviceWrapper(HardwareWrapper):

    def __init__(self, device):
        super().__init__(device, identifier, name, manufacturer)
