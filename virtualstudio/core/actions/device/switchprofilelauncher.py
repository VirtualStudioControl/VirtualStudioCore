import sys
from typing import Tuple

from config import PLUGIN_DIRECTORY
from virtualstudio.common.action_manager.actionmanager import registerCategoryIcon
from virtualstudio.common.io import filewriter
from virtualstudio.common.structs.action.action_launcher import *
from virtualstudio.common.tools import icontools
from virtualstudio.common.tools.icontools import readPNGIcon

from virtualstudio.core.actions.device.switchprofile.buttonswitchprofileaction import ButtonSwitchProfileAction
from virtualstudio.core.actions.device.switchprofile.imagebuttonswitchprofileaction import ImageButtonSwitchProfileAction

class SwitchProfileLauncher(ActionLauncher):

    def __init__(self):
        super(SwitchProfileLauncher, self).__init__()
        registerCategoryIcon(["Device"], sys.path[0] + "/assets/icons/device/category_device.png")

        self.ACTIONS = {
            CONTROL_TYPE_BUTTON: ButtonSwitchProfileAction,
            #CONTROL_TYPE_FADER: FaderDebugAction,
            CONTROL_TYPE_IMAGE_BUTTON: ImageButtonSwitchProfileAction,
            #CONTROL_TYPE_ROTARY_ENCODER: RotaryEncoderDebugAction
        }

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
        return [CONTROL_TYPE_BUTTON, CONTROL_TYPE_IMAGE_BUTTON]

    def getActionStateCount(self, controlType: str) -> int:
        return 1

    def getActionUI(self, controlType: str) -> Tuple[str, str]:
        return UI_TYPE_QTUI, \
               icontools.encodeIconData(
                   filewriter.readFileBinary(sys.path[0] + "/assets/ui/device/switchprofile.ui"))

    #endregion