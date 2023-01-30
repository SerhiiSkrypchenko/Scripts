import testNet2
import requests
import data
import testNet1
import testNet3
#srakap p9 node

getLogs = {"": "%2Fapl", "requestType": "getLog", "adminPassword": "12345"}
response = requests.request("GET", testNet2.peer2 + "/apl", headers=data.headers, params=getLogs)
print(response.json())

"""getLogs = {"": "%2Fapl", "requestType": "getLog", "adminPassword": "1"}
response = requests.request("GET", testNet3.peer2 + "/apl", headers=data.headers, params=getLogs)
print(response.json())"""

