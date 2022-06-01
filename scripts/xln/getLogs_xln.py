import requests
import data
import config_Luna_Wallet

url = config_Luna_Wallet.xln_t1_1
ADMIN_PASSWORD = config_Luna_Wallet.ADMIN_PASSWORD_T1
#srakap p9 node

getLogs = {"": "%2Fapl", "requestType": "getLog", "adminPassword": ADMIN_PASSWORD}
response = requests.request("GET", url + "/api/rpc", headers=data.headers, params=getLogs)
print(response.json())



