from virtualstudio.common.account_manager.account_manager import *


def onSendAccountList(msg):
    response = {
        "accounts_loaded": areAccountsLoaded()
    }

    accountList = []

    if response["accounts_loaded"]:
        accounts = getAccountList()

        for account in accounts:
            accountList.append(account.toDict())

    response["accounts"] = accountList
    response["accountTypes"] = getAccountTypeIcons()
    response["categories"] = getCategoryIcons()

    return response


def onSetAccountData(msg):
    accountDict = msg['account']
    success, uuid = updateAccount(accountDict)
    return {'success': success, 'uuid': uuid}