import random
import time
import json

import requests
import testNet1
import testNet2
import testNet3
import data
import conf
import string
import os.path
import sys


class VaultWallet:
    def __init__(self, account, sender, passphrase, wallet):
        self.account = account
        self.sender = sender
        self.passPhrase = passphrase
        self.wallet = wallet

vault20 = VaultWallet(conf.account20, conf.sender20, conf.PassPhrase20, conf.wallet20)
vault19 = VaultWallet(conf.account19, conf.sender19, conf.PassPhrase19, conf.wallet19)
vault18 = VaultWallet(conf.account18, conf.sender18, conf.PassPhrase18, conf.wallet18)
vault17 = VaultWallet(conf.account17, conf.sender17, conf.PassPhrase17, conf.wallet17)
vault16 = VaultWallet(conf.account16, conf.sender16, conf.PassPhrase16, conf.wallet16)
vault15 = VaultWallet(conf.account15, conf.sender15, conf.PassPhrase15, conf.wallet15)
vault14 = VaultWallet(conf.account14, conf.sender14, conf.PassPhrase14, conf.wallet14)
vault13 = VaultWallet(conf.account13, conf.sender13, conf.PassPhrase13, conf.wallet13)
vault12 = VaultWallet(conf.account12, conf.sender12, conf.PassPhrase12, conf.wallet12)
vault11 = VaultWallet(conf.account11, conf.sender11, conf.PassPhrase11, conf.wallet11)
vault10 = VaultWallet(conf.account10, conf.sender10, conf.PassPhrase10, conf.wallet10)
vault9 = VaultWallet(conf.account9, conf.sender9, conf.PassPhrase9, conf.wallet9)
vault8 = VaultWallet(conf.account8, conf.sender8, conf.PassPhrase8, conf.wallet8)
vault7 = VaultWallet(conf.account7, conf.sender7, conf.PassPhrase7, conf.wallet7)
vault6 = VaultWallet(conf.account6, conf.sender6, conf.PassPhrase6, conf.wallet6)
vault5 = VaultWallet(conf.account5, conf.sender5, conf.PassPhrase5, conf.wallet5)
vault4 = VaultWallet(conf.account4, conf.sender4, conf.PassPhrase4, conf.wallet4)
vault3 = VaultWallet(conf.account3, conf.sender3, conf.PassPhrase3, conf.wallet3)
vault2 = VaultWallet(conf.account2, conf.sender2, conf.PassPhrase2, conf.wallet2)

vault21 = VaultWallet(conf.account21, conf.sender21, conf.PassPhrase21, conf.wallet21)
vault22 = VaultWallet(conf.account22, conf.sender22, conf.PassPhrase22, conf.wallet22)
vault23 = VaultWallet(conf.account23, conf.sender23, conf.PassPhrase23, conf.wallet23)
vault24 = VaultWallet(conf.account24, conf.sender24, conf.PassPhrase24, conf.wallet24)

vault25 = VaultWallet(conf.account25, conf.sender25, conf.PassPhrase25, conf.wallet25)
vault26 = VaultWallet(conf.account26, conf.sender26, conf.PassPhrase26, conf.wallet26)
vault27 = VaultWallet(conf.account27, conf.sender27, conf.PassPhrase27, conf.wallet27)
vault28 = VaultWallet(conf.account28, conf.sender28, conf.PassPhrase28, conf.wallet28)
vault29 = VaultWallet(conf.account29, conf.sender29, conf.PassPhrase29, conf.wallet29)


#vaults = ([vault26, vault27, vault25, vault28, vault29])

vault30 = VaultWallet(conf.account30, conf.sender30, conf.PassPhrase30, conf.wallet30)
vault31 = VaultWallet(conf.account31, conf.sender31, conf.PassPhrase31, conf.wallet31)
vault32 = VaultWallet(conf.account32, conf.sender32, conf.PassPhrase32, conf.wallet32)
vault33 = VaultWallet(conf.account33, conf.sender33, conf.PassPhrase33, conf.wallet33)
vault34 = VaultWallet(conf.account34, conf.sender34, conf.PassPhrase34, conf.wallet34)
vault35 = VaultWallet(conf.account35, conf.sender35, conf.PassPhrase35, conf.wallet35)
vault36 = VaultWallet(conf.account36, conf.sender36, conf.PassPhrase36, conf.wallet36)
vault37 = VaultWallet(conf.account37, conf.sender37, conf.PassPhrase37, conf.wallet37)
vault38 = VaultWallet(conf.account38, conf.sender38, conf.PassPhrase38, conf.wallet38)
#vaults = ([vault35, vault36, vault37, vault38])


