import requests
import config_Luna_Wallet


ADMIN_PASSWORD = config_Luna_Wallet.ADMIN_PASSWORD_T1


def stopForgingTn(url):
    print("----------------------------------------------------------------------")
    payload = {"requestType": "stopForging", "adminPassword": ADMIN_PASSWORD}
    response = requests.request("POST", url + "/api/rpc", params=payload)
    #print(response.request)
    #print(response.url)
    print(response.json())
    #print(response.text)
    print(" <<< ------------------  FORGING STOPPED ON " + url + " ---------------------- >>> ")

stopForgingTn(config_Luna_Wallet.xln_mn_1)
stopForgingTn(config_Luna_Wallet.xln_mn_2)
stopForgingTn(config_Luna_Wallet.xln_mn_3)
stopForgingTn(config_Luna_Wallet.xln_mn_4)
stopForgingTn(config_Luna_Wallet.xln_mn_5)
stopForgingTn(config_Luna_Wallet.xln_mn_6)
stopForgingTn(config_Luna_Wallet.xln_mn_7)






