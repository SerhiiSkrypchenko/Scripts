import requests
import config_Luna_Wallet

url = config_Luna_Wallet.xln_t1_1
ADMIN_PASSWORD = config_Luna_Wallet.ADMIN_PASSWORD_T1

def trimDerivedTables(url):
    print("---------- START trimDerivedTables on --->>> " + url + " <<< ----")
    querystring = {"requestType": "trimDerivedTables", "adminPassword": ADMIN_PASSWORD}
    response = requests.request("POST", url + "/api/rpc", params=querystring)
    print(response.text)
    print("--------END of trimDerivedTables proccess on peer --->>> " + url + " <<< --------")

trimDerivedTables(url)