vaults = ([vault2, vault3, vault4, vault5, vault6, vault7, vault8, vault9, vault10, vault11, vault12, vault13, vault14, vault15,
           vault16, vault17, vault18, vault19, vault20, vault21, vault22, vault23, vault24,
           vault34, vault33, vault32, vault31, vault30, vault35, vault36, vault37, vault38, vault26, vault27, vault25, vault28, vault29])

#vaults = ([vault21, vault22, vault23, vault24])
#vaults = ([vault17, vault18, vault19, vault20])
#vaults = ([vault2, vault3, vault4, vault5, vault6, vault7, vault8, vault9, vault10, vault11, vault12, vault13, vault14, vault15, vault16])


def printVault(vaultWallet):
    print("ACCOUNT = " + vaultWallet.account)
    print("SENDER = " + vaultWallet.sender)
    print("PASSPHRASE = " + vaultWallet.passPhrase)
    print("ETH/PAX WALLET = " + vaultWallet.wallet)


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
        payload = "offerType=0&pairCurrency=1&pairRate=" + random.choice(
            url) + "&offerAmount=1000000000000&sender=" + conf.sender8 + "" \
                                                                         "&passphrase" \
                                                                         "=" + conf.account8PassPhrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + conf.wallet8 + ""
        response = requests.request("POST", "http://" + random.choice(url) + "/rest/dex/offer", data=payload,
                                    headers=headers)
        print(response.text)
        time.sleep(sleepTime)

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

def buyOrders(url, vaults, pairRate, offerAmount):
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
        payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&sender=" + sender + "" \
                                                                                                                              "&passphrase" \
                                                                                                                              "=" + passphrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + wallet + ""
        print(randomUrl)
        try:
            response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                    headers=headers)
            print(response.json())
            print("----- END -----")
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except UnicodeError as e:
            print("Error = " + str(e))

        i += 1


def sellOrders(url, vaults, pairRate, offerAmount):
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
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&walletAddress" \
                                                                                                        "=" + wallet + "&sender=" + sender + "" \
                                                                                                                                             "&passphrase=" + passphrase + "&feeATM=200000000" \
                                                                                                                                                                           "&amountOfTime=86400"

        try:
            response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                    headers=headers)
            print(response.json())
            print("----- END -----")
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except UnicodeError as e:
            print("Error = " + str(e))
        i += 1


def buyOrders2(url, vaults, pairRate, offerAmount):
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
        payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&sender=" + sender + "" \
                                                                                                                              "&passphrase" \
                                                                                                                              "=" + passphrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + wallet + ""
        payload1 = "offerType=0&pairCurrency=2&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&sender=" + sender + "" \
                                                                                                                              "&passphrase" \
                                                                                                                              "=" + passphrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + wallet + ""

        try:
            response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                    headers=headers)
            print("RESPONSE ETH = " + str(response.json()))

            response1 = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload1,
                                        headers=headers)
            print("RESPONSE PAX = " + str(response1.json()))

            print("----- END -----")
            print("")
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except UnicodeError as e:
            print("Error = " + str(e))
        except json.decoder.JSONDecodeError as e:
            print("Error = " + str(e))
        i += 1


def sellOrders2(url, vaults, pairRate, offerAmount):
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
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&walletAddress" \
                                                                                                        "=" + wallet + "&sender=" + sender + "" \
                                                                                                                                             "&passphrase=" + passphrase + "&feeATM=200000000" \
                                                                                                                                                                           "&amountOfTime=86400"
        payload1 = "offerType=1&pairCurrency=2&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&walletAddress" \
                                                                                                        "=" + wallet + "&sender=" + sender + "" \
                                                                                                                                             "&passphrase=" + passphrase + "&feeATM=200000000" \
                                                                                                                                                                           "&amountOfTime=86400"


        print(randomUrl)
        try:
            response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                    headers=headers)
            print("RESPONSE ETH = " + str(response.json()))

            response1 = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload1,
                                        headers=headers)

            print("RESPONSE PAX = " + str(response1.json()))

            print("----- END -----")
            print("")
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except UnicodeError as e:
            print("Error = " + str(e))
        except json.decoder.JSONDecodeError as e:
            print("Error = " + str(e))
        i += 1





