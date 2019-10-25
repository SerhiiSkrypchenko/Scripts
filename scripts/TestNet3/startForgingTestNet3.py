import requests
import random
import functions
import testNet3


def getForging(url):
    getForging = {"": "%2Fapl", "requestType": "getForging", "adminPassword": "1"}
    response = requests.request("GET", "http://" + url + "/apl", params=getForging)
    if response:
        print(response.json())
    # if response:
    # generators = response.json()["generators"]
    # print("Generators on " + url + " peer = " + str(generators))


#getForging(testNet1.peer1)
#getForging(testNet1.peer2)
#getForging(testNet1.peer3)
#getForging(testNet1.peer4)
#getForging(testNet1.peer5)
#getForging(testNet1.peer6)
#getForging(testNet1.peer7)


functions.startForgingTn(testNet3.t3, 1, 200)