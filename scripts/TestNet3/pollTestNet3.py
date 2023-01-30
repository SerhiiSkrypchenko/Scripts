import requests
import testNet3
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
# urls2 = random.choice([url21, url22, url23, url24, url25, url26, url27, url28, url29])
urls2 = random.choice([url21, localhost])

alive = True
while alive:
    pollByAccountId = {"name": "ApolloInFuture", "votingModel": "0", "finishHeight": "44000", "minNumberOfOptions": "1",
                       "maxNumberOfOptions": "1", "minRangeValue": "0", "maxRangeValue": "1", "feeATM": "1000000000",
                       "description": "Description+of+POLLNAME", "answers": ["YES", "NO", "PERHAPS"],
                       "create_poll_answers[]": "1",
                       "minBalanceModel": "0", "minBalanceType": "0", "option00": "1", "option01": "2", "option02": "3",
                       "passphrase": "11", "sender": "7821792282123976600", "deadline": "1440",
                       "requestType": "createPoll",
                       "create_poll_answers%5B%5D": "1"}

    response = requests.request("POST",
                                urls3,
                                params=pollByAccountId)
    print(response.text)

    poll = response.json()["transaction"]
    print("-----------------------------------------------------")
    print("poll by AccountID = " + str(poll))
    print("-----------------------------------------------------")

    pollByBalance = {"name": "ByBalance" + str(random.randint(1, 100)),
                     "votingModel": "1",
                     "minBalance": "10000",
                     "finishHeight": "44000",
                     "minNumberOfOptions": "1", "maxNumberOfOptions": "1", "minRangeValue": "0", "maxRangeValue": "1",
                     "feeATM": "1000000000",
                     "description": "description: voting by Balance",
                     "answers": ["YES", "NO", "MAYBE"], "create_poll_answers[]": "YES", "minBalanceModel": "1",
                     "option00": "YES", "option01": "NO", "option02": "MAYBE", "passphrase": "11",
                     "sender": "7821792282123976600", "deadline": "1440", "requestType": "createPoll",
                     "create_poll_answers%5B%5D": "YES"}
    response = requests.request("POST",
                                urls3,
                                params=pollByBalance)
    print(response.text)

    pollBalance = response.json()["transaction"]
    print("-----------------------------------------------------")
    print("poll by Account Balance " + str(pollBalance))
    print("-----------------------------------------------------")

    k = 0
    for k in range(0, 120):
        print(k)
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", urls3, params=getAccountId)
        print(response.text)

        account = response.json()["account"]
        print("-----------------------------------------------------")

        querystring1 = {"0": "8", "1": "6", "2": "4", "3": "1", "4": "4", "5": "0", "6": "8", "7": "0", "8": "3",
                        "9": "5",
                        "10": "2", "11": "1", "12": "3", "13": "8", "14": "2", "15": "0", "16": "6", "17": "4",
                        "18": "6",
                        "requestType": "castVote", "poll": str(poll), "vote00": "1", "vote01": "-128",
                        "vote02": "-128", "feeATM": "100000000",
                        "secretPhrase": str(k),
                        "sender": str(account), "deadline": "1440"}

        response = requests.request("POST",
                                    urls3,
                                    params=querystring1)

        print(response.text)
        print("-----------------------------------------------------")
        querystring2 = {"0": "1", "1": "6", "2": "5", "3": "7", "4": "9", "5": "9", "6": "5", "7": "9", "8": "3",
                        "9": "6",
                        "10": "2", "11": "9", "12": "2", "13": "0", "14": "3", "15": "9", "16": "3", "17": "6",
                        "18": "9", "19": "8",
                        "requestType": "castVote", "poll": str(pollBalance), "vote00": "1", "vote01": "-128",
                        "vote02": "-128", "feeATM": "100000000",
                        "secretPhrase": str(k),
                        "sender": str(account), "deadline": "1440"}

        response = requests.request("POST",
                                    urls3,
                                    params=querystring2)

        print(response.text)
        print("-----------------------------------------------------")
        k += 1

    k = 121
    for k in range(121, 160):
        print(k)
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", urls3, params=getAccountId)
        print(response.text)

        account = response.json()["account"]
        print("-----------------------------------------------------")

        querystring1 = {"0": "8", "1": "6", "2": "4", "3": "1", "4": "4", "5": "0", "6": "8", "7": "0", "8": "3",
                        "9": "5",
                        "10": "2", "11": "1", "12": "3", "13": "8", "14": "2", "15": "0", "16": "6", "17": "4",
                        "18": "6",
                        "requestType": "castVote", "poll": str(poll), "vote00": "-128", "vote01": "1",
                        "vote02": "-128", "feeATM": "100000000",
                        "secretPhrase": str(k),
                        "sender": str(account), "deadline": "1440"}

        response = requests.request("POST",
                                    urls3,
                                    params=querystring1)

        print(response.text)
        print("-----------------------------------------------------")
        querystring2 = {"0": "1", "1": "6", "2": "5", "3": "7", "4": "9", "5": "9", "6": "5", "7": "9", "8": "3",
                        "9": "6",
                        "10": "2", "11": "9", "12": "2", "13": "0", "14": "3", "15": "9", "16": "3", "17": "6",
                        "18": "9", "19": "8",
                        "requestType": "castVote", "poll": str(pollBalance), "vote00": "1", "vote01": "-128",
                        "vote02": "-128", "feeATM": "100000000",
                        "secretPhrase": str(k),
                        "sender": str(account), "deadline": "1440"}

        response = requests.request("POST",
                                    urls3,
                                    params=querystring2)

        print(response.text)
        print("-----------------------------------------------------")
        k += 1

    k = 161
    for k in range(161, 201):
        print(k)
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", urls3, params=getAccountId)
        print(response.text)

        account = response.json()["account"]
        print("-----------------------------------------------------")

        querystring1 = {"0": "8", "1": "6", "2": "4", "3": "1", "4": "4", "5": "0", "6": "8", "7": "0", "8": "3",
                        "9": "5",
                        "10": "2", "11": "1", "12": "3", "13": "8", "14": "2", "15": "0", "16": "6", "17": "4",
                        "18": "6",
                        "requestType": "castVote", "poll": str(poll), "vote00": "-128", "vote01": "-128",
                        "vote02": "1", "feeATM": "100000000",
                        "secretPhrase": str(k),
                        "sender": str(account), "deadline": "1440"}

        response = requests.request("POST",
                                    urls3,
                                    params=querystring1)

        print(response.text)
        print("-----------------------------------------------------")
        querystring2 = {"0": "1", "1": "6", "2": "5", "3": "7", "4": "9", "5": "9", "6": "5", "7": "9", "8": "3",
                        "9": "6",
                        "10": "2", "11": "9", "12": "2", "13": "0", "14": "3", "15": "9", "16": "3", "17": "6",
                        "18": "9", "19": "8",
                        "requestType": "castVote", "poll": str(pollBalance), "vote00": "1", "vote01": "-128",
                        "vote02": "-128", "feeATM": "100000000",
                        "secretPhrase": str(k),
                        "sender": str(account), "deadline": "1440"}

        response = requests.request("POST",
                                    urls3,
                                    params=querystring2)

        print(response.text)
        print("-----------------------------------------------------")
        k += 1

