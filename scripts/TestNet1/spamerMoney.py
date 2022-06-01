import json

import requests
import random
import data
import time
import testNet2
import testNet3
import testNet1
import testNet4_tap
import testNetStage
URL = testNetStage.t15All

alive = True
while alive:
    p = 1
    for p in range(1, 199):
        print(" <<<< --- START ---- >>>> " + str(p))

        i = random.randint(1, 100)
        t1 = random.choice(URL)
        print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
        response = requests.request("GET", t1 + "/apl",
                                    params=getAccountId)
        # response.status_code
        #print(response.json())
        accountReceive = response.json()["accountRS"]
        #print("-------------")
        print(str("accountReceive = " + accountReceive))
        account = response.json()["account"]
        print(response.json())
        print("account = " + account)
        #print("-------------")

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
        response = requests.request("GET",
                                    t1 + "/apl",
                                    params=getAccountId)
        #print(response.json())
        accountSender = response.json()["accountRS"]
        sender = response.json()["account"]
        #print("-------------")
        print("accountSender = " + accountSender)
        #print(str("account = " + sender))
        print(" PEER  = >> " + t1 + " << = ")
        amountATM = random.choice(["2000000000", "3000000000", "4000000000", "5000000000", "6000000000", "7000000000", "8000000000"])
        print("amountATM = " + amountATM)
        response = requests.request("POST",
                                    t1 + "/apl",
                                    params=data.sendMoneyFromStandardWalletToVaultWallet(str(accountReceive),
                                                                                         amountATM,
                                                                                         str(p),
                                                                                         "400000000",
                                                                                         sender))
        print(response.json())
        if "errorDescription" in response.text:
            print()
        else:
            print("recipient = " + response.json()["transactionJSON"]["recipient"])
            print("sender = " + response.json()["transactionJSON"]["sender"])
        #print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
        print("----------- END -------------")
        time.sleep(3)
        p += 1









