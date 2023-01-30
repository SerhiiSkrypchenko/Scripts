import string

import requests
import random
import functions
import testNet1
from functions import aliasTransactionsTn
from functions import aliasTransactions
import testNet3
import testNet2
import testNetStage
import time

def id_generator(size=3, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def aliasTransactionsTn(testNet):
    alive = True
    while alive:
        k = 1
        for k in range(1, 201):
            print(k)
            print("-------------")
            i = random.randint(1, 200)
            p = random.randint(1, 200)
            url = random.choice(testNet)

            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
            response = requests.request("GET",
                                        url + "/apl",
                                        params=getAccountId)
            print(response.json())
            accountReceive = response.json()["accountRS"]
            print("-------------")
            print(str("accountReceive = " + accountReceive))
            print("-------------")

            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
            response = requests.request("GET",
                                        url + "/apl",
                                        params=getAccountId)
            print(response.json())
            accountSender = response.json()["accountRS"]
            sender = response.json()["account"]
            print("-------------")
            print(str("accountSender = " + accountSender))
            print(str("account = " + sender))

            print(
                "------------------------------------------ CREATING ALIAS #1 URI TYPE -------------------------------")

            aliasnameURI = "URI" + str(id_generator())
            createAliasURL = {"requestType": "setAlias",
                              "aliasName": aliasnameURI,
                              "type": "uri",
                              "feeATM": "2500000000",
                              "aliasURI": "www.destroy" + str(random.randint(1, 30)) + ".com",
                              "secretPhrase": str(p),
                              "sender": accountSender,
                              "deadline": "1440"}
            response = requests.request("POST", url + "/apl", params=createAliasURL)
            print(response.text)
            aliasURI = response.json()["transaction"]
            print("aliasID = " + str(aliasURI))
            print("alias NAME = " + str(aliasnameURI))
            print(
                "--------PEER: " + url + " <<< -------- END OF CREATING ALIAS #1 -------------------")
            time.sleep(0)
            print(
                "------------------------------------------ CREATING ALIAS #2 ACCOUNT TYPE -----------------------------------")
            aliasnameAccount = "URI" + str(id_generator())
            createAliasAccount = {"requestType": "setAlias",
                               "aliasName": aliasnameAccount,
                               "type": "account",
                               "feeATM": "2500000000",
                               "aliasURI": accountReceive,
                               "secretPhrase": str(p),
                               "sender": accountSender,
                               "deadline": "1440"}
            response = requests.request("POST", url + "/apl", params=createAliasAccount)
            print(response.text)
            aliasID = response.json()["transaction"]
            print("aliasID = " + str(aliasID))
            print("alias NAME = " + str(aliasnameAccount))
            print(
                "-------- Peer: " + url + " <<< --- END OF CREATING ALIAS #2 ------------------------")
            time.sleep(0)
            print(
                "------------------------------------------ CREATING ALIAS #3 Other Type --------------------------")
            aliasnameOther = "URI" + str(id_generator())
            createAliasOther = {"requestType": "setAlias",
                               "aliasName": aliasnameOther,
                               "type": "general",
                               "feeATM": "2500000000",
                               "aliasURI": "DATA" + str(random.randint(1, 20)),
                               "secretPhrase": str(p),
                               "sender": accountSender,
                               "deadline": "1440"}
            response = requests.request("POST", url + "/apl", params=createAliasOther)
            print(response.text)
            aliasID = response.json()["transaction"]
            print("aliasID = " + str(aliasID))
            print("alias NAME = " + str(aliasnameOther))
            print(
                "----------------------------------- END OF CREATING ALIAS #3 ----------------------------------------")
            time.sleep(20)
            print(
                "----------------------------------- DELETING " + aliasnameURI + " ----------------------------------------")

            deleteAlias = {"0": "1", "1": "2", "2": "0", "3": "9", "4": "9", "5": "3", "6": "6", "7": "5",
                           "8": "0",
                           "9": "7", "10": "3", "11": "8", "12": "2", "13": "7", "14": "1", "15": "9",
                           "16": "1",
                           "17": "7", "18": "2", "19": "0",
                           "alias": str(aliasnameURI),
                           "feeATM": "2500000000",
                           "secretPhrase": str(p),
                           "sender": accountSender,
                           "deadline": "1440",
                           "priceATM": "0",
                           "requestType": "deleteAlias"}
            response = requests.request("POST", url + "/apl", params=deleteAlias)
            print(response.json())
            print(
                "--------------------------------- DELETING " + aliasnameURI + " IS FINISHED --------------------------------")
            time.sleep(20)
            while "errorDescription" in response.json():
                deleteAlias = {"0": "1", "1": "2", "2": "0", "3": "9", "4": "9", "5": "3", "6": "6",
                               "7": "5",
                               "8": "0",
                               "9": "7", "10": "3", "11": "8", "12": "2", "13": "7", "14": "1", "15": "9",
                               "16": "1",
                               "17": "7", "18": "2", "19": "0",
                               "alias": str(aliasnameURI),
                               "feeATM": "2500000000",
                               "secretPhrase": str(p),
                               "sender": accountSender,
                               "deadline": "1440",
                               "priceATM": "0",
                               "requestType": "deleteAlias"}
                response = requests.request("POST", url + "/apl", params=deleteAlias)
                print(response.json())
                print(
                    "---------------------------------- DELETING " + aliasnameURI + " IS FINISHED --------------------------")
                time.sleep(20)

            print(
                "-------------------------- TRANSFER " + aliasname + "----------------------------------")
            transferAlias = {"0": "1", "1": "2", "2": "6", "3": "5", "4": "3", "5": "0", "6": "5", "7": "5",
                             "8": "2",
                             "9": "3", "10": "4", "11": "5", "12": "1", "13": "5", "14": "2", "15": "0",
                             "16": "4",
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
            response = requests.request("POST", url + "/apl", params=transferAlias)
            print(response.json())
            print(
                "--------------------------  TRANSFER " + aliasname + " IS FINISHED  -----------------")
            time.sleep(20)
            while "errorDescription" in response.json():
                transferAlias = {"0": "1", "1": "2", "2": "6", "3": "5", "4": "3", "5": "0", "6": "5",
                                 "7": "5",
                                 "8": "2",
                                 "9": "3", "10": "4", "11": "5", "12": "1", "13": "5", "14": "2", "15": "0",
                                 "16": "4",
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
                response = requests.request("POST", url + "/apl", params=transferAlias)
                print(response.json())
                print(
                    "--------------------------------  TRANSFER " + aliasname + " IS FINISHED  ---------------------")
                time.sleep(20)
            k += 1


aliasTransactionsTn(testNetStage.t15All)


