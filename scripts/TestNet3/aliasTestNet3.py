import requests
import random

# Test Net 3
url31 = "http://51.15.250.32/apl"
url32 = "http://51.15.253.171/apl"
url33 = "http://51.15.210.116/apl"
url34 = "http://51.15.242.197/apl"
url35 = "http://51.15.218.241/apl"
urls3 = random.choice([url32, url33, url34, url35])
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
urls2 = random.choice([url21, url22, url23, url24, url25, url26, url27, url28, url29])
#urls2 = random.choice([localhost])

j = 0
for j in range(0, 10000000000000000000000000000000000000000):
    k = 1
    for k in range(1, 201):
        print(k)
        print("-------------")
        i = random.randint(1, 200)
        p = random.randint(1, 200)

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
        response = requests.request("GET",
                                    urls3,
                                    params=getAccountId)
        print(response.json())
        accountReceive = response.json()["accountRS"]
        print("-------------")
        print(str("accountReceive = " + accountReceive))
        print("-------------")

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
        response = requests.request("GET",
                                    urls3,
                                    params=getAccountId)
        print(response.json())
        accountSender = response.json()["accountRS"]
        sender = response.json()["account"]
        print("-------------")
        print(str("accountSender = " + accountSender))
        print(str("account = " + sender))
        print("------------------------------------------ CREATING ALIAS #1 ------------------------------------------")
        aliasname = "A" + str(random.randint(1, 10000))
        createAliasURL = {"requestType": "setAlias", "aliasName": aliasname,
                          "feeATM": "2500000000",
                          "aliasURI": "www.destroy" + str(random.randint(1, 30)) + ".com",
                          "secretPhrase": str(p),
                          "sender": accountSender,
                          "deadline": "1440"}
        response = requests.request("POST", urls3, params=createAliasURL)
        print(response.text)
        alias = response.json()["transaction"]
        print(alias)
        print("----------------------------------- END OF CREATING ALIAS #1 ------------------------------------------")
        print("------------------------------------------ CREATING ALIAS #2 ------------------------------------------")
        aliasname1 = "B" + str(random.randint(1, 10000))
        createAliasURL1 = {"requestType": "setAlias", "aliasName": aliasname1,
                           "feeATM": "2500000000",
                           "aliasURI": str(accountReceive),
                           "secretPhrase": str(p),
                           "sender": accountSender,
                           "deadline": "1440"}
        response = requests.request("POST", urls3, params=createAliasURL1)
        print(response.text)
        print("----------------------------------- END OF CREATING ALIAS #2 ------------------------------------------")
        print("------------------------------------------ CREATING ALIAS #3 ------------------------------------------")
        aliasname2 = "C" + str(random.randint(1, 10000))
        createAliasURL2 = {"requestType": "setAlias", "aliasName": aliasname2,
                           "feeATM": "2500000000",
                           "aliasURI": "DATA" + str(random.randint(1, 20)),
                           "secretPhrase": str(p),
                           "sender": accountSender,
                           "deadline": "1440"}
        response = requests.request("POST", urls3, params=createAliasURL2)
        print(response.text)
        print("----------------------------------- END OF CREATING ALIAS #3 ------------------------------------------")
        print("----------------------------------- DELETE ALIAS #1 ------------------------------------------")
        z = 0
        while z <= 30:
            deleteAlias = {"0": "1", "1": "2", "2": "0", "3": "9", "4": "9", "5": "3", "6": "6", "7": "5", "8": "0",
                           "9": "7", "10": "3", "11": "8", "12": "2", "13": "7", "14": "1", "15": "9", "16": "1",
                           "17": "7", "18": "2", "19": "0",
                           "alias": str(alias),
                           "feeATM": "2500000000",
                           "secretPhrase": str(p),
                           "sender": accountSender,
                           "deadline": "1440",
                           "priceATM": "0",
                           "requestType": "deleteAlias"}
            response = requests.request("POST", urls3, params=deleteAlias)
            print(response.json())
            print("----------------------------------- DELETE of ALIAS #1 FINISHED------------------------------------")
            z += 1
        z = 0
        while z <= 30:
            print("--------------------------------------- TRANSFER ALIAS #1 -----------------------------------------")
            transferAlias = {"0": "1", "1": "2", "2": "6", "3": "5", "4": "3", "5": "0", "6": "5", "7": "5", "8": "2",
                             "9": "3", "10": "4", "11": "5", "12": "1", "13": "5", "14": "2", "15": "0", "16": "4",
                             "17": "9",
                             "18": "7", "19": "0",
                             "requestType": "sellAlias",
                             "recipient": str(accountReceive),
                             "feeATM": "3000000000",
                             "add_message": "true",
                             "permanent_message": "false",
                             "priceATM": "0",
                             "aliasName": aliasname,
                             "secretPhrase": str(p),
                             "messageToEncrypt": "MESSAGE+TRANSFER+ALIAS",
                             "sender": accountSender,
                             "deadline": "1440"}
            response = requests.request("POST", urls3, params=transferAlias)
            print(response.json())
            print("---------------------------------------- END OF TRANSFERING ALIAS --------------------------------")
            z += 1
        k += 1
