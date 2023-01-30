import requests

balancer = "https://www.lunaonewallet.com"

ADMIN_PASSWORD = "12345"
#srakap p9 node

getLogs = {"": "%2Fapl", "requestType": "getLog", "adminPassword": ADMIN_PASSWORD}
response = requests.request("GET", balancer + "/api/rpc", params=getLogs)
print(response.json())



