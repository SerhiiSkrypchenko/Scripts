import testNet2
import requests
import data

for k in range(1, 200, 1):
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
    response = requests.request("GET", testNet2.peer1 + "/apl", headers=data.headers, params=getAccountId)
    account = response.json()["accountRS"]
    print(str(k) + ": " + account)