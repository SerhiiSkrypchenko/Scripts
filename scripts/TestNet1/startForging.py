import requests
import random
import testNet1
import functions
import testNet2
import testNet2
import testNet3
import testNet4_tap
from functions import startForging



#startForging(testNet2.t2, 115, 200)
#startForging(testNet2.t2All, 1, 110)
#startForging(testNet4_tap.t4, 1, 200)
#startForging(testNet2.t2All, 1, 110)
startForging(testNet1.t1, 1, 200)


def startForging1(peer, fromAccount, toAccount):
    k = fromAccount
    for k in range(fromAccount, toAccount + 1):
        urls = peer
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", "https://" + "apl-t2-1.testnet2.apollowallet.org" + "/apl", params=getAccountId)
        print(response.json())
        account = response.json()["account"]
        print(str(account))
        startForging = {"requestType": "startForging", "secretPhrase": str(k), "sender": str(account),
                        "deadline": "1440"}
        response = requests.request("POST", "http://" + urls + "/apl", params=startForging)
        print(response.text)
        print(str(k) + " request <<<< ------ Account " + account + " with secretPhrase " + str(
            k) + " on peer " + urls + " is started ------------- >>>>")
        k += 1


#startForging1(testNet1.peer6, 120, 200)
