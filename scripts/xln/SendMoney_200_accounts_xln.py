import requests
import random
xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

url = ([xln_t2_1])
senderSecretPharse = "LunaInitAccount"
amountMLN = "10000000000000"


def sendMoney(recipient, amountMLN, secretPhrase, feeMLN):
    return {"requestType": "sendMoney", "recipient": recipient, "amountMLN": amountMLN,
            "secretPhrase": secretPhrase, "feeMLN": feeMLN, "deadline": "1440"
            }

def sendMoneyToManyAccounts(url, startNumber, finishNumber):
    for k in range(int(startNumber), int(finishNumber) + 1, 1):
        print(k)
        print(" ----- SEND MONEY TO >>> " + str(k) + " <<<---- ACCOUNT --- ")
        random_url = random.choice(url)
        """getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
        response = requests.request("GET", random_url + "/xln-api",
                                    params=getAccountId)
        accountReceive = response.json()["accountRS"]
        print(str("accountReceive = " + accountReceive))"""

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", random_url + "/xln-api", params=getAccountId)
        #print(response.json())
        account = response.json()["accountRS"]
        print("---- RECIPIENT ---- >>>> " + str(account))
        response = requests.request("POST", random_url + "/xln-api",
                                    params=sendMoney(str(account),
                                                                                         amountMLN,
                                                                                         senderSecretPharse,
                                                                                         "100000000"
                                                                                         ))
        print(response.json())
        print("<<< -------- >>> FINISHED <<< ---------->>> ")

sendMoneyToManyAccounts(url, 0, 200)




