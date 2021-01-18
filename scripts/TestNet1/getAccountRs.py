import testNet1
import requests
import data

for k in range(1, 500, 1):
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
    response = requests.request("GET", "http://" + testNet1.peer2 + "/apl", headers=data.headers, params=getAccountId)
    account = response.json()["accountRS"]
    print(account)