import requests
import data

xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

url = ([xln_t2_1])
#srakap p9 node

getLogs = {"": "%2Fapl", "requestType": "getLog", "adminPassword": "12345"}
response = requests.request("GET", xln_t2_1 + "/xln-api", headers=data.headers, params=getLogs)
print(response.json())