def dexOrders(url, sleepTime, type):
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"

    }
    if type == 1:
        pairRate1 = str(random.randint(2000, 3999))
        print(pairRate1)
        pairRate2 = str(random.randint(4000, 6999))
        print(pairRate2)
        pairRate3 = str(random.randint(7000, 9999))
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
    offerAmount = ("1000000000000", "2000000000000", "1500000000000", "2500000000000")
    i = 1
    for i in range(1, 20):
        sellOrders(url, vaults, pairRate, offerAmount)
        buyOrders(url, vaults, pairRate, offerAmount)
        i += 1

def dexOrders2(url, sleepTime, type):
    if type == 1:
        pairRate1 = random.choice(["5000", "6000", "7000", "8000"])
        print(pairRate1)
        pairRate2 = random.choice(["4500", "5500", "1500", "2500"])
        print(pairRate2)
        pairRate3 = random.choice(["3500", "3000", "1000", "9000"])
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
    offerAmount = ("1000000000000", "2000000000000", "3000000000000", "4000000000000", "5000000000000")
    while True:
        sellOrders2(url, vaults, pairRate, offerAmount)
        #time.sleep(1200)
        buyOrders2(url, vaults, pairRate, offerAmount)
        #cancelRandomOrder(url)





#ETH
def exchangeTransactionsOneByOneSellBuy(url, sleepTime, numberOfCircles):
    offerAmount = ("100000000000", "200000000000", "150000000000", "250000000000")
    for i in range(0, numberOfCircles):
        for j in range(0, len(vaults) - 1):
            try:
                # SELL ORDER FROM ACCOUNT
                account = vaults[j].account
                sender = vaults[j].sender
                passphrase = vaults[j].passPhrase
                wallet = vaults[j].wallet
                print("----- START SELL ORDER-----")
                randomUrl = url
                printVault(vaults[j])
                headers = {
                    'Content-Type': "application/x-www-form-urlencoded"

                }
                offerAmount1 = random.choice(offerAmount)
                print("offerAmount = " + offerAmount1)
                pairRate1 = str(random.randint(2000, 9999))
                print("pairRate = " + pairRate1)
                payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&walletAddress" \
                                                                                                                "=" + wallet + "&sender=" + sender + "" \
                                                                                                                                                     "&passphrase=" + passphrase + "&feeATM=200000000" \
                                                                                                                                                                                   "&amountOfTime=86400"
                print(randomUrl)
                response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                            headers=headers)
                print(response.json())
                print("----- END -----")
                time.sleep(sleepTime)

                # BUY ORDER FROM ACCOUNT
                k = j + 1
                account = vaults[k].account
                sender = vaults[k].sender
                passphrase = vaults[k].passPhrase
                wallet = vaults[k].wallet
                print("----- START BUY ORDER-----")
                randomUrl = random.choice(url)
                printVault(vaults[k])
                headers = {
                    'Content-Type': "application/x-www-form-urlencoded"

                }
                # offerAmount1 = random.choice(offerAmount)
                print("offerAmount = " + offerAmount1)
                # pairRate1 = random.choice(pairRate)
                print("pairRate = " + pairRate1)
                payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&sender=" + sender + "" \
                                                                                                                                      "&passphrase" \
                                                                                                                                      "=" + passphrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + wallet + ""
                response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                            headers=headers)
                print(response.json())
                print("----- END -----")
                print(" ---------------- -------------- -------------- ----------- -------------")
                # time.sleep(sleepTime)
            except Exception as ex:
                print("Error: " + str(ex))
        i += 1

