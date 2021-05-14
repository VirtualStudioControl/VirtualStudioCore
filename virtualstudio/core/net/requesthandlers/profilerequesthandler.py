from virtualstudio.common.profile_manager.profileset import ProfileSet
from ...devicemanager.device_manager import getDeviceByID

from virtualstudio.common.net.protocols.virtualstudiocom import constants
from virtualstudio.common.profile_manager.profilemanager import getOrCreateProfileSet

def onSendProfileSet(msg):
    deviceID = msg[constants.REQ_PROFILE_SET_PARAM_DEVICE]

    hardware = getDeviceByID(deviceID)
    profileSet: ProfileSet = getOrCreateProfileSet(hardware)
    response = {
        "profileset": profileSet.toDict()
    }

    return response