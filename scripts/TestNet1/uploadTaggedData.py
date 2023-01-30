import requests
import testNet2
import random
import string
import time
import json
import testNet1
import testNet3
import testNet4_tap
import testNetStage

def id_generator(size=5, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

URL = testNetStage.t15All

while True:
    k = 1
    for k in range(1, 100):
        print("NEW TRY of upload and extend -> " + str(k))
        t1 = random.choice(URL)
        print(t1)

        getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(k)}
        response = requests.request("GET",
                                    t1 + "/apl",
                                    params=getAccountId)
        print(response.json())
        account = response.json()["accountRS"]
        print(str("account = " + account))
        fin = open('3.jpg', 'rb')
        files = {'file': fin}
        param = {
            "name": str(id_generator(3)) + " #$%^&*()-_=+\|'?/.,][{};:`~!@- '"''"",
            "tags": str(id_generator(5)) + "$%^&*()-_=+\|'?/.,][{};:`~!@- '"''" ",
            "channel": "channel #$%^&*()-_=+\|'?/.,][{};:`~!@- '"''" ",
            "feeATM": "4000000000",
            "description": "#$%^&*()-_"
                           ""
                           ""
                           ""
                           ""
                           ""
                           ""
                           ""
                           "=+\|'?/.,]['"''"{};:`~!@- "+ str(id_generator(20)),
            "messageIsText": "false",
            "messageIsPrunable": "true",
            "sender": str(account),
            "deadline": "1440",
            "isCustomFee": "true",
            "secretPhrase": str(k),
            "amountOfTime": "86400"}
        try:
            response = requests.post(t1 + "/apl?requestType=uploadTaggedData", param,
                                 files=files)
            print(response.json())
            transaction = response.json()['transaction']
            print("transaction = " + transaction)
            print("END upload Tagged Data")
        except requests.exceptions.ConnectionError:
            requests.status_code = "Connection refused"
        except UnicodeError as e:
            print("Error = " + str(e))
        except json.decoder.JSONDecodeError as e:
            print("Error = " + str(e))
        #k+=1
        time.sleep(30)

        for k in range(0, 2):
            try:
                print("start extend ")
                print("try is " + str(k))
                t1 = random.choice(URL)
                print(t1)
                param = {
                    "feeATM": "4000000000",
                    "sender": str(account),
                    "deadline": "1440",
                    "transaction": transaction,
                    "secretPhrase": str(k)
                    }
                response = requests.post(t1 + "/apl?requestType=extendTaggedData", param)
                print(response.json())
                #transaction = response.json()['transaction']
                #print("next transaction = " + transaction)
                print("------extend is finished-----")
                time.sleep(20)

            except requests.exceptions.ConnectionError:
                requests.status_code = "Connection refused"
            except UnicodeError as e:
                print("Error = " + str(e))
            except json.decoder.JSONDecodeError as e:
                print("Error = " + str(e))
            k += 1
