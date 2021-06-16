from typing import Optional

from virtualstudio.common.profile_manager.profileset import ProfileSet
from virtualstudio.common.structs.profile.profile import Profile, fromDict as profileFromDict
from ...devicemanager.device_manager import getDeviceByID

from virtualstudio.common.net.protocols.virtualstudiocom import constants
from virtualstudio.common.profile_manager.profilemanager import getOrCreateProfileSet

from virtualstudio.core.tools.tools import saveProfileSets


def onSendProfileSet(msg):
    deviceID = msg[constants.REQ_PROFILE_SET_PARAM_DEVICE]

    hardware = getDeviceByID(deviceID)
    profileSet: ProfileSet = getOrCreateProfileSet(hardware)
    saveProfileSets()
    response = {
        "profileset": profileSet.toDict()
    }

    return response


def onSetCurrentProfile(msg):
    deviceID = msg[constants.REQ_SET_CURRENT_PROFILE_PARAM_DEVICE]
    profileName = msg[constants.REQ_SET_CURRENT_PROFILE_PARAM_PROFILENAME]

    hardware = getDeviceByID(deviceID)
    profileSet = getOrCreateProfileSet(hardware)
    hardware.bindProfile(profileSet.getProfile(profileName))

    response = {
        "success": True,
    }

    return response


def onAddProfileToSet(msg):
    deviceID = msg[constants.REQ_ADD_PROFILE_PARAM_DEVICE]
    profileDict = msg[constants.REQ_ADD_PROFILE_PARAM_PROFILE]

    profileSet: Optional[ProfileSet] = None
    try:
        hardware = getDeviceByID(deviceID)
        profileSet = getOrCreateProfileSet(hardware)
        profile: Profile = profileFromDict(profileDict)
        profileSet.appendProfile(profile)
        saveProfileSets()
        success = True
    except:
        success = False

    response = {
        "success": success,
        "profileset": profileSet.toDict()
    }

    return response


def onUpdateProfile(msg):
    deviceID = msg[constants.REQ_UPDATE_PROFILE_PARAM_DEVICE]
    profileDict = msg[constants.REQ_UPDATE_PROFILE_PARAM_PROFILE]

    profileSet: Optional[ProfileSet] = None
    try:
        hardware = getDeviceByID(deviceID)
        profileSet = getOrCreateProfileSet(hardware)
        profile: Profile = profileFromDict(profileDict)
        profileSet.updateProfile(profile)
        saveProfileSets()
        success = True
    except:
        success = False

    response = {
        "success": success,
        "profileset": profileSet.toDict()
    }

    return response


def onRemoveProfile(msg):
    deviceID = msg[constants.REQ_REMOVE_PROFILE_PARAM_DEVICE]
    profileName = msg[constants.REQ_REMOVE_PROFILE_PARAM_PROFILENAME]

    hardware = getDeviceByID(deviceID)
    profileSet = getOrCreateProfileSet(hardware)

    try:
        profileSet.removeProfile(profileName)
        saveProfileSets()
        success = True
    except:
        success = False

    response = {
        "success": success,
        "profileset": profileSet.toDict()
    }

    return response

