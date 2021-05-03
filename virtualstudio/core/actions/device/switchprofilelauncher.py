import sys

from virtualstudio.common.action_manager.actionmanager import registerCategoryIcon
from virtualstudio.common.structs.action.action_launcher import ActionLauncher
from virtualstudio.common.tools.icontools import readPNGIcon


class SwitchProfileLauncher(ActionLauncher):

    def __init__(self):
        super(SwitchProfileLauncher, self).__init__()
        registerCategoryIcon(["Device"], sys.path[0] + "/assets/icons/device/category_device.png")

    #region Metadata

    def getName(self):
        return "Switch Profile"

    def getIcon(self):
        return readPNGIcon(sys.path[0] + "/assets/icons/device/action_switchprofile.png")

    def getCategory(self):
        return ["Device"]

    def getAuthor(self):
        return "eric"

    def getVersion(self):
        return (0,0,1)

    def allowedControls(self):
        return []

    def getActionUI(self, control):
        return ""

    def getActionForControl(self, control):
        pass

    #endregion