import requests
import config_Luna_Wallet


url = config_Luna_Wallet.balancer
ADMIN_PASSWORD = config_Luna_Wallet.ADMIN_PASSWORD_T1
#srakap p9 node

getLogs = {"": "%2Fapl", "requestType": "getLog", "adminPassword": ADMIN_PASSWORD}
response = requests.request("GET", url + "/api/rpc", params=getLogs)
print(response.json())



