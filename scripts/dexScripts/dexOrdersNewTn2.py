import testNet3
import testNet2
import json
import requests
import random
import conf
from exchangeFunctions import printVault
import time
from exchangeFunctions import cancelAllOpenBuyOrderETH
from exchangeFunctions import cancelAllOpenBuyOrderPAX
from exchangeFunctions import cancelAllOpenSellOrderETH
from exchangeFunctions import cancelAllOpenSellOrderPAX




class VaultWallet:
    def __init__(self, account, sender, passphrase, wallet):
        self.account = account
        self.sender = sender
        self.passPhrase = passphrase
        self.wallet = wallet


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

vault20 = VaultWallet(conf.account20, conf.sender20, conf.PassPhrase20, conf.wallet20)
vault19 = VaultWallet(conf.account19, conf.sender19, conf.PassPhrase19, conf.wallet19)
vault18 = VaultWallet(conf.account18, conf.sender18, conf.PassPhrase18, conf.wallet18)
vault17 = VaultWallet(conf.account17, conf.sender17, conf.PassPhrase17, conf.wallet17)

vault13 = VaultWallet(conf.account13, conf.sender13, conf.PassPhrase13, conf.wallet13)
vault14 = VaultWallet(conf.account14, conf.sender14, conf.PassPhrase14, conf.wallet14)
vault15 = VaultWallet(conf.account15, conf.sender15, conf.PassPhrase15, conf.wallet15)
vault16 = VaultWallet(conf.account16, conf.sender16, conf.PassPhrase16, conf.wallet16)

vault21 = VaultWallet(conf.account21, conf.sender21, conf.PassPhrase21, conf.wallet21)
vault22 = VaultWallet(conf.account22, conf.sender22, conf.PassPhrase22, conf.wallet22)
vault23 = VaultWallet(conf.account23, conf.sender23, conf.PassPhrase23, conf.wallet23)
vault24 = VaultWallet(conf.account24, conf.sender24, conf.PassPhrase24, conf.wallet24)
vaults = ([vault21, vault22, vault23, vault24])


def DexTransactions(url, sleepTime):
    k = 1
    while True:
        print(" =======> " + str(k) + "    ==== > cicle of rounds")
        pr = random.randint(21, 77)
        print(pr)
        pairRate = int(str(pr) + "00000")
        print("pairRate = " + str(pairRate))
        offerAmount = 1000000000
        for i in range(1, 7):
            print(" FROM LOW TO HIGH = " + str(i) + " step of parameters: pairRate = " + str(
                pairRate) + " and offerAmount = " + str(offerAmount))
            print(
                " --------------- NEW BUY STARTED ------------------- LOW-HIGH ----------------- pair rate * offerAmount = " + str(
                    pairRate * offerAmount))
            buyDex(url, vaults, str(pairRate), str(offerAmount))
            time.sleep(sleepTime)

            print(" --------------- NEW SELL STARTED ------------------ LOW-HIGH ----------------- pair rate * offerAmount = " + str(pairRate*offerAmount))
            sellDex(url, vaults, str(pairRate), str(offerAmount))

            pairRate = pairRate + 1000000 * k
            offerAmount = offerAmount + 1000000000
            time.sleep(sleepTime)
            i += 1
        time.sleep(900)
        for j in range(1, 7):
            pairRate = pairRate - 1000000 * k
            offerAmount = offerAmount - 1000000000
            print(" FROM HIGH TO LOW = " + str(j) + " step of next parameters: pairRate = " + str(
                pairRate) + " and offerAmount = " + str(offerAmount))
            print(
                " --------------- NEW BUY STARTED ------------------ HIGH-LOW ----------------- pair rate * offerAmount = " + str(
                    pairRate * offerAmount))
            buyDex(url, vaults, str(pairRate), str(offerAmount))
            time.sleep(sleepTime)
            print(" --------------- NEW SELL STARTED ------------------- HIGH-LOW ----------------- pair rate * offerAmount = " + str(pairRate*offerAmount))
            sellDex(url, vaults, str(pairRate), str(offerAmount))
            time.sleep(sleepTime)
            j += 1
        time.sleep(900)
        #cancelAllOpenBuyOrderETH(url)
        #cancelAllOpenBuyOrderPAX(url)
        #cancelAllOpenSellOrderETH(url)
        #cancelAllOpenSellOrderPAX(url)
        #time.sleep(240)
        k+=1
        if k == 3:
            k = 1


def sellDex(url, vaults, pairRate, offerAmount):
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
        payload = "offerType=1&pairCurrency=1&pairRate=" + pairRate + "&offerAmount=" + offerAmount + "&walletAddress" \
                                                                                                        "=" + wallet + "&sender=" + sender + "" \
                                                                                                                                             "&passphrase=" + passphrase + "&feeATM=200000000" \
                                                                                                                                                                           "&amountOfTime=9000"

        payload1 = "offerType=1&pairCurrency=2&pairRate=" + pairRate + "&offerAmount=" + offerAmount + "&walletAddress" \
                                                                                                        "=" + wallet + "&sender=" + sender + "" \
                                                                                                                                             "&passphrase=" + passphrase + "&feeATM=200000000" \
                                                                                                                                                                           "&amountOfTime=9000"


        print(randomUrl)
        try:
            print(" <-------- START SELL ORDER ----------> ")
            response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                    headers=headers)
            print("RESPONSE ETH = " + str(response.json()))
            time.sleep(20)
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

def buyDex(url, vaults, pairRate, offerAmount):
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

        payload = "offerType=0&pairCurrency=1&pairRate=" + pairRate + "&offerAmount=" + offerAmount + "&sender=" + sender + "" \
                                                                                                                              "&passphrase" \
                                                                                                                              "=" + passphrase + "&feeATM=200000000&amountOfTime=9000&walletAddress=" + wallet + ""

        payload1 = "offerType=0&pairCurrency=2&pairRate=" + pairRate + "&offerAmount=" + offerAmount + "&sender=" + sender + "" \
                                                                                                                              "&passphrase" \
                                                                                                                              "=" + passphrase + "&feeATM=200000000&amountOfTime=9000&walletAddress=" + wallet + ""

        try:
            print(" <-------- START BUY ORDER ----------> ")
            response = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload,
                                    headers=headers)
            print("RESPONSE ETH = " + str(response.json()))
            time.sleep(20)
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

DexTransactions(testNet2.exchange_peers, 240)