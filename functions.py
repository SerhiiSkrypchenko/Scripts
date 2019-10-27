import random
import time

import requests
import testNet1
import testNet2
import testNet3
import data
import conf
import string
import json

def getCurrentHeight(url):
    querystring = {"": "%2Fapl", "requestType": "getBlock"}
    response = requests.request("GET", "http://" + url + "/apl", params=querystring)
    # print(response.json())
    if response:
        currentHeight = response.json()["height"]
        print("Current Height on " + url + " = " + str(currentHeight) + " blocks ")
        return currentHeight


def getCurrentHeightTn(tn):
    if tn == testNet1.t1:
        heightPeer1 = getCurrentHeight(testNet1.peer1)
        heightPeer2 = getCurrentHeight(testNet1.peer2)
        heightPeer3 = getCurrentHeight(testNet1.peer3)
        # heightPeer4 = getCurrentHeight(testNet1.peer4)
        heightPeer5 = getCurrentHeight(testNet1.peer5)
        heightPeer6 = getCurrentHeight(testNet1.peer6)
        heightPeer7 = getCurrentHeight(testNet1.peer7)
        minHeight = min(heightPeer1, heightPeer2, heightPeer3, heightPeer5, heightPeer6, heightPeer7)
        print("min Height = " + str(minHeight) + " blocks")
        return minHeight
    else:
        if tn == testNet2.t2:
            heightPeer1 = getCurrentHeight(testNet2.peer1)
            heightPeer2 = getCurrentHeight(testNet2.peer2)
            heightPeer3 = getCurrentHeight(testNet2.peer3)
            heightPeer4 = getCurrentHeight(testNet2.peer4)
            heightPeer5 = getCurrentHeight(testNet2.peer5)
            heightPeer6 = getCurrentHeight(testNet2.peer6)
            heightPeer7 = getCurrentHeight(testNet2.peer7)
            minHeight = min(heightPeer1, heightPeer2, heightPeer3, heightPeer4, heightPeer5, heightPeer6, heightPeer7)
            # minHeight = min(heightPeer1, heightPeer2, heightPeer5, heightPeer6, heightPeer7)
            print("min Height = " + str(minHeight) + " blocks")
            return minHeight
        else:
            heightPeer1 = getCurrentHeight(testNet3.peer1)
            heightPeer2 = getCurrentHeight(testNet3.peer2)
            heightPeer3 = getCurrentHeight(testNet3.peer3)
            heightPeer4 = getCurrentHeight(testNet3.peer4)
            # heightPeer5 = getCurrentHeight(testNet3.peer5)
            minHeight = min(heightPeer1, heightPeer2, heightPeer3, heightPeer4)
            print("min Height = " + str(minHeight) + " blocks")
            return minHeight


def getForkHeight(tn):
    def getForkTn1():
        startHeight = getCurrentHeightTn(tn)
        print(startHeight)
        print(" <<< ------- >>> ")
        peer1BlockId = getBlockId(startHeight, testNet1.peer1)
        peer2BlockId = getBlockId(startHeight, testNet1.peer2)
        peer3BlockId = getBlockId(startHeight, testNet1.peer3)
        # peer4BlockId = getBlockId(startHeight, testNet1.peer4)
        peer5BlockId = getBlockId(startHeight, testNet1.peer5)
        peer6BlockId = getBlockId(startHeight, testNet1.peer6)
        peer7BlockId = getBlockId(startHeight, testNet1.peer7)
        print(" <<< ------- >>> ")
        while not (peer2BlockId == peer3BlockId == peer5BlockId == peer6BlockId == peer7BlockId == peer1BlockId):
            # peer1BlockId == peer2BlockId == peer3BlockId == peer4BlockId == peer5BlockId == peer6BlockId == peer7BlockId:
            startHeight = startHeight - 1
            peer1BlockId = getBlockId(startHeight, testNet1.peer1)
            peer2BlockId = getBlockId(startHeight, testNet1.peer2)
            peer3BlockId = getBlockId(startHeight, testNet1.peer3)
            # peer4BlockId = getBlockId(startHeight, testNet1.peer4)
            peer5BlockId = getBlockId(startHeight, testNet1.peer5)
            peer6BlockId = getBlockId(startHeight, testNet1.peer6)
            peer7BlockId = getBlockId(startHeight, testNet1.peer7)
            print(" <<< ------- >>> ")

    def getForkTn2():
        startHeight = getCurrentHeightTn(tn)
        print(startHeight)
        print(" <<< ------- >>> ")
        peer1BlockId = getBlockId(startHeight, testNet2.peer1)
        peer2BlockId = getBlockId(startHeight, testNet2.peer2)
        peer3BlockId = getBlockId(startHeight, testNet2.peer3)
        peer4BlockId = getBlockId(startHeight, testNet2.peer4)
        peer5BlockId = getBlockId(startHeight, testNet2.peer5)
        peer6BlockId = getBlockId(startHeight, testNet2.peer6)
        peer7BlockId = getBlockId(startHeight, testNet2.peer7)
        print(" <<< ------- >>> ")
        while not (peer1BlockId == peer2BlockId == peer3BlockId == peer4BlockId == peer5BlockId == peer6BlockId == peer7BlockId):
                #peer1BlockId == peer2BlockId == peer4BlockId == peer6BlockId == peer5BlockId == peer7BlockId):
            #peer1BlockId == peer2BlockId == peer3BlockId == peer4BlockId == peer5BlockId == peer6BlockId == peer7BlockId
            startHeight = startHeight - 1
            peer1BlockId = getBlockId(startHeight, testNet2.peer1)
            peer2BlockId = getBlockId(startHeight, testNet2.peer2)
            peer3BlockId = getBlockId(startHeight, testNet2.peer3)
            peer4BlockId = getBlockId(startHeight, testNet2.peer4)
            peer5BlockId = getBlockId(startHeight, testNet2.peer5)
            peer6BlockId = getBlockId(startHeight, testNet2.peer6)
            peer7BlockId = getBlockId(startHeight, testNet2.peer7)
            print(" <<< ------- >>> ")

    def getForkTn3():
        startHeight = getCurrentHeightTn(tn)
        print(startHeight)
        print(" <<< ------- >>> ")
        peer1BlockId = getBlockId(startHeight, testNet3.peer1)
        peer2BlockId = getBlockId(startHeight, testNet3.peer2)
        peer3BlockId = getBlockId(startHeight, testNet3.peer3)
        peer4BlockId = getBlockId(startHeight, testNet3.peer4)
        # peer5BlockId = getBlockId(startHeight, testNet3.peer5)
        print(" <<< ------- >>> ")
        while not peer1BlockId == peer2BlockId == peer3BlockId == peer4BlockId:
            startHeight = startHeight - 1
            peer1BlockId = getBlockId(startHeight, testNet3.peer1)
            peer2BlockId = getBlockId(startHeight, testNet3.peer2)
            peer3BlockId = getBlockId(startHeight, testNet3.peer3)
            peer4BlockId = getBlockId(startHeight, testNet3.peer4)
            # peer5BlockId = getBlockId(startHeight, testNet3.peer5)
            print(" <<< ------- >>> ")

    if tn == testNet1.t1:
        getForkTn1()
    else:
        if tn == testNet2.t2:
            getForkTn2()
        else:
            getForkTn3()


def getBlockId(height, url):
    querystring = {"": "%2Fapl", "requestType": "getBlockId", "height": str(height)}
    response = requests.request("GET", "http://" + url + "/apl", params=querystring)
    if response:
        blockId = response.json()["block"]
        print("Peer " + url + ": BlockId of " + str(height) + " = " + blockId + " ")
        return blockId


def getBlockIdTn(height, tn):
    if tn == testNet1.t1:
        getBlockId(height, testNet1.peer1)
        getBlockId(height, testNet1.peer2)
        getBlockId(height, testNet1.peer3)
        getBlockId(height, testNet1.peer4)
        getBlockId(height, testNet1.peer5)
        getBlockId(height, testNet1.peer6)
        getBlockId(height, testNet1.peer7)
    else:
        if tn == testNet2.t2:
            getBlockId(height, testNet2.peer1)
            getBlockId(height, testNet2.peer2)
            getBlockId(height, testNet2.peer3)
            getBlockId(height, testNet2.peer4)
            getBlockId(height, testNet2.peer5)
            getBlockId(height, testNet2.peer6)
            getBlockId(height, testNet2.peer7)
        else:
            getBlockId(height, testNet3.peer1)
            getBlockId(height, testNet3.peer2)
            getBlockId(height, testNet3.peer3)
            getBlockId(height, testNet3.peer4)
            # getBlockId(height, testNet3.peer5)


def restShards(url):
    if url == testNet1.peer1 or url == testNet1.peer6:
        print(" <<< ---- !!!! NO SHARDS SHOULD BE !!!! ----- " + url + " ------------------------- >>> ")
    else:
        print("<<< --------- " + url + " -------------- >>>")

    blockChainStatus(url)
    response = requests.request("GET", "http://" + url + "/rest/shards")
    print(response.text)
    querystring = {"": "%2Fapl", "requestType": "getBlock"}
    response = requests.request("GET", "http://" + url + "/apl", params=querystring)
    if response:
        currentHeight = response.json()["height"]
        print("Current Height on " + url + " = " + str(currentHeight) + " blocks ")
    currentHeight = 0
    print("------------ END -----------")
    print("                            ")


def restShardsTn(tn):
    if tn == testNet1.t1:
        print("<<<<< --------- apl-t1-1.testnet.apollowallet.org ------- >>>>>>")
        # blockChainStatus(testNet1.peer1)
        restShards(testNet1.peer1)
        print("<<<<< --------- apl-t1-2.testnet.apollowallet.org ------- >>>>>>")
        restShards(testNet1.peer2)
        print("<<<<< --------- apl-t1-3.testnet.apollowallet.org ------- >>>>>>")
        restShards(testNet1.peer3)
        print("<<<<< --------- apl-t1-4.testnet.apollowallet.org ------- >>>>>>")
        restShards(testNet1.peer4)
        print("<<<<< --------- apl-t1-5.testnet.apollowallet.org #wallet.test.apollowallet.org ------- >>>>>>")
        restShards(testNet1.peer5)
        print("<<<<< --------- #apl-t2-8.testnet.apollowallet.org ------- >>>>>>")
        restShards(testNet1.peer6)
        print("<<<<< --------- #apl-t2-9.testnet.apollowallet.org ------- >>>>>>")
        restShards(testNet1.peer7)
    else:
        if tn == testNet2.t2:
            print("<<<<< --------- apl-t2-1.testnet2.testnet.apollowallet.org ------- >>>>>>")
            restShards(testNet2.peer1)
            print("<<<<< --------- apl-t2-4.testnet2.testnet.apollowallet.org ------- >>>>>>")
            restShards(testNet2.peer2)
            print("<<<<< --------- apl-t2-5.testnet2.testnet.apollowallet.org ------- >>>>>>")
            restShards(testNet2.peer3)
            print("<<<<< --------- apl-t2-2.testnet2.testnet.apollowallet.org ------- >>>>>>")
            restShards(testNet2.peer4)
            print("<<<<< --------- apl-t2-3.testnet2.testnet.apollowallet.org  ------- >>>>>>")
            restShards(testNet2.peer5)
            print("<<<<< --------- apl-t2-8.testnetapl-redesign.testnet2.apollowallet.org ------- >>>>>>")
            restShards(testNet2.peer6)
            print("<<<<< --------- apl-t2-0.testnet2apl-t2-0.testnet2.testnet.apollowallet.org apl-t2-9.testnetapl-exchange.testnet.apollowallet.org ------- >>>>>>")
            restShards(testNet2.peer7)
        else:
            restShards(testNet3.peer1)
            restShards(testNet3.peer2)
            restShards(testNet3.peer3)
            restShards(testNet3.peer4)
            restShards(testNet3.peer5)


def blockChainStatus(url):
    getBlockChainStatus = {"": "%2Fapl", "requestType": "getBlockchainStatus"}
    try:
        response = requests.request("GET", "http://" + url + "/apl", params=getBlockChainStatus)
        version = response.json()["version"]
        print("BACK END VERSION on " + url + " = " + version)

    except Exception as ex:
        print("Error: " + str(ex))