#ETH
def dexBuySellETH(url, sleepTime, numberOfCircles):
    offerAmount = ("1000000000000", "2000000000000", "1500000000000", "2500000000000")
    for i in range(0, numberOfCircles):
        for j in range(0, len(vaults) - 1):
            # BUY ORDER FROM ACCOUNT
            account = vaults[j].account
            sender = vaults[j].sender
            passphrase = vaults[j].passPhrase
            wallet = vaults[j].wallet

            print("----- START BUY ORDER-----")
            randomUrl = random.choice(url)
            print(randomUrl)
            printVault(vaults[j])
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"

            }
            offerAmount1 = random.choice(offerAmount)
            print("offerAmount = " + offerAmount1)
            pairRate1 = str(random.randint(2000, 9999))
            print("pairRate = " + pairRate1)
            payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&sender=" + sender + "" \
                                                                                                                                  "&passphrase" \
                                                                                                                                  "=" + passphrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + wallet + ""

            try:
                response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                            headers=headers)
                print(response.json())
                print("----- END -----")
            except requests.exceptions.RequestException as e:
                # A serious problem happened, like an SSLError or InvalidURL
                print("Error = " + str(e))
            except requests.exceptions.ConnectionError:
                requests.status_code = "Connection refused"
            except UnicodeError as e:
                print("Error = " + str(e))
            except json.decoder.JSONDecodeError as e:
                print("Error = " + str(e))


            time.sleep(sleepTime)

            # SELL ORDER FROM ACCOUNT
            k = j + 1
            account = vaults[k].account
            sender = vaults[k].sender
            passphrase = vaults[k].passPhrase
            wallet = vaults[k].wallet
            print("----- START SELL ORDER-----")
            randomUrl = random.choice(url)
            printVault(vaults[k])
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"

            }
            # offerAmount1 = random.choice(offerAmount)
            print("offerAmount = " + offerAmount1)
            # pairRate1 = random.choice(pairRate)
            print("pairRate = " + pairRate1)
            payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&walletAddress" \
                                                                                                            "=" + wallet + "&sender=" + sender + "" \
                                                                                                                                                 "&passphrase=" + passphrase + "&feeATM=200000000" \
                                                                                                                                                                               "&amountOfTime=86400"
            print(randomUrl)
            try:
                response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                        headers=headers)
                print(response.json())
                print("----- END -----")
                print("")
            except requests.exceptions.RequestException as e:
                # A serious problem happened, like an SSLError or InvalidURL
                time.sleep(sleepTime)
                print("Error = " + str(e))
            except requests.exceptions.ConnectionError:
                requests.status_code = "Connection refused"
            except UnicodeError as e:
                print("Error = " + str(e))
            except json.decoder.JSONDecodeError as e:
                print("Error = " + str(e))

            time.sleep(sleepTime)

        j += 1
    i += 1


#PAX
def exchangeTransactionsOneByOneSellBuyPAX(url, sleepTime, numberOfCircles):
    offerAmount = ("1000000000000", "2000000000000", "3000000000000", "4000000000000")
    for i in range(0, numberOfCircles):
        for j in range(0, len(vaults) - 1):
            # SELL ORDER FROM ACCOUNT
            account = vaults[j].account
            sender = vaults[j].sender
            passphrase = vaults[j].passPhrase
            wallet = vaults[j].wallet
            print("----- START SELL ORDER-----")
            randomUrl = url
            printVault(vaults[j])
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"

            }
            offerAmount1 = random.choice(offerAmount)
            print("offerAmount = " + offerAmount1)
            pairRate1 = str(random.choice((7000000, 8000000, 9000000)))
            print("pairRate = " + pairRate1)
            payload = "offerType=1&pairCurrency=2&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&walletAddress" \
                                                                                                            "=" + wallet + "&sender=" + sender + "" \
                                                                                                                                                 "&passphrase=" + passphrase + "&feeATM=200000000" \
                                                                                                                                                                               "&amountOfTime=86400"
            print(randomUrl)
            response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                        headers=headers)
            print(response.json())
            print("----- END -----")
            time.sleep(sleepTime)

            # BUY ORDER FROM ACCOUNT
            k = j + 1
            account = vaults[k].account
            sender = vaults[k].sender
            passphrase = vaults[k].passPhrase
            wallet = vaults[k].wallet
            print("----- START BUY ORDER-----")
            randomUrl = random.choice(url)
            printVault(vaults[k])
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"

            }
            # offerAmount1 = random.choice(offerAmount)
            print("offerAmount = " + offerAmount1)
            # pairRate1 = random.choice(pairRate)
            print("pairRate = " + pairRate1)
            payload = "offerType=0&pairCurrency=2&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&sender=" + sender + "" \
                                                                                                                                  "&passphrase" \
                                                                                                                                  "=" + passphrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + wallet + ""
            response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                        headers=headers)
            print(response.json())
            print("----- END -----")
            print(" ---------------- -------------- -------------- ----------- -------------")
            # time.sleep(sleepTime)
        i += 1


