import random

import requests
import testNet2
import testNet3
import testNet1


limit = 300

i = 200000000000
end = i + limit

while (i <= end):
    print(" <<<< --- START ---- >>>> " + str(i))
    t1 = random.choice(testNet1.mixer)
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
    response = requests.request("GET", "http://" + t1 + "/apl",
                                params=getAccountId)
    #print(response.json())
    accountReceive = response.json()["accountRS"]

    print(str("accountReceive #" + str(i) + " = " + accountReceive))
    print("secretPhrase of accountReceive is " + str(i))

    getAccount = {"": "%2Fapl", "requestType": "getAccount", "account": accountReceive}
    response = requests.request("GET",
                                "http://" + t1 + "/apl",
                                params=getAccount)
    #print(response.json())
    if "balanceATM" in response.json():
        balance = response.json()["balanceATM"]
        print("balance = " + balance)
    else:
        print("balance has NO APL ")
    print("-----------------------------")
    i += 1