def startForgingTn(urls, fromAccount, toAccount):
    if urls == testNet1.t1:
        k = fromAccount
        for k in range(fromAccount, toAccount + 1):
            urls = random.choice(
                [testNet1.peer1, testNet1.peer2, testNet1.peer3, testNet1.peer4, testNet1.peer5, testNet1.peer6,
                 testNet1.peer7])
            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
            response = requests.request("GET", "http://" + urls + "/apl", params=getAccountId)
            # print(response.json())
            account = response.json()["account"]
            # print(str(account))
            startForging = {"requestType": "startForging", "secretPhrase": str(k), "sender": str(account),
                            "deadline": "1440"}
            response = requests.request("POST", "http://" + urls + "/apl", params=startForging)
            # print(response.text)
            print(str(k) + " request <<<< ------ Account " + account + " with secretPhrase " + str(
                k) + " on peer " + urls + " is started ------------- >>>>")
            k += 1
    else:
        if urls == testNet2.t2:
            k = fromAccount
            for k in range(fromAccount, toAccount + 1):
                peers = random.choice(urls)
                getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
                response = requests.request("GET", "http://" + peers + "/apl", params=getAccountId)
                # print(response.json())
                account = response.json()["account"]
                # print(str(account))
                startForging = {"requestType": "startForging", "secretPhrase": str(k), "sender": str(account),
                                "deadline": "1440"}
                response = requests.request("POST", "http://" + peers + "/apl", params=startForging)
                # print(response.text)
                print(str(k) + " request <<<< ------ Account " + account + " with secretPhrase " + str(
                    k) + " on peer " + peers + " is started ------------- >>>>")
                k += 1
        else:
            if urls == testNet3.t3:
                k = fromAccount
                for k in range(fromAccount, toAccount + 1):
                    urls = random.choice(
                        [testNet3.peer1, testNet3.peer2, testNet3.peer3, testNet3.peer4, testNet3.peer5])
                    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
                    response = requests.request("GET", "http://" + urls + "/apl", params=getAccountId)
                    # print(response.json())
                    account = response.json()["account"]
                    # print(str(account))
                    startForging = {"requestType": "startForging", "secretPhrase": str(k), "sender": str(account),
                                    "deadline": "1440"}
                    response = requests.request("POST", "http://" + urls + "/apl", params=startForging)
                    # print(response.text)
                    print(str(k) + " request <<<< ------ Account " + account + " with secretPhrase " + str(
                        k) + " on peer " + urls + " is started ------------- >>>>")
                    k += 1
            else:
                k = fromAccount
                for k in range(fromAccount, toAccount + 1):
                    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
                    response = requests.request("GET", "http://" + urls + "/apl", params=getAccountId)
                    # print(response.json())
                    account = response.json()["account"]
                    # print(str(account))
                    startForging = {"requestType": "startForging", "secretPhrase": str(k), "sender": str(account),
                                    "deadline": "1440"}
                    response = requests.request("POST", "http://" + urls + "/apl", params=startForging)
                    # print(response.text)
                    print(str(k) + " request <<<< ------ Account " + account + " with secretPhrase " + str(
                        k) + " on peer " + urls + " is started ------------- >>>>")
                    k += 1


def startForging(peer, fromAccount, toAccount):
    k = fromAccount
    for k in range(fromAccount, toAccount + 1):
        urls = random.choice(peer)
        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", "http://" + urls + "/apl", params=getAccountId)
        # print(response.json())
        account = response.json()["account"]
        # print(str(account))
        startForging = {"requestType": "startForging", "secretPhrase": str(k), "sender": str(account),
                        "deadline": "1440"}
        response = requests.request("POST", "http://" + urls + "/apl", params=startForging)
        # print(response.text)
        print(str(k) + " request <<<< ------ Account " + account + " with secretPhrase " + str(
            k) + " on peer " + urls + " is started ------------- >>>>")
        k += 1


def stopForgingTn(url):
    if url == testNet1.t1:
        print("----------------------------------------------------------------------")
        querystring = {"requestType": "stopForging", "adminPassword": "1"}
        response = requests.request("POST", "http://" + testNet1.peer1 + "/apl", params=querystring)
        print(response.text)
        print(" <<< ------------------  FORGING STOPPED ON " + testNet1.peer1 + "---------------------- >>> ")

        querystring = {"requestType": "stopForging", "adminPassword": "1"}
        response = requests.request("POST", "http://" + testNet1.peer2 + "/apl", params=querystring)
        print(response.text)
        print(" <<< ------------------  FORGING STOPPED ON " + testNet1.peer2 + "---------------------- >>> ")

        querystring = {"requestType": "stopForging", "adminPassword": "1"}
        response = requests.request("POST", "http://" + testNet1.peer3 + "/apl", params=querystring)
        print(response.text)
        print(" <<< ------------------  FORGING STOPPED ON " + testNet1.peer3 + "---------------------- >>> ")

        querystring = {"requestType": "stopForging", "adminPassword": "1"}
        response = requests.request("POST", "http://" + testNet1.peer4 + "/apl", params=querystring)
        print(response.text)
        print(" <<< ------------------  FORGING STOPPED ON " + testNet1.peer4 + "---------------------- >>> ")

        querystring = {"requestType": "stopForging", "adminPassword": "1"}
        response = requests.request("POST", "http://" + testNet1.peer5 + "/apl", params=querystring)
        print(response.text)
        print(" <<< ------------------  FORGING STOPPED ON " + testNet1.peer5 + "---------------------- >>> ")

        querystring = {"requestType": "stopForging", "adminPassword": "1"}
        response = requests.request("POST", "http://" + testNet1.peer6 + "/apl", params=querystring)
        print(response.text)
        print(" <<< ------------------  FORGING STOPPED ON " + testNet1.peer6 + "---------------------- >>> ")

        querystring = {"requestType": "stopForging", "adminPassword": "1"}
        response = requests.request("POST", "http://" + testNet1.peer7 + "/apl", params=querystring)
        print(response.text)
        print(" <<< ------------------  FORGING STOPPED ON " + testNet1.peer7 + "---------------------- >>> ")
    else:
        if url == testNet2.t2:
            print("----------------------------------------------------------------------")
            querystring = {"requestType": "stopForging", "adminPassword": "1"}
            response = requests.request("POST", "http://" + testNet2.peer1 + "/apl", params=querystring)
            print(response.text)
            print(" <<< ------------------  FORGING STOPPED ON " + testNet2.peer1 + "---------------------- >>> ")

            querystring = {"requestType": "stopForging", "adminPassword": "1"}
            response = requests.request("POST", "http://" + testNet2.peer2 + "/apl", params=querystring)
            print(response.text)
            print(" <<< ------------------  FORGING STOPPED ON " + testNet2.peer2 + "---------------------- >>> ")

            querystring = {"requestType": "stopForging", "adminPassword": "1"}
            response = requests.request("POST", "http://" + testNet2.peer3 + "/apl", params=querystring)
            print(response.text)
            print(" <<< ------------------  FORGING STOPPED ON " + testNet2.peer3 + "---------------------- >>> ")

            querystring = {"requestType": "stopForging", "adminPassword": "1"}
            response = requests.request("POST", "http://" + testNet2.peer4 + "/apl", params=querystring)
            print(response.text)
            print(" <<< ------------------  FORGING STOPPED ON " + testNet2.peer4 + "---------------------- >>> ")

            querystring = {"requestType": "stopForging", "adminPassword": "1"}
            response = requests.request("POST", "http://" + testNet2.peer5 + "/apl", params=querystring)
            print(response.text)
            print(" <<< ------------------  FORGING STOPPED ON " + testNet2.peer5 + "---------------------- >>> ")

            querystring = {"requestType": "stopForging", "adminPassword": "1"}
            response = requests.request("POST", "http://" + testNet2.peer6 + "/apl", params=querystring)
            print(response.text)
            print(" <<< ------------------  FORGING STOPPED ON " + testNet2.peer6 + "---------------------- >>> ")

            querystring = {"requestType": "stopForging", "adminPassword": "1"}
            response = requests.request("POST", "http://" + testNet2.peer7 + "/apl", params=querystring)
            print(response.text)
            print(" <<< ------------------  FORGING STOPPED ON " + testNet2.peer7 + "---------------------- >>> ")
        else:
            if url == testNet3.t3:
                print("----------------------------------------------------------------------")
                querystring = {"requestType": "stopForging", "adminPassword": "1"}
                response = requests.request("POST", "http://" + testNet3.peer1 + "/apl", params=querystring)
                print(response.text)
                print(" <<< ------------------  FORGING STOPPED ON " + testNet3.peer1 + "---------------------- >>> ")

                querystring = {"requestType": "stopForging", "adminPassword": "1"}
                response = requests.request("POST", "http://" + testNet3.peer2 + "/apl", params=querystring)
                print(response.text)
                print(" <<< ------------------  FORGING STOPPED ON " + testNet3.peer2 + "---------------------- >>> ")

                querystring = {"requestType": "stopForging", "adminPassword": "1"}
                response = requests.request("POST", "http://" + testNet3.peer3 + "/apl", params=querystring)
                print(response.text)
                print(" <<< ------------------  FORGING STOPPED ON " + testNet3.peer3 + "---------------------- >>> ")

                querystring = {"requestType": "stopForging", "adminPassword": "1"}
                response = requests.request("POST", "http://" + testNet3.peer4 + "/apl", params=querystring)
                print(response.text)
                print(" <<< ------------------  FORGING STOPPED ON " + testNet3.peer4 + "---------------------- >>> ")

                querystring = {"requestType": "stopForging", "adminPassword": "1"}
                response = requests.request("POST", "http://" + testNet3.peer5 + "/apl", params=querystring)
                print(response.text)
                print(" <<< ------------------  FORGING STOPPED ON " + testNet3.peer5 + "---------------------- >>> ")
            else:
                print("----------------------------------------------------------------------")
                querystring = {"requestType": "stopForging", "adminPassword": "1"}
                response = requests.request("POST", "http://" + url + "/apl", params=querystring)
                print(response.text)
                print(" <<< ------------------  FORGING STOPPED ON " + url + "---------------------- >>> ")


def orderTransactions(url):
    alive = True
    while alive:
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"

        }
        print("--------------------------- BUY APL for ETH ---------------------------------")
        payload = "offerType=0&pairCurrency=1&pairRate=200000&offerAmount=2000000000000&sender=7821792282123976600" \
                  "&passphrase" \
                  "=11&feeATM=200000000&amountOfTime=86400&walletAddress=0x3d81757ee49fda2af1b63ee8eb7ffa67ab4ef0ee"
        response = requests.request("POST", "http://" + url + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        # transaction1 = response.json()["transaction"]
        print("-----------------------------------------------------------------------------")
        print("--------------------------- BUY APL for ETH ---------------------------------")
        payload = "offerType=0&pairCurrency=1&pairRate=200000&offerAmount=3000000000000&sender=7821792282123976600" \
                  "&passphrase" \
                  "=11&feeATM=200000000&amountOfTime=86400&walletAddress=0x3d81757ee49fda2af1b63ee8eb7ffa67ab4ef0ee"
        response = requests.request("POST", "http://" + url + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        print("-----------------------------------------------------------------------------")
        print("--------------------------- SELL APL for ETH --------------------------------")
        payload = "offerType=1&pairCurrency=1&pairRate=200000&offerAmount=2000000000000&walletAddress" \
                  "=0x3d81757ee49fda2af1b63ee8eb7ffa67ab4ef0ee&sender=7821792282123976600&passphrase=11&feeATM" \
                  "=200000000" \
                  "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        # transaction2 = response.json()["transaction"]
        print("-----------------------------------------------------------------------------")
        print("--------------------------- SELL APL for ETH --------------------------------")
        payload = "offerType=1&pairCurrency=1&pairRate=200000&offerAmount=2000000000000&walletAddress" \
                  "=0x3d81757ee49fda2af1b63ee8eb7ffa67ab4ef0ee&sender=7821792282123976600" \
                  "&passphrase=11&feeATM=200000000" \
                  "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        print("-----------------------------------------------------------------------------")
        print("--------------------------- BUY APL for PAX --------------------------------")
        payload = "offerType=0&pairCurrency=2&pairRate=3000000&offerAmount=1000000000000&walletAddress" \
                  "=0x3d81757ee49fda2af1b63ee8eb7ffa67ab4ef0ee&sender=7821792282123976600&passphrase=11" \
                  "&feeATM=200000000" \
                  "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        # transaction3 = response.json()["transaction"]
        print("-----------------------------------------------------------------------------")
        print("--------------------------- BUY APL for PAX --------------------------------")
        payload = "offerType=0&pairCurrency=2&pairRate=4000000&offerAmount=1000000000000&walletAddress" \
                  "=0x3d81757ee49fda2af1b63ee8eb7ffa67ab4ef0ee&sender=7821792282123976600&passphrase=11" \
                  "&feeATM=200000000" \
                  "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        print("-----------------------------------------------------------------------------")
        print("--------------------------- SELL APL for PAX --------------------------------")
        payload = "offerType=1&pairCurrency=2&pairRate=5000000&offerAmount=1000000000000&walletAddress" \
                  "=0xd17ebebd28b1b26505787c5798b339cbdb31ff77&sender=7821792282123976600&passphrase=11" \
                  "&feeATM=200000000&amountOfTime=86400"
        response = requests.request("POST", "http://" + url + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        # transaction4 = response.json()["transaction"]
        print("-----------------------------------------------------------------------------")
        print("--------------------------- SELL APL for PAX --------------------------------")
        payload = "offerType=1&pairCurrency=2&pairRate=6000000&offerAmount=1000000000000&walletAddress" \
                  "=0xd17ebebd28b1b26505787c5798b339cbdb31ff77&sender=7821792282123976600&passphrase=11" \
                  "&feeATM=200000000" \
                  "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        print("-----------------------------------------------------------------------------")
        # cancelOrder(url, transaction1)
        print("--------------------------- Cancel <-- SELL APL for ETH --> --------------------------------")
        # cancelOrder(url, transaction2)
        print("-----------------------------------------------------------------------------")
        print("--------------------------- Cancel <-- BUY APL for PAX --> --------------------------------")
        # cancelOrder(url, transaction3)
        print("-----------------------------------------------------------------------------")
        print("--------------------------- Cancel <-- SELL APL for PAX --> --------------------------------")
        # cancelOrder(url, transaction4)
        print("-----------------------------------------------------------------------------")


def orderSellBuy(url, sleepTime):
    alive = True
    while alive:
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"

        }
        # ----------- SELL ORDERS -------------
        pairRate1 = str(random.randint(200000, 399999))
        print(pairRate1)
        pairRate2 = str(random.randint(400000, 699999))
        print(pairRate2)
        pairRate3 = str(random.randint(700000, 999999))
        print(pairRate3)
        print(" ->>>>> 1 <<<<<- APL-62W5-U29R-UL36-DHHGZ creates SELL order")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet8 + "&sender=" + conf.sender8 + "" \
                                                                                                                        "&passphrase=" + conf.account8PassPhrase + "&feeATM=200000000" \
                                                                                                                                                                   "&amountOfTime=86400"
        response = requests.request("POST", "http://" + random.choice(url) + "/rest/dex/offer", data=payload,
                                    headers=headers)
        print(response.text)
        time.sleep(sleepTime)

        # transaction2 = response.json()["transaction"]

        print(" ->>>>> 2 <<<<<-  APL-AHWS-NGBG-V4LK-8Q65T creates SELL order ")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate2 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet2 + "&sender=" + conf.sender2 + "" \
                                                                                                                        "&passphrase=" + conf.account2PassPhrase + "&feeATM=200000000" \
                                                                                                                                                                   "&amountOfTime=86400"
        response = requests.request("POST", "http://" + random.choice(url) + "/rest/dex/offer", data=payload,
                                    headers=headers)
        print(response.text)
        time.sleep(sleepTime)

        print(" --->>>> 3 <<<<<--- APL-62W5-U29R-UL36-DHHGZ creates SELL order ")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate3 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet7 + "&sender=" + conf.sender7 + "" \
                                                                                                                        "&passphrase=" + conf.account7PassPhrase + "&feeATM=200000000" \
                                                                                                                                                                   "&amountOfTime=86400"
        response = requests.request("POST", "http://" + random.choice(url) + "/rest/dex/offer", data=payload,
                                    headers=headers)
        print(response.text)
        time.sleep(sleepTime)

        # ----------- BUY ORDERS -------------
        print("----- BUY APL for ETH --> 1")
        payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=1000000000000&sender=" + conf.sender2 + "" \
                                                                                                                             "&passphrase" \
                                                                                                                             "=" + conf.account2PassPhrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + conf.wallet2 + ""
        response = requests.request("POST", "http://" + random.choice(url) + "/rest/dex/offer", data=payload,
                                    headers=headers)
        print(response.text)
        time.sleep(sleepTime)
        # transaction1 = response.json()["transaction"]

        print("------ BUY APL for ETH --> 2")
        payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate2 + "&offerAmount=1000000000000&sender=" + conf.sender7 + "" \
                                                                                                                             "&passphrase" \
                                                                                                                             "=" + conf.account7PassPhrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + conf.wallet7 + ""
        response = requests.request("POST", "http://" + random.choice(url) + "/rest/dex/offer", data=payload,
                                    headers=headers)
        print(response.text)
        time.sleep(sleepTime)

        print("------ BUY APL for ETH --> 3")
        payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate3 + "&offerAmount=1000000000000&sender=" + conf.sender8 + "" \
                                                                                                                             "&passphrase" \
                                                                                                                             "=" + conf.account8PassPhrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + conf.wallet8 + ""
        response = requests.request("POST", "http://" + random.choice(url) + "/rest/dex/offer", data=payload,
                                    headers=headers)
        print(response.text)
        time.sleep(sleepTime)


def orderBuySell(url, sleepTime, type):
    alive = True
    while alive:
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"

        }
        if type == 1:
            pairRate1 = str(random.randint(200000, 399999))
            print(pairRate1)
            pairRate2 = str(random.randint(400000, 699999))
            print(pairRate2)
            pairRate3 = str(random.randint(700000, 999999))
            print(pairRate3)
        else:
            pairRate1 = "333333"
            print(pairRate1)
            pairRate2 = "444444"
            print(pairRate2)
            pairRate3 = "555555"
            print(pairRate3)

        # ----------- BUY ORDERS -------------
        print("----- BUY APL for ETH --> 1")
        payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=1000000000000&sender=" + conf.sender2 + "" \
                                                                                                                             "&passphrase" \
                                                                                                                             "=" + conf.PassPhrase2 + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + conf.wallet2 + ""
        response = requests.request("POST", "http://" + random.choice(url) + "/rest/dex/offer", data=payload,
                                    headers=headers)

        print(response.text)
        time.sleep(sleepTime)
        # transaction1 = response.json()["transaction"]

        print("------ BUY APL for ETH --> 2")
        payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate2 + "&offerAmount=1000000000000&sender=" + conf.sender7 + "" \
                                                                                                                             "&passphrase" \
                                                                                                                             "=" + conf.PassPhrase7 + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + conf.wallet7 + ""
        response = requests.request("POST", "http://" + random.choice(url) + "/rest/dex/offer", data=payload,
                                    headers=headers)
        print(response.text)
        time.sleep(sleepTime)

        print("------ BUY APL for ETH --> 3")
        payload = "offerType=0&pairCurrency=1&pairRate=" + random.choice(
            url) + "&offerAmount=1000000000000&sender=" + conf.sender8 + "" \
                                                                         "&passphrase" \
                                                                         "=" + conf.PassPhrase8 + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + conf.wallet8 + ""
        response = requests.request("POST", "http://" + random.choice(url) + "/rest/dex/offer", data=payload,
                                    headers=headers)
        print(response.text)
        time.sleep(sleepTime)

        print(" ->>>>> 1 <<<<<- APL-62W5-U29R-UL36-DHHGZ creates SELL order")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet8 + "&sender=" + conf.sender8 + "" \
                                                                                                                        "&passphrase=" + conf.PassPhrase8 + "&feeATM=200000000" \
                                                                                                                                                            "&amountOfTime=86400"
        response = requests.request("POST", "http://" + random.choice(url) + "/rest/dex/offer", data=payload,
                                    headers=headers)
        print(response.text)
        time.sleep(sleepTime)

        # transaction2 = response.json()["transaction"]

        print(" ->>>>> 2 <<<<<-  APL-AHWS-NGBG-V4LK-8Q65T creates SELL order ")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate2 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet2 + "&sender=" + conf.sender2 + "" \
                                                                                                                        "&passphrase=" + conf.PassPhrase2 + "&feeATM=200000000" \
                                                                                                                                                            "&amountOfTime=86400"
        response = requests.request("POST", "http://" + random.choice(url) + "/rest/dex/offer", data=payload,
                                    headers=headers)
        print(response.text)
        time.sleep(sleepTime)

        print(" --->>>> 3 <<<<<--- APL-62W5-U29R-UL36-DHHGZ creates SELL order ")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate3 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet7 + "&sender=" + conf.sender7 + "" \
                                                                                                                        "&passphrase=" + conf.PassPhrase7 + "&feeATM=200000000" \
                                                                                                                                                            "&amountOfTime=86400"
        response = requests.request("POST", "http://" + random.choice(url) + "/rest/dex/offer", data=payload,
                                    headers=headers)
        print(response.text)
        time.sleep(sleepTime)


def orderBuySellSeveralMatching(url1, url2, sleepTime):
    alive = True
    while alive:
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"

        }
        # ----------- SELL ORDERS -------------
        pairRate1 = str(random.randint(200000, 399999))
        # pairRate1 = "333333"
        print(pairRate1)
        pairRate2 = str(random.randint(400000, 699999))
        # pairRate2 = "444444"
        print(pairRate2)
        pairRate3 = str(random.randint(700000, 999999))
        # pairRate3 = "555555"
        print(pairRate3)

        # ----------- BUY ORDERS -------------
        print("----- BUY APL for ETH --> 1")
        payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=1000000000000&sender=" + conf.sender2 + "" \
                                                                                                                             "&passphrase" \
                                                                                                                             "=" + conf.account2PassPhrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + conf.wallet2 + ""
        response = requests.request("POST", "http://" + url2 + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        time.sleep(sleepTime)
        # transaction1 = response.json()["transaction"]

        print("------ BUY APL for ETH --> 2")
        payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate2 + "&offerAmount=1000000000000&sender=" + conf.sender7 + "" \
                                                                                                                             "&passphrase" \
                                                                                                                             "=" + conf.account7PassPhrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + conf.wallet7 + ""
        response = requests.request("POST", "http://" + url1 + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        time.sleep(sleepTime)

        print("------ BUY APL for ETH --> 3")
        payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate3 + "&offerAmount=1000000000000&sender=" + conf.sender8 + "" \
                                                                                                                             "&passphrase" \
                                                                                                                             "=" + conf.account8PassPhrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + conf.wallet8 + ""
        response = requests.request("POST", "http://" + url1 + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        time.sleep(sleepTime)

        print(" ->>>>> 1 <<<<<- APL-62W5-U29R-UL36-DHHGZ creates SELL order")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet8 + "&sender=" + conf.sender8 + "" \
                                                                                                                        "&passphrase=" + conf.account8PassPhrase + "&feeATM=200000000" \
                                                                                                                                                                   "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url1 + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        time.sleep(sleepTime)
        print(" ->>>>> 1 <<<<<- APL-62W5-U29R-UL36-DHHGZ creates SELL order")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet8 + "&sender=" + conf.sender8 + "" \
                                                                                                                        "&passphrase=" + conf.account8PassPhrase + "&feeATM=200000000" \
                                                                                                                                                                   "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url1 + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        time.sleep(sleepTime)
        print(" ->>>>> 1 <<<<<- APL-62W5-U29R-UL36-DHHGZ creates SELL order")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet8 + "&sender=" + conf.sender8 + "" \
                                                                                                                        "&passphrase=" + conf.account8PassPhrase + "&feeATM=200000000" \
                                                                                                                                                                   "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url1 + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        time.sleep(sleepTime)

        # transaction2 = response.json()["transaction"]

        print(" ->>>>> 2 <<<<<-  APL-AHWS-NGBG-V4LK-8Q65T creates SELL order ")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate2 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet2 + "&sender=" + conf.sender2 + "" \
                                                                                                                        "&passphrase=" + conf.account2PassPhrase + "&feeATM=200000000" \
                                                                                                                                                                   "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url2 + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        time.sleep(sleepTime)
        print(" ->>>>> 2 <<<<<-  APL-AHWS-NGBG-V4LK-8Q65T creates SELL order ")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate2 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet2 + "&sender=" + conf.sender2 + "" \
                                                                                                                        "&passphrase=" + conf.account2PassPhrase + "&feeATM=200000000" \
                                                                                                                                                                   "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url2 + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        time.sleep(sleepTime)
        print(" ->>>>> 2 <<<<<-  APL-AHWS-NGBG-V4LK-8Q65T creates SELL order ")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate2 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet2 + "&sender=" + conf.sender2 + "" \
                                                                                                                        "&passphrase=" + conf.account2PassPhrase + "&feeATM=200000000" \
                                                                                                                                                                   "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url2 + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        time.sleep(sleepTime)

        print(" --->>>> 3 <<<<<--- APL-62W5-U29R-UL36-DHHGZ creates SELL order ")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate3 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet7 + "&sender=" + conf.sender7 + "" \
                                                                                                                        "&passphrase=" + conf.account7PassPhrase + "&feeATM=200000000" \
                                                                                                                                                                   "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url2 + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        time.sleep(sleepTime)
        print(" --->>>> 3 <<<<<--- APL-62W5-U29R-UL36-DHHGZ creates SELL order ")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate3 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet7 + "&sender=" + conf.sender7 + "" \
                                                                                                                        "&passphrase=" + conf.account7PassPhrase + "&feeATM=200000000" \
                                                                                                                                                                   "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url2 + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        time.sleep(sleepTime)
        print(" --->>>> 3 <<<<<--- APL-62W5-U29R-UL36-DHHGZ creates SELL order ")
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate3 + "&offerAmount=1000000000000&walletAddress" \
                                                                       "=" + conf.wallet7 + "&sender=" + conf.sender7 + "" \
                                                                                                                        "&passphrase=" + conf.account7PassPhrase + "&feeATM=200000000" \
                                                                                                                                                                   "&amountOfTime=86400"
        response = requests.request("POST", "http://" + url2 + "/rest/dex/offer", data=payload, headers=headers)
        print(response.text)
        time.sleep(sleepTime)


def cancelOrder(url, orderId, sender, passphrase):
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }
    print("--------------------------- Cancel " + orderId + " --------------------")
    payload = "orderId=" + str(orderId) + "&sender=" + sender + "&" \
                                                                "passphrase=" + passphrase + "&" \
                                                                                             "feeATM=100000000"
    response = requests.request("POST", "http://" + url + "/rest/dex/offer" + "/cancel", data=payload, headers=headers)
    print(response.json())


def sendMoneyPhased(recipient, amountATM, secretPhrase, feeATM, sender, phasingFinishHeight):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "1440",
            "sender": sender, "phasingFinishHeight": phasingFinishHeight, "phased": "true", "phasingVotingModel": "1",
            "phasingQuorum": "1"}


def phasedTransactions(url):
    alive = True
    while alive:
        querystring = {"": "%2Fapl", "requestType": "getBlock"}
        response = requests.request("GET", "http://" + url + "/apl", params=querystring)
        print(response.text)
        currentHeight = response.json()["height"]
        #finishHeight = 300001
        finishHeight = currentHeight + 10000
        print("-----------------------------------------------------")
        print("Current Height = " + str(currentHeight))
        print("Finish Height = " + str(finishHeight))
        print("-----------------------------------------------------")
        k = 1
        for k in range(1, 201):
            print(k)
            print("-------------")
            i = random.randint(1, 200)
            p = random.randint(1, 200)
            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
            response = requests.request("GET",
                                        "http://" + url + "/apl",
                                        params=getAccountId)
            accountReceive = response.json()["accountRS"]
            print(str("accountReceive = " + accountReceive))
            print("------------------------------")

            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
            response = requests.request("GET",
                                        "http://" + url + "/apl",
                                        params=getAccountId)
            accountSender = response.json()["accountRS"]
            sender = response.json()["account"]
            print(str("---> accountSender => " + accountSender + "<<< --- "))
            print(str("---> account => " + sender + "<<< --- "))
            print("------------------------------")

            response = requests.request("POST",
                                        "http://" + url + "/apl",
                                        params=sendMoneyPhased(str(accountReceive),
                                                               str(random.randint(2000000000, 200000000000)),
                                                               str(p),
                                                               "3300000000",
                                                               sender,
                                                               str(finishHeight)))

            print(response.json())
            print("----------------------------------------------------------------------------------------------")
            k += 1
            time.sleep(0)


def aliasTransactions(url):
    alive = True
    while alive:
        k = 1
        for k in range(1, 201):
            print(k)
            print("-------------")
            i = random.randint(1, 200)
            p = random.randint(1, 200)

            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
            response = requests.request("GET",
                                        "http://" + url + "/apl",
                                        params=getAccountId)
            print(response.json())
            accountReceive = response.json()["accountRS"]
            print("-------------")
            print(str("accountReceive = " + accountReceive))
            print("-------------")

            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
            response = requests.request("GET",
                                        "http://" + url + "/apl",
                                        params=getAccountId)
            print(response.json())
            accountSender = response.json()["accountRS"]
            sender = response.json()["account"]
            print("-------------")
            print(str("accountSender = " + accountSender))
            print(str("account = " + sender))
            print(
                "------------------------------------------ CREATING ALIAS #1 ----------------------------------------")
            aliasname = "A" + str(random.randint(1, 10000))
            createAliasURL = {"requestType": "setAlias", "aliasName": aliasname,
                              "feeATM": "2500000000",
                              "aliasURI": "www.destroy" + str(random.randint(1, 30)) + ".com",
                              "secretPhrase": str(p),
                              "sender": accountSender,
                              "deadline": "1440"}
            response = requests.request("POST", "http://" + url + "/apl", params=createAliasURL)
            print(response.text)
            alias = response.json()["transaction"]
            print(alias)
            print(
                "----------------------------------- END OF CREATING ALIAS #1 ----------------------------------------")
            print(
                "------------------------------------------ CREATING ALIAS #2 ----------------------------------------")
            aliasname1 = "B" + str(random.randint(1, 10000))
            createAliasURL1 = {"requestType": "setAlias", "aliasName": aliasname1,
                               "feeATM": "2500000000",
                               "aliasURI": str(accountReceive),
                               "secretPhrase": str(p),
                               "sender": accountSender,
                               "deadline": "1440"}
            response = requests.request("POST", "http://" + url + "/apl", params=createAliasURL1)
            print(response.text)
            print(
                "----------------------------------- END OF CREATING ALIAS #2 ----------------------------------------")
            print(
                "------------------------------------------ CREATING ALIAS #3 ----------------------------------------")
            aliasname2 = "C" + str(random.randint(1, 10000))
            createAliasURL2 = {"requestType": "setAlias", "aliasName": aliasname2,
                               "feeATM": "2500000000",
                               "aliasURI": "DATA" + str(random.randint(1, 20)),
                               "secretPhrase": str(p),
                               "sender": accountSender,
                               "deadline": "1440"}
            response = requests.request("POST", "http://" + url + "/apl", params=createAliasURL2)
            print(response.text)
            print(
                "----------------------------------- END OF CREATING ALIAS #3 ----------------------------------------")
            print("----------------------------------- DELETING " + alias + " ----------------------------------------")

            deleteAlias = {"0": "1", "1": "2", "2": "0", "3": "9", "4": "9", "5": "3", "6": "6", "7": "5", "8": "0",
                           "9": "7", "10": "3", "11": "8", "12": "2", "13": "7", "14": "1", "15": "9", "16": "1",
                           "17": "7", "18": "2", "19": "0",
                           "alias": str(alias),
                           "feeATM": "2500000000",
                           "secretPhrase": str(p),
                           "sender": accountSender,
                           "deadline": "1440",
                           "priceATM": "0",
                           "requestType": "deleteAlias"}
            response = requests.request("POST", "http://" + url + "/apl", params=deleteAlias)
            print(response.json())
            print(
                "--------------------------------- DELETING " + alias + " IS FINISHED --------------------------------")
            while "errorDescription" in response.json():
                deleteAlias = {"0": "1", "1": "2", "2": "0", "3": "9", "4": "9", "5": "3", "6": "6", "7": "5",
                               "8": "0",
                               "9": "7", "10": "3", "11": "8", "12": "2", "13": "7", "14": "1", "15": "9",
                               "16": "1",
                               "17": "7", "18": "2", "19": "0",
                               "alias": str(alias),
                               "feeATM": "2500000000",
                               "secretPhrase": str(p),
                               "sender": accountSender,
                               "deadline": "1440",
                               "priceATM": "0",
                               "requestType": "deleteAlias"}
                response = requests.request("POST", "http://" + url + "/apl", params=deleteAlias)
                print(response.json())
                time.sleep(20)
                print(
                    "---------------------------------- DELETING " + alias + " IS FINISHED --------------------------")

            print(
                "-------------------------- TRANSFER " + aliasname + "----------------------------------")
            transferAlias = {"0": "1", "1": "2", "2": "6", "3": "5", "4": "3", "5": "0", "6": "5", "7": "5",
                             "8": "2",
                             "9": "3", "10": "4", "11": "5", "12": "1", "13": "5", "14": "2", "15": "0", "16": "4",
                             "17": "9",
                             "18": "7", "19": "0",
                             "requestType": "sellAlias",
                             "recipient": str(accountReceive),
                             "feeATM": "3000000000",
                             "add_message": "true",
                             "permanent_message": "false",
                             "priceATM": "0",
                             "aliasName": aliasname,
                             "secretPhrase": str(p),
                             "messageToEncrypt": "MESSAGE+TRANSFER+ALIAS",
                             "sender": accountSender,
                             "deadline": "1440"}
            response = requests.request("POST", "http://" + url + "/apl", params=transferAlias)
            print(response.json())
            print(
                "--------------------------  TRANSFER " + aliasname + " IS FINISHED  -----------------")
            while "errorDescription" in response.json():
                transferAlias = {"0": "1", "1": "2", "2": "6", "3": "5", "4": "3", "5": "0", "6": "5", "7": "5",
                                 "8": "2",
                                 "9": "3", "10": "4", "11": "5", "12": "1", "13": "5", "14": "2", "15": "0", "16": "4",
                                 "17": "9",
                                 "18": "7", "19": "0",
                                 "requestType": "sellAlias",
                                 "recipient": str(accountReceive),
                                 "feeATM": "3000000000",
                                 "add_message": "true",
                                 "permanent_message": "false",
                                 "priceATM": "0",
                                 "aliasName": aliasname,
                                 "secretPhrase": str(p),
                                 "messageToEncrypt": "MESSAGE+TRANSFER+ALIAS",
                                 "sender": accountSender,
                                 "deadline": "1440"}
                response = requests.request("POST", "http://" + url + "/apl", params=transferAlias)
                print(response.json())
                time.sleep(20)
                print(
                    "--------------------------------  TRANSFER " + aliasname + " IS FINISHED  ---------------------")
            k += 1


def aliasTransactionsTn(url):
    if url == testNet1.t1:
        alive = True
        while alive:
            k = 1
            for k in range(1, 201):
                print(k)
                print("-------------")
                i = random.randint(1, 200)
                p = random.randint(1, 200)
                t1 = random.choice([testNet1.peer1, testNet1.peer2, testNet1.peer3, testNet1.peer4, testNet1.peer5])
                getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
                response = requests.request("GET",
                                            "http://" + t1 + "/apl",
                                            params=getAccountId)
                print(response.json())
                accountReceive = response.json()["accountRS"]
                print("-------------")
                print(str("accountReceive = " + accountReceive))
                print("-------------")

                getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
                response = requests.request("GET",
                                            "http://" + t1 + "/apl",
                                            params=getAccountId)
                print(response.json())
                accountSender = response.json()["accountRS"]
                sender = response.json()["account"]
                print("-------------")
                print(str("accountSender = " + accountSender))
                print(str("account = " + sender))
                print(
                    "------------------------------------------ CREATING ALIAS #1 -------------------------------")
                aliasname = "A" + str(random.randint(1, 10000))
                createAliasURL = {"requestType": "setAlias", "aliasName": aliasname,
                                  "feeATM": "2500000000",
                                  "aliasURI": "www.destroy" + str(random.randint(1, 30)) + ".com",
                                  "secretPhrase": str(p),
                                  "sender": accountSender,
                                  "deadline": "1440"}
                response = requests.request("POST", "http://" + t1 + "/apl", params=createAliasURL)
                print(response.text)
                alias = response.json()["transaction"]
                print(alias)
                print(
                    "--------PEER: " + t1 + " <<< -------- END OF CREATING ALIAS #1 -------------------")
                print(
                    "------------------------------------------ CREATING ALIAS #2 -----------------------------------")
                aliasname1 = "B" + str(random.randint(1, 10000))
                createAliasURL1 = {"requestType": "setAlias", "aliasName": aliasname1,
                                   "feeATM": "2500000000",
                                   "aliasURI": str(accountReceive),
                                   "secretPhrase": str(p),
                                   "sender": accountSender,
                                   "deadline": "1440"}
                response = requests.request("POST", "http://" + t1 + "/apl", params=createAliasURL1)
                print(response.text)
                print(
                    "-------- Peer: " + t1 + " <<< --- END OF CREATING ALIAS #2 ------------------------")
                print(
                    "------------------------------------------ CREATING ALIAS #3 --------------------------")
                aliasname2 = "C" + str(random.randint(1, 10000))
                createAliasURL2 = {"requestType": "setAlias", "aliasName": aliasname2,
                                   "feeATM": "2500000000",
                                   "aliasURI": "DATA" + str(random.randint(1, 20)),
                                   "secretPhrase": str(p),
                                   "sender": accountSender,
                                   "deadline": "1440"}
                response = requests.request("POST", "http://" + t1 + "/apl", params=createAliasURL2)
                print(response.text)
                print(
                    "----------------------------------- END OF CREATING ALIAS #3 ----------------------------------------")
                print(
                    "----------------------------------- DELETING " + alias + " ----------------------------------------")

                deleteAlias = {"0": "1", "1": "2", "2": "0", "3": "9", "4": "9", "5": "3", "6": "6", "7": "5", "8": "0",
                               "9": "7", "10": "3", "11": "8", "12": "2", "13": "7", "14": "1", "15": "9", "16": "1",
                               "17": "7", "18": "2", "19": "0",
                               "alias": str(alias),
                               "feeATM": "2500000000",
                               "secretPhrase": str(p),
                               "sender": accountSender,
                               "deadline": "1440",
                               "priceATM": "0",
                               "requestType": "deleteAlias"}
                response = requests.request("POST", "http://" + t1 + "/apl", params=deleteAlias)
                print(response.json())
                print(
                    "--------------------------------- DELETING " + alias + " IS FINISHED --------------------------------")
                while "errorDescription" in response.json():
                    deleteAlias = {"0": "1", "1": "2", "2": "0", "3": "9", "4": "9", "5": "3", "6": "6", "7": "5",
                                   "8": "0",
                                   "9": "7", "10": "3", "11": "8", "12": "2", "13": "7", "14": "1", "15": "9",
                                   "16": "1",
                                   "17": "7", "18": "2", "19": "0",
                                   "alias": str(alias),
                                   "feeATM": "2500000000",
                                   "secretPhrase": str(p),
                                   "sender": accountSender,
                                   "deadline": "1440",
                                   "priceATM": "0",
                                   "requestType": "deleteAlias"}
                    response = requests.request("POST", "http://" + t1 + "/apl", params=deleteAlias)
                    print(response.json())
                    print(
                        "---------------------------------- DELETING " + alias + " IS FINISHED --------------------------")

                print(
                    "-------------------------- TRANSFER " + aliasname + "----------------------------------")
                transferAlias = {"0": "1", "1": "2", "2": "6", "3": "5", "4": "3", "5": "0", "6": "5", "7": "5",
                                 "8": "2",
                                 "9": "3", "10": "4", "11": "5", "12": "1", "13": "5", "14": "2", "15": "0", "16": "4",
                                 "17": "9",
                                 "18": "7", "19": "0",
                                 "requestType": "sellAlias",
                                 "recipient": str(accountReceive),
                                 "feeATM": "3000000000",
                                 "add_message": "true",
                                 "permanent_message": "false",
                                 "priceATM": "0",
                                 "aliasName": aliasname,
                                 "secretPhrase": str(p),
                                 "messageToEncrypt": "MESSAGE+TRANSFER+ALIAS",
                                 "sender": accountSender,
                                 "deadline": "1440"}
                response = requests.request("POST", "http://" + t1 + "/apl", params=transferAlias)
                print(response.json())
                print(
                    "--------------------------  TRANSFER " + aliasname + " IS FINISHED  -----------------")
                while "errorDescription" in response.json():
                    transferAlias = {"0": "1", "1": "2", "2": "6", "3": "5", "4": "3", "5": "0", "6": "5", "7": "5",
                                     "8": "2",
                                     "9": "3", "10": "4", "11": "5", "12": "1", "13": "5", "14": "2", "15": "0",
                                     "16": "4",
                                     "17": "9",
                                     "18": "7", "19": "0",
                                     "requestType": "sellAlias",
                                     "recipient": str(accountReceive),
                                     "feeATM": "3000000000",
                                     "add_message": "true",
                                     "permanent_message": "false",
                                     "priceATM": "0",
                                     "aliasName": aliasname,
                                     "secretPhrase": str(p),
                                     "messageToEncrypt": "MESSAGE+TRANSFER+ALIAS",
                                     "sender": accountSender,
                                     "deadline": "1440"}
                    response = requests.request("POST", "http://" + t1 + "/apl", params=transferAlias)
                    print(response.json())
                    print(
                        "--------------------------------  TRANSFER " + aliasname + " IS FINISHED  ---------------------")
                k += 1
    else:
        if url == testNet2.t2:
            alive = True
            while alive:
                k = 1
                for k in range(1, 201):
                    print(k)
                    print("-------------")
                    i = random.randint(1, 200)
                    p = random.randint(1, 200)
                    t2 = random.choice(testNet2.t2)
                    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
                    response = requests.request("GET",
                                                "http://" + t2 + "/apl",
                                                params=getAccountId)
                    print(response.json())
                    accountReceive = response.json()["accountRS"]
                    print("-------------")
                    print(str("accountReceive = " + accountReceive))
                    print("-------------")

                    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
                    response = requests.request("GET",
                                                "http://" + t2 + "/apl",
                                                params=getAccountId)
                    print(response.json())
                    accountSender = response.json()["accountRS"]
                    sender = response.json()["account"]
                    print("-------------")
                    print(str("accountSender = " + accountSender))
                    print(str("account = " + sender))
                    print(
                        "------------------------------------------ CREATING ALIAS #1 -------------------------------")
                    aliasname = "A" + str(random.randint(1, 10000))
                    createAliasURL = {"requestType": "setAlias", "aliasName": aliasname,
                                      "feeATM": "2500000000",
                                      "aliasURI": "www.destroy" + str(random.randint(1, 30)) + ".com",
                                      "secretPhrase": str(p),
                                      "sender": accountSender,
                                      "deadline": "1440"}
                    response = requests.request("POST", "http://" + t2 + "/apl", params=createAliasURL)
                    print(response.text)
                    alias = response.json()["transaction"]
                    print(alias)
                    print(
                        "--------PEER: " + t2 + " <<< -------- END OF CREATING ALIAS #1 -------------------")
                    print(
                        "------------------------------------------ CREATING ALIAS #2 -----------------------------------")
                    aliasname1 = "B" + str(random.randint(1, 10000))
                    createAliasURL1 = {"requestType": "setAlias", "aliasName": aliasname1,
                                       "feeATM": "2500000000",
                                       "aliasURI": str(accountReceive),
                                       "secretPhrase": str(p),
                                       "sender": accountSender,
                                       "deadline": "1440"}
                    response = requests.request("POST", "http://" + t2 + "/apl", params=createAliasURL1)
                    print(response.text)
                    print(
                        "-------- Peer: " + t2 + " <<< --- END OF CREATING ALIAS #2 ------------------------")
                    print(
                        "------------------------------------------ CREATING ALIAS #3 --------------------------")
                    aliasname2 = "C" + str(random.randint(1, 10000))
                    createAliasURL2 = {"requestType": "setAlias", "aliasName": aliasname2,
                                       "feeATM": "2500000000",
                                       "aliasURI": "DATA" + str(random.randint(1, 20)),
                                       "secretPhrase": str(p),
                                       "sender": accountSender,
                                       "deadline": "1440"}
                    response = requests.request("POST", "http://" + t2 + "/apl", params=createAliasURL2)
                    print(response.text)
                    print(
                        "----------------------------------- END OF CREATING ALIAS #3 ----------------------------------------")
                    print(
                        "----------------------------------- DELETING " + alias + " ----------------------------------------")

                    deleteAlias = {"0": "1", "1": "2", "2": "0", "3": "9", "4": "9", "5": "3", "6": "6", "7": "5",
                                   "8": "0",
                                   "9": "7", "10": "3", "11": "8", "12": "2", "13": "7", "14": "1", "15": "9",
                                   "16": "1",
                                   "17": "7", "18": "2", "19": "0",
                                   "alias": str(alias),
                                   "feeATM": "2500000000",
                                   "secretPhrase": str(p),
                                   "sender": accountSender,
                                   "deadline": "1440",
                                   "priceATM": "0",
                                   "requestType": "deleteAlias"}
                    response = requests.request("POST", "http://" + t2 + "/apl", params=deleteAlias)
                    print(response.json())
                    print(
                        "--------------------------------- DELETING " + alias + " IS FINISHED --------------------------------")
                    while "errorDescription" in response.json():
                        deleteAlias = {"0": "1", "1": "2", "2": "0", "3": "9", "4": "9", "5": "3", "6": "6", "7": "5",
                                       "8": "0",
                                       "9": "7", "10": "3", "11": "8", "12": "2", "13": "7", "14": "1", "15": "9",
                                       "16": "1",
                                       "17": "7", "18": "2", "19": "0",
                                       "alias": str(alias),
                                       "feeATM": "2500000000",
                                       "secretPhrase": str(p),
                                       "sender": accountSender,
                                       "deadline": "1440",
                                       "priceATM": "0",
                                       "requestType": "deleteAlias"}
                        response = requests.request("POST", "http://" + t2 + "/apl", params=deleteAlias)
                        print(response.json())
                        time.sleep(20)
                        print(
                            "---------------------------------- DELETING " + alias + " IS FINISHED --------------------------")

                    print(
                        "-------------------------- TRANSFER " + aliasname + "----------------------------------")
                    transferAlias = {"0": "1", "1": "2", "2": "6", "3": "5", "4": "3", "5": "0", "6": "5", "7": "5",
                                     "8": "2",
                                     "9": "3", "10": "4", "11": "5", "12": "1", "13": "5", "14": "2", "15": "0",
                                     "16": "4",
                                     "17": "9",
                                     "18": "7", "19": "0",
                                     "requestType": "sellAlias",
                                     "recipient": str(accountReceive),
                                     "feeATM": "3000000000",
                                     "add_message": "true",
                                     "permanent_message": "false",
                                     "priceATM": "0",
                                     "aliasName": aliasname,
                                     "secretPhrase": str(p),
                                     "messageToEncrypt": "MESSAGE+TRANSFER+ALIAS",
                                     "sender": accountSender,
                                     "deadline": "1440"}
                    response = requests.request("POST", "http://" + t2 + "/apl", params=transferAlias)
                    print(response.json())
                    while "errorDescription" in response.json():
                        transferAlias = {"0": "1", "1": "2", "2": "6", "3": "5", "4": "3", "5": "0", "6": "5", "7": "5",
                                         "8": "2",
                                         "9": "3", "10": "4", "11": "5", "12": "1", "13": "5", "14": "2", "15": "0",
                                         "16": "4",
                                         "17": "9",
                                         "18": "7", "19": "0",
                                         "requestType": "sellAlias",
                                         "recipient": str(accountReceive),
                                         "feeATM": "3000000000",
                                         "add_message": "true",
                                         "permanent_message": "false",
                                         "priceATM": "0",
                                         "aliasName": aliasname,
                                         "secretPhrase": str(p),
                                         "messageToEncrypt": "MESSAGE+TRANSFER+ALIAS",
                                         "sender": accountSender,
                                         "deadline": "1440"}
                        response = requests.request("POST", "http://" + t2 + "/apl", params=transferAlias)
                        print(response.json())
                        time.sleep(20)
                        print(
                            "--------------------------------  TRANSFER " + aliasname + " IS FINISHED  ---------------------")
                    k += 1
        else:
            if url == testNet3.t3:
                alive = True
                while alive:
                    k = 1
                    for k in range(1, 201):
                        print(k)
                        print("-------------")
                        i = random.randint(1, 200)
                        p = random.randint(1, 200)
                        t3 = random.choice(
                            [testNet3.peer1, testNet3.peer2, testNet3.peer3, testNet3.peer4, testNet3.peer5])
                        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
                        response = requests.request("GET",
                                                    "http://" + t3 + "/apl",
                                                    params=getAccountId)
                        print(response.json())
                        accountReceive = response.json()["accountRS"]
                        print("-------------")
                        print(str("accountReceive = " + accountReceive))
                        print("-------------")

                        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
                        response = requests.request("GET",
                                                    "http://" + t3 + "/apl",
                                                    params=getAccountId)
                        print(response.json())
                        accountSender = response.json()["accountRS"]
                        sender = response.json()["account"]
                        print("-------------")
                        print(str("accountSender = " + accountSender))
                        print(str("account = " + sender))
                        print(
                            "------------------------------------------ CREATING ALIAS #1 -------------------------------")
                        aliasname = "A" + str(random.randint(1, 10000))
                        createAliasURL = {"requestType": "setAlias", "aliasName": aliasname,
                                          "feeATM": "2500000000",
                                          "aliasURI": "www.destroy" + str(random.randint(1, 30)) + ".com",
                                          "secretPhrase": str(p),
                                          "sender": accountSender,
                                          "deadline": "1440"}
                        response = requests.request("POST", "http://" + t3 + "/apl", params=createAliasURL)
                        print(response.text)
                        alias = response.json()["transaction"]
                        print(alias)
                        print(
                            "--------PEER: " + t3 + " <<< -------- END OF CREATING ALIAS #1 -------------------")
                        print(
                            "------------------------------------------ CREATING ALIAS #2 -----------------------------------")
                        aliasname1 = "B" + str(random.randint(1, 10000))
                        createAliasURL1 = {"requestType": "setAlias", "aliasName": aliasname1,
                                           "feeATM": "2500000000",
                                           "aliasURI": str(accountReceive),
                                           "secretPhrase": str(p),
                                           "sender": accountSender,
                                           "deadline": "1440"}
                        response = requests.request("POST", "http://" + t3 + "/apl", params=createAliasURL1)
                        print(response.text)
                        print(
                            "-------- Peer: " + t3 + " <<< --- END OF CREATING ALIAS #2 ------------------------")
                        print(
                            "------------------------------------------ CREATING ALIAS #3 --------------------------")
                        aliasname2 = "C" + str(random.randint(1, 10000))
                        createAliasURL2 = {"requestType": "setAlias", "aliasName": aliasname2,
                                           "feeATM": "2500000000",
                                           "aliasURI": "DATA" + str(random.randint(1, 20)),
                                           "secretPhrase": str(p),
                                           "sender": accountSender,
                                           "deadline": "1440"}
                        response = requests.request("POST", "http://" + t3 + "/apl", params=createAliasURL2)
                        print(response.text)
                        print(
                            "----------------------------------- END OF CREATING ALIAS #3 ----------------------------------------")
                        print(
                            "----------------------------------- DELETING " + alias + " ----------------------------------------")

                        deleteAlias = {"0": "1", "1": "2", "2": "0", "3": "9", "4": "9", "5": "3", "6": "6", "7": "5",
                                       "8": "0",
                                       "9": "7", "10": "3", "11": "8", "12": "2", "13": "7", "14": "1", "15": "9",
                                       "16": "1",
                                       "17": "7", "18": "2", "19": "0",
                                       "alias": str(alias),
                                       "feeATM": "2500000000",
                                       "secretPhrase": str(p),
                                       "sender": accountSender,
                                       "deadline": "1440",
                                       "priceATM": "0",
                                       "requestType": "deleteAlias"}
                        response = requests.request("POST", "http://" + t3 + "/apl", params=deleteAlias)
                        print(response.json())
                        print(
                            "--------------------------------- DELETING " + alias + " IS FINISHED --------------------------------")
                        while "errorDescription" in response.json():
                            deleteAlias = {"0": "1", "1": "2", "2": "0", "3": "9", "4": "9", "5": "3", "6": "6",
                                           "7": "5",
                                           "8": "0",
                                           "9": "7", "10": "3", "11": "8", "12": "2", "13": "7", "14": "1", "15": "9",
                                           "16": "1",
                                           "17": "7", "18": "2", "19": "0",
                                           "alias": str(alias),
                                           "feeATM": "2500000000",
                                           "secretPhrase": str(p),
                                           "sender": accountSender,
                                           "deadline": "1440",
                                           "priceATM": "0",
                                           "requestType": "deleteAlias"}
                            response = requests.request("POST", "http://" + t3 + "/apl", params=deleteAlias)
                            print(response.json())
                            print(
                                "---------------------------------- DELETING " + alias + " IS FINISHED --------------------------")

                        print(
                            "-------------------------- TRANSFER " + aliasname + "----------------------------------")
                        transferAlias = {"0": "1", "1": "2", "2": "6", "3": "5", "4": "3", "5": "0", "6": "5", "7": "5",
                                         "8": "2",
                                         "9": "3", "10": "4", "11": "5", "12": "1", "13": "5", "14": "2", "15": "0",
                                         "16": "4",
                                         "17": "9",
                                         "18": "7", "19": "0",
                                         "requestType": "sellAlias",
                                         "recipient": str(accountReceive),
                                         "feeATM": "3000000000",
                                         "add_message": "true",
                                         "permanent_message": "false",
                                         "priceATM": "0",
                                         "aliasName": aliasname,
                                         "secretPhrase": str(p),
                                         "messageToEncrypt": "MESSAGE+TRANSFER+ALIAS",
                                         "sender": accountSender,
                                         "deadline": "1440"}
                        response = requests.request("POST", "http://" + t3 + "/apl", params=transferAlias)
                        print(response.json())
                        print(
                            "--------------------------  TRANSFER " + aliasname + " IS FINISHED  -----------------")
                        while "errorDescription" in response.json():
                            transferAlias = {"0": "1", "1": "2", "2": "6", "3": "5", "4": "3", "5": "0", "6": "5",
                                             "7": "5",
                                             "8": "2",
                                             "9": "3", "10": "4", "11": "5", "12": "1", "13": "5", "14": "2", "15": "0",
                                             "16": "4",
                                             "17": "9",
                                             "18": "7", "19": "0",
                                             "requestType": "sellAlias",
                                             "recipient": str(accountReceive),
                                             "feeATM": "3000000000",
                                             "add_message": "true",
                                             "permanent_message": "false",
                                             "priceATM": "0",
                                             "aliasName": aliasname,
                                             "secretPhrase": str(p),
                                             "messageToEncrypt": "MESSAGE+TRANSFER+ALIAS",
                                             "sender": accountSender,
                                             "deadline": "1440"}
                            response = requests.request("POST", "http://" + t3 + "/apl", params=transferAlias)
                            print(response.json())
                            print(
                                "--------------------------------  TRANSFER " + aliasname + " IS FINISHED  ---------------------")
                        k += 1
            else:
                alive = True
                while alive:
                    k = 1
                    for k in range(1, 201):
                        print(k)
                        print("-------------")
                        i = random.randint(1, 200)
                        p = random.randint(1, 200)
                        t1 = random.choice(
                            [testNet1.peer1, testNet1.peer2, testNet1.peer3, testNet1.peer4, testNet1.peer5])
                        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
                        response = requests.request("GET",
                                                    "http://" + url + "/apl",
                                                    params=getAccountId)
                        print(response.json())
                        accountReceive = response.json()["accountRS"]
                        print("-------------")
                        print(str("accountReceive = " + accountReceive))
                        print("-------------")

                        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
                        response = requests.request("GET",
                                                    "http://" + url + "/apl",
                                                    params=getAccountId)
                        print(response.json())
                        accountSender = response.json()["accountRS"]
                        sender = response.json()["account"]
                        print("-------------")
                        print(str("accountSender = " + accountSender))
                        print(str("account = " + sender))
                        print(
                            "------------------------------------------ CREATING ALIAS #1 -------------------------------")
                        aliasname = "A" + str(random.randint(1, 10000))
                        createAliasURL = {"requestType": "setAlias", "aliasName": aliasname,
                                          "feeATM": "2500000000",
                                          "aliasURI": "www.destroy" + str(random.randint(1, 30)) + ".com",
                                          "secretPhrase": str(p),
                                          "sender": accountSender,
                                          "deadline": "1440"}
                        response = requests.request("POST", "http://" + url + "/apl", params=createAliasURL)
                        print(response.text)
                        alias = response.json()["transaction"]
                        print(alias)
                        print(
                            "--------PEER: " + t1 + " <<< -------- END OF CREATING ALIAS #1 -------------------")
                        print(
                            "------------------------------------------ CREATING ALIAS #2 -----------------------------------")
                        aliasname1 = "B" + str(random.randint(1, 10000))
                        createAliasURL1 = {"requestType": "setAlias", "aliasName": aliasname1,
                                           "feeATM": "2500000000",
                                           "aliasURI": str(accountReceive),
                                           "secretPhrase": str(p),
                                           "sender": accountSender,
                                           "deadline": "1440"}
                        response = requests.request("POST", "http://" + url + "/apl", params=createAliasURL1)
                        print(response.text)
                        print(
                            "-------- Peer: " + t1 + " <<< --- END OF CREATING ALIAS #2 ------------------------")
                        print(
                            "------------------------------------------ CREATING ALIAS #3 --------------------------")
                        aliasname2 = "C" + str(random.randint(1, 10000))
                        createAliasURL2 = {"requestType": "setAlias", "aliasName": aliasname2,
                                           "feeATM": "2500000000",
                                           "aliasURI": "DATA" + str(random.randint(1, 20)),
                                           "secretPhrase": str(p),
                                           "sender": accountSender,
                                           "deadline": "1440"}
                        response = requests.request("POST", "http://" + url + "/apl", params=createAliasURL2)
                        print(response.text)
                        print(
                            "----------------------------------- END OF CREATING ALIAS #3 ----------------------------------------")
                        print(
                            "----------------------------------- DELETING " + alias + " ----------------------------------------")

                        deleteAlias = {"0": "1", "1": "2", "2": "0", "3": "9", "4": "9", "5": "3", "6": "6", "7": "5",
                                       "8": "0",
                                       "9": "7", "10": "3", "11": "8", "12": "2", "13": "7", "14": "1", "15": "9",
                                       "16": "1",
                                       "17": "7", "18": "2", "19": "0",
                                       "alias": str(alias),
                                       "feeATM": "2500000000",
                                       "secretPhrase": str(p),
                                       "sender": accountSender,
                                       "deadline": "1440",
                                       "priceATM": "0",
                                       "requestType": "deleteAlias"}
                        response = requests.request("POST", "http://" + url + "/apl", params=deleteAlias)
                        print(response.json())
                        print(
                            "--------------------------------- DELETING " + alias + " IS FINISHED --------------------------------")
                        while "errorDescription" in response.json():
                            deleteAlias = {"0": "1", "1": "2", "2": "0", "3": "9", "4": "9", "5": "3", "6": "6",
                                           "7": "5",
                                           "8": "0",
                                           "9": "7", "10": "3", "11": "8", "12": "2", "13": "7", "14": "1", "15": "9",
                                           "16": "1",
                                           "17": "7", "18": "2", "19": "0",
                                           "alias": str(alias),
                                           "feeATM": "2500000000",
                                           "secretPhrase": str(p),
                                           "sender": accountSender,
                                           "deadline": "1440",
                                           "priceATM": "0",
                                           "requestType": "deleteAlias"}
                            response = requests.request("POST", "http://" + url + "/apl", params=deleteAlias)
                            print(response.json())
                            print(
                                "---------------------------------- DELETING " + alias + " IS FINISHED --------------------------")

                        print(
                            "-------------------------- TRANSFER " + aliasname + "----------------------------------")
                        transferAlias = {"0": "1", "1": "2", "2": "6", "3": "5", "4": "3", "5": "0", "6": "5", "7": "5",
                                         "8": "2",
                                         "9": "3", "10": "4", "11": "5", "12": "1", "13": "5", "14": "2", "15": "0",
                                         "16": "4",
                                         "17": "9",
                                         "18": "7", "19": "0",
                                         "requestType": "sellAlias",
                                         "recipient": str(accountReceive),
                                         "feeATM": "3000000000",
                                         "add_message": "true",
                                         "permanent_message": "false",
                                         "priceATM": "0",
                                         "aliasName": aliasname,
                                         "secretPhrase": str(p),
                                         "messageToEncrypt": "MESSAGE+TRANSFER+ALIAS",
                                         "sender": accountSender,
                                         "deadline": "1440"}
                        response = requests.request("POST", "http://" + url + "/apl", params=transferAlias)
                        print(response.json())
                        print(
                            "--------------------------  TRANSFER " + aliasname + " IS FINISHED  -----------------")
                        while "errorDescription" in response.json():
                            transferAlias = {"0": "1", "1": "2", "2": "6", "3": "5", "4": "3", "5": "0", "6": "5",
                                             "7": "5",
                                             "8": "2",
                                             "9": "3", "10": "4", "11": "5", "12": "1", "13": "5", "14": "2", "15": "0",
                                             "16": "4",
                                             "17": "9",
                                             "18": "7", "19": "0",
                                             "requestType": "sellAlias",
                                             "recipient": str(accountReceive),
                                             "feeATM": "3000000000",
                                             "add_message": "true",
                                             "permanent_message": "false",
                                             "priceATM": "0",
                                             "aliasName": aliasname,
                                             "secretPhrase": str(p),
                                             "messageToEncrypt": "MESSAGE+TRANSFER+ALIAS",
                                             "sender": accountSender,
                                             "deadline": "1440"}
                            response = requests.request("POST", "http://" + url + "/apl", params=transferAlias)
                            print(response.json())
                            print(
                                "--------------------------------  TRANSFER " + aliasname + " IS FINISHED  ---------------------")
                        k += 1


def assetTransactions(url):
    alive = True
    while alive:
        print("-------- ASSET CREATE ------------")
        assetName = "BEST" + str(random.randint(1, 99))
        # urls1 = random.choice([url])
        availableAssets = 10000
        createAsset = {"requestType": "issueAsset", "decimals": "1", "name": str(assetName),
                       "feeATM": "10000000000000",
                       "description": "destroy " + str(random.randint(1, 100)), "passphrase": "11",
                       "sender": "7821792282123976600", "deadline": "1440",
                       "quantityATU": str(availableAssets)}

        response = requests.request("POST", "http://" + url + "/apl", params=createAsset)
        print(response.json())
        assetID = response.json()["transaction"]
        print(response.status_code)
        print("assetID = " + assetID)
        print("-------- ASSET " + assetID + " IS CREATED --------")
        quantityATU = 100

        k = 0
        for k in range(0, 100):
            print("-----" + str(k) + "------")
            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
            response = requests.request("GET", "http://" + url + "/apl",
                                        params=getAccountId)
            # print(response.json())
            accountRS = response.json()["accountRS"]
            account = response.json()["account"]
            print("Recipient #" + str(k) + " IS " + str(accountRS))
            print("Recipient #" + str(k) + " IS " + str(account))
            print(
                "------ TRANSFER ASSET TO ---- >>>> " + str(accountRS) + " <<<<------>>>> " + str(account) + " <<< ---")

            transferAsset = {"decimals": "1", "sender": "7821792282123976600", "requestType": "transferAsset",
                             "quantityATU": quantityATU,
                             "assetID": str(assetID), "assetName": assetName,
                             "availableAssets": str(availableAssets - (quantityATU * k)),
                             "recipient": str(accountRS), "message": "transfer asset to " + str(accountRS),
                             "feeATM": "5000000000",
                             "asset": str(assetID), "passphrase": "11", "deadline": "1440"}
            response = requests.request("POST", "http://" + url + "/apl", params=transferAsset)
            print(response.text)
            while "errorDescription" in response.json():
                transferAsset = {"decimals": "1", "sender": "7821792282123976600", "requestType": "transferAsset",
                                 "quantityATU": quantityATU,
                                 "assetID": str(assetID), "assetName": assetName,
                                 "availableAssets": str(availableAssets - (quantityATU * k)),
                                 "recipient": str(accountRS), "message": "transfer asset to " + str(accountRS),
                                 "feeATM": "5000000000",
                                 "asset": str(assetID), "passphrase": "11", "deadline": "1440"}
                response = requests.request("POST", "http://" + url + "/apl", params=transferAsset)
                print(response.text)
                time.sleep(20)
            print(
                "------ TRANSFER ASSET TO ---- >>>> " + str(accountRS) + " <<<<------>>>> " + str(account) + " <<< ---")

            print("-------------------------------- >>>>>>> DELETING ASSET PROCCESS STARTED <<<<<<<< ---------")
            deleteAsset = {"requestType": "deleteAssetShares", "quantityATU": str(quantityATU), "assetID": str(assetID),
                           "decimals": "1", "assetName": assetName, "feeATM": "5000000000", "asset": str(assetID),
                           "sender": str(account), "secretPhrase": str(k), "deadline": "1440"}
            response = requests.request("POST", "http://" + url + "/apl", params=deleteAsset)
            print(response.text)
            print("----------- >>> DELETING ASSET FROM <<< --- >>> " + str(accountRS) + " <<< ---------")
            while "errorDescription" in response.json():
                deleteAsset = {"requestType": "deleteAssetShares", "quantityATU": str(quantityATU),
                               "assetID": str(assetID),
                               "decimals": "1", "assetName": assetName, "feeATM": "5000000000", "asset": str(assetID),
                               "sender": str(account), "secretPhrase": str(k), "deadline": "1440"}
                response = requests.request("POST", "http://" + url + "/apl", params=deleteAsset)
                print(response.text)
                print("----------- >>> DELETING ASSET FROM <<< --- >>> " + str(accountRS) + " <<< ---------")
                time.sleep(20)
        k += 1


def listProduct(url):
    alive = True
    while alive:
        listProduct = {"messageFile": "-1", "requestType": "dgsListing",
                       "tags": "Product" + str(random.randint(1, 30)),
                       "priceATM": "4000000000", "quantity": "10",
                       "description": "description%20of%20product%20for%20Sale",
                       "passphrase": "11",
                       "sender": "7821792282123976600", "deadline": "1440",
                       "name": "PICTURE" + str(random.randint(1, 100)),
                       "feeATM": "1000000000"}

        response = requests.request("POST", "http://" + random.choice(url) + "/apl", params=listProduct)
        print(response.text)
        time.sleep(20)
    return


def pollTransaction(url, finishHeight):
    alive = True
    while alive:
        poll = createPollByAccountId(url, finishHeight)
        pollBalance = createPollByBalance(url, finishHeight)

        k = 0
        for k in range(0, 200):
            def joinPollByAccountId(pollToJoin, secretPhrase, sender):
                querystring1 = {"0": "8", "1": "6", "2": "4", "3": "1", "4": "4", "5": "0", "6": "8", "7": "0",
                                "8": "3",
                                "9": "5",
                                "10": "2", "11": "1", "12": "3", "13": "8", "14": "2", "15": "0", "16": "6", "17": "4",
                                "18": "6",
                                "requestType": "castVote", "poll": str(pollToJoin),
                                "vote00": random.choice(["-128", "1"]),
                                "vote01": random.choice(["-128", "1"]),
                                "vote02": "1",
                                "feeATM": "100000000",
                                "secretPhrase": str(secretPhrase),
                                "sender": str(sender), "deadline": "1440"}
                response = requests.request("POST",
                                            "http://" + url + "/apl",
                                            params=querystring1)
                print(response.json())
                while "errorDescription" in response.json():
                    response = requests.request("POST",
                                                "http://" + url + "/apl",
                                                params=querystring1)
                    print(response.json())

            def joinPollByBalance(pollToJoinBalance, secretPhraseBalance, senderBalance):
                querystring2 = {"0": "1", "1": "6", "2": "5", "3": "7", "4": "9", "5": "9", "6": "5", "7": "9",
                                "8": "3",
                                "9": "6",
                                "10": "2", "11": "9", "12": "2", "13": "0", "14": "3", "15": "9", "16": "3", "17": "6",
                                "18": "9", "19": "8",
                                "requestType": "castVote", "poll": str(pollToJoinBalance),
                                "vote00": ["1"],
                                "vote01": random.choice(["-128", "1"]),
                                "vote02": random.choice(["-128", "1"]),
                                "feeATM": "100000000",
                                "secretPhrase": str(secretPhraseBalance),
                                "sender": str(senderBalance), "deadline": "1440"}

                response = requests.request("POST",
                                            "http://" + url + "/apl",
                                            params=querystring2)
                print(response.json())
                while "errorDescription" in response.json():
                    response = requests.request("POST",
                                                "http://" + url + "/apl",
                                                params=querystring2)
                    print(response.json())


            print(k)
            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
            response = requests.request("GET", "http://" + url + "/apl", params=getAccountId)
            print(response.text)
            account = response.json()["account"]
            print("----------->>> JOIN TO POLL BY ACCOUNT ID <<<------------")
            joinPollByAccountId(poll, k, account)
            time.sleep(3)
            print("----------->>> JOINING TO POLL BY ACCOUNT ID IS FINISHED <<<-------------")

            print("----------->>> JOIN TO POLL BY BALANCE <<<------------")
            joinPollByBalance(pollBalance, k, account)
            time.sleep(3)
            print("----------->>> JOINING TO POLL BY BALANCE IS FINISHED <<<-------------")
            k += 1


def createPollByAccountId(url, finishHeight):
    print("----- >>> CREATING POLL BY ACCOUNT ID <<< -----")
    pollByAccountId = {"name": "ApolloInFuture", "votingModel": "0", "finishHeight": str(finishHeight),
                       "minNumberOfOptions": "1",
                       "maxNumberOfOptions": "3", "minRangeValue": "0", "maxRangeValue": "2",
                       "feeATM": "1000000000",
                       "description": "Description+of+POLLNAME", "answers": ["YES", "NO", "PERHAPS"],
                       "create_poll_answers[]": "1",
                       "minBalanceModel": "0", "minBalanceType": "0", "option00": "1", "option01": "2",
                       "option02": "3",
                       "passphrase": "11", "sender": "7821792282123976600", "deadline": "1440",
                       "requestType": "createPoll",
                       "create_poll_answers%5B%5D": "1"}
    response = requests.request("POST",
                                "http://" + url + "/apl",
                                params=pollByAccountId)
    print(response.json())
    poll = response.json()["transaction"]
    print("poll by AccountID = " + str(poll))
    print("---- >>> POLL IS CREATED <<< ----")
    return (poll)


def createPollByBalance(url, finishHeight):
    print("---- >>> CREATING POLL BY ACCOUNT BALANCE <<< ----")
    pollByBalance = {"name": "ByBalance" + str(random.randint(1, 100)),
                     "votingModel": "1",
                     "minBalance": "10000",
                     "finishHeight": str(finishHeight),
                     "minNumberOfOptions": "1", "maxNumberOfOptions": "3", "minRangeValue": "0",
                     "maxRangeValue": "2",
                     "feeATM": "1000000000",
                     "description": "description: voting by Balance",
                     "answers": ["YES", "NO", "MAYBE"], "create_poll_answers[]": "YES", "minBalanceModel": "1",
                     "option00": "YES", "option01": "NO", "option02": "MAYBE", "passphrase": "11",
                     "sender": "7821792282123976600", "deadline": "1440", "requestType": "createPoll",
                     "create_poll_answers%5B%5D": "YES"}
    response = requests.request("POST",
                                "http://" + url + "/apl",
                                params=pollByBalance)
    print(response.text)
    pollBalance = response.json()["transaction"]
    print("poll by Account Balance " + str(pollBalance))
    print("---- >>> POLL IS CREATED <<< ----")
    return (pollBalance)


def referenced_Phased_Transactions(url):

    url = random.choice(url)
    querystring = {"": "%2Fapl", "requestType": "getBlock"}
    response = requests.request("GET", "http://" + url + "/apl", params=querystring)
    # print(response.text)
    currentHeight = response.json()["height"]
    print("Current Height = " + str(currentHeight))
    #finishHeight = 300001
    finishHeight = currentHeight + 10000
    print("Finish Height = " + str(finishHeight))

    response = requests.request("POST", "http://" + url + "/apl", data=data.payload,
                                headers=data.headers,
                                params=data.sendMoneyPhased(conf.account2,
                                                               str(random.randint(2000000000, 200000000000)),
                                                               conf.account1SecretPhrase,
                                                               "3300000000",
                                                               conf.sender1,
                                                               str(finishHeight)))


    #print(response.json())
    fullHash = response.json()["fullHash"]
    #print("fullHash = " + fullHash)
    alive = True
    while alive:
        k = 1
        for k in range(1, 201):
            print("<<<<< START >>>>>>")
            url = random.choice(testNet2.t2)
            print(k)
            print("URL = " + url)
            querystring = {"": "%2Fapl", "requestType": "getBlock"}
            response = requests.request("GET", "http://" + url + "/apl", params=querystring)
            # print(response.text)
            currentHeight = response.json()["height"]
            print("Current Height = " + str(currentHeight))
            #finish_Height = 299999
            finish_Height = finishHeight - 2000 - ( 30 * k )
            print("Finish_Height = " + str(finish_Height))

            i = random.randint(1, 200)
            p = random.randint(1, 200)
            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
            response = requests.request("GET",
                                        "http://" + url + "/apl",
                                        params=getAccountId)
            #print(response.json())
            accountReceive = response.json()["accountRS"]
            #print("-------------")
            print(str("accountReceive = " + accountReceive))
            #print("-------------")

            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
            response = requests.request("GET",
                                        "http://" + url + "/apl",
                                        params=getAccountId)
            #print(response.json())
            accountSender = response.json()["accountRS"]
            sender = response.json()["account"]
            #print("-------------")
            print(str("accountSender = " + accountSender))
            #print(str("account = " + sender))
            #print("-------------")

            response = requests.request("POST",
                                        "http://" + url + "/apl",
                                        params=data.sendMoney_Phased_Referenced(str(accountReceive),
                                                                                str(random.randint(2000000000,
                                                                                                   200000000000)),
                                                                                str(p),
                                                                                "3000000000",
                                                                                sender,
                                                                                finish_Height,
                                                                                fullHash))
            print(response.json())
            fullHash = response.json()["fullHash"]
            print("<<<<< END >>>>>")
            print()
            k += 1
            time.sleep(0)




def referencedSendMoneyTransactions(url):
    if url == testNet1.t1:
        response = requests.request("POST", "http://" + testNet1.peer2 + "/apl", data=data.payload,
                                    headers=data.headers,
                                    params=data.sendMoneyFromStandardWalletToVaultWallet(conf.account2, "20000000000",
                                                                                         conf.account1SecretPhrase,
                                                                                         "200000000",
                                                                                         conf.sender1))
        print(response.json())
        fullHash = response.json()["fullHash"]
        print("fullHash = " + fullHash)
        alive = True
        while alive:
            k = 1
            for k in range(1, 201):
                print(k)
                print("-------------")
                i = random.randint(1, 200)
                p = random.randint(1, 200)
                url = random.choice([testNet1.peer1, testNet1.peer2, testNet1.peer3, testNet1.peer4, testNet1.peer5])
                getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
                response = requests.request("GET",
                                            "http://" + url + "/apl",
                                            params=getAccountId)
                print(response.json())
                accountReceive = response.json()["accountRS"]
                print("-------------")
                print(str("accountReceive = " + accountReceive))
                print("-------------")

                getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
                response = requests.request("GET",
                                            "http://" + url + "/apl",
                                            params=getAccountId)
                print(response.json())
                accountSender = response.json()["accountRS"]
                sender = response.json()["account"]
                print("-------------")
                print(str("accountSender = " + accountSender))
                print(str("account = " + sender))
                print("-------------")

                response = requests.request("POST",
                                            "http://" + url + "/apl",
                                            params=data.sendMoneyReferenced(str(accountReceive),
                                                                            str(random.randint(2000000000,
                                                                                               200000000000)),
                                                                            str(p),
                                                                            "400000000",
                                                                            sender, fullHash))
                print(response.json())
                fullHash = response.json()["fullHash"]
                print("----------------------------------------------------------------------------------------------")
                k += 1
    else:
        if url == testNet2.t2:
            response = requests.request("POST", "http://" + testNet2.peer1 + "/apl", data=data.payload,
                                        headers=data.headers,
                                        params=data.sendMoneyFromStandardWalletToVaultWallet(conf.account2,
                                                                                             "20000000000",
                                                                                             conf.account1SecretPhrase,
                                                                                             "200000000",
                                                                                             conf.sender1))
            print(response.json())
            fullHash = response.json()["fullHash"]
            print("fullHash = " + fullHash)
            alive = True
            while alive:
                k = 1
                for k in range(1, 201):
                    print(k)
                    print("-------------")
                    i = random.randint(1, 200)
                    p = random.randint(1, 200)
                    url = random.choice(testNet2.t2)
                    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
                    response = requests.request("GET",
                                                "http://" + url + "/apl",
                                                params=getAccountId)
                    print(response.json())
                    accountReceive = response.json()["accountRS"]
                    print("-------------")
                    print(str("accountReceive = " + accountReceive))
                    print("-------------")

                    getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
                    response = requests.request("GET",
                                                "http://" + url + "/apl",
                                                params=getAccountId)
                    print(response.json())
                    accountSender = response.json()["accountRS"]
                    sender = response.json()["account"]
                    print("-------------")
                    print(str("accountSender = " + accountSender))
                    print(str("account = " + sender))
                    print("-------------")

                    response = requests.request("POST",
                                                "http://" + url + "/apl",
                                                params=data.sendMoneyReferenced(str(accountReceive),
                                                                                str(random.randint(2000000000,
                                                                                                   200000000000)),
                                                                                str(p),
                                                                                "400000000",
                                                                                sender, fullHash))
                    print(response.json())
                    fullHash = response.json()["fullHash"]
                    print(
                        "----------------------------------------------------------------------------------------------")
                    k += 1
                    time.sleep(0)
        else:
            if url == testNet3.t3:
                response = requests.request("POST", "http://" + testNet3.peer3 + "/apl", data=data.payload,
                                            headers=data.headers,
                                            params=data.sendMoneyFromStandardWalletToVaultWallet(conf.account2,
                                                                                                 "20000000000",
                                                                                                 conf.account1SecretPhrase,
                                                                                                 "200000000",
                                                                                                 conf.sender1))
                print(response.json())
                fullHash = response.json()["fullHash"]
                print("fullHash = " + fullHash)
                alive = True
                while alive:
                    k = 1
                    for k in range(1, 201):
                        print(k)
                        print("-------------")
                        i = random.randint(1, 200)
                        p = random.randint(1, 200)
                        url = random.choice(
                            [testNet3.peer1, testNet3.peer2, testNet3.peer3, testNet3.peer4, testNet3.peer5])
                        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
                        response = requests.request("GET",
                                                    "http://" + url + "/apl",
                                                    params=getAccountId)
                        print(response.json())
                        accountReceive = response.json()["accountRS"]
                        print("-------------")
                        print(str("accountReceive = " + accountReceive))
                        print("-------------")

                        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
                        response = requests.request("GET",
                                                    "http://" + url + "/apl",
                                                    params=getAccountId)
                        print(response.json())
                        accountSender = response.json()["accountRS"]
                        sender = response.json()["account"]
                        print("-------------")
                        print(str("accountSender = " + accountSender))
                        print(str("account = " + sender))
                        print("-------------")

                        response = requests.request("POST",
                                                    "http://" + url + "/apl",
                                                    params=data.sendMoneyReferenced(str(accountReceive),
                                                                                    str(random.randint(2000000000,
                                                                                                       200000000000)),
                                                                                    str(p),
                                                                                    "400000000",
                                                                                    sender, fullHash))
                        print(response.json())
                        fullHash = response.json()["fullHash"]
                        print(
                            "----------------------------------------------------------------------------------------------")
                        k += 1
            else:
                response = requests.request("POST", "http://" + url + "/apl", data=data.payload,
                                            headers=data.headers,
                                            params=data.sendMoneyFromStandardWalletToVaultWallet(conf.account2,
                                                                                                 "20000000000",
                                                                                                 conf.account1SecretPhrase,
                                                                                                 "200000000",
                                                                                                 conf.sender1))
                print(response.json())
                fullHash = response.json()["fullHash"]
                print("fullHash = " + fullHash)
                alive = True
                while alive:
                    k = 1
                    for k in range(1, 201):
                        print(k)
                        print("-------------")
                        i = random.randint(1, 200)
                        p = random.randint(1, 200)
                        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
                        response = requests.request("GET",
                                                    "http://" + url + "/apl",
                                                    params=getAccountId)
                        print(response.json())
                        accountReceive = response.json()["accountRS"]
                        print("-------------")
                        print(str("accountReceive = " + accountReceive))
                        print("-------------")

                        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
                        response = requests.request("GET",
                                                    "http://" + url + "/apl",
                                                    params=getAccountId)
                        print(response.json())
                        accountSender = response.json()["accountRS"]
                        sender = response.json()["account"]
                        print("-------------")
                        print(str("accountSender = " + accountSender))
                        print(str("account = " + sender))
                        print("-------------")

                        response = requests.request("POST",
                                                    "http://" + url + "/apl",
                                                    params=data.sendMoneyReferenced(str(accountReceive),
                                                                                    str(random.randint(2000000000,
                                                                                                       200000000000)),
                                                                                    str(p),
                                                                                    "400000000",
                                                                                    sender, fullHash))
                        print(response.json())
                        fullHash = response.json()["fullHash"]
                        print(
                            "----------------------------------------------------------------------------------------------")
                        k += 1


def popOff(url, height):
    print("---------- START POP OFF on --->>> " + url + " <<< ----")
    querystring = {"requestType": "popOff", "adminPassword": "1", "height": str(height)}
    response = requests.request("POST", "http://" + url + "/apl", params=querystring)
    print(response.text)
    print("--------END of POP OFF proccess on peer --->>> " + url + " <<< --------")


def sendMoneyToAccounts(url, numberOfAccounts):
    k = 1
    for k in range(1, numberOfAccounts + 1):
        print(k)
        print(" ----- SEND MONEY TO >>> " + str(k) + " <<<---- ACCOUNT --- ")

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET", "http://" + url + "/apl", headers=data.headers, params=getAccountId)
        print(response.json())
        account = response.json()["accountRS"]
        print("---- RECIPIENT ---- >>>> " + str(account))
        response = requests.request("POST", "http://" + url + "/apl", data=data.payload,
                                    headers=data.headers,
                                    params=data.sendMoneyFromStandardWalletToVaultWallet(str(account),
                                                                                         "1000000000000000",
                                                                                         conf.account1SecretPhrase,
                                                                                         "200000000",
                                                                                         conf.sender1))
        print(response.json())
        print("<<< -------- >>> FINISHED <<< ---------->>> ")
        k += 1


def sendMoneyToVaultWallet(url, numberOfAccounts):
    print(" ----- >>>> SENDING MONEY TO VAULT WALLETS <<<< ---- ")
    for i in range(0, 14):
        response = requests.request("POST", "http://" + url + "/apl", data=data.payload, headers=data.headers,
                                    params=data.sendMoneyFromStandardWalletToVaultWallet(conf.vaultAccounts[i],
                                                                                         "1000000000000000",
                                                                                         conf.account1SecretPhrase,
                                                                                         "200000000",
                                                                                         conf.sender1))
        print(response.json())
        print(" <<<< -------------------- >>>> ")
        i += 1


def id_generator(size=100, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def shufflingTransactions(participantCount, url):
    alive = True
    while alive:
        j = 1
        for j in range(1, 200):
            urls = random.choice(url)
            print(urls)

            response = requests.request("GET", "http://" + urls + "/apl", params={"": "%2Fapl",
                                                                                  "requestType": "getAccountId",
                                                                                  "secretPhrase": str(j)})

            account = response.json()["account"]
            # START SHUFFLING
            response = requests.request("POST", "http://" + urls + "/apl",
                                        params={"amount": random.randint(100000000000, 550000000000),
                                                "registrationPeriod": "1439",
                                                "participantCount": str(
                                                    participantCount),
                                                "feeATM": "5000000000",
                                                "secretPhrase": str(j),
                                                "sender": str(account),
                                                "deadline": "2000",
                                                "requestType": "shufflingCreate",
                                                "holdingType": "0"})
            shufflingFullHash = response.json()["fullHash"]
            print("shufflingFullHash = >>>> " + str(shufflingFullHash))
            j += 1
            k = 1
            for k in range(1, participantCount + 3):
                print(k)
                secretPhrase = id_generator()  # recipient secretPhrase generator

                response = requests.request("GET", "http://" + urls + "/apl", params={"": "%2Fapl",
                                                                                      "requestType": "getAccountId",
                                                                                      "secretPhrase": secretPhrase})
                publicKey = response.json()["publicKey"]

                response = requests.request("GET", "http://" + urls + "/apl", params={"": "%2Fapl",
                                                                                      "requestType": "getAccountId",
                                                                                      "secretPhrase": str(k)})
                account = response.json()["account"]

                # JOIN TO SHUFFLING
                response = requests.request("POST", "http://" + urls + "/apl",
                                            params={"requestType": "startShuffler",
                                                    "shufflingFullHash": shufflingFullHash,
                                                    "recipientSecretPhrase": secretPhrase, "secretPhrase": str(k),
                                                    "recipientPublicKey": publicKey,
                                                    "createNoneTransactionMethod": "true", "feeATM": "300000000",
                                                    "account": account,
                                                    "deadline": "1440"})
                print(response.text)
                print(" <<<< --------------------------------------------------------- >>>> ")
                k += 1
                time.sleep(0)


def sendMoneyPrunable(recipient, amountATM, secretPhrase, feeATM, sender):
    return {"requestType": "sendMoney", "recipient": recipient, "amountATM": amountATM,
            "secretPhrase": secretPhrase, "feeATM": feeATM, "deadline": "1440",
            "sender": sender, "messageIsPrunable": True, "messageIsText": True, "messageToEncrypt": "loading"}


def sendMessage(url):
    alive = True
    while alive:
        k = 1
        for k in range(1, 201):
            print(k)
            print("-------------")
            i = random.randint(1, 200)
            p = random.randint(1, 200)
            urls = random.choice(url)
            print("-----" + urls + "-----")
            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
            response = requests.request("GET",
                                        "http://" + urls + "/apl",
                                        params=getAccountId)
            print(response.json())
            accountReceive = response.json()["accountRS"]
            print("-------------")
            print(str("accountReceive = " + accountReceive))
            print("-------------")

            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
            response = requests.request("GET",
                                        "http://" + urls + "/apl",
                                        params=getAccountId)
            print(response.json())
            accountSender = response.json()["accountRS"]
            sender = response.json()["account"]
            print("-------------")
            print(str("accountSender = " + accountSender))
            print(str("account = " + sender))
            print(" <<<<<<< --------- " + urls + " ----- >>>>>>>")
            print("-------------")

            sendMessage = {"requestType": "sendMessage",
                           "recipient": str(accountReceive),
                           "messageToEncrypt": "MESSAGE " + str(id_generator()),
                           "secretPhrase": str(p),
                           "feeATM": "600000000",
                           "deadline": "1440",
                           "sender": str(sender),
                           "isCustomFee": "false",
                           "messageFile": "undefined",
                           "messageIsPrunable": "true",
                           "messageIsText": "true"}
            try:
                response = requests.request("POST", "http://" + urls + "/apl", params=sendMessage)

                print(response.json())
                print(" <<<<<<< --------- " + urls + " ----- >>>>>>>")
                print("----------------------------------------------------------------------------------------------")
            except requests.exceptions.ConnectionError:
                requests.status_code = "Connection refused"
            except json.decoder.JSONDecodeError as e:
                print("Error = " + str(e))
            k += 1
            time.sleep(1)



def return_json(url):
    try:
        response = requests.get(url)
        json_obj = response.json()
        return json_obj
    except requests.exceptions.RequestException as e:
        # A serious problem happened, like an SSLError or InvalidURL
        return "Error: {}".format(e)

def issueCurrency(url, name, code, description, type, initialSupply, maxSupply, feeATM, sender, passphrase):
    param = {'requestType': 'issueCurrency',
             'name': name,
             'code': code,
             'description': description,
             'type': type,
             'initialSupply': initialSupply,
             'maxSupply': maxSupply,
             'feeATM': feeATM,
             'sender': sender,
             'passphrase': passphrase
             }
    # randomUrl = random.choice(url)
    response = requests.post("http://" + url + "/apl", param)
    print(response.json())
    return response