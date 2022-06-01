import requests
import config_Luna_Wallet

ADMIN_PASSWORD = config_Luna_Wallet.ADMIN_PASSWORD_T1

def fullReset(peer, adminPassword):
    fullReset = {"requestType": "fullReset", "adminPassword": adminPassword,
                    "deadline": "1440"}
    response_fullReset = requests.request("POST", peer + "/api/rpc", params=fullReset)
    print(response_fullReset.json())

fullReset(config_Luna_Wallet.xln_t1_4, ADMIN_PASSWORD)
