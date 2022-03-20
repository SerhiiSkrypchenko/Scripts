import requests
import random
import data
import time
import testNet2
import testNet3
import testNet1
import testNet4_tap

URL = testNet2.t2
second = "second"
first = "first"
print("secret phrase of first acc is : " + first)
print("secret phrase of second acc is : " + second)

fee_APL = 100000000
t1 = random.choice(URL)
sec = 30
print(t1)

getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": second}
response = requests.request("GET", t1 + "/apl",
                                    params=getAccountId)
accountReceive = response.json()["accountRS"]
receive = response.json()["account"]
print(str("accountReceive = " + accountReceive))

getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": first}
response = requests.request("GET",
                                    t1 + "/apl",
                                    params=getAccountId)
accountSender = response.json()["accountRS"]
sender = response.json()["account"]
print(sender)

getAccountFirst = {"": "%2Fapl", "requestType": "getAccount", "account": sender}
response = requests.request("GET", t1 + "/apl", params=getAccountFirst)
print(response.json())
if "errorDescription" in response.text:
    response = requests.request("POST",
                                t1 + "/apl",
                                params=data.sendMoneyPrivate(str(accountSender),
                                                             str(200000000000000),
                                                             "0",
                                                             str(fee_APL),
                                                             "9211698109297098287"))
    print(response.json())
else:
    balanceFirstAccount = response.json()['balanceATM']
    print("balance of first account is " + balanceFirstAccount)


getAccountSecond = {"": "%2Fapl", "requestType": "getAccount", "account": receive}
response = requests.request("GET", t1 + "/apl", params=getAccountSecond)
print(response.json())
if "errorDescription" in response.text:
    """response = requests.request("POST",
                                t1 + "/apl",
                                params=data.sendMoneyPrivate(str(accountReceive),
                                                             str(200000000000000),
                                                             "0",
                                                             str(fee_APL),
                                                             "9211698109297098287"))"""
    print(response.json())
else:
    balanceSecondAccount = response.json()["balanceATM"]
    print("balance of second account is " + balanceSecondAccount)


time.sleep(10)
alive = True
while alive:
        print(" <<<< --- START ---- sendMoney to another accounts>>>> ")

        t1 = random.choice(URL)
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": second}
        response = requests.request("GET", t1 + "/apl",
                                    params=getAccountId)
        accountReceive = response.json()["accountRS"]
        receive = response.json()["account"]
        print(str("accountReceive = " + accountReceive))

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": first}
        response = requests.request("GET",
                                    t1 + "/apl",
                                    params=getAccountId)
        accountSender = response.json()["accountRS"]
        sender = response.json()["account"]
        print(str("accountSender = " + accountSender))
        print(" PEER  = >> " + t1 + " << = ")
        getAccountFirst = {"": "%2Fapl", "requestType": "getAccount", "account": sender}
        response = requests.request("GET", t1 + "/apl", params=getAccountFirst)
        base_APL_AMOUNT = int(response.json()['balanceATM'])
        response = requests.request("POST",
                                    t1 + "/apl",
                                    params=data.sendMoneyFromStandardWalletToVaultWallet(str(accountReceive),
                                                                                         str(base_APL_AMOUNT-fee_APL),
                                                                                         first,
                                                                                         str(fee_APL),
                                                                                         sender))
        print("TRANSACTION from first -> second")
        print(response.json())
        time.sleep(sec)
        getAccountSecond = {"": "%2Fapl", "requestType": "getAccount", "account": receive}
        response = requests.request("GET", t1 + "/apl", params=getAccountSecond)
        base_APL_AMOUNT = int(response.json()['balanceATM'])


        response = requests.request("POST",
                                    t1 + "/apl",
                                    params=data.sendMoneyFromStandardWalletToVaultWallet(str(accountSender),
                                                                 str(base_APL_AMOUNT - fee_APL),
                                                                 second,
                                                                 str(fee_APL),
                                                                 receive))
        print("TRANSACTION from second -> first")
        print(response.json())
        base_APL_AMOUNT = base_APL_AMOUNT - fee_APL
        time.sleep(sec)











