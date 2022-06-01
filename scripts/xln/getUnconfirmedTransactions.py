import requests
import data
import config_Luna_Wallet


url = config_Luna_Wallet.xln_t1_1


def getUnconfirmedTransactions():
    getUnconfirmedTransactions = {"requestType": "getUnconfirmedTransactions"}
    response = requests.request("GET", url + "/api/rpc", headers=data.headers, params=getUnconfirmedTransactions)
    print(response.json())

getUnconfirmedTransactions()




