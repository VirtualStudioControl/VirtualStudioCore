from virtualstudio.common.structs.action.button_action import ButtonAction


class ButtonSwitchProfileAction(ButtonAction):

    #region handlers

    def onLoad(self):
        self.setGUIParameter("combo_device", "itemTexts", ["Device A", "Device B"])
        print(self.getParams())

    def onAppear(self):
        pass

    def onDisappear(self):
        pass

    def onSettingsGUIAppear(self):
        pass

    def onSettingsGUIDisappear(self):
        pass

    def onParamsChanged(self, parameters: dict):
        pass

    #endregion

    #region Hardware Event Handlers

    def onKeyDown(self):
        pass

    def onKeyUp(self):
        pass

    #endregion