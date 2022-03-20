import testNet2
import requests
import data
import testNet1
import testNet3
import testNetStage
tn2_Admin_Password = "12345"
tn3_Admin_Password = "1"

pass_admin = tn2_Admin_Password
"""getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", testNet2.peer2 + "/apl", headers=data.headers, params=getForging)
print(response.json())
"""
getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", testNet2.peer2 + "/apl", headers=data.headers, params=getForging)
print(response.json())

getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", testNet2.peer3 + "/apl", headers=data.headers, params=getForging)
print(response.json())

getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", testNet2.peer4 + "/apl", headers=data.headers, params=getForging)
print(response.json())

getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", testNet2.peer5 + "/apl", headers=data.headers, params=getForging)
print(response.json())

getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", testNet2.peer6 + "/apl", headers=data.headers, params=getForging)
print(response.json())

getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", testNet2.peer7 + "/apl", headers=data.headers, params=getForging)
print(response.json())

"""getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": tn3_Admin_Password}
response = requests.request("GET", testNet3.peer8 + "/apl", headers=data.headers, params=getForging)
print(response.json())"""
