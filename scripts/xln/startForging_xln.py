import requests
import random
import time
import config_Luna_Wallet

url = config_Luna_Wallet.xln_t1

def startForging(peer, fromAccount, toAccount):
    k = fromAccount
    for k in range(fromAccount, toAccount + 1):
        urls = random.choice(peer)
        print("STARTING FORGING ON ======= " + urls)
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", urls + "/api/rpc", params=getAccountId)
        # print(response.json())
        account = response.json()["account"]
        print(response.json())
        print("account = " + str(account))
        # print(str(account))
        startForging = {"requestType": "startForging", "secretPhrase": str(k), "sender": str(account),
                        "deadline": "1440"}
        response_StartForging = requests.request("POST", urls + "/api/rpc", params=startForging)
        print(response_StartForging.text)
        print(str(k) + " request <<<< ------ Account " + str(account) + " with secretPhrase " + str(
            k) + " on peer " + urls + " is started ------------- >>>>")
        k += 1
        time.sleep(0)

def startForgingOnAccount(peer, secretPhrase):
    urls = random.choice(peer)
    startForging = {"requestType": "startForging", "secretPhrase": secretPhrase,
                    "deadline": "1440"}
    response_StartForging = requests.request("POST", urls + "/api/rpc", params=startForging)
    print(response_StartForging.json())

#startForgingOnAccount(xln_t2, "LunaInitAccount")
#startForgingOnAccount(xln_t2, "1")
startForging(url, 1, 200)