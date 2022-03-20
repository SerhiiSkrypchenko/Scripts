import requests
import random
import data
import time

xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

url = ([xln_t2_1, xln_t2_2, xln_t2_3])
#LunaInitAccount = secretPhrase of main account

def sendMoney(recipient, amountMLN, secretPhrase, feeMLN, sender):
    return {"requestType": "sendMoney", "recipient": recipient, "amountMLN": amountMLN,
            "secretPhrase": secretPhrase, "feeMLN": feeMLN, "deadline": "1440",
            "sender": sender}

alive = True
while alive:
    for p in range(0, 199):
        print(" <<<< --- START ---- >>>> " + str(p))
        i = random.randint(1, 200)
        random_url = random.choice(url)
        print(" <<<<<<< --------- " + random_url + " ----- >>>>>>>")

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
        response = requests.request("GET", random_url + "/xln-api",
                                    params=getAccountId)
        accountReceive = response.json()["accountRS"]
        print(str("accountReceive = " + accountReceive))
        account = response.json()["account"]
        print(response.json())
        print("account = " + account)

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
        response = requests.request("GET",
                                    random_url + "/xln-api",
                                    params=getAccountId)
        accountSender = response.json()["accountRS"]
        sender = response.json()["account"]
        print("accountSender = " + accountSender)
        amountMLN = random.choice(["2000000000", "3000000000", "4000000000", "5000000000", "6000000000", "7000000000", "8000000000"])
        print("amountMLN = " + amountMLN)
        response = requests.request("POST",
                                    random_url + "/xln-api",
                                    params=sendMoney(str(accountReceive),
                                                    amountMLN,
                                                    str(p),
                                                    "400000000",
                                                    sender))
        print(response.json())
        if "errorDescription" in response.text:
            print()
        else:
            print("recipient = " + response.json()["transactionJSON"]["recipient"])
            print("sender = " + response.json()["transactionJSON"]["sender"])
        print("----------- END -------------")
        time.sleep(1)
        p += 1









