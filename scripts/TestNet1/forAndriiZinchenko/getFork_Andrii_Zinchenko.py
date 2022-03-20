import requests
port = ":7876"
peer1 = "http://51.15.250.32" + port
peer2 = "http://51.15.253.171" + port
peer3 = "http://51.15.210.116" + port
#peer3 = "51.15.210.116"
peer4 = "http://51.15.242.197" + port
peer5 = "http://51.15.218.241" + port
peer6 = "http://51.15.130.37" + port
#peer7 = "51.15.46.49" + port  #mixer
peer8 = "http://51.15.102.159" + port #delphi


def getCurrentHeightTn():
                heightPeer1 = getCurrentHeight(peer1)
                heightPeer2 = getCurrentHeight(peer2)
                heightPeer3 = getCurrentHeight(peer3)
                heightPeer4 = getCurrentHeight(peer4)
                heightPeer5 = getCurrentHeight(peer5)
                heightPeer6 = getCurrentHeight(peer6)
                minHeight = min(heightPeer6, heightPeer3, heightPeer4, heightPeer1, heightPeer2, heightPeer5)
                print("min Height = " + str(minHeight) + " blocks")
                return minHeight


def getCurrentHeight(url):
    querystring = {"": "%2Fapl", "requestType": "getBlock"}
    response = requests.request("GET", url + "/apl", params=querystring)
    # print(response.json())
    if response:
        currentHeight = response.json()["height"]
        print("Current Height on " + url + " = " + str(currentHeight) + " blocks ")
        return currentHeight


def getBlockId(height, url):
    querystring = {"": "%2Fapl", "requestType": "getBlockId", "height": str(height)}
    response = requests.request("GET", url + "/apl", params=querystring)
    if response:
        blockId = response.json()["block"]
        print("Peer " + url + ": BlockId of " + str(height) + " = " + blockId + " ")
        return blockId


def getForkTn3():
    startHeight = getCurrentHeightTn()
    print(startHeight)
    print(" <<< ------- >>> ")
    peer1BlockId = getBlockId(startHeight, peer1)
    peer2BlockId = getBlockId(startHeight, peer2)
    peer3BlockId = getBlockId(startHeight, peer3)
    peer4BlockId = getBlockId(startHeight, peer4)
    peer5BlockId = getBlockId(startHeight, peer5)
    peer6BlockId = getBlockId(startHeight, peer6)
    print(" <<< ------- >>> ")
    while not peer6BlockId == peer3BlockId == peer4BlockId == peer2BlockId == peer1BlockId == peer5BlockId:
        startHeight = startHeight - 1
        peer1BlockId = getBlockId(startHeight, peer1)
        peer2BlockId = getBlockId(startHeight, peer2)
        peer3BlockId = getBlockId(startHeight, peer3)
        peer4BlockId = getBlockId(startHeight, peer4)
        peer5BlockId = getBlockId(startHeight, peer5)
        peer6BlockId = getBlockId(startHeight, peer6)
        print(" <<< ------- >>> ")


getForkTn3()

