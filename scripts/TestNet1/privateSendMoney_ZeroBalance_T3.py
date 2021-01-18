import requests
import random
import data
import time
import testNet2
import testNet3
import testNet1

alive = True
while alive:
    i = 20568
    base_APL_AMOUNT = 10000000000000
    fee_APL = 100000000
    alive = True
    while alive:
        print(" <<<< --- START ---- sendMoney to another accounts>>>> ")
        print("secret phrase is " + str(i))
        t1 = random.choice(testNet3.t3)
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i+1)}
        response = requests.request("GET", "http://" + t1 + "/apl",
                                    params=getAccountId)
        accountReceive = response.json()["accountRS"]
        print(str("accountReceive = " + accountReceive))


        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
        response = requests.request("GET",
                                    "http://" + t1 + "/apl",
                                    params=getAccountId)
        accountSender = response.json()["accountRS"]
        sender = response.json()["account"]
        print(str("accountSender = " + accountSender))

        getAccountFirst = {"": "%2Fapl", "requestType": "getAccount", "account": sender}
        response = requests.request("GET", "http://" + t1 + "/apl", params=getAccountFirst)
        print(response.json())
        balanceFirstAccount = response.json()['balanceATM']
        print(balanceFirstAccount)

        print(" PEER  = >> " + t1 + " << = ")
        response = requests.request("POST",
                                    "http://" + t1 + "/apl",
                                    params=data.sendMoneyPrivate(str(accountReceive),
                                                                                         str(int(balanceFirstAccount)-fee_APL),
                                                                                         str(i),
                                                                                         str(fee_APL),
                                                                                         sender))
        print("PRIVATE TRANSACTION")
        print(response.json())
        #balanceFirstAccount = balanceFirstAccount-fee_APL
        print("----------- END -------------")
        time.sleep(45)
        i+=1










