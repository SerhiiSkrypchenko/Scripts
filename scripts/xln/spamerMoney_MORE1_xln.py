import requests
import random
import time
import aiohttp
import asyncio
import config_Luna_Wallet


url = config_Luna_Wallet.xln_mn
#LunaInitAccount = secretPhrase of main account

#"add_message": True,
#"messageToEncrypt": "test message long test message longtest message long test message longtest message long test message longtest message long test message long test message long test message long test message long test message long test message long test message long test message long test message longtest message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long test message long",


def sendMoney(recipient, amountMLN, secretPhrase, feeMLN):
    return {"requestType": "sendMoney", "recipient": recipient, "amountMLN": amountMLN,
            "secretPhrase": secretPhrase, "feeMLN": feeMLN, "deadline": "1440"
            }

if __name__ == '__main__':
    alive = True
    while alive:
        for p in range(2, 200):
            print(" <<<< --- START ---- >>>> " + str(p))
            i = random.randint(1, 200)
            random_url = random.choice(url)
            print(" <<<<<<< --------- " + random_url + " ----- >>>>>>>")
            headers = {

                'Authorization': 'Basic cWE6UUFMdW5hT25lVGVzdHMxMjMjI0Be'
            }
            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(i)}
            response = requests.request("GET", random_url + "/api/rpc",
                                        params=getAccountId, verify = False)
            print(response.json())
            accountReceive = response.json()["accountXLN"]
            print(str("accountReceive = " + accountReceive))
            account = response.json()["account"]
            print(response.json())
            print("account = " + account)

            getAccountId = {"": "%2Fapl", "requestType": "getAccountId", "secretPhrase": str(p)}
            response = requests.request("GET",
                                        random_url + "/api/rpc",
                                        params=getAccountId, verify = False)
            accountSender = response.json()["accountXLN"]
            sender = response.json()["account"]
            print("accountSender = " + accountSender)
            amountMLN = random.choice(
                ["2000000000", "3000000000", "4000000000", "5000000000", "6000000000", "7000000000", "8000000000"])
            print("amountMLN = " + amountMLN)
            response = requests.request("POST",
                                        random_url + "/api/rpc",
                                        data=sendMoney(str(accountReceive),
                                                         amountMLN,
                                                         str(p),
                                                         "400000000"
                                                         ), verify = False)
            # print(response.request.url)
            # print(response.request.body)
            # print(response.request.headers)
            print(response.json())
            if "errorDescription" in response.text:
                print()
            else:
                print("recipient = " + response.json()["transactionJSON"]["recipient"])
                print("sender = " + response.json()["transactionJSON"]["sender"])
            print("----------- END -------------")
            time.sleep(0)
            p += 1









