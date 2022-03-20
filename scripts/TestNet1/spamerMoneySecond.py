import requests
import random
import data

# Test Net 3
url31 = "http://51.15.250.32/apl"
url32 = "http://51.15.253.171/apl"
url33 = "http://51.15.210.116/apl"
url34 = "http://51.15.242.197/apl"
url35 = "http://51.15.218.241/apl"
urls3 = random.choice([url31, url32, url33, url34, url35])
# Test Net 2
localhost = "http://localhost:7876/apl"
url21 = "http://51.15.247.49/apl"
url22 = "http://51.15.209.252/apl"
url23 = "http://51.15.228.90/apl"
url24 = "http://51.15.228.126/apl"
url25 = "http://51.15.228.171/apl"
url26 = "http://51.15.46.25/apl"
url27 = "http://51.15.72.23/apl"
url28 = "http://51.15.100.44/apl"
url29 = "http://51.15.233.93/apl"
# urls2 = random.choice([url21, url22, url23, url24, url25, url26, url27, url28, url29])
urls2 = random.choice([localhost])
# Test Net 1
url11 = "http://51.15.235.41/apl" #no shards
url12 = "http://51.15.69.39/apl"
url13 = "http://51.15.59.37/apl"
url14 = "http://51.15.114.68/apl"
url15 = "http://51.15.140.80/apl"
url16 = "http://51.15.100.44/apl" #no shards
url17 = "http://51.15.233.93/apl"
localhost = "http://localhost:7876/apl"
#t1 = random.choice([url11, url12, url13, url14, url15, url16, url17])

alive = True
while alive:
    k = 1
    for k in range(1, 201):
        print(k)
        t1 = random.choice([url12, url14, url15, url16])
        print("-------------")
        i = random.randint(1, 200)
        p = random.randint(1, 200)

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
        response = requests.request("GET",
                                    t1,
                                    params=getAccountId)
        print(response.json())
        accountReceive = response.json()["accountRS"]
        print("secret Pass of receiver= " + str(i))
        print("-------------")
        print(str("accountReceive = " + accountReceive))
        print("-------------")

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
        response = requests.request("GET",
                                    t1,
                                    params=getAccountId)
        print(response.json())
        accountSender = response.json()["accountRS"]
        sender = response.json()["account"]
        print("secret Pass of sender= " + str(p))
        print("-------------")
        print(str("accountSender = " + accountSender))
        print(str("account = " + sender))
        print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
        print("-------------")

        response = requests.request("POST",
                                    t1,
                                    params=data.sendMoneyFromStandardWalletToVaultWallet(str(accountReceive),
                                                                                         str(random.randint(2000000000, 200000000000)),
                                                                                         str(p),
                                                                                         "400000000",
                                                                                         sender))
        print(response.json())
        print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
        print("----------------------------------------------------------------------------------------------")
        k += 1

