import requests
import urllib3
import time
urllib3.disable_warnings()
import config_Luna_Wallet

url = config_Luna_Wallet.xln_t1_1

def getBlock(url):
    #querystring = {"": "%2Fapl", "requestType": "getBlock"}
    response = requests.request("GET", url + "/api/rest/block/one", verify=False)
    if response:
        #print(response.json())
        currentHeight = response.json()["height"]
        numberOfTransactions = response.json()["numberOfTransactions"]
        print("Current Height on " + url + " = " + str(currentHeight) + " blocks; " + " numberOfTransactions = " + str(numberOfTransactions))




while True:
    getBlock(url)
    time.sleep(1)












