import requests
import random
import time
import json
import config_Luna_Wallet

url = config_Luna_Wallet.xln_t1


def setAccounInfoStandard(url):
    for i in range(1, 200):
        print(" STEP = " + str(i))
        name = "AccountInfo Name AccountInfo Name AccountInfo Name AccountInfo Name A !@#$%^&*()_+=-[]\';,./|}{:<>?|."
        description = "Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Account Info Description of Accou"
        message = "MESSAGE  MESSAGE  !@#$%^&*()_+=-[]\';,./|}{:<>?| MESSAGE MESSAGE MESSAGE MESSAGE MESSAGE  MESSAGE MESSAGE  MESSAGE  !@#$%^&*()_+=-[]\';,./|}{:<>?| MESSAGE MESSAGE MESSAGE MESSAGE MESSAGE  MESSAGE MESSAGE  MESSAGE  !@#$%^&*()_+=-[]\';,./|}{:<>?| MESSAGE MESSAGE MESSAGE !@#$%^&*()_+=-[]\';,./|}{:<>?|  ..."
        randomUrl = random.choice(url)
        print("------------>   Random URL = " + randomUrl)

        setAccountInfo = {"requestType": "setAccountInfo", "name": name, "description": description,
                          "deadline": "1440", "message": message, "secretPhrase": str(i),
                          "feeMLN": "9000000000"}

        print(randomUrl)
        try:
            response = requests.request("POST", randomUrl + "/api/rpc", params=setAccountInfo)
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
        time.sleep(2)


setAccounInfoStandard(url)
