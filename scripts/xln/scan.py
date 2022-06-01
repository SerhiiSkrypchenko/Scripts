import requests
import config_Luna_Wallet

url = config_Luna_Wallet.xln_t1_3
ADMIN_PASSWORD = config_Luna_Wallet.ADMIN_PASSWORD_T1

def scanByBlocks(url, blocks, validate):
    print("---------- START SCAN on --->>> " + url + " <<< ----")
    querystring = {"requestType": "scan", "adminPassword": ADMIN_PASSWORD, "numBlocks": str(blocks), "validate": validate}
    response = requests.request("POST", url + "/api/rpc", params=querystring)
    print(response.text)
    print("--------END of SCAN proccess on peer --->>> " + url + " <<< --------")

def scanByHeight(url, height, validate):
    print("---------- START SCAN on --->>> " + url + " <<< ----")
    querystring = {"requestType": "scan", "adminPassword": ADMIN_PASSWORD, "height": height, "validate": validate}
    response = requests.request("POST", url + "/api/rpc", params=querystring)
    print(response.text)
    print("--------END of SCAN proccess on peer --->>> " + url + " <<< --------")

scanByHeight(url, 0, True)





