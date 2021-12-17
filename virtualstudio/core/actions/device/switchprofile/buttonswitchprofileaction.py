from typing import Optional

from virtualstudio.common.profile_manager import profilemanager
from virtualstudio.common.profile_manager.profilemanager import getOrCreateProfileSet
from virtualstudio.common.structs.action.button_action import ButtonAction
from virtualstudio.common.structs.hardware.hardware_wrapper import HardwareWrapper
from virtualstudio.core.devicemanager import device_manager
from virtualstudio.core.devicemanager.device_manager import getDeviceByID, deviceNameToID

STATE_INACTIVE = 0x00
STATE_ACTIVE =0x01


class ButtonSwitchProfileAction(ButtonAction):

    # region handlers

    def onLoad(self):
        self.hardware: Optional[HardwareWrapper] = None
        self.deviceName: Optional[str] = None

    def onAppear(self):
        self.setGUIParameter("combo_device", "itemTexts", device_manager.getLoadedDeviceNames())
        profileSet = profilemanager.getProfileSetFromFamily(device_manager.getLoadedDeviceNames()[0])
        self.setGUIParameter("combo_profile", "itemTexts", profileSet.getProfileNames())

        self.deviceName = self.getGUIParameter("combo_device", "currentText")
        if self.deviceName is not None:
            self.hardware = getDeviceByID(deviceNameToID(self.deviceName))
            if self.hardware is not None:
                self.hardware.addProfileChangedCallback(self.onHardwareProfileChanged)

        self.updateProfileState()

    def onDisappear(self):
        if self.hardware is not None:
            self.hardware.removeProfileChangedCallback(self.onHardwareProfileChanged)

    def onSettingsGUIAppear(self):
        pass

    def onSettingsGUIDisappear(self):
        pass

    def onParamsChanged(self, parameters: dict):
        devName = self.getGUIParameter("combo_device", "currentText")

        if devName != self.deviceName:
            if self.hardware is not None:
                self.hardware.removeProfileChangedCallback(self.onHardwareProfileChanged)
            self.deviceName = devName
            self.hardware = getDeviceByID(deviceNameToID(self.deviceName))
            if self.hardware is not None:
                self.hardware.addProfileChangedCallback(self.onHardwareProfileChanged)

        profileSet = profilemanager.getProfileSetFromFamily(self.getGUIParameter("combo_device", "currentText"))
        if profileSet is not None:
            profileNames = profileSet.getProfileNames()
            if self.getGUIParameter("combo_profile", "currentText") not in profileNames and len(profileNames) > 0:
                self.setGUIParameter("combo_profile", "currentIndex", 0, silent=True)
                self.setGUIParameter("combo_profile", "currentText", profileNames[0], silent=True)

            self.setGUIParameter("combo_profile", "itemTexts", profileNames)

        self.updateProfileState()

    # endregion

    #region Callbacks

    def onHardwareProfileChanged(self, profileName):
        self.updateProfileState(profileName)

    def updateProfileState(self, profileName=None):
        if profileName is None:
            profileName = self.getGUIParameter("combo_profile", "currentText")
        if self.hardware is None:
            self.setState(STATE_INACTIVE)
            self.logger.info("Hardware is None, State Inactive")
            return
        if self.hardware.currentProfile == profileName:
            self.setState(STATE_ACTIVE)
            self.logger.info("State Active")
            return
        self.logger.info("State Inactive: {} != {}".format(self.hardware.currentProfile, profileName))
        self.setState(STATE_INACTIVE)

    #endregion

    # region Hardware Event Handlers

    def onKeyDown(self):
        pass

    def onKeyUp(self):
        device = self.getGUIParameter("combo_device", "currentText")
        profile = self.getGUIParameter("combo_profile", "currentText")

        self.hardware = getDeviceByID(deviceNameToID(device))
        profileSet = getOrCreateProfileSet(self.hardware)
        self.hardware.bindProfile(profileSet.getProfile(profile))

        self.updateProfileState()
        self.ensureLEDState()
    # endregion