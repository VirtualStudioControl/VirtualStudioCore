from virtualstudio.common.profile_manager import profilemanager
from virtualstudio.common.structs.action.imagebutton_action import ImageButtonAction
from virtualstudio.core.devicemanager import device_manager


class ImageButtonSwitchProfileAction(ImageButtonAction):

    #region handlers

    def onLoad(self):
        pass

    def onAppear(self):
        self.setGUIParameter("combo_device", "itemTexts", device_manager.getLoadedDeviceNames())
        self.setGUIParameter("combo_profile", "itemTexts", ["Profile A", "Profile B"])

    def onDisappear(self):
        pass

    def onSettingsGUIAppear(self):
        pass

    def onSettingsGUIDisappear(self):
        pass

    def onParamsChanged(self, parameters: dict):
        print(parameters)
        profileSet = profilemanager.getProfileSetFromFamily(self.getGUIParameter("combo_device", "currentText"))
        print(profileSet.getProfileNames())
        self.setGUIParameter("combo_profile", "itemTexts", profileSet.getProfileNames())
        #self.setGUIParameter("combo_profile", "", profileSet.getProfileNames())

    #endregion

    #region Hardware Event Handlers

    def onKeyDown(self):
        pass

    def onKeyUp(self):
        device = self.getGUIParameter("combo_device", "currentText")
        profile = self.getGUIParameter("combo_profile", "currentText")

        print("Switching {} to {}".format(device, profile))

    #endregion