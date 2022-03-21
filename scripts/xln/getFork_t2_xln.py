import requests
port = ":7876"

xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

WRONG_HEIGHT = -1

known_peers = [xln_t2_1, xln_t2_2, xln_t2_3]
available_peers= []

def getCurrentHeightTn():
    minHeight = 1E12
    for peer in known_peers:
        peerHeight = getCurrentHeight(peer)
        if peerHeight != WRONG_HEIGHT:
            available_peers.append(peer)
            print("peer="+peer+" height="+str(peerHeight))
            minHeight = min(minHeight, peerHeight)

    print("min Height = " + str(minHeight) + " blocks")
    return minHeight


def getCurrentHeight(url):
    querystring = {"": "%2Fapl", "requestType": "getBlock"}
    try:
        response = requests.request("GET", url + "/xln-api", params=querystring)
        # print(response.json())
        if response:
            currentHeight = response.json()["height"]
            #print("Current Height on " + url + " = " + str(currentHeight) + " blocks ")
            return currentHeight
        else:
            return WRONG_HEIGHT
    except: #request.exceptions.ConnectionError:
        print("Error: occured on ",url);
        return WRONG_HEIGHT


def getBlockId(height, url):
    if height > 0:
        querystring = {"": "%2Fapl", "requestType": "getBlockId", "height": str(height)}
        try:
            response = requests.request("GET", url + "/xln-api", params=querystring)
            if response:
                blockId = response.json()["block"]
                print("Peer " + url + ": BlockId of " + str(height) + " = " + blockId + " ")
                return blockId
            else:
                return 0
        except:
            print("Error: occured on ",url);
            return 0
    else:
        print("Error request, wrong height=", height)
        return 0

def getForkTn2Xln():
    startHeight = getCurrentHeightTn()
    while startHeight != 0:
        print("start height = "+str(startHeight))
        print(" <<< ------- >>> ")
        blocks = []
        for peer in available_peers:
            blocks.append(getBlockId(startHeight, peer))
        print(" <<< ------- >>> ")
        prevId = blocks[0]
        for id in blocks:
            if prevId != id:
                startHeight = startHeight - 1
                break
        if prevId == id:
            #print(" <<< ------- >>> ")
            break

getForkTn2Xln()

