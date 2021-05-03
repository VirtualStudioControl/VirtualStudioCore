from ...devicemanager.device_manager import getLoadedDevices, areDevicesLoaded


def onSendDeviceList(msg):
    response = {
        "devices_loaded": areDevicesLoaded()
    }

    deviceList = []

    devices = getLoadedDevices()

    for d in devices:
        deviceList.append(devices[d].toDict())
    response["devices"] = deviceList

    return response