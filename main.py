import sys
import streamdeck.transport.LibUSBHIDAPI as LibUSBHIDAPI

from virtualstudio.common.logging import logengine
from virtualstudio.common.plugin.module_loader import loadModulesFromPath
from virtualstudio.common.action_manager.actionmanager import loadActions
from virtualstudio.common.io.configtools import readJSON, writeJSON
from virtualstudio.common.profile_manager import profilemanager

from virtualstudio.core.devicemanager.device_manager import loadDevices
from virtualstudio.core.net.comserver import ComServer

import config

#region Builtin Action Imports
from virtualstudio.core.actions.device.switchprofilelauncher import SwitchProfileLauncher
from virtualstudio.core.actions.device.multiactionlauncher import MultiActionLauncher
#endregion

def setConfiguration():
    LibUSBHIDAPI.NATIVE_LIB_PATH = config.NATIVE_LIBRARY_PATH_HIDAPI
    loadModulesFromPath(config.PLUGIN_DIRECTORY)

def loadData():
    try:
        profilesets = readJSON(config.PROFILE_DATA_DIRECTORY + "/" + config.PROFILE_SET_DATA_FILE)
        profilemanager.fromDict(profilesets)
    except FileNotFoundError as err:
        print(err)
        #pass # Ignored, If no Profile file is found, just use new empty Profilesets


def run():
    loadDevices()
    loadActions()
    loadData()
    server: ComServer = ComServer("127.0.0.1", config.CONFIGURATION_PORT)
    server.start()


if __name__ == "__main__":
    setConfiguration()

    run()

