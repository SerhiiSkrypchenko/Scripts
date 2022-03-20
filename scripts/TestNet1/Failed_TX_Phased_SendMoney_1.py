import requests
import random
import time

"""peer1 = "https://apl-tnf-1.tnf.apollowallet.org"
peer2 = "https://apl-tnf-2.tnf.apollowallet.org"
peer3 = "https://apl-tnf-3.tnf.apollowallet.org"
peer4 = "https://apl-tnf-4.tnf.apollowallet.org"
peer5 = "https://apl-tnf-5.tnf.apollowallet.org"
peer6 = "https://apl-tnf-6.tnf.apollowallet.org"""

peer1 = "https://apl-t2-1.testnet2.apollowallet.org"
peer2 = "https://apl-t2-2.testnet2.apollowallet.org"
peer3 = "https://apl-t2-3.testnet2.apollowallet.org"
peer4 = "https://apl-t2-4.testnet2.apollowallet.org"
peer5 = "https://apl-t2-5.testnet2.apollowallet.org"
peer6 = "https://apl-redesign.testnet2.apollowallet.org"
peer7 = "https://apl-exchange.testnet.apollowallet.org"
localhost = "http://localhost:7876"
peer31 = "http://51.15.250.32:7876"
peer32 = "http://51.15.253.171:7876"
t2All = ([peer3, peer2, peer4, peer5])
#t2All = ([peer31, peer32])
URL = t2All

second = "failed8"
first = "failed7"
print("secret phrase of first acc is : " + first)
print("secret phrase of second acc is : " + second)

#"add_message": True,
#"messageToEncrypt": "test message long test message longtest message long test message longtest message long test message longtest message long test message long test message long test message long test message long test message long test message long test message long test message long test message longtest message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long",

"""def sendMoneyPhased(recipient, amountATM, secretPhrase, feeATM, sender, phasingFinishHeight):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "30",
            "sender": sender, "phasingFinishHeight": phasingFinishHeight, "phased": "true", "phasingVotingModel": "1",
            "phasingQuorum": "1",
            "add_message": True,
            "messageToEncrypt": "test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long"
    }"""


def sendMoney(recipient, amountATM, secretPhrase, feeATM, sender):
    url = URL
    peer = random.choice(url)
    print(peer)
    querystring = {"": "%2Fapl", "requestType": "getBlock"}
    response = requests.request("GET", peer + "/apl", params=querystring)
    print(response.text)
    currentHeight = response.json()["height"]
    finishHeight = currentHeight + 2
    print("-----------------------------------------------------")
    print("Current Height = " + str(currentHeight))
    print("Finish Height = " + str(finishHeight))
    print("-----------------------------------------------------")
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "1440", "sender": sender,
            "phased": "true",
            "phasingVotingModel": "-1",
            "phasingQuorum": "0",
            "phasingFinishHeight": finishHeight
            }

fee_APL = 2100000000
randomUrl = random.choice(URL)
sec = 1

getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": second}
response = requests.request("GET", randomUrl + "/apl",
                            params=getAccountId)
accountReceive = response.json()["accountRS"]
receive = response.json()["account"]
print(str("accountReceive = " + accountReceive))
print(str("accountReceiveID = " + receive))

getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": first}
response = requests.request("GET",
                            randomUrl + "/apl",
                            params=getAccountId)
accountSender = response.json()["accountRS"]
sender = response.json()["account"]
print(str("accountSender = " + accountSender))
print(str("accountSenderID = " + sender))

getAccountFirst = {"": "%2Fapl", "requestType": "getAccount", "account": sender}
response = requests.request("GET", randomUrl + "/apl", params=getAccountFirst)
print(response.json())
if "errorDescription" in response.text:
    response = requests.request("POST",
                                randomUrl + "/apl",
                                params=sendMoney(str(accountSender),
                                                        str(2000000000000),
                                                        "0",
                                                        str(fee_APL),
                                                        "9211698109297098287"))
    print(response.json())
else:
    balanceFirstAccount = response.json()['balanceATM']
    print("balance of first account is " + balanceFirstAccount)

getAccountSecond = {"": "%2Fapl", "requestType": "getAccount", "account": receive}
response = requests.request("GET", randomUrl + "/apl", params=getAccountSecond)
print(response.json())
if "errorDescription" in response.text:
    """response = requests.request("POST",
                                randomUrl + "/apl",
                                params=sendMoneyPrivate(str(accountReceive),
                                                        str(200000000000000),
                                                        "0",
                                                        str(fee_APL),
                                                        "9211698109297098287"))"""
    print(response.json())
else:
    balanceSecondAccount = response.json()["balanceATM"]
    print("balance of second account is " + balanceSecondAccount)
time.sleep(10)
alive = True
while alive:
    print(" <<<< --- START ---- >>>> ")
    randomUrl = random.choice(URL)
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": second}
    response = requests.request("GET", randomUrl + "/apl",
                                params=getAccountId)
    accountReceive = response.json()["accountRS"]
    receive = response.json()["account"]
    print(str("accountReceive = " + accountReceive))
    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": first}
    response = requests.request("GET",
                                randomUrl + "/apl",
                                params=getAccountId)
    accountSender = response.json()["accountRS"]
    sender = response.json()["account"]
    print(str("accountSender = " + accountSender))
    print(" PEER  = >> " + randomUrl + " << = ")

    getAccountFirst = {"": "%2Fapl", "requestType": "getAccount", "account": sender}
    response = requests.request("GET", randomUrl + "/apl", params=getAccountFirst)
    base_APL_AMOUNT = int(response.json()['balanceATM'])

    response = requests.request("POST",
                                randomUrl + "/apl",
                                params=sendMoney(str(accountReceive),
                                                        str(base_APL_AMOUNT - fee_APL - fee_APL),
                                                        first,
                                                        str(fee_APL),
                                                        sender))
    print("PRIVATE TRANSACTION #1 from first -> second")
    print(response.json())
    response = requests.request("POST",
                                randomUrl + "/apl",
                                params=sendMoney(str(accountReceive),
                                                        str(100000000),
                                                        first,
                                                        str(fee_APL),
                                                        sender))
    print("PRIVATE TRANSACTION #2 from first -> second")
    print(response.json())
    time.sleep(sec)
    getAccountSecond = {"": "%2Fapl", "requestType": "getAccount", "account": receive}
    response = requests.request("GET", randomUrl + "/apl", params=getAccountSecond)
    base_APL_AMOUNT = int(response.json()['balanceATM'])

    response = requests.request("POST",
                                randomUrl + "/apl",
                                params=sendMoney(str(accountSender),
                                                        str(base_APL_AMOUNT - fee_APL - fee_APL),
                                                        second,
                                                        str(fee_APL),
                                                        receive))
    print("PRIVATE TRANSACTION #1 from second -> first")
    print(response.json())
    response = requests.request("POST",
                                randomUrl + "/apl",
                                params=sendMoney(str(accountSender),
                                                        str(100000000),
                                                        second,
                                                        str(fee_APL),
                                                        receive))
    print("PRIVATE TRANSACTION #2 from second -> first")
    print(response.json())
    print("<<<< ---- END ---- >>>>")
    time.sleep(sec)
