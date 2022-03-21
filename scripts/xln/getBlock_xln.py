import requests
import urllib3
urllib3.disable_warnings()

xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

def getBlock(url):
    querystring = {"": "%2Fapl", "requestType": "getBlock"}
    response = requests.request("GET", url + "/xln-api", params=querystring, verify=False)
    if response:
        print(response.json())
        currentHeight = response.json()["height"]
        print("Current Height on " + url + " = " + str(currentHeight) + " blocks ")

while True:
    getBlock(xln_t2_1)
    getBlock(xln_t2_2)
    getBlock(xln_t2_3)












