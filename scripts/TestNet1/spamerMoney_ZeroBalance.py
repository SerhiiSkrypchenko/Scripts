import requests
import random
import data
import time
import testNet2
import testNet3
import testNet1

alive = True
while alive:
    """print(" <<<< --- START ---- >>>> sendMoney to ")

    i = 500
    NPZ_ACCOUNT = "9211698109297098287"
    base_APL_AMOUNT = 3000000000000
    fee_APL = 200000000
    t1 = random.choice(testNet2.t2)
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
    response = requests.request("GET", "http://" + t1 + "/apl",
                                params=getAccountId)
    accountReceive = response.json()["accountRS"]
    response = requests.request("POST",
                                "http://" + t1 + "/apl",
                                params=data.sendMoneyFromStandardWalletToVaultWallet(str(accountReceive),
                                                                                         str(base_APL_AMOUNT),
                                                                                     str(i),
                                                                                     str(fee_APL),
                                                                                     NPZ_ACCOUNT))
    print(response.json())"""
    i = 1081
    base_APL_AMOUNT = 2922900000000
    fee_APL = 100000000
    alive = True
    while alive:
        print(" <<<< --- START ---- sendMoney to another accounts>>>> ")
        print("secret phrase is " + str(i))
        t1 = random.choice(testNet2.t2)
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i+1)}
        response = requests.request("GET", t1 + "/apl",
                                    params=getAccountId)
        accountReceive = response.json()["accountRS"]
        print(str("accountReceive = " + accountReceive))

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
        response = requests.request("GET",
                                    t1 + "/apl",
                                    params=getAccountId)
        accountSender = response.json()["accountRS"]
        sender = response.json()["account"]
        print(str("accountSender = " + accountSender))
        print(" PEER  = >> " + t1 + " << = ")
        response = requests.request("POST",
                                    t1 + "/apl",
                                    params=data.sendMoneyPrivate(str(accountReceive),
                                                                                         str(base_APL_AMOUNT-200000000-fee_APL),
                                                                                         str(i),
                                                                                         str(fee_APL),
                                                                                         sender))
        print("PRIVATE TRANSACTION")
        print(response.json())
        response = requests.request("POST",
                                    t1 + "/apl",
                                    params=data.sendMoneyFromStandardWalletToVaultWallet(str(accountReceive),
                                                                 str(100000000),
                                                                 str(i),
                                                                 str(fee_APL),
                                                                 sender))
        print("SIMPLE SEND MONEY TRANSACTION")
        print(response.json())
        base_APL_AMOUNT = base_APL_AMOUNT-2*fee_APL
        print("----------- END -------------")
        time.sleep(3000)
        i+=1










