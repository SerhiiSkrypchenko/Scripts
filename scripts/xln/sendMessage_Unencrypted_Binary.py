import requests
import random
import time
import json
import string
import config_Luna_Wallet


url = config_Luna_Wallet.xln_t1
#LunaInitAccount = secretPhrase of main account

def id_generator(size=100, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def sendMessage(url):
    alive = True
    while alive:
        k = 1
        for k in range(1, 200):
            print(k)
            print("-------------")
            i = random.randint(1, 200)
            p = random.randint(1, 200)
            urls = random.choice(url)
            print("-----" + urls + "-----")
            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
            response = requests.request("GET",
                                        urls + "/api/rpc",
                                        params=getAccountId)
            print(response.json())
            accountReceive = response.json()["accountXLN"]
            print("-------------")
            print(str("accountReceive = " + accountReceive))
            print("-------------")

            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
            response = requests.request("GET",
                                        urls + "/api/rpc",
                                        params=getAccountId)
            print(response.json())
            accountSender = response.json()["accountXLN"]
            sender = response.json()["account"]
            print("-------------")
            print(str("accountSender = " + accountSender))
            print(str("account = " + sender))
            print(" <<<<<<< --------- " + urls + " ----- >>>>>>>")
            print("-------------")

            sendMessage = {"requestType": "sendMessage",
                           "recipient": str(accountReceive),
                           "message": "cd6a3755ef9936cfd908d687fbcace67622f81c4990b654bb1dd66423514f7dd",
                           "secretPhrase": str(p),
                           "feeMLN": "2000000000",
                           "deadline": "1440",
                           "sender": str(sender),
                           "isCustomFee": "true",
                           "messageIsText": "false"
                           }

            try:
                response = requests.request("POST", urls + "/api/rpc", params=sendMessage)
                print(response.json())
                print(" <<<<<<< --------- " + urls + " ----- >>>>>>>")
                print("----------------------------------------------------------------------------------------------")
            except requests.exceptions.ConnectionError:
                requests.status_code = "Connection refused"
            except json.decoder.JSONDecodeError as e:
                print("Error = " + str(e))
            k += 1
            time.sleep(0)


sendMessage(url)




