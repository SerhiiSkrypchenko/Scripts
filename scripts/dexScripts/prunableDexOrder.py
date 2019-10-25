import exchangeFunctions
import requests
import random
import functions
from testNet1 import t1
from testNet1 import localhost
import mainNet
from testNet2 import t2
import testNet3
import testNet2
import exchangeFunctions
import time
from exchangeFunctions import vaults
from exchangeFunctions import printVault
import json


def prunableDexOrders(url, amountOfTime, type):
    if type == 1:
        pairRate1 = str(random.randint(200, 399))
        print(pairRate1)
        pairRate2 = str(random.randint(400, 699))
        print(pairRate2)
        pairRate3 = str(random.randint(700, 999))
        print(pairRate3)
        pairRate = (pairRate1, pairRate2, pairRate3)
    else:
        pairRate1 = "333333"
        print(pairRate1)
        pairRate2 = "444444"
        print(pairRate2)
        pairRate3 = "555555"
        print(pairRate3)
        pairRate = (pairRate1, pairRate2, pairRate3)
    offerAmount = ("10000000000", "20000000000", "15000000000", "25000000000")
    while True:
        prunableSellOrders(url, vaults, pairRate, offerAmount, amountOfTime)
        #time.sleep(sleepTime)
        prunableBuyOrders(url, vaults, pairRate, offerAmount, amountOfTime)


def prunableSellOrders(url, vaults, pairRate, offerAmount, amountOfTimeSec):
    for i in range(0, len(vaults)):
        account = vaults[i].account
        sender = vaults[i].sender
        passphrase = vaults[i].passPhrase
        wallet = vaults[i].wallet
        print("----- START SELL ORDER-----")
        randomUrl = random.choice(url)
        print("------------>   Random URL = " + randomUrl)
        printVault(vaults[i])
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"

        }
        offerAmount1 = random.choice(offerAmount)
        print("offerAmount = " + offerAmount1)
        pairRate1 = random.choice(pairRate)
        print("pairRate = " + pairRate1)
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate1 + "&messageIsPrunable=True&offerAmount=" + offerAmount1 + "&walletAddress" \
                                                                                                        "=" + wallet + "&sender=" + sender + "" \
                                                                                                                                             "&passphrase=" + passphrase + "&feeATM=200000000" \
                                                                                                                                                                           "&amountOfTime=" + str(amountOfTimeSec)
        print(randomUrl)
        try:
            response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                    headers=headers)
            print("RESPONSE = " + str(response.json()))
            print("----- END -----")
            print("")
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except UnicodeError as e:
            print("Error = " + str(e))
        except json.decoder.JSONDecodeError as e:
            print("Error = " + str(e))
        i += 1

def prunableBuyOrders(url, vaults, pairRate, offerAmount, amountOfTimeSec):
    for i in range(0, len(vaults)):
        account = vaults[i].account
        sender = vaults[i].sender
        passphrase = vaults[i].passPhrase
        wallet = vaults[i].wallet
        print("----- START BUY ORDER-----")
        randomUrl = random.choice(url)
        print("------------>   Random URL = " + randomUrl)
        printVault(vaults[i])
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"

        }
        offerAmount1 = random.choice(offerAmount)
        print("offerAmount = " + offerAmount1)
        pairRate1 = random.choice(pairRate)
        print("pairRate = " + pairRate1)
        payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate1 + "&messageIsPrunable=True&offerAmount=" + offerAmount1 + "&sender=" + sender + "" \
                                                                                                                              "&passphrase" \
                                                                                                                              "=" + passphrase + "&feeATM=200000000&amountOfTime=" + str(amountOfTimeSec) + "&walletAddress=" + wallet + ""
        try:
            response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                    headers=headers)
            print("RESPONSE = " + str(response.json()))
            print("----- END -----")
            print("")
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except UnicodeError as e:
            print("Error = " + str(e))
        except json.decoder.JSONDecodeError as e:
            print("Error = " + str(e))
        i += 1

prunableDexOrders(testNet2.local, 1800, 1)