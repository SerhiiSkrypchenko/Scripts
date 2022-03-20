import requests
import random
import time

peer1 = "https://apl-t2-1.testnet2.apollowallet.org"
peer2 = "https://apl-t2-2.testnet2.apollowallet.org"
peer3 = "https://apl-t2-3.testnet2.apollowallet.org"
peer4 = "https://apl-t2-4.testnet2.apollowallet.org"
peer5 = "https://apl-t2-5.testnet2.apollowallet.org"
peer6 = "https://apl-redesign.testnet2.apollowallet.org"
peer7 = "https://apl-exchange.testnet.apollowallet.org"
t2 = ([peer1, peer2, peer3, peer4])


def startForging(peer, fromAccount, toAccount):
    for k in range(fromAccount, toAccount + 1):
        urls = random.choice(peer)
        print("STARTING FORGING ON ======= " + urls)
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", urls + "/apl", params=getAccountId)
        # print(response.json())
        account = response.json()["account"]
        print(response.json())
        print("account = " + str(account))
        # print(str(account))
        startForging = {"requestType": "startForging", "secretPhrase": str(k), "sender": str(account),
                        "deadline": "1440"}
        response_StartForging = requests.request("POST", urls + "/apl", params=startForging)
        print(response_StartForging.json())
        print(str(k) + " request <<<< ------ Account " + str(account) + " with secretPhrase " + str(
            k) + " on peer " + urls + " is started ------------- >>>>")
        print("")
        k += 1
        time.sleep(4)


startForging(t2, 1, 200)
