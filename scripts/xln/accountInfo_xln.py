import requests
import random
import time
import json

xln_t2_1 = "http://163.172.130.129"
xln_t2_2 = "http://163.172.191.246"
xln_t2_3 = "http://163.172.168.167"

url = ([xln_t2_1, xln_t2_2, xln_t2_3])



def setAccounInfoStandard(url):
    for i in range(1, 200):
        print(" STEP = " + str(i))
        name = "AccountInfo Name AccountInfo Name AccountInfo Name AccountInfo Name A !@#$%^&*()_+=-[]\';,./|}{:<>?|"
        message = "MESSAGE  MESSAGE  !@#$%^&*()_+=-[]\';,./|}{:<>?| MESSAGE MESSAGE MESSAGE MESSAGE MESSAGE  MESSAGE MESSAGE  MESSAGE  !@#$%^&*()_+=-[]\';,./|}{:<>?| MESSAGE MESSAGE MESSAGE MESSAGE MESSAGE  MESSAGE MESSAGE  MESSAGE  !@#$%^&*()_+=-[]\';,./|}{:<>?| MESSAGE MESSAGE MESSAGE !@#$%^&*()_+=-[]\';,./|}{:<>?| "
        randomUrl = random.choice(url)
        print("------------>   Random URL = " + randomUrl)

        setAccountInfo = {"requestType": "setAccountInfo", "name": name,
                          "deadline": "1440", "message": message, "secretPhrase": str(i),
                          "feeMLN": "5000000000"}

        print(randomUrl)
        try:
            response = requests.request("POST", randomUrl + "/xln-api", params=setAccountInfo)
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
