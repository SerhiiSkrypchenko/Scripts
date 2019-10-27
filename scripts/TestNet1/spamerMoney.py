import requests
import random
import data
import time
import testNet2
import testNet1
import testNet3
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError




# убрать https://
alive = True
while alive:
    p = 1
    for p in range(1, 200):
        print(" --------- >>>> " + str(p))

        i = random.randint(1, 200)
        t1 = random.choice(testNet2.t2)
        print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
        response = requests.request("GET", "http://" + t1 + "/apl",
                                    params=getAccountId)
        # response.status_code
        #print(response.json())
        accountReceive = response.json()["accountRS"]
        #print("-------------")
        print(str("accountReceive = " + accountReceive))
        #print("-------------")

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
        response = requests.request("GET",
                                    "http://" + t1 + "/apl",
                                    params=getAccountId)
        #print(response.json())
        accountSender = response.json()["accountRS"]
        sender = response.json()["account"]
        #print("-------------")
        print(str("accountSender = " + accountSender))
        #print(str("account = " + sender))
        #print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
        #print("-------------")

        response = requests.request("POST",
                                    "http://" + t1 + "/apl",
                                    params=data.sendMoneyFromStandardWalletToVaultWallet(str(accountReceive),
                                                                                         str(random.randint(
                                                                                             2000000000,
                                                                                             200000000000)),
                                                                                         str(p),
                                                                                         "400000000",
                                                                                         sender))
        print(response.json())
        #print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
        print()
        #time.sleep(1)
        p += 1









