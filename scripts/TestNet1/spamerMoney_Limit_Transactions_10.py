import requests
import random
import data
import time
import testNet2
import testNet3
import testNet1

limit = 10000
j = 1
while (j<=limit):
    f = open("transactions10.txt", "a+")
    p = random.randint(1, 100)
    print(" <<<< --- START ---- >>>> " + str(j))
    i = random.randint(1, 100)
    t1 = random.choice(testNet2.p1)
    #print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
    response = requests.request("GET", "http://" + t1 + "/apl",
                                params=getAccountId)
    # response.status_code
    # print(response.json())
    accountReceive = response.json()["accountRS"]
    # print("-------------")
    #print(str("accountReceive = " + accountReceive))
    account = response.json()["account"]
    #print(response.json())
    #print("account = " + account)
    # print("-------------")

    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
    response = requests.request("GET",
                                "http://" + t1 + "/apl",
                                params=getAccountId)
    # print(response.json())
    accountSender = response.json()["accountRS"]
    sender = response.json()["account"]
    # print("-------------")
    #print(str("accountSender = " + accountSender))
    # print(str("account = " + sender))
    #print(" PEER  = >> " + t1 + " << = ")
    response = requests.request("POST",
                                "http://" + t1 + "/apl",
                                params=data.sendMoneyFromStandardWalletToVaultWallet(str(accountReceive),
                                                                                     random.choice([
                                                                                         "2000000000",
                                                                                         "3000000000",
                                                                                         "4000000000", "5000000000",
                                                                                         "6000000000", "7000000000",
                                                                                         "8000000000"]),
                                                                                     str(p),
                                                                                     "400000000",
                                                                                     sender))
    #print(response.json())
    f.write(response.json()["transaction"] + "\r")
    # print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
    print("----------- END -------------")
    #time.sleep()
    j += 1
f.close()









