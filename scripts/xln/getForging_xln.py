import requests
import data

xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

tn2_Admin_Password = "12345"
tn3_Admin_Password = "1"

pass_admin = tn2_Admin_Password

getForging = {"requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", xln_t2_1 + "/xln-api", headers=data.headers, params=getForging)
print(response.json())

getForging = {"requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", xln_t2_2 + "/xln-api", headers=data.headers, params=getForging)
print(response.json())

getForging = {"requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", xln_t2_3 + "/xln-api", headers=data.headers, params=getForging)
print(response.json())


