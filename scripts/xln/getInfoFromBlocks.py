import requests
import urllib3
import config_Luna_Wallet

urllib3.disable_warnings()
url = config_Luna_Wallet.xln_t1_1


def getAverageNumberOfTransactions(url, startHeight, finishHeight):
    numberOfTransactions = 0
    for k in range(startHeight, finishHeight):
        params = {"height": k}
        response = requests.request("GET", url + "/api/rest/block/one", params=params)
        if response:
            # print(response.json())
            currentHeight = response.json()["height"]
            numberOfTransactionsInBlock = response.json()["numberOfTransactions"]
            print("Current Height on " + url + " = " + str(
                currentHeight) + " blocks; " + " numberOfTransactions = " + str(numberOfTransactionsInBlock))
            numberOfTransactions = numberOfTransactionsInBlock + numberOfTransactions
            print("Amount of transactions = " + str(numberOfTransactions))
    averageNumberOfTransactions = numberOfTransactions / (finishHeight - startHeight)
    print("Total transactions amount = " + str(numberOfTransactions))
    print("Average number of tx in block= " + str(averageNumberOfTransactions))


def getAverageSecPerBlock(url, startHeight, finishHeight):
    response = requests.request("GET", url + "/api/rest/block/one", params={"height": startHeight})
    startTimeStamp = response.json()["timestamp"]
    response = requests.request("GET", url + "/api/rest/block/one", params={"height": finishHeight})
    finishTimeStamp = response.json()["timestamp"]
    amountOfBlocks = finishHeight - startHeight
    averageSecPerBlock = (finishTimeStamp - startTimeStamp) / amountOfBlocks
    print("Amount of blocks in testing = " + str(amountOfBlocks))
    print("Average second per block = " + str(averageSecPerBlock))
    print("Start height = " + str(startHeight))
    print("Finish height = " + str(finishHeight))


getAverageNumberOfTransactions(url, 25200, 25320)
getAverageSecPerBlock(url, 25200, 25320)
