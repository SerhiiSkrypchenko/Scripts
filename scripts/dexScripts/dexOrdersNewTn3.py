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
import time





class VaultWallet:
    def __init__(self, account, sender, passphrase, wallet):
        self.account = account
        self.sender = sender
        self.passPhrase = passphrase
        self.wallet = wallet


vault35 = VaultWallet(conf.account35, conf.sender35, conf.PassPhrase35, conf.wallet35)
vault36 = VaultWallet(conf.account36, conf.sender36, conf.PassPhrase36, conf.wallet36)
vault37 = VaultWallet(conf.account37, conf.sender37, conf.PassPhrase37, conf.wallet37)
vault38 = VaultWallet(conf.account38, conf.sender38, conf.PassPhrase38, conf.wallet38)
vaults = ([vault35, vault36, vault37, vault38])


def DexTransactions(url, sleepTime):
    for i in range(0, len(vaults)):
        print(url)
        randomUrl = random.choice(url)
        account = vaults[i].account
        passphrase = vaults[i].passPhrase
        wallet = vaults[i].wallet
        print(account)
        payload = "account=" + account + "&passphrase=" + passphrase + ""
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
        }
        response = requests.request("POST", "http://" + randomUrl + "/rest/keyStore/accountInfo", data=payload,
                                    headers=headers)
        print(response.text)
        querystring = {"eth": str(wallet)}

        response = requests.request("GET", "http://" + randomUrl + "/rest/dex/balance", headers=headers, params=querystring)
        print(response.text)
        print("")
    k = 1
    print('The time is      :', time.ctime())
    start = time.time()
    finish = time.time() + 40000
    print('40000 secs from now :', time.ctime(finish))
    while (start < finish):
        print(" =======> " + str(k) + "    ==== > cicle of rounds")
        pr = random.randint(10, 30)
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
        start = time.time()
        print('Current time is :', time.ctime(start))
        #cancelAllOpenBuyOrderETH(url)
        #cancelAllOpenBuyOrderPAX(url)
        #cancelAllOpenSellOrderETH(url)
        #cancelAllOpenSellOrderPAX(url)
        #time.sleep(240)
        k+=1
        if k == 4:
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
            time.sleep(10)
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
            time.sleep(10)
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

DexTransactions(testNet3.local, 80)