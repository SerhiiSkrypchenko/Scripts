import requests
import random
import time

xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

xln_t2 = ([xln_t2_1])

def startForging(peer, fromAccount, toAccount):
    k = fromAccount
    for k in range(fromAccount, toAccount + 1):
        urls = random.choice(peer)
        print("STARTING FORGING ON ======= " + urls)
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", urls + "/xln-api", params=getAccountId)
        # print(response.json())
        account = response.json()["account"]
        print(response.json())
        print("account = " + str(account))
        # print(str(account))
        startForging = {"requestType": "startForging", "secretPhrase": str(k), "sender": str(account),
                        "deadline": "1440"}
        response_StartForging = requests.request("POST", urls + "/xln-api", params=startForging)
        print(response_StartForging.text)
        print(str(k) + " request <<<< ------ Account " + str(account) + " with secretPhrase " + str(
            k) + " on peer " + urls + " is started ------------- >>>>")
        k += 1
        time.sleep(0)

def startForgingOnAccount(peer, secretPhrase, account):
    urls = random.choice(peer)
    startForging = {"requestType": "startForging", "secretPhrase": secretPhrase, "sender": str(account),
                    "deadline": "1440"}
    response_StartForging = requests.request("POST", urls + "/xln-api", params=startForging)
    print(response_StartForging.json())

startForging(xln_t2, 0, 0)