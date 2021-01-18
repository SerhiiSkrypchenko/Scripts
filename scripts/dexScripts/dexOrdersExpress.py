import testNet3
import testNet2
import json
import requests
import random
import conf
from exchangeFunctions import printVault
import time
import testNet1
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



vault25 = VaultWallet(conf.account25, conf.sender25, conf.PassPhrase25, conf.wallet25)
vault26 = VaultWallet(conf.account26, conf.sender26, conf.PassPhrase26, conf.wallet26)
vault27 = VaultWallet(conf.account27, conf.sender27, conf.PassPhrase27, conf.wallet27)
vault28 = VaultWallet(conf.account28, conf.sender28, conf.PassPhrase28, conf.wallet28)
vault29 = VaultWallet(conf.account29, conf.sender29, conf.PassPhrase29, conf.wallet29)

vaultsBuy = ([vault25, vault28])
vaultsSell = ([vault26, vault27, vault29])
vaults = ([vault26, vault27, vault25, vault28, vault29])


def DexTransactions(url, sleepTime):
        print(" <<<< ---- LOG IN ACCOUNTS ----- >>>> ")
        vaultLogin(url)
        print("<<<< ------ vault log in is finished ----- >>>>> ")
        print("<<<< ------ BALANCES ----- >>>>> ")
        ethBalance(url)
        k = 1
        print(" =======> " + str(k) + "    ==== > cicle of rounds")
        pr = random.randint(31, 50)
        print(pr)
        pairRate = int(str(pr) + "00000")
        print("pairRate = " + str(pairRate))
        offerAmount = 1000000000
        offerAmountPax = offerAmount + 9000000000

        for i in range(1, 9):
            print(" FROM LOW TO HIGH = " + str(i) + " step of parameters: pairRate = " + str(
                pairRate) + " and offerAmount = " + str(offerAmount))
            print(
                " --------------- NEW BUY STARTED ------------------- LOW-HIGH ----------------- pair rate * offerAmount = " + str(
                    pairRate * offerAmount))
            buyDexETH(url, vaultsBuy, str(pairRate), str(offerAmount))
            buyDexPAX(url, vaultsBuy, str(pairRate), str(offerAmountPax))
            time.sleep(sleepTime)

            print(" --------------- NEW SELL STARTED ------------------ LOW-HIGH ----------------- pair rate * offerAmount = " + str(pairRate*offerAmount))
            sellDexETH(url, vaultsSell, str(pairRate), str(offerAmount))
            sellDexPAX(url, vaultsSell, str(pairRate), str(offerAmountPax))
            pairRate = pairRate + 1000000 * k
            offerAmount = offerAmount + 1000000000
            offerAmountPax = offerAmountPax + 1000000000
            time.sleep(sleepTime)
            i += 1
        time.sleep(3600)
        for j in range(1, 9):
            pairRate = pairRate - 1000000 * k
            offerAmount = offerAmount - 1000000000
            offerAmountPax = offerAmountPax - 1000000000
            print(" FROM HIGH TO LOW = " + str(j) + " step of next parameters: pairRate = " + str(
                pairRate) + " and offerAmount = " + str(offerAmount))
            print(
                " --------------- NEW BUY STARTED ------------------ HIGH-LOW ----------------- pair rate * offerAmount = " + str(
                    pairRate * offerAmount))
            buyDexETH(url, vaultsBuy, str(pairRate), str(offerAmount))
            buyDexPAX(url, vaultsBuy, str(pairRate), str(offerAmountPax))
            time.sleep(sleepTime)
            print(" --------------- NEW SELL STARTED ------------------- HIGH-LOW ----------------- pair rate * offerAmount = " + str(pairRate*offerAmount))
            sellDexETH(url, vaultsSell, str(pairRate), str(offerAmount))
            sellDexPAX(url, vaultsSell, str(pairRate), str(offerAmountPax))
            time.sleep(sleepTime)
            j += 1
        print(" <<<<<< -------- END OF SCRIPT -------- >>>>>> ")
        #time.sleep(180)
        #cancelAllOpenBuyOrderETH(url)
        #cancelAllOpenBuyOrderPAX(url)
        #cancelAllOpenSellOrderETH(url)
        #cancelAllOpenSellOrderPAX(url)
        #time.sleep(240)

def ethBalance(url):
    for i in range(0, len(vaults)):
        randomUrl = random.choice(url)
        account = vaults[i].account
        passphrase = vaults[i].passPhrase
        wallet = vaults[i].wallet
        print(account)

        querystring = {"eth": str(wallet)}

        headers = {
            'Content-Type': "application/x-www-form-urlencoded"

        }

        response = requests.request("GET", "http://" + randomUrl + "/rest/dex/balance", headers=headers, params=querystring)
        print(response.text)


def vaultLogin(url):
    for i in range(0, len(vaults)):
        print(url)
        randomUrl = random.choice(url)
        account = vaults[i].account
        passphrase = vaults[i].passPhrase
        print(account)
        payload = "account=" + account + "&passphrase=" + passphrase + ""
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
        }
        response = requests.request("POST", "http://" + randomUrl + "/rest/keyStore/accountInfo", data=payload,
                                    headers=headers)
        print(response.text)
        print("")

def sellDexETH(url, vaults, pairRate, offerAmount):
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
            time.sleep(10)
            print("----- END -----")
            print("")
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except UnicodeError as e:
            print("Error = " + str(e))
        except json.decoder.JSONDecodeError as e:
            print("Error = " + str(e))
        i += 1

def sellDexPAX(url, vaults, pairRate, offerAmount):
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
            response1 = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload1,
                                        headers=headers)
            print("RESPONSE PAX = " + str(response1.json()))
            time.sleep(10)
            print("----- END -----")
            print("")
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except UnicodeError as e:
            print("Error = " + str(e))
        except json.decoder.JSONDecodeError as e:
            print("Error = " + str(e))
        i += 1

def buyDexETH(url, vaults, pairRate, offerAmount):
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
            time.sleep(10)
            print("----- END -----")
            print("")
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except UnicodeError as e:
            print("Error = " + str(e))
        except json.decoder.JSONDecodeError as e:
            print("Error = " + str(e))
        i += 1

def buyDexPAX(url, vaults, pairRate, offerAmount):
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

        payload1 = "offerType=0&pairCurrency=2&pairRate=" + pairRate + "&offerAmount=" + offerAmount + "&sender=" + sender + "" \
                                                                                                                              "&passphrase" \
                                                                                                                              "=" + passphrase + "&feeATM=200000000&amountOfTime=9000&walletAddress=" + wallet + ""

        try:
            print(" <-------- START BUY ORDER ----------> ")
            response1 = requests.request("POST", "http://" + randomUrl + "/rest/dex/offer", data=payload1,
                                        headers=headers)
            print("RESPONSE PAX = " + str(response1.json()))
            time.sleep(10)
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