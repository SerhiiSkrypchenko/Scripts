import requests
import config_Luna_Wallet


ADMIN_PASSWORD = config_Luna_Wallet.ADMIN_PASSWORD_T1


def stopForgingTn(url):
    print("----------------------------------------------------------------------")
    querystring = {"requestType": "stopForging", "adminPassword": ADMIN_PASSWORD}
    response = requests.request("POST", url + "/api/rpc", params=querystring)
    print(response.text)
    print(" <<< ------------------  FORGING STOPPED ON " + url + " ---------------------- >>> ")

#stopForgingTn(config_Luna_Wallet.xln_t1_1)
#stopForgingTn(config_Luna_Wallet.xln_t1_2)
#stopForgingTn(config_Luna_Wallet.xln_t1_3)
#stopForgingTn(config_Luna_Wallet.xln_t1_4)
stopForgingTn(config_Luna_Wallet.xln_t1_1)






