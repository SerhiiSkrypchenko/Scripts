import requests
import random
import data
import time
import testNet2
import testNet3
import testNet1

alive = True
while alive:
    i = 900301
    base_APL_AMOUNT = 20000000000000
    fee_APL = 100000000
    alive = True
    while alive:
        print(" <<<< --- START ---- sendMoney to another accounts>>>> ")
        print("secret phrase is " + str(i))
        t1 = random.choice(testNet2.p1)
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
                                    params=data.sendMoney(str(accountReceive),
                                                                                         str(base_APL_AMOUNT-fee_APL),
                                                                                         str(i),
                                                                                         str(fee_APL),
                                                                                         sender))

        """response = requests.request("POST",
                                    "http://" + t1 + "/apl",
                                    params=data.sendMoneyPrivate(str(accountReceive),
                                                          str(base_APL_AMOUNT - fee_APL),
                                                          str(i),
                                                          str(fee_APL),
                                                          sender))"""

        print("SIMPLE TRANSACTION")
        """print("PRIVATE TRANSACTION")"""
        print(response.json())
        base_APL_AMOUNT = base_APL_AMOUNT-fee_APL
        print("----------- END -------------")
        time.sleep(60)
        i+=1










