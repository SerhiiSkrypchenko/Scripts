import testNet2
import requests
import data
import testNet1
import testNet3
tn2_Admin_Password = "12345"
tn3_Admin_Password = "1"

"""peer1 = "51.15.235.41" #no shards #apl-t1-1.testnet.apollowallet.org
peer2 = "51.15.69.39" #apl-t1-2.testnet.apollowallet.org
peer3 = "51.15.59.37" #apl-t1-3.testnet.apollowallet.org
peer4 = "51.15.114.68" #apl-t1-4.testnet.apollowallet.org
peer5 = "51.15.140.80" #apl-t1-5.testnet.apollowallet.org #wallet.test.apollowallet.org
peer6 = "51.15.100.44" #no shards #apl-t1-8.testnet.apollowallet.org
peer7 = "51.15.233.93" #apl-t1-9.testnet.apollowallet.org"""
#peer8 = "51.15.104.205" #apl-t1-6.testnet.apollowallet.org

peer1 = "https://apl-t1-1.testnet.apollowallet.org"
peer2 = "https://apl-t1-2.testnet.apollowallet.org"
peer3 = "https://apl-t1-3.testnet.apollowallet.org"
peer4 = "https://apl-t1-4.testnet.apollowallet.org"
peer5 = "https://apl-t1-5.testnet.apollowallet.org"
peer6 = "https://apl-t1-8.testnet.apollowallet.org"
peer7 = "https://apl-t1-9.testnet.apollowallet.org"
#peer8 = "https://apl-t1-6.testnet.apollowallet.org"
peer8 = "https://wallet.test.apollowallet.org"

pass_admin = tn2_Admin_Password
getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", "http://51.15.235.41:7876" + "/apl", headers=data.headers, params=getForging)
print(response.json())

getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", "http://51.15.69.39:7876" + "/apl", headers=data.headers, params=getForging)
print(response.json())

getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", "http://51.15.59.37:7876" + "/apl", headers=data.headers, params=getForging)
print(response.json())

getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", "http://51.15.114.68:7876" + "/apl", headers=data.headers, params=getForging)
print(response.json())

getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", "http://51.15.140.80:7876" + "/apl", headers=data.headers, params=getForging)
print(response.json())

getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", "http://51.15.100.44:7876" + "/apl", headers=data.headers, params=getForging)
print(response.json())

getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": pass_admin}
response = requests.request("GET", "http://51.15.233.93:7876" + "/apl", headers=data.headers, params=getForging)
print(response.json())

"""getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": tn3_Admin_Password}
response = requests.request("GET", testNet3.peer8 + "/apl", headers=data.headers, params=getForging)
print(response.json())"""
