import requests
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

j = 0
for j in range(0, 100000000000000000000000000000000000000000000000000):
    print("----------------------------------------------------------------- " + str(
        j) + " ---------------------------------------------------")
    assetName = "Destroy" + str(random.randint(1, 99))
    availableAssets = 10000
    createAsset = {"requestType": "issueAsset", "decimals": "1", "name": str(assetName),
                   "feeATM": "10000000000000",
                   "description": "destroy " + str(random.randint(1, 100)), "passphrase": "11",
                   "sender": "7821792282123976600", "deadline": "1440",
                   "quantityATU": str(availableAssets)}

    response = requests.request("POST", urls2, params=createAsset)

    print(response.text)
    print("-----------------------------------------------------")
    assetID = response.json()["transaction"]
    print("assetID = " + assetID)
    print("-----------------------------------------------------")
    quantityATU = 100

    k = 0
    for k in range(0, 100):
        print(k)
        print("-------------")

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", urls2,
                                    params=getAccountId)
        print(response.json())
        accountRS = response.json()["accountRS"]
        account = response.json()["account"]
        print("-------------")
        print(str(accountRS))
        print(str(account))
        print("-------------")

        transferAsset = {"decimals": "1", "sender": "7821792282123976600", "requestType": "transferAsset",
                         "quantityATU": quantityATU,
                         "assetID": str(assetID), "assetName": assetName,
                         "availableAssets": str(availableAssets - (quantityATU * k)),
                         "recipient": str(accountRS), "message": "transfer asset to " + str(accountRS),
                         "feeATM": "5000000000",
                         "asset": str(assetID), "passphrase": "11", "deadline": "1440"}
        response = requests.request("POST", urls2, params=transferAsset)
        print(response.text)
        print("-------------------------- " + "transfer asset to  " + str(accountRS) + "  --------------")

        i = 1
        while i <= 10:
            print("------ delete ---- " + str(i) + " ---------")
            deleteAsset = {"requestType": "deleteAssetShares", "quantityATU": str(quantityATU), "assetID": str(assetID),
                           "decimals": "1", "assetName": assetName, "feeATM": "5000000000", "asset": str(assetID),
                           "sender": str(account), "secretPhrase": str(k), "deadline": "1440"}
            response = requests.request("POST", urls2, params=deleteAsset)
            print(response.text)
            print("-------------------------- " + "delete asset from  " + str(accountRS) + "  --------------")
            i += 1
        k += 1
j += 1