#PAX
def exchangeTransactionsOneByOneBuySellPAX(url, sleepTime, numberOfCircles):
    offerAmount = ("1000000000000", "2000000000000", "3000000000000", "4000000000000")
    for i in range(0, numberOfCircles):
        for j in range(0, len(vaults) - 1):
            # BUY ORDER FROM ACCOUNT
            account = vaults[j].account
            sender = vaults[j].sender
            passphrase = vaults[j].passPhrase
            wallet = vaults[j].wallet

            print("----- START BUY ORDER-----")
            randomUrl = url
            printVault(vaults[j])
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"

            }
            offerAmount1 = random.choice(offerAmount)
            print("offerAmount = " + offerAmount1)
            pairRate1 = str(random.choice((1000000, 2000000, 3000000, 4000000, 5000000, 6000000)))
            print("pairRate = " + pairRate1)
            payload = "offerType=0&pairCurrency=2&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&sender=" + sender + "" \
                                                                                                                                  "&passphrase" \
                                                                                                                                  "=" + passphrase + "&feeATM=200000000&amountOfTime=86400&walletAddress=" + wallet + ""

            response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                        headers=headers)
            print(response.json())
            print("----- END -----")

            time.sleep(sleepTime)

            # SELL ORDER FROM ACCOUNT
            k = j + 1
            account = vaults[k].account
            sender = vaults[k].sender
            passphrase = vaults[k].passPhrase
            wallet = vaults[k].wallet
            print("----- START SELL ORDER-----")
            randomUrl = random.choice(url)
            printVault(vaults[k])
            headers = {
                'Content-Type': "application/x-www-form-urlencoded"

            }
            # offerAmount1 = random.choice(offerAmount)
            print("offerAmount = " + offerAmount1)
            # pairRate1 = random.choice(pairRate)
            print("pairRate = " + pairRate1)
            payload = "offerType=1&pairCurrency=2&pairRate=" + pairRate1 + "&offerAmount=" + offerAmount1 + "&walletAddress" \
                                                                                                            "=" + wallet + "&sender=" + sender + "" \
                                                                                                                                                 "&passphrase=" + passphrase + "&feeATM=200000000" \
                                                                                                                                                                               "&amountOfTime=86400"
            print(randomUrl)

            response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                        headers=headers)
            print(response.json())
            print("----- END -----")
            print(" ---------------- -------------- -------------- ----------- -------------")

        i += 1

def vaultLogin(url):
    for i in range(0, len(vaults)):
        print(url)
        account = vaults[i].account
        passphrase = vaults[i].passPhrase
        print(account)
        payload = "account=" + account + "&passphrase=" + passphrase + ""
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
        }
        response = requests.request("POST", "http://" + url + "/rest/keyStore/accountInfo", data=payload,
                                    headers=headers)
        print(response.text)
        print("")


def ethBalance(url):
    for i in range(0, len(vaults)):
        account = vaults[i].account
        passphrase = vaults[i].passPhrase
        wallet = vaults[i].wallet
        print(account)

        querystring = {"eth": str(wallet)}

        headers = {
            'Content-Type': "application/x-www-form-urlencoded"

        }


        response = requests.request("GET", "http://" + url + "/rest/dex/balance", headers=headers, params=querystring)
        print(response.url)
        print(response.text)


def uploadSecretFile(url):
    i = 0
    for i in range(0, len(vaults)):
        print(url)
        account = vaults[i].account
        passPhrase = vaults[i].passPhrase
        print(account)
        print(os.path.abspath(account))
        f = open(account, 'rb')
        file_content = f.read()
        print(file_content)
        f.close()
        #payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"keyStore\"; filename=\"C:\\FilesForImport\\" + account + "\"\r\nContent-Type: false\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"passPhrase\"\r\n\r\n" + passPhrase + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Content-Type': "application/x-www-form-urlencoded"

        }
        payload = {"keyStore": str(file_content), "passPhrase": str(passPhrase)}

        response = requests.request("POST", "http://" + url + "/rest/keyStore/upload", data=payload, headers=headers)
        print("")
        print(response.content)
        i += 1


def uploadSecretFile1(url):
    i = 0
    for i in range(0, len(vaults)):
        print(url)
        account = vaults[i].account
        passPhrase = vaults[i].passPhrase
        print(account)
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"keyStore\"; filename=\"C:\\FilesForImport\\" + account + "\"\r\nContent-Type: false\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"passPhrase\"\r\n\r\n" + passPhrase + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Content-Type': "application/x-www-form-urlencoded"

        }
        print(os.path.abspath("C:\\FilesForImport\\" + account + ""))

        response = requests.request("POST", "http://" + url + "/rest/keyStore/upload", data=payload, headers=headers)
        print(response.content)
        i += 1

