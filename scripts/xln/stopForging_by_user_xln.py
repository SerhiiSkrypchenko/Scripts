import requests
import config_Luna_Wallet


url = config_Luna_Wallet.xln_t1

#tn2 = 12345
#tn3 = 1
secretPhrase = "LunaInitAccount"
def stopForgingByAccount(url):
    print("----------------------------------------------------------------------")
    querystring = {"requestType": "stopForging", "secretPhrase": "LunaInitAccount"}
    response = requests.request("POST", url + "/api/rpc", params=querystring)
    print(response.json())
    print(" <<< ------------------  FORGING STOPPED ON  " + url + "     ---------------------- >>> ")

stopForgingByAccount(config_Luna_Wallet.xln_t1_1)
stopForgingByAccount(config_Luna_Wallet.xln_t1_2)
stopForgingByAccount(config_Luna_Wallet.xln_t1_3)







