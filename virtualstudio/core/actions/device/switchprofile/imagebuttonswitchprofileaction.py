from virtualstudio.common.profile_manager import profilemanager
from virtualstudio.common.profile_manager.profilemanager import getOrCreateProfileSet
from virtualstudio.common.structs.action.imagebutton_action import ImageButtonAction
from virtualstudio.core.devicemanager import device_manager
from virtualstudio.core.devicemanager.device_manager import getDeviceByID, deviceNameToID


class ImageButtonSwitchProfileAction(ImageButtonAction):

    #region handlers

    def onLoad(self):
        pass

    def onAppear(self):
        self.ensureGUIParameter("combo_device", "itemTexts", device_manager.getLoadedDeviceNames())
        profileSet = profilemanager.getProfileSetFromFamily(device_manager.getLoadedDeviceNames()[0])
        self.ensureGUIParameter("combo_profile", "itemTexts", profileSet.getProfileNames())

    def onDisappear(self):
        pass

    def onSettingsGUIAppear(self):
        pass

    def onSettingsGUIDisappear(self):
        pass

    def onParamsChanged(self, parameters: dict):
        profileSet = profilemanager.getProfileSetFromFamily(self.getGUIParameter("combo_device", "currentText"))
        if profileSet is not None:
            profileNames = profileSet.getProfileNames()
            if self.getGUIParameter("combo_profile", "currentText") not in profileNames and len(profileNames) > 0:
                self.setGUIParameter("combo_profile", "currentIndex", 0, silent=True)
                self.setGUIParameter("combo_profile", "currentText", profileNames[0], silent=True)

            self.setGUIParameter("combo_profile", "itemTexts", profileNames)

    #endregion

    #region Hardware Event Handlers

    def onKeyDown(self):
        pass

    def onKeyUp(self):
        device = self.getGUIParameter("combo_device", "currentText")
        profile = self.getGUIParameter("combo_profile", "currentText")

        hardware = getDeviceByID(deviceNameToID(device))
        profileSet = getOrCreateProfileSet(hardware)
        hardware.bindProfile(profileSet.getProfile(profile))

    #endregion