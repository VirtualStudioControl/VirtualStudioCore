import sys
from typing import Tuple

from virtualstudio.common.action_manager.actionmanager import registerCategoryIcon
from virtualstudio.common.structs.action.action_launcher import *
from virtualstudio.common.tools.icontools import readPNGIcon

class MultiActionLauncher(ActionLauncher):

    def __init__(self):
        super(MultiActionLauncher, self).__init__()
        registerCategoryIcon(["Device"], sys.path[0] + "/assets/icons/device/category_device.png")

    #region Metadata

    def getName(self):
        return "Multi Action"

    def getIcon(self):
        return readPNGIcon(sys.path[0] + "/assets/icons/device/action_multiaction.png")

    def getCategory(self):
        return ["Device"]

    def getAuthor(self):
        return "eric"

    def getVersion(self):
        return (0,0,1)

    def getID(self):
        return "{}.{}.{}-{}".format(self.getAuthor(), self.getCategory(), self.getName(), self.getVersion())

    def allowedControls(self):
        return []

    def getActionStateCount(self, controlType: str) -> int:
        return 1

    def getActionUI(self, controlType: str) -> Tuple[str, str]:
        return UI_TYPE_INVALID, ""

    def getActionForControl(self, control):
        pass

    #endregion