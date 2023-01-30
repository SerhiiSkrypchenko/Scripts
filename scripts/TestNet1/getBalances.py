import testNet2
import testNet3
import testNet1
import requests
import data

"""for k in range(1, 200, 1):
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
    response = requests.request("GET", testNet1.peer1 + "/apl", headers=data.headers, params=getAccountId)
    account = response.json()["accountRS"]
    #print(str(k) + ": " + account)

    getAccount = {"": "%2Fapl", "requestType": "getAccount", "account": str(account)}
    response = requests.request("GET", testNet3.peer1 + "/apl", headers=data.headers, params=getAccount)
    balanceATM = response.json()["balanceATM"]
    print(str(k) + " Balance: " + balanceATM)"""




"""getAccount = {"": "%2Fapl", "requestType": "getAccount", "account": "9382286186955367677", "includeEffectiveBalance": True}
response = requests.request("GET", testNet2.peer2 + "/apl", headers=data.headers, params=getAccount)
balanceATM = response.json()["balanceATM"]
effective = response.json()["effectiveBalanceAPL"]
guaranteedBalanceATM = response.json()["guaranteedBalanceATM"]
print("Balance = " + balanceATM + "; Effective balance = " + str(effective) + "; Guaranteed = " + guaranteedBalanceATM)

getAccount = {"": "%2Fapl", "requestType": "getAccount", "account": "9382286186955367677", "includeEffectiveBalance": True}
response = requests.request("GET", testNet2.peer3 + "/apl", headers=data.headers, params=getAccount)
balanceATM = response.json()["balanceATM"]
effective = response.json()["effectiveBalanceAPL"]
guaranteedBalanceATM = response.json()["guaranteedBalanceATM"]
print("Balance = " + balanceATM + "; Effective balance = " + str(effective) + "; Guaranteed = " + guaranteedBalanceATM)


getAccount = {"": "%2Fapl", "requestType": "getAccount", "account": "9382286186955367677", "includeEffectiveBalance": True}
response = requests.request("GET", testNet2.peer4 + "/apl", headers=data.headers, params=getAccount)
balanceATM = response.json()["balanceATM"]
effective = response.json()["effectiveBalanceAPL"]
guaranteedBalanceATM = response.json()["guaranteedBalanceATM"]
print("Balance = " + balanceATM + "; Effective balance = " + str(effective) + "; Guaranteed = " + guaranteedBalanceATM)

getAccount = {"": "%2Fapl", "requestType": "getAccount", "account": "9382286186955367677", "includeEffectiveBalance": True}
response = requests.request("GET", testNet2.peer5 + "/apl", headers=data.headers, params=getAccount)
balanceATM = response.json()["balanceATM"]
effective = response.json()["effectiveBalanceAPL"]
guaranteedBalanceATM = response.json()["guaranteedBalanceATM"]
print("Balance = " + balanceATM + "; Effective balance = " + str(effective) + "; Guaranteed = " + guaranteedBalanceATM)

getAccount = {"": "%2Fapl", "requestType": "getAccount", "account": "9382286186955367677", "includeEffectiveBalance": True}
response = requests.request("GET", testNet2.peer6 + "/apl", headers=data.headers, params=getAccount)
balanceATM = response.json()["balanceATM"]
effective = response.json()["effectiveBalanceAPL"]
guaranteedBalanceATM = response.json()["guaranteedBalanceATM"]
print("Balance = " + balanceATM + "; Effective balance = " + str(effective) + "; Guaranteed = " + guaranteedBalanceATM)

getAccount = {"": "%2Fapl", "requestType": "getAccount", "account": "9382286186955367677", "includeEffectiveBalance": True}
response = requests.request("GET", testNet2.peer7 + "/apl", headers=data.headers, params=getAccount)
balanceATM = response.json()["balanceATM"]
effective = response.json()["effectiveBalanceAPL"]
guaranteedBalanceATM = response.json()["guaranteedBalanceATM"]
print("Balance = " + balanceATM + "; Effective balance = " + str(effective) + "; Guaranteed = " + guaranteedBalanceATM)"""

