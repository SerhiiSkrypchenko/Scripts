import requests
import data
import conf
import random

url1 = "http://51.15.250.32/apl"
url2 = "http://51.15.253.171/apl"
url3 = "http://51.15.210.116/apl"
url4 = "http://51.15.242.197/apl"
url5 = "http://51.15.218.241/apl"

k = 1
for k in range(1, 201):
    print(k)
    print("-------------")

    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
    response = requests.request("GET", random.choice([url1, url2, url3, url4, url5]), headers=data.headers, params=getAccountId)
    print(response.json())
    accountRS = response.json()["accountRS"]
    account = response.json()["account"]
    print("-------------")
    print(str(accountRS))
    print(str(account))
    print("-------------")

    querystring = {"": "%2Fapl", "requestType": "getAccount", "account": str(accountRS)}
    response = requests.request("GET", random.choice([url1, url2, url3, url4, url5]), params=querystring)
    print(response.text)
    unconfirmedBalanceATM = response.json()["unconfirmedBalanceATM"]
    print(unconfirmedBalanceATM)
    print("-------------")

    amountATM = int(unconfirmedBalanceATM)-200000000
    response = requests.request("POST", random.choice([url1, url2, url3, url4, url5]),
                                params=data.sendMoneyFromStandardWalletToVaultWallet(conf.account1, str(amountATM),
                                                                                     str(k),
                                                                                     "200000000",
                                                                                     account))
    print(response.json())
    print("----------------------------------------------------------------------------------------------")
    k += 1
