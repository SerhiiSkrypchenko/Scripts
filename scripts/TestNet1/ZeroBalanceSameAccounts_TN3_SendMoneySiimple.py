import requests
import random
import data
import time
import testNet2
import testNet3
import testNet1
URL = testNet2.t2
second = "second"
first = "first"
print("secret phrase of first acc is : " + first)
print("secret phrase of second acc is : " + second)

fee_APL = 100000000
t1 = random.choice(URL)

getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": second}
response = requests.request("GET", "http://" + t1 + "/apl",
                                    params=getAccountId)
accountReceive = response.json()["accountRS"]
receive = response.json()["account"]
print(str("accountReceive = " + accountReceive))

getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": first}
response = requests.request("GET",
                                    "http://" + t1 + "/apl",
                                    params=getAccountId)
accountSender = response.json()["accountRS"]
sender = response.json()["account"]

getAccountFirst = {"": "%2Fapl", "requestType": "getAccount", "account": sender}
response = requests.request("GET", "http://" + t1 + "/apl", params=getAccountFirst)
print(response.json())
balanceFirstAccount = response.json()['balanceATM']
print(balanceFirstAccount)

getAccountSecond = {"": "%2Fapl", "requestType": "getAccount", "account": receive}
response = requests.request("GET", "http://" + t1 + "/apl", params=getAccountSecond)
print(response.json())
balanceSecondAccount = response.json()["balanceATM"]
print(balanceSecondAccount)

if int(balanceFirstAccount) > 0 and int(balanceSecondAccount) == 0:
    base_APL_AMOUNT = int(balanceFirstAccount)
elif int(balanceSecondAccount) > 0 and int(balanceFirstAccount) == 0:
    base_APL_AMOUNT = int(balanceSecondAccount)
    response = requests.request("POST",
                                "http://" + t1 + "/apl",
                                params=data.sendMoneyFromStandardWalletToVaultWallet(str(accountSender),
                                                             str(base_APL_AMOUNT - fee_APL),
                                                             second,
                                                             str(fee_APL),
                                                             receive))
    print(response.json())
    print("TRANSACTION from second -> first")
    time.sleep(30)
    getAccountFirst = {"": "%2Fapl", "requestType": "getAccount", "account": sender}
    response = requests.request("GET", "http://" + t1 + "/apl", params=getAccountFirst)
    base_APL_AMOUNT = int(response.json()["balanceATM"])
    print(base_APL_AMOUNT)
elif int(balanceFirstAccount) == 0 and int(balanceSecondAccount) == 0:
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": "0"}
    response = requests.request("GET",
                                "http://" + t1 + "/apl",
                                params=getAccountId)
    accountSender = response.json()["accountRS"]
    genezis = response.json()["account"]
    response = requests.request("POST",
                                "http://" + t1 + "/apl",
                                params=data.sendMoneyFromStandardWalletToVaultWallet(str(sender),
                                                             str(1000000000000),
                                                             "0",
                                                             str(fee_APL),
                                                             genezis))
    print(" TRANSACTION from first -> second")
    print(response.json())
    base_APL_AMOUNT = 1000000000000 - fee_APL
    time.sleep(30)

alive = True
while alive:
        print(" <<<< --- START ---- sendMoney to another accounts>>>> ")

        t1 = random.choice(URL)
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": second}
        response = requests.request("GET", "http://" + t1 + "/apl",
                                    params=getAccountId)
        accountReceive = response.json()["accountRS"]
        receive = response.json()["account"]
        print(str("accountReceive = " + accountReceive))

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": first}
        response = requests.request("GET",
                                    "http://" + t1 + "/apl",
                                    params=getAccountId)
        accountSender = response.json()["accountRS"]
        sender = response.json()["account"]
        print(str("accountSender = " + accountSender))
        print(" PEER  = >> " + t1 + " << = ")
        getAccountFirst = {"": "%2Fapl", "requestType": "getAccount", "account": sender}
        response = requests.request("GET", "http://" + t1 + "/apl", params=getAccountFirst)
        base_APL_AMOUNT = int(response.json()['balanceATM'])
        response = requests.request("POST",
                                    "http://" + t1 + "/apl",
                                    params=data.sendMoneyFromStandardWalletToVaultWallet(str(accountReceive),
                                                                                         str(base_APL_AMOUNT-fee_APL),
                                                                                         first,
                                                                                         str(fee_APL),
                                                                                         sender))
        print("TRANSACTION from first -> second")
        print(response.json())
        time.sleep(30)
        getAccountSecond = {"": "%2Fapl", "requestType": "getAccount", "account": receive}
        response = requests.request("GET", "http://" + t1 + "/apl", params=getAccountSecond)
        base_APL_AMOUNT = int(response.json()['balanceATM'])


        response = requests.request("POST",
                                    "http://" + t1 + "/apl",
                                    params=data.sendMoneyFromStandardWalletToVaultWallet(str(accountSender),
                                                                 str(base_APL_AMOUNT - fee_APL),
                                                                 second,
                                                                 str(fee_APL),
                                                                 receive))
        print("TRANSACTION from second -> first")
        print(response.json())
        base_APL_AMOUNT = base_APL_AMOUNT - fee_APL
        time.sleep(30)











