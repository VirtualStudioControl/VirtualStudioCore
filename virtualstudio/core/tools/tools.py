import config

from ..devicemanager.device_manager import getCurrentProfileNameDict

from virtualstudio.common.io.configtools import writeJSON
from virtualstudio.common.profile_manager import profilemanager


def saveProfileSets():
    writeJSON(config.PROFILE_DATA_DIRECTORY + "/" + config.PROFILE_SET_DATA_FILE, profilemanager.toDict())


def saveCurrentProfileNames():
    writeJSON(config.PROFILE_DATA_DIRECTORY + "/" + config.DEVICE_CURRENT_PROFILE_NAME, getCurrentProfileNameDict())
