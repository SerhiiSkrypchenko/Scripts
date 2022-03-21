import requests
import data

xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

xln_t2 = ([xln_t2_1, xln_t2_2, xln_t2_3])

for k in range(1, 200, 1):
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
    response = requests.request("GET", xln_t2_1 + "/xln-api", params=getAccountId)
    account = response.json()["accountRS"]
    #print(str(k) + ": " + account)

    getAccount = {"": "%2Fapl", "requestType": "getAccount", "account": str(account), "includeEffectiveBalance": True}
    response = requests.request("GET", xln_t2_1 + "/xln-api", params=getAccount)
    print(response.json())
    balanceMLN = response.json()["balanceMLN"]
    unconfirmedBalanceMLN = response.json()["unconfirmedBalanceMLN"]
    print(str(k) + " Balance: " + balanceMLN + " ; unconfirmedBalanceMLN = " + unconfirmedBalanceMLN)




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

