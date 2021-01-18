import functions
from testNet1 import t1
import testNet2
import testNet3
from functions import getForkHeight
from testNet2 import t2
from testNet3 import t3
import karantin
import mainNet
import testNet4_tap
import requests

url = testNet4_tap.peer1


def count_Amount_Transactions(url, startHeight, finishHeight):
    total_Number_Of_Transactions = 0
    max_Number_transactions_In_Block = 0
    min_Number_transactions_In_Block = 2
    number_Of_Blocks = finishHeight + 1 - startHeight

    for i in range (startHeight, finishHeight+1, 1):
        number_Transactions_In_Block = getBlock(i, url)
        total_Number_Of_Transactions = total_Number_Of_Transactions + number_Transactions_In_Block
        print("Total number of transactions are = " + str(total_Number_Of_Transactions))

        if (number_Transactions_In_Block > max_Number_transactions_In_Block):
            max_Number_transactions_In_Block = number_Transactions_In_Block
        if (number_Transactions_In_Block < min_Number_transactions_In_Block):
            min_Number_transactions_In_Block = number_Transactions_In_Block

    average_Number_Of_Transactions = total_Number_Of_Transactions/number_Of_Blocks
    print("AVERAGE number of transactions in BLOCK = " + str(average_Number_Of_Transactions))
    print("min number of transactions in BLOCK = " + str(min_Number_transactions_In_Block))
    print("max number of transactions in BLOCK = " + str(max_Number_transactions_In_Block))
    print("number of blocks = " + str(number_Of_Blocks))


def getBlock(height, url):
    querystring = {"": "%2Fapl", "requestType": "getBlock", "includeTransactions": "true", "includeExecutedPhased": "true", "height": str(height)}
    response = requests.request("GET", "http://" + url + "/apl", params=querystring)
    number_Of_Transactions = response.json()["numberOfTransactions"]
    print("Number of transactions on height " + str(height) + " = " + str(number_Of_Transactions))
    return number_Of_Transactions

#count_Amount_Transactions(testNet3.peer7, 613913, 614072)

count_Amount_Transactions(testNet4_tap.peer1, 73329, 73314)
