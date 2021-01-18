import requests
import random
import data
import time
import testNet2
import testNet3
import testNet1
from exchangeFunctions import vaults
from exchangeFunctions import printVault
import json

http = "http://"

def AccountPropertyVault(url):
    for i in range(0, len(vaults)):
        print(" STEP = " + str(i))
        value = "standard wallets -> ooopppsss ->   " \
                "';:.,<>/?][{}\|=+-_)($#@!%^&*()  ->  " \
                " END 1.1.1.1.1"
        property = "';:.,<>/?][{}\|=+-_)($#@!%^&*()"
        account = vaults[i].account
        sender = vaults[i].sender
        passphrase = vaults[i].passPhrase

        randomUrl = random.choice(url)
        print("------------>   Random URL = " + randomUrl)
        printVault(vaults[i])
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
        }

        setAccountProperty = {"requestType": "setAccountProperty", "value": value, "sender": sender,
                          "deadline": "1440", "property": property, "passphrase": passphrase,
                          "feeATM": "1000000000"}

        deleteAccountProperty = {"requestType": "deleteAccountProperty", "incoming": "true", "setterRS": account,
                                 "value": value, "sender": sender,
                          "deadline": "1440", "property": property, "passphrase": passphrase,
                          "feeATM": "1000000000"}

        print(randomUrl)
        try:
            print("SET ACCOUNT property")
            response = requests.request("POST", http + randomUrl + "/apl", params=setAccountProperty)
            print("RESPONSE = " + str(response.json()))
            print("")
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except UnicodeError as e:
            print("Error = " + str(e))
        except json.decoder.JSONDecodeError as e:
            print("Error = " + str(e))
        time.sleep(5)
        try:
            print("DELETE ACCOUNT PROPERTY")
            response = requests.request("POST", http + randomUrl + "/apl", params=deleteAccountProperty)
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

def setAccountPropertyStandard(url):
    while True:
        for i in range(1, 200):
            print(" STEP = " + str(i))
            value = "standard wallets -> ooopppsss ->   " \
                "';:.,<>/?][{}\|=+-_)($#@!%^&*()  ->  " \
                " END 1.1.1.1.1"
            property = "';:.,<>/?][{}\|=+-_)($#@!%^&*()"
            randomUrl = random.choice(url)
            print("------------>   Random URL = " + randomUrl)
            setAccountInfo = {"requestType": "setAccountProperty", "value": value,
                              "deadline": "1440", "property": property, "secretPhrase": str(i),
                              "feeATM": "1000000000"}
            deleteAccountProperty = {"requestType": "deleteAccountProperty", "incoming": "true",
                                     "value": value,
                                     "deadline": "1440", "property": property, "secretPhrase": str(i),
                                     "feeATM": "1000000000"}

            print(randomUrl)
            try:
                print("SET ACCOUNT PROPERTY")
                response = requests.request("POST", http + randomUrl + "/apl", params=setAccountInfo)
                print("RESPONSE = " + str(response.json()))
                print("----- END -----")
                print("")
            except requests.exceptions.ConnectionError:
                requests.status_code = "Connection refused"
            except UnicodeError as e:
                print("Error = " + str(e))
            except json.decoder.JSONDecodeError as e:
                print("Error = " + str(e))
            time.sleep(240)
            try:
                print("DELETE ACCOUNT PROPERTY")
                response = requests.request("POST", http + randomUrl + "/apl", params=deleteAccountProperty)
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


setAccountPropertyStandard(testNet2.t2All)
AccountPropertyVault(testNet2.t2All)
setAccountPropertyStandard(testNet2.t2All)
