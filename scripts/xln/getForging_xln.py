import requests
import data
import config_Luna_Wallet

url = config_Luna_Wallet.xln_mn_ALL
ADMIN_PASSWORD = config_Luna_Wallet.ADMIN_PASSWORD_T1

for peer in url:
    getForging = {"requestType": "getForging", "adminPassword": ADMIN_PASSWORD}
    response = requests.request("GET", peer + "/api/rpc",
                                params=getForging)
    print(peer + ":")
    print(response.json())
    print()


