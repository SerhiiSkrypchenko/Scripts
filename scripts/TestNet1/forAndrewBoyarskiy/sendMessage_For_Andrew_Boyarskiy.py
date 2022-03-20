import requests
import random
import time
import json
import string

peer1 = "https://apl-t2-1.testnet2.apollowallet.org"
peer2 = "https://apl-t2-2.testnet2.apollowallet.org"
peer3 = "https://apl-t2-3.testnet2.apollowallet.org"
peer4 = "https://apl-t2-4.testnet2.apollowallet.org"
peer5 = "https://apl-t2-5.testnet2.apollowallet.org"
peer6 = "https://apl-redesign.testnet2.apollowallet.org"
peer7 = "https://apl-exchange.testnet.apollowallet.org"


t2All = ([peer2, peer3, peer4, peer5, peer6, peer7, peer1])

def id_generator(size=100, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def sendMessage(url):
    alive = True
    while alive:
        k = 1
        for k in range(1, 201):
            print(k)
            print("-------------")
            i = random.randint(1, 200)
            p = random.randint(1, 200)
            urls = random.choice(url)
            print("-----" + urls + "-----")
            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
            response = requests.request("GET",
                                        urls + "/apl",
                                        params=getAccountId)
            print(response.json())
            accountReceive = response.json()["accountRS"]
            print("-------------")
            print(str("accountReceive = " + accountReceive))
            print("-------------")

            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
            response = requests.request("GET",
                                        urls + "/apl",
                                        params=getAccountId)
            print(response.json())
            accountSender = response.json()["accountRS"]
            sender = response.json()["account"]
            print("-------------")
            print(str("accountSender = " + accountSender))
            print(str("account = " + sender))
            print(" <<<<<<< --------- " + urls + " ----- >>>>>>>")
            print("-------------")

            sendMessage = {"requestType": "sendMessage",
                           "recipient": str(accountReceive),
                           "message": " MESSAGE"
                                      ""
                                      ""
                                      "          "
                                      "KILL SHARDING   !!!! "
                                      "         #$%^&*()-_=+\|'?/" ".        "
                                      "                    ,][{};:` /''~'' !@-                           "
                                      ""
                                      ""
                                      "                                                       " + str(id_generator()),
                           "secretPhrase": str(p),
                           "feeATM": "600000000",
                           "deadline": "1440",
                           "sender": str(sender),
                           "isCustomFee": "false",
                           #"messageFile": "undefined",
                           "messageIsPrunable": "true",
                           "messageIsText": "true",
                           "messageToEncrypt": "true",
                           "messageToEncryptIsText": "true",
                           "encryptedMessageData": "1",
                           "encryptedMessageNonce": "1",
                           "encryptedMessageIsPrunable": "1",
                           "compressMessageToEncrypt": "MESSAGE "
                                                       ""
                                                       ""
                                                       ""
                                                       ""
                                                       ""
                                                       "                                                                     #$%^&*()-_=+\|'?/" ".,][{};:` /''~'' !@-",
                           "messageToEncryptToSelf": "MESSAGE to encrypt #$%^&*()           "
                                                     ""
                                                     ""
                                                     ""
                                                     ""
                                                     ""
                                                     ""
                                                     "                                                                -_=+\|'?/" ".,][{};:` /''~'' !@-",
                           "messageToEncryptToSelfIsText": "true",
                           "encryptToSelfMessageData": "1",
                           "encryptToSelfMessageNonce": "1",
                           "compressMessageToEncryptToSelf": "MESSAGE to encrypt                                                                       #$%^&*()-_=+\|'?/" ".,][{};:` /''~'' !@-"

                           }
                           #"messageIsText": "true"}
            try:
                response = requests.request("POST", urls + "/apl", params=sendMessage)
                print(response.json())
                print(" <<<<<<< --------- " + urls + " ----- >>>>>>>")
                print("----------------------------------------------------------------------------------------------")
            except requests.exceptions.ConnectionError:
                requests.status_code = "Connection refused"
            except json.decoder.JSONDecodeError as e:
                print("Error = " + str(e))
            k += 1
            time.sleep(2)


sendMessage(t2All)


