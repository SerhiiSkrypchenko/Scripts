import requests
import random
port = ":2402"

xln_t2_1 = "http://1.t2.testnet.lunaonewallet.com"
xln_t2_2 = "http://2.t2.testnet.lunaonewallet.com"
xln_t2_3 = "http://3.t2.testnet.lunaonewallet.com"
xln_t2_4 = "http://4.t2.testnet.lunaonewallet.com"
xln_t2_5 = "http://5.t2.testnet.lunaonewallet.com"


#xln_t2 = ([xln_t2_1])
xln_t2 = ([xln_t2_3, xln_t2_2, xln_t2_1, xln_t2_4, xln_t2_5])
senderSecretPharse = "LunaInitAccount"




def sendMoney(recipient, amountMLN, secretPhrase, feeMLN):
    return {"requestType": "sendMoney", "recipient": recipient, "amountMLN": amountMLN,
            "secretPhrase": secretPhrase, "feeMLN": feeMLN, "deadline": "1440"
            }

def sendMoneyToManyAccounts(url, startNumber, finishNumber):
    total =0
    for k in range(int(startNumber), int(finishNumber) + 1, 1):
        print(k)
        print(" ----- SEND MONEY TO >>> " + str(k) + " <<<---- ACCOUNT --- ")
        random_url = random.choice(url)
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", random_url + "/api/rpc", params=getAccountId)
        #print(response.json())
        account = response.json()["accountRS"]
        print("---- RECIPIENT ---- >>>> " + str(account))
        amountMLN = random.choice([1000000000000000, 100000000000000, 20000000000000, 50000000000000, 70000000000000, 30000000000000, 80000000000000, 500000000000000])
        response = requests.request("POST", random_url + "/api/rpc",
                                    params=sendMoney(str(account),
                                                                                         amountMLN,
                                                                                         senderSecretPharse,
                                                                                         "100000000"
                                                                                         ))
        print(response.json())
        total = amountMLN + total
        print(total)
        print("<<< -------- >>> FINISHED <<< ---------->>> ")

sendMoneyToManyAccounts(url, 300, 400)




