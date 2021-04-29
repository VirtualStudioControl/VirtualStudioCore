import sys
import streamdeck.transport.LibUSBHIDAPI as LibUSBHIDAPI

from virtualstudio.core.devicemanager.device_manager import loadDevices
from virtualstudio.core.net.comserver import ComServer

def setConfiguration():
    # TODO: Write Plattform Independent
    LibUSBHIDAPI.NATIVE_LIB_PATH = sys.path[0] + "\\native\\hidapi.dll"


def run():
    loadDevices()
    server: ComServer = ComServer("127.0.0.1", 4233)
    server.start()


if __name__ == "__main__":
    setConfiguration()
    run()
