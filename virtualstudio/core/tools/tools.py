import config
from virtualstudio.common.io.configtools import writeJSON
from virtualstudio.common.profile_manager import profilemanager


def saveProfileSets():
    writeJSON(config.PROFILE_DATA_DIRECTORY + "/" + config.PROFILE_SET_DATA_FILE, profilemanager.toDict())
