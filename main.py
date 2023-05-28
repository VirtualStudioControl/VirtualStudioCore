import sys
from time import sleep

import streamdeck.transport.LibUSBHIDAPI as LibUSBHIDAPI

from virtualstudio.common.logging import logengine
from virtualstudio.common.account_manager import account_manager
from virtualstudio.common.eventmanager import eventmanager
from virtualstudio.common.plugin.module_loader import loadModulesFromPath
from virtualstudio.common.action_manager.actionmanager import loadActions
from virtualstudio.common.io.configtools import readJSON, writeJSON
from virtualstudio.common.profile_manager import profilemanager

from virtualstudio.core.data import constants as consts
from virtualstudio.core.devicemanager.device_manager import loadDevices, closeDevices
from virtualstudio.core.net import pytideserver
from virtualstudio.core.net.comserver import ComServer
from virtualstudio.core.tools.tools import storeAccounts, loadAccounts as loadAccountManager


import config

#region Builtin Action Imports
from virtualstudio.core.actions.device.switchprofilelauncher import SwitchProfileLauncher
from virtualstudio.core.actions.device.multiactionlauncher import MultiActionLauncher
#endregion


def initialiseLogging():
    logengine.LOG_FORMAT = config.LOG_FORMAT
    logengine.LOG_TO_CONSOLE = config.LOG_TO_CONSOLE


def setConfiguration():
    LibUSBHIDAPI.NATIVE_LIB_PATH = config.NATIVE_LIBRARY_PATH_HIDAPI

    for path in config.PLUGIN_DIRECTORY:
        sys.path.append(path)

    for path in config.PLUGIN_DIRECTORY:
        loadModulesFromPath(path)


def loadData():
    try:
        profilesets = readJSON(config.PROFILE_DATA_DIRECTORY + "/" + config.PROFILE_SET_DATA_FILE)
        profilemanager.fromDict(profilesets)
    except FileNotFoundError as err:
        print(err)
        #pass # Ignored, If no Profile file is found, just use new empty Profilesets


def loadAccounts():
    account_manager.storeAccountData = storeAccounts
    loadAccountManager()


def run():
    initialiseLogging()

    setConfiguration()
    try:
        loadAccounts()
        loadActions()
        loadData()
        loadDevices()

        pytideserver.runServer()

        consts.COM_SERVER = ComServer("127.0.0.1", config.CONFIGURATION_PORT)
        eventmanager.registerSink(consts.COM_SERVER.sendMessageJSON)
        consts.COM_SERVER.run()



    finally:
        print("Closing Devices")
        pytideserver.stopServer()
        closeDevices()

#        while(True):
#            sleep(1)


if __name__ == "__main__":
    run()