def flush(url):
    i = 0
    for i in range(0, len(vaults)):
        print(url)
        account = vaults[i].account
        accountId = vaults[i].sender
        passPhrase = vaults[i].passPhrase
        print(account)
        querystring = {"accountid": str(accountId), "passphrase": str(passPhrase)}

        headers = {
            'cache-control': "no-cache",
            'Postman-Token': "2f706d35-611a-445d-8755-62235c719219"
        }

        response = requests.request("GET", "http://" + url + "/rest/dex/flush", params=querystring)
        print(response.text)
        i += 1
#нужно написать скрипт который был отменял все открытые ордера
def getAllOrders(url):
    response = requests.request("GET", "http://" + url + "/rest/dex/offers?orderType=0&pairCurrency=1&status=0&isAvailableForNow=true")
    print("BUY ETH ORDERS:")
    print(response.json())

# Type of the offer. (BUY = 0 /SELL = 1)
# Criteria by Paired currency. (APL=0, ETH=1, PAX=2)
# Offer status. (Open = 0, Close = 2)
# Return offers available for now. By default = false

def getDexOrders(url, orderType, pairCurrency, status, accountId, isAvailableForNow):
    param = {'orderType': orderType,
             'pairCurrency': pairCurrency,
             'status': status,
             'accountId': accountId,
             'isAvailableForNow': isAvailableForNow
           }
    try:
        response = requests.get("http://" + url + "/rest/dex/offers", param)
        print(response.json())
        result = response.json()
        for i in range(len(response.json())):
            try:
                for key, value in result[i].items():
                    if key == "id":
                        print(value)
            except:
                pass
    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"
    except UnicodeError as e:
        print("Error = " + str(e))
    except json.decoder.JSONDecodeError as e:
        print("Error = " + str(e))
    return response

def cancelOrder(url, orderId, sender, passphrase):
    param = {'orderId': orderId,
             'sender': sender,
             'passphrase': passphrase,
             'feeATM': 100000000
             }
    #randomUrl = random.choice(url)
    response = requests.post("http://" + url + "/rest/dex/offer/cancel", param)
    print(response.json())
    return response

#CANCELING OPEN SELL ORDERS APL/ETH
def cancelAllOpenSellOrderETH(url):
    for i in range(0, len(vaults)):
        account = vaults[i].account
        sender = vaults[i].sender
        passphrase = vaults[i].passPhrase
        wallet = vaults[i].wallet
        print("----- START CANCEL ORDERS FROM -----" + str(account))
        randomUrl = random.choice(url)
        print("------------>   Random URL = " + randomUrl)
        printVault(vaults[i])

        #get All Open SELL Orders APL/ETH by Account
        res = getDexOrders(randomUrl, 1, 1, 0, sender, True)
        res_json = res.json()

        #cirlce for canceling orders
        for j in range(len(res_json)):
            try:
                for key, value in res_json[j].items():
                    if key == "id":
                        print(str(j) + " Order to cancel is " + str(value))
                        try:
                            cancelOrder(randomUrl, str(value), sender, passphrase)
                            print("")
                        except requests.exceptions.ConnectionError:
                            requests.status_code = "Connection refused"
                        except UnicodeError as e:
                            print("Error = " + str(e))
                        except json.decoder.JSONDecodeError as e:
                            print("Error = " + str(e))
            except:
                pass
            j += 1
        i += 1

#CANCELING OPEN BUY ORDERS APL/ETH
def cancelAllOpenBuyOrderETH(url):
    for i in range(0, len(vaults)):
        account = vaults[i].account
        sender = vaults[i].sender
        passphrase = vaults[i].passPhrase
        wallet = vaults[i].wallet
        print("----- START CANCEL ORDERS FROM -----" + str(account))
        randomUrl = random.choice(url)
        print("------------>   Random URL = " + randomUrl)
        printVault(vaults[i])

        # get All Open SELL Orders APL/ETH by Account
        res = getDexOrders(randomUrl, 0, 1, 0, sender, True)
        res_json = res.json()

        # cirlce for canceling orders
        for j in range(len(res_json)):
            try:
                for key, value in res_json[j].items():
                    if key == "id":
                        print(str(j) + " Order to cancel is " + str(value))
                        try:
                            cancelOrder(randomUrl, str(value), sender, passphrase)
                            print("")
                        except requests.exceptions.ConnectionError:
                            requests.status_code = "Connection refused"
                        except UnicodeError as e:
                            print("Error = " + str(e))
                        except json.decoder.JSONDecodeError as e:
                            print("Error = " + str(e))
            except:
                pass
            j += 1
        i += 1


