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


def setAccounInfoVault(url):
    for i in range(0, len(vaults)):
        print(" STEP = " + str(i))
        name = "БАГ ДЛЯ ЮРЫ"
        message = "БАГ ДЛЯ ЮРЫ"
        account = vaults[i].account
        sender = vaults[i].sender
        passphrase = vaults[i].passPhrase
        print("SET ACCOUNT INFO")
        randomUrl = random.choice(url)
        print("------------>   Random URL = " + randomUrl)
        printVault(vaults[i])
        headers = {
            'Content-Type': "application/x-www-form-urlencoded"
        }

        setAccountInfo = {"requestType": "setAccountInfo", "name": name, "sender": sender,
                          "deadline": "1440", "message": message, "passphrase": passphrase,
                          "feeATM": "1000000000"}

        print(randomUrl)
        try:
            response = requests.request("POST", randomUrl + "/apl", params=setAccountInfo)
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
        time.sleep(20)

def setAccounInfoStandard(url):
    for i in range(1, 200):
        print(" STEP = " + str(i))
        name = "БАГ для ЮРЫ"
        message = "БАГ для ЮРЫ"
        randomUrl = random.choice(url)
        print("------------>   Random URL = " + randomUrl)

        setAccountInfo = {"requestType": "setAccountInfo", "name": name,
                          "deadline": "1440", "message": message, "secretPhrase": str(i),
                          "feeATM": "1000000000"}

        print(randomUrl)
        try:
            response = requests.request("POST", randomUrl + "/apl", params=setAccountInfo)
            print("RESPONSE = " + str(response.json()))
            print("----- END -----")
            print("")
            time.sleep(0)
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except UnicodeError as e:
            print("Error = " + str(e))
        except json.decoder.JSONDecodeError as e:
            print("Error = " + str(e))
        i += 1
        time.sleep(20)

#setAccounInfoVault(testNet2.t2)
setAccounInfoStandard(testNet1.t1)
