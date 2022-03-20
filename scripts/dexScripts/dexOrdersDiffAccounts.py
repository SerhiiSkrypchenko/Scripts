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




vault30 = VaultWallet(conf.account30, conf.sender30, conf.PassPhrase30, conf.wallet30)
vault31 = VaultWallet(conf.account31, conf.sender31, conf.PassPhrase31, conf.wallet31)
vault32 = VaultWallet(conf.account32, conf.sender32, conf.PassPhrase32, conf.wallet32)
vault33 = VaultWallet(conf.account33, conf.sender33, conf.PassPhrase33, conf.wallet33)
vault34 = VaultWallet(conf.account34, conf.sender34, conf.PassPhrase34, conf.wallet34)

vaultsBuy = ([vault33, vault34])
vaultsSell = ([vault32, vault31, vault30])
vaults = ([vault34, vault33, vault32, vault31, vault30])


def DexTransactions(url, sleepTime):
        print(" <<<< ---- LOG IN ACCOUNTS ----- >>>> ")
        vaultLogin(url)
        print("<<<< ------ vault log in is finished ----- >>>>> ")
        print("<<<< ------ BALANCES ----- >>>>> ")
        ethBalance(url)
        k = 1
        print('The time is      :', time.ctime())
        start = time.time()
        finish = time.time() + 40000
        print('36000 secs from now :', time.ctime(finish))
        while (start < finish):
            print(" =======> " + str(k) + "    ==== > cicle of rounds")
            pr = random.randint(51, 77)
            print(pr)
            pairRate = int(str(pr) + "00000")
            print("pairRate = " + str(pairRate))
            offerAmount = 1000000000
            offerAmountPax = offerAmount + 9000000000

            for i in range(1, 5):
                print(" FROM LOW TO HIGH = " + str(i) + " step of parameters: pairRate = " + str(
                    pairRate) + " and offerAmount = " + str(offerAmount))
                print(
                    " --------------- NEW BUY STARTED ------------------- LOW-HIGH ----------------- pair rate * offerAmount = " + str(
                        pairRate * offerAmount))
                buyDexETH(url, vaultsBuy, str(pairRate), str(offerAmount))
                buyDexPAX(url, vaultsBuy, str(pairRate), str(offerAmountPax))
                time.sleep(sleepTime)

                print(
                    " --------------- NEW SELL STARTED ------------------ LOW-HIGH ----------------- pair rate * offerAmount = " + str(
                        pairRate * offerAmount))
                sellDexETH(url, vaultsSell, str(pairRate), str(offerAmount))
                sellDexPAX(url, vaultsSell, str(pairRate), str(offerAmountPax))
                pairRate = pairRate + 1000000 * k
                offerAmount = offerAmount + 1000000000
                offerAmountPax = offerAmountPax + 1000000000
                time.sleep(sleepTime)
                i += 1
            time.sleep(600)
            for j in range(1, 7):
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
                print(
                    " --------------- NEW SELL STARTED ------------------- HIGH-LOW ----------------- pair rate * offerAmount = " + str(
                        pairRate * offerAmount))
                sellDexETH(url, vaultsSell, str(pairRate), str(offerAmount))
                sellDexPAX(url, vaultsSell, str(pairRate), str(offerAmountPax))
                time.sleep(sleepTime)
                j += 1
            time.sleep(600)
            start = time.time()
            print('Current time is:', time.ctime(start))
            k+=1
            if k == 3:
                k = 1
            # cancelAllOpenBuyOrderETH(url)
            # cancelAllOpenBuyOrderPAX(url)
            # cancelAllOpenSellOrderETH(url)
            # cancelAllOpenSellOrderPAX(url)
            # time.sleep(240)

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

        response = requests.request("GET", randomUrl + "/rest/dex/balance", headers=headers, params=querystring)
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
        response = requests.request("POST", randomUrl + "/rest/keyStore/accountInfo", data=payload,
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
            response = requests.request("POST", randomUrl + "/rest/dex/offer", data=payload,
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
            response1 = requests.request("POST", randomUrl + "/rest/dex/offer", data=payload1,
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
            response = requests.request("POST", randomUrl + "/rest/dex/offer", data=payload,
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
            response1 = requests.request("POST", randomUrl + "/rest/dex/offer", data=payload1,
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

DexTransactions(testNet2.p1, 120)