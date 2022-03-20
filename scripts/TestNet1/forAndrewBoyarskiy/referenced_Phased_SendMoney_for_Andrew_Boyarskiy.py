import time
import requests
import random

peer1 = "https://apl-t2-1.testnet2.apollowallet.org"
peer2 = "https://apl-t2-2.testnet2.apollowallet.org"
peer3 = "https://apl-t2-3.testnet2.apollowallet.org"
peer4 = "https://apl-t2-4.testnet2.apollowallet.org"
peer5 = "https://apl-t2-5.testnet2.apollowallet.org"
peer6 = "https://apl-redesign.testnet2.apollowallet.org"
peer7 = "https://apl-exchange.testnet.apollowallet.org"
t2 = ([peer1, peer2, peer3, peer4, peer5])

payload = ""
headers = {
    'Content-Type': "application/json"
}

def sendMoneyPhased(recipient, amountATM, secretPhrase, feeATM, sender, phasingFinishHeight):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "1440",
            "sender": sender, "phasingFinishHeight": phasingFinishHeight, "phased": "true", "phasingVotingModel": "1",
            "phasingQuorum": "1"}

def sendMoney_Phased_Referenced(recipient, amountATM, secretPhrase, feeATM, sender, phasingFinishHeight,
                                referencedTransactionFullHash):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "1440",
            "sender": sender, "phasingFinishHeight": phasingFinishHeight, "phased": "true", "phasingVotingModel": "1",
            "phasingQuorum": "1", "referencedTransactionFullHash": referencedTransactionFullHash,
            "messageIsPrunable": True}

def generateAccountReceiver(i, testnet):
    url = random.choice(testnet)
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
    response = requests.request("GET",
                                url + "/apl",
                                params=getAccountId)
    accountReceive = response.json()["accountRS"]
    print(str("accountReceive = " + accountReceive))
    return accountReceive

def generateAccountSender(p, testnet):
    url = random.choice(testnet)
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
    response = requests.request("GET",
                                url + "/apl",
                                params=getAccountId)
    accountSender = response.json()["accountRS"]
    sender = response.json()["account"]
    print(str("accountSender = " + accountSender))
    return sender

def referenced_Phased_Transactions(testnet):
    url = random.choice(testnet)

    # Receive current height to calculate finishHeight of first transaction
    querystring = {"": "%2Fapl", "requestType": "getBlock"}
    response = requests.request("GET", url + "/apl", params=querystring)
    currentHeight = response.json()["height"]
    print("Current Height = " + str(currentHeight))
    finishHeight = currentHeight + 3000
    print("Finish Height = " + str(finishHeight))

    # Generate new random accounts for first transaction
    p_sender = random.randint(1, 200)
    sender = generateAccountSender(p_sender, testnet)
    i_receiver = random.randint(1, 200)
    receiver = generateAccountReceiver(i_receiver, testnet)

    # Create first phased transaction with phasingFinishHeight = currentHeight + 3000 blocks
    response = requests.request("POST", url + "/apl", data=payload,
                                headers=headers,
                                params=sendMoneyPhased(receiver,
                                                       str(random.randint(2000000000, 200000000000)),
                                                       str(p_sender),
                                                       "3300000000",
                                                       sender,
                                                       str(finishHeight)))
    fullHash = response.json()["fullHash"]

    alive = True
    while alive:
        for k in range(1, 201):
            print("<<<<< START >>>>>>")
            url = random.choice(testnet)
            print(k)
            print("URL = " + url)
            # Calculate finishHeight (less than previuos on 30 blocks)
            querystring = {"": "%2Fapl", "requestType": "getBlock"}
            response = requests.request("GET", url + "/apl", params=querystring)
            currentHeight = response.json()["height"]
            print("Current Height = " + str(currentHeight))
            finish_Height = finishHeight - (30 * k)
            print("Finish_Height = " + str(finish_Height))

            # Generate new random accounts for test
            p_sender = random.randint(1, 200)
            sender = generateAccountSender(p_sender, testnet)
            i_receiver = random.randint(1, 200)
            receiver = generateAccountReceiver(i_receiver, testnet)

            #Create sendMoney tx with phased and referenced
            response = requests.request("POST",
                                        url + "/apl",
                                        params=sendMoney_Phased_Referenced(str(receiver),
                                                                           str(random.randint(2000000000,
                                                                                              200000000000)),
                                                                           str(p_sender),
                                                                           "3000000000",
                                                                           sender,
                                                                           finish_Height,
                                                                           fullHash))
            print(response.json())
            if "errorDescription" in response.text:
                print()
            else:
                fullHash = response.json()["fullHash"]
            print("<<<<< END >>>>>")
            print()
            k += 1
            time.sleep(0)


referenced_Phased_Transactions(t2)
