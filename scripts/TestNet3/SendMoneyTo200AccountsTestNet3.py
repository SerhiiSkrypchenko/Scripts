import requests

import data
import conf
import random

url1 = "http://51.15.250.32/apl"
url2 = "http://51.15.253.171/apl"
url3 = "http://51.15.210.116/apl"
url4 = "http://51.15.242.197/apl"
url5 = "http://51.15.218.241/apl"

# send Money to APL-AHWS-NGBG-V4LK-8Q65T
response = requests.request("POST", url1, data=data.payload, headers=data.headers,
                            params=data.sendMoneyFromStandardWalletToVaultWallet(conf.account2, "20000000000",
                                                                                 conf.account1SecretPhrase, "200000000",
                                                                                 conf.sender1))
print(response.json())




k = 1
for k in range(1, 201):
    print(k)
    print("-------------")

    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
    response = requests.request("GET", url1, headers=data.headers, params=getAccountId)
    print(response.json())
    account = response.json()["accountRS"]
    print("-------------")
    print(str(account))
    print("-------------")

    response = requests.request("POST", random.choice([url1, url2, url3]), data=data.payload,
                                headers=data.headers,
                                params=data.sendMoneyFromStandardWalletToVaultWallet(str(account), "1000000000000000",
                                                                                     conf.account1SecretPhrase,
                                                                                     "200000000",
                                                                                     conf.sender1))
    print(response.json())
    print("----------------------------------------------------------------------------------------------")
    k += 1
