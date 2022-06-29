import requests
import config_Luna_Wallet


url = config_Luna_Wallet.xln_mn_ALL

#tn2 = 12345
#tn3 = 1
secretPhrase = "LunaInitAccount"
def stopForgingByAccount(url):
    print("----------------------------------------------------------------------")
    querystring = {"requestType": "stopForging", "secretPhrase": "1"}
    response = requests.request("POST", url + "/api/rpc", params=querystring)
    print(response.json())
    print(" <<< ------------------  FORGING STOPPED ON  " + url + "     ---------------------- >>> ")

stopForgingByAccount(config_Luna_Wallet.xln_mn_1)
stopForgingByAccount(config_Luna_Wallet.xln_mn_2)
stopForgingByAccount(config_Luna_Wallet.xln_mn_3)
stopForgingByAccount(config_Luna_Wallet.xln_mn_4)
stopForgingByAccount(config_Luna_Wallet.xln_mn_5)
stopForgingByAccount(config_Luna_Wallet.xln_mn_6)
stopForgingByAccount(config_Luna_Wallet.xln_mn_7)




