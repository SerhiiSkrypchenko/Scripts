import requests
import random
import time
import json
import string


xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

url = ([xln_t2_1, xln_t2_2, xln_t2_3])
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
                                        urls + "/xln-api",
                                        params=getAccountId)
            print(response.json())
            accountReceive = response.json()["accountRS"]
            print("-------------")
            print(str("accountReceive = " + accountReceive))
            print("-------------")

            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
            response = requests.request("GET",
                                        urls + "/xln-api",
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
                                      "                                                      ....//" + str(id_generator()),
                           "secretPhrase": str(p),
                           "feeMLN": "2000000000",
                           "deadline": "1440",
                           "sender": str(sender),
                           "isCustomFee": "false",
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

                           #"messageFile": "undefined",
                           }
                           #"messageIsText": "true"}
            try:
                response = requests.request("POST", urls + "/xln-api", params=sendMessage)
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




