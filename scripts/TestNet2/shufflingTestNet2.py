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
urls2 = random.choice([localhost])
j = 0
for j in range(0, 10000000000000000000000000000000000000000000000000000000000):
    print("-------------------------------------------- " + str(j) + " -------------------------------------------")
    querystring = {"amount": "700000000000", "registrationPeriod": "1439", "participantCount": "30",
                   "feeATM": "5000000000",
                   "passphrase": "11", "sender": "7821792282123976600", "deadline": "2000",
                   "requestType": "shufflingCreate", "holdingType": "0"}

    response = requests.request("POST", urls2, params=querystring)
    print(response.json())
    shufflingFullHash = response.json()["fullHash"]
    print("-----------------------------------------------------")
    print("shufflingFullHash = " + str(shufflingFullHash))
    print("-----------------------------------------------------")

    k = 1
    for k in range(1, 35):
        print(k)

        secretPhrase = random.randrange(1000, 10000000, 10)
        print("Secret Phrase = " + str(secretPhrase))
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": secretPhrase}
        response = requests.request("GET", urls2, params=getAccountId)

        publicKey = response.json()["publicKey"]
        print("Public Key = " + str(publicKey))
        print("-------------------------------------------------")

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", urls2, params=getAccountId)

        account = response.json()["account"]
        print("Account = " + str(account))
        print("-------------------------------------------------")

        response = requests.request("POST", urls2,
                                    params={"requestType": "startShuffler",
                                            "shufflingFullHash": shufflingFullHash,
                                            "recipientSecretPhrase": secretPhrase, "secretPhrase": str(k),
                                            "recipientPublicKey": publicKey,
                                            "createNoneTransactionMethod": "true", "feeATM": "300000000",
                                            "account": account,
                                            "deadline": "2000"})
        print(response.text)
        print("---------------------------------------------------------")
        k += 1
j += 1