def cancelAllOpenBuyOrderPAX(url):
    for i in range(0, len(vaults)):
        account = vaults[i].account
        sender = vaults[i].sender
        passphrase = vaults[i].passPhrase
        wallet = vaults[i].wallet
        print("----- START CANCEL ORDERS FROM -----" + str(account))
        randomUrl = random.choice(url)
        print("------------>   Random URL = " + randomUrl)
        printVault(vaults[i])

        # get All Open SELL Orders APL/ETH by Account
        res = getDexOrders(randomUrl, 0, 2, 0, sender, False)
        res_json = res.json()

        # cirlce for canceling orders
        for j in range(len(res_json)):
            try:
                for key, value in res_json[j].items():
                    if key == "id":
                        print(str(j) + " Order to cancel is " + str(value))
                        try:
                            cancelOrder(randomUrl, str(value), sender, passphrase)
                            print("")
                        except requests.exceptions.ConnectionError:
                            requests.status_code = "Connection refused"
                        except UnicodeError as e:
                            print("Error = " + str(e))
                        except json.decoder.JSONDecodeError as e:
                            print("Error = " + str(e))
            except:
                pass
            j += 1
        i += 1

def cancelAllOpenSellOrderPAX(url):
    for i in range(0, len(vaults)):
        account = vaults[i].account
        sender = vaults[i].sender
        passphrase = vaults[i].passPhrase
        wallet = vaults[i].wallet
        print("----- START CANCEL ORDERS FROM -----" + str(account))
        randomUrl = random.choice(url)
        print("------------>   Random URL = " + randomUrl)
        printVault(vaults[i])

        # get All Open SELL Orders APL/ETH by Account
        res = getDexOrders(randomUrl, 1, 2, 0, sender, False)
        res_json = res.json()

        # cirlce for canceling orders
        for j in range(len(res_json)):
            try:
                for key, value in res_json[j].items():
                    if key == "id":
                        print(str(j) + " Order to cancel is " + str(value))
                        try:
                            cancelOrder(randomUrl, str(value), sender, passphrase)
                            print("")
                        except requests.exceptions.ConnectionError:
                            requests.status_code = "Connection refused"
                        except UnicodeError as e:
                            print("Error = " + str(e))
                        except json.decoder.JSONDecodeError as e:
                            print("Error = " + str(e))
            except:
                pass
            j += 1
        i += 1


def cancelRandomOrder(url):
    for i in range(0, len(vaults)):
        account = vaults[i].account
        sender = vaults[i].sender
        passphrase = vaults[i].passPhrase
        wallet = vaults[i].wallet
        print("----- START CANCEL ORDERS FROM -----" + str(account))
        randomUrl = random.choice(url)
        print("------------>   Random URL = " + randomUrl)
        printVault(vaults[i])

        orderType = random.choice([1, 0])
        print("orderType = " + str(orderType))
        res = getDexOrders(randomUrl, orderType, 1, 0, sender, False)
        res_json = res.json()

        # cirlce for canceling orders
        for j in range(len(res_json)):
            try:
                for key, value in res_json[j].items():
                    if key == "id":
                        print(str(j) + " Order to cancel is " + str(value))
                        try:
                            cancelOrder(randomUrl, str(value), sender, passphrase)
                            print("Canceling of -- " + str(value) + " -- is SKIPPED")
                            print("")
                        except requests.exceptions.ConnectionError:
                            requests.status_code = "Connection refused"
                        except UnicodeError as e:
                            print("Error = " + str(e))
                        except json.decoder.JSONDecodeError as e:
                            print("Error = " + str(e))
            except:
                pass
            j += 1
        i += 1

#cancelRandomOrder(testNet2.exchange_peers)
#cancelAllOpenSellOrderPAX(testNet2.exchange_peers)

#cancelOrder(testNet2.peer1, "17326318758377288947", "7821792282123976600", "11")


#getDexOrders(testNet2.peer1, 0, 1, 0, "7821792282123976600", True)


