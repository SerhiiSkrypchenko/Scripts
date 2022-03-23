import requests

xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

url = ([xln_t2_1])

def scanByBlocks(url, blocks, validate):
    print("---------- START SCAN on --->>> " + url + " <<< ----")
    querystring = {"requestType": "scan", "adminPassword": "12345", "numBlocks": str(blocks), "validate": validate}
    response = requests.request("POST", url + "/xln-api", params=querystring)
    print(response.text)
    print("--------END of SCAN proccess on peer --->>> " + url + " <<< --------")

def scanByHeight(url, height, validate):
    print("---------- START SCAN on --->>> " + url + " <<< ----")
    querystring = {"requestType": "scan", "adminPassword": "12345", "height": height, "validate": validate}
    response = requests.request("POST", url + "/xln-api", params=querystring)
    print(response.text)
    print("--------END of SCAN proccess on peer --->>> " + url + " <<< --------")

scanByHeight(xln_t2_2, 1100, True)





