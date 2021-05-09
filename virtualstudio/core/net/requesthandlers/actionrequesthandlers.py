from virtualstudio.common.action_manager.actionmanager import getAllLaunchers, areActionsLoaded, getActionByID, listCategoryIcons


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

def onSendActionIcon(msg):
    actionID = msg['payload']['actionID']
    action = getActionByID(actionID)

    if action is not None:
        return {
            'icon': action.getIcon()
        }
    return {}