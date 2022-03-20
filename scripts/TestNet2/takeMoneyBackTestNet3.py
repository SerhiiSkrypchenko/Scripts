import requests
import data
import conf
import random

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
urls2 = random.choice([url21, localhost])

k = 1
for k in range(1, 201):
    print(k)
    print("-------------")

    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
    response = requests.request("GET", urls2, headers=data.headers, params=getAccountId)
    print(response.json())
    accountRS = response.json()["accountRS"]
    account = response.json()["account"]
    print("-------------")
    print(str(accountRS))
    print(str(account))
    print("-------------")

    querystring = {"": "%2Fapl", "requestType": "getAccount", "account": str(accountRS)}
    response = requests.request("GET", urls2, params=querystring)
    print(response.text)
    unconfirmedBalanceATM = response.json()["unconfirmedBalanceATM"]
    print(unconfirmedBalanceATM)
    print("-------------")

    amountATM = int(unconfirmedBalanceATM)-200000000
    response = requests.request("POST", urls2,
                                params=data.sendMoneyFromStandardWalletToVaultWallet(conf.account1, str(amountATM),
                                                                                     str(k),
                                                                                     "200000000",
                                                                                     account))
    print(response.json())
    print("----------------------------------------------------------------------------------------------")
    k += 1
