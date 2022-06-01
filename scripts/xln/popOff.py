import requests
import config_Luna_Wallet

ADMIN_PASSWORD = config_Luna_Wallet.ADMIN_PASSWORD_T1
url = config_Luna_Wallet.xln_t1_2

def popOffByBlocks(url, blocks):
    print("---------- START POP OFF on --->>> " + url + " <<< ----")
    querystring = {"requestType": "popOff", "adminPassword": ADMIN_PASSWORD, "numBlocks": str(blocks)}
    response = requests.request("POST", url + "/api/rpc", params=querystring)
    print(response.text)
    print("--------END of POP OFF proccess on peer --->>> " + url + " <<< --------")

def popOffByHeight(url, height, validate):
    print("---------- START POP OFF on --->>> " + url + " <<< ----")
    querystring = {"requestType": "popOff", "adminPassword": ADMIN_PASSWORD, "height": str(height), "validate": validate}
    response = requests.request("POST", url + "/api/rpc", params=querystring)
    print(response.text)
    print("--------END of POP OFF proccess on peer --->>> " + url + " <<< --------")

#popOffByHeight(xln_t2_1, 1, False)

popOffByHeight(url, 1, True)



