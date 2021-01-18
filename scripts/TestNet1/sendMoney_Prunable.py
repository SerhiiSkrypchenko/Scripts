from json import JSONDecodeError

import requests
import random
import self as self
from urllib3.exceptions import NewConnectionError, MaxRetryError
import data
import time
import functions
import testNet3
import testNet2
import json

http = "http://"

alive = True
while alive:
    k = 1
    for k in range(1, 201):
        print(k)
        print("-------------")
        i = random.randint(1, 200)
        p = random.randint(1, 200)
        t1 = random.choice(testNet2.t2All)
        print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
        response = requests.request("GET",
                                    http + t1 + "/apl",
                                    params=getAccountId)
        print(response.json())
        accountReceive = response.json()["accountRS"]
        print("-------------")
        print(str("accountReceive = " + accountReceive))
        print("-------------")

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
        response = requests.request("GET",
                                    http + t1 + "/apl",
                                    params=getAccountId)
        print(response.json())
        accountSender = response.json()["accountRS"]
        sender = response.json()["account"]
        print("-------------")
        print(str("accountSender = " + accountSender))
        print(str("account = " + sender))
        print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
        print("-------------")
        try:
            response = requests.request("POST",
                                    http + t1 + "/apl",
                                    params=functions.sendMoneyPrunable(str(accountReceive),
                                                                                         str(random.randint(2000000000, 200000000000)),
                                                                                         str(p),
                                                                                         "400000000",
                                                                                         sender))
            print(response.json())
            print(" <<<<<<< --------- " + t1 + " ----- >>>>>>>")
            print("----------------------------------------------------------------------------------------------")
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except UnicodeError as e:
            print("Error = " + str(e))
        except json.decoder.JSONDecodeError as e:
            print("Error = " + str(e))
        except JSONDecodeError as e:
            print("Error = " + str(e))
        except TimeoutError as e:
            print("Error = " + str(e))
        except self.raw_decode as e:
            print("Error = " + str(e))
        except NewConnectionError as e:
            print("Error = " + str(e))
        except ConnectionError as e:
            print("Error = " + str(e))
        except MaxRetryError as e:
            print("Error = " + str(e))
        k += 1
        time.sleep(0)

