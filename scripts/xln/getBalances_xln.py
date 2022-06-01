import requests
import config_Luna_Wallet
import random

url = random.choice(config_Luna_Wallet.xln_t1)

oldEffBalance = 0
for k in range(1, 200, 1):
    getAccountId = {"requestType": "getAccountId", "secretPhrase": str(k)}
    response = requests.request("GET", url + "/api/rpc", params=getAccountId)
    print(response.json())
    account = response.json()["accountXLN"]
    #print(str(k) + ": " + account)

    getAccount = {"requestType": "getAccount", "account": str(account), "includeEffectiveBalance": True}
    response = requests.request("GET", url + "/api/rpc", params=getAccount)
    #print(response.json())
    balanceMLN = response.json()["balanceMLN"]
    unconfirmedBalanceMLN = response.json()["unconfirmedBalanceMLN"]
    effectiveBalanceXLN = response.json()["effectiveBalanceXLN"]
    print(str(k) + " BalanceMLN: " + balanceMLN + " ; unconfirmedBalanceMLN = " + unconfirmedBalanceMLN + " ; effectiveBalanceXLN = " + str(effectiveBalanceXLN) + " XLN")
    oldEffBalance = effectiveBalanceXLN + oldEffBalance
    print("balance total = " + str(oldEffBalance))
