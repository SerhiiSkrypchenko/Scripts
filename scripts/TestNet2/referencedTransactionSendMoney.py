import requests
import random
import data
import conf

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
urls2 = random.choice([url21, url22, url23, url24, url25, url26, url27, url28, url29])
# urls2 = random.choice([url21, localhost])
j = 0
response = requests.request("POST", urls2, data=data.payload, headers=data.headers,
                            params=data.sendMoneyFromStandardWalletToVaultWallet(conf.account2, "20000000000",
                                                                                 conf.account1SecretPhrase, "200000000",
                                                                                 conf.sender1))
print(response.json())
fullHash = response.json()["fullHash"]
print("fullHash = " + fullHash)

for j in range(0, 10000000000000000000000000000000000000000000000000000000000):
    k = 1
    for k in range(1, 201):
        print(k)
        print("-------------")
        i = random.randint(1, 200)
        p = random.randint(1, 200)

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
        response = requests.request("GET",
                                    urls2,
                                    params=getAccountId)
        print(response.json())
        accountReceive = response.json()["accountRS"]
        print("-------------")
        print(str("accountReceive = " + accountReceive))
        print("-------------")

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
        response = requests.request("GET",
                                    urls2,
                                    params=getAccountId)
        print(response.json())
        accountSender = response.json()["accountRS"]
        sender = response.json()["account"]
        print("-------------")
        print(str("accountSender = " + accountSender))
        print(str("account = " + sender))
        print("-------------")

        response = requests.request("POST",
                                    urls2,
                                    params=data.sendMoneyReferenced(str(accountReceive),
                                                                    str(random.randint(2000000000, 200000000000)),
                                                                    str(p),
                                                                    "400000000",
                                                                    sender, fullHash))
        print(response.json())
        fullHash = response.json()["fullHash"]
        print("----------------------------------------------------------------------------------------------")
        k += 1
