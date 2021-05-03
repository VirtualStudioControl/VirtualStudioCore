import sys
import streamdeck.transport.LibUSBHIDAPI as LibUSBHIDAPI

from virtualstudio.common.logging import logengine
from virtualstudio.common.action_manager.actionmanager import loadActions

from virtualstudio.core.devicemanager.device_manager import loadDevices
from virtualstudio.core.net.comserver import ComServer

import config

#region Builtin Action Imports
from virtualstudio.core.actions.device.switchprofilelauncher import SwitchProfileLauncher
from virtualstudio.core.actions.device.multiactionlauncher import MultiActionLauncher
#endregion

def setConfiguration():
    LibUSBHIDAPI.NATIVE_LIB_PATH = config.NATIVE_LIBRARY_PATH_HIDAPI


def run():
    loadDevices()
    loadActions()
    server: ComServer = ComServer("127.0.0.1", config.CONFIGURATION_PORT)
    server.start()


if __name__ == "__main__":
    setConfiguration()
    run()
