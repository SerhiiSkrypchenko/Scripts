import requests
import random
import config_Luna_Wallet

url = config_Luna_Wallet.xln_t1

senderSecretPhrase = "0"
#senderSecretPhrase = "LunaInitAccount"
amountMLN = "110000000000000"


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
        response = requests.request("GET", random_url + "/api/rpc", params=getAccountId)
        # print(response.json())
        account = response.json()["accountXLN"]
        print("---- RECIPIENT ---- >>>> " + str(account))
        response = requests.request("POST", random_url + "/api/rpc",
                                    params=sendMoney(str(account),
                                                     amountMLN,
                                                     senderSecretPhrase,
                                                     "100000000"
                                                     ))
        print(response.json())
        print("<<< -------- >>> FINISHED <<< ---------->>> ")


sendMoneyToManyAccounts(url, 1, 200)
