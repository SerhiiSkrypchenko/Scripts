import requests

import random

xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

url = ([xln_t2_1])

def popOffByBlocks(url, blocks):
    print("---------- START POP OFF on --->>> " + url + " <<< ----")
    querystring = {"requestType": "popOff", "adminPassword": "12345", "numBlocks": str(blocks)}
    response = requests.request("POST", url + "/xln-api", params=querystring)
    print(response.text)
    print("--------END of POP OFF proccess on peer --->>> " + url + " <<< --------")

def popOffByHeight(url, height):
    print("---------- START POP OFF on --->>> " + url + " <<< ----")
    querystring = {"requestType": "popOff", "adminPassword": "12345", "height": str(height)}
    response = requests.request("POST", url + "/xln-api", params=querystring)
    print(response.text)
    print("--------END of POP OFF proccess on peer --->>> " + url + " <<< --------")

popOffByHeight(xln_t2_2, 1)

#popOffByBlocks(xln_t2_2, 6000)



