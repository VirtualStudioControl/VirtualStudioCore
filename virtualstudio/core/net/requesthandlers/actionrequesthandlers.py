from virtualstudio.common.action_manager.actionmanager import getAllLaunchers, areActionsLoaded, getActionByID, listCategoryIcons

from virtualstudio.common.structs.action.action_launcher import ActionLauncher, UI_TYPE_INVALID
from virtualstudio.common.structs.action.action_info import ActionInfo, fromDict as actionInfoFromDict

from virtualstudio.common.net.protocols.virtualstudiocom import constants


def onSendActionList(msg):
    response = {
        "actions_loaded": areActionsLoaded()
    }

    actionList = []

    if response["actions_loaded"]:
        launchers = getAllLaunchers()

        for action in launchers:
            actionList.append(launchers[action].toDict())

    response["actions"] = actionList
    response["categories"] = listCategoryIcons()

    return response


def onGetActionStates(msg):
    actionInfo: ActionInfo = actionInfoFromDict(msg[constants.REQ_GET_ACTION_STATES_PARAM_ACTION])

    try:
        actionLauncher = getActionByID(actionInfo.launcher)
        stateCount = actionLauncher.getActionStateCount(actionInfo.controlType)
        success = True
    except:
        stateCount = -1
        success = False

    response = {
        "success": success,
        "states": stateCount
    }

    return response


def onGetActionWidget(msg):
    actionInfo: ActionInfo = actionInfoFromDict(msg[constants.REQ_GET_ACTION_STATES_PARAM_ACTION])

    try:
        actionLauncher = getActionByID(actionInfo.launcher)
        uitype, widget = actionLauncher.getActionUI(actionInfo.controlType)
        success = True
    except:
        uitype = UI_TYPE_INVALID
        widget = ""
        success = False

    response = {
        "success": success,
        "widgetdatatype": uitype,
        "widgetdata": widget
    }

    return response


def onSetActionData(msg):
    #TODO: Implement
    print("onSetActionData NOT IMPLEMENTED ! // actionrequesthandlers")
    pass
