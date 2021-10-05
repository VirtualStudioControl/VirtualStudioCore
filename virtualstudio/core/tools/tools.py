import config

from ..devicemanager.device_manager import getCurrentProfileNameDict

from virtualstudio.common.io.configtools import writeJSON, readJSON
from virtualstudio.common.profile_manager import profilemanager
from virtualstudio.common.account_manager import account_manager
from virtualstudio.common.account_manager.account_info import fromDict as accountFromDict

def saveProfileSets():
    writeJSON(config.PROFILE_DATA_DIRECTORY + "/" + config.PROFILE_SET_DATA_FILE, profilemanager.toDict())


def saveCurrentProfileNames():
    writeJSON(config.PROFILE_DATA_DIRECTORY + "/" + config.DEVICE_CURRENT_PROFILE_NAME, getCurrentProfileNameDict())


def storeAccounts():
    accountList = []

    for account in account_manager.ACCOUNTS:
        accountList.append(account_manager.ACCOUNTS[account].toDictWthPasswd())

    accountData = {
        "uuid-counter": account_manager.UUID_COUNTER,
        "category-icons": account_manager.CATEGORY_ICONS,
        "accounts": accountList
    }

    writeJSON(config.ACCOUNT_DATA_DIRECTORY + "/" + config.ACCOUNT_DATA_FILE, accountData)

def loadAccounts():
    accountData = readJSON(config.ACCOUNT_DATA_DIRECTORY + "/" + config.ACCOUNT_DATA_FILE)

    accounts = {}

    for accountDict in accountData["accounts"]:
        accountObj = accountFromDict(accountDict)
        accounts[accountObj.uuid] = accountObj

    account_manager.UUID_COUNTER = accountData["uuid-counter"]
    account_manager.CATEGORY_ICONS = accountData["category-icons"]
    account_manager.ACCOUNTS.update(accounts)